import httpx
import pytest
from fastapi.testclient import TestClient
from openai import APIConnectionError, APIStatusError, APITimeoutError

from app import main
from app.demo_data import DEMO_POLICY


client = TestClient(main.app)
POLICY_INPUT = {"policy_text": "Allow source edits but never read secrets."}


@pytest.fixture(autouse=True)
def no_private_configuration(monkeypatch):
    monkeypatch.setattr(main, "has_api_key", lambda: True)
    monkeypatch.setattr(main, "configured_model", lambda: "nvidia/test-model")


def install_failure(monkeypatch, error):
    def fail(_):
        raise error
    monkeypatch.setattr(main, "compile_policy", fail)


@pytest.mark.parametrize("status", [400, 401, 402, 403, 404, 422, 429, 500])
def test_provider_status_is_actionable_without_exposing_body(monkeypatch, caplog, status):
    request = httpx.Request("POST", "https://api.tokenfactory.nebius.com/v1/chat/completions")
    error = APIStatusError("PRIVATE_RESPONSE_CANARY", response=httpx.Response(status, request=request),
                           body={"secret": "PRIVATE_RESPONSE_CANARY"})
    install_failure(monkeypatch, error)
    result = client.post("/api/policies/compile", json=POLICY_INPUT)
    assert result.status_code == 502
    assert f"HTTP {status}" in result.json()["detail"]
    assert "PRIVATE_RESPONSE_CANARY" not in result.text + caplog.text


@pytest.mark.parametrize("timeout", [False, True])
def test_connection_errors_are_reported_without_retries(monkeypatch, timeout):
    request = httpx.Request("POST", "https://api.tokenfactory.nebius.com/v1/chat/completions")
    error = APITimeoutError(request=request) if timeout else APIConnectionError(request=request)
    install_failure(monkeypatch, error)
    result = client.post("/api/policies/compile", json=POLICY_INPUT)
    assert result.status_code == (504 if timeout else 502)
    assert "No draft was accepted" in result.json()["detail"]


def test_unexpected_error_does_not_expose_message_or_stack(monkeypatch, caplog):
    install_failure(monkeypatch, RuntimeError("PRIVATE_EXCEPTION_CANARY"))
    result = client.post("/api/policies/compile", json=POLICY_INPUT)
    assert result.status_code == 502
    assert "PRIVATE_EXCEPTION_CANARY" not in result.text + caplog.text


def test_success_returns_draft_not_execution_claim(monkeypatch):
    monkeypatch.setattr(main, "compile_policy", lambda _: (DEMO_POLICY, "nvidia/test-model", "json_schema"))
    result = client.post("/api/policies/compile", json=POLICY_INPUT)
    assert result.status_code == 200
    assert result.json()["status"] == "compiled"
    assert "no coding task was executed" in result.json()["message"]
