import type {
  DemoComparison,
  NebiusConnectionStatus,
  Policy,
  PolicyCompileResponse,
  PolicyValidationResponse,
} from "./types";

// The current milestone is intentionally local-only; deployment configuration comes later.
const API_BASE_URL = "http://127.0.0.1:8000";

export async function fetchDemoComparison(): Promise<DemoComparison> {
  const response = await fetch(`${API_BASE_URL}/api/demo/comparison`);
  if (!response.ok) {
    throw new Error("The local RuleBranch API is unavailable.");
  }
  return (await response.json()) as DemoComparison;
}

export async function fetchNebiusConnectionStatus(): Promise<NebiusConnectionStatus> {
  const response = await fetch(`${API_BASE_URL}/api/nebius/status`);
  if (!response.ok) {
    throw new Error("RuleBranch could not check Token Factory.");
  }
  return (await response.json()) as NebiusConnectionStatus;
}

export async function compilePolicyWithNebius(policyText: string): Promise<PolicyCompileResponse> {
  const response = await fetch(`${API_BASE_URL}/api/policies/compile`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ policy_text: policyText }),
  });
  if (!response.ok) {
    const payload = (await response.json().catch(() => null)) as { detail?: string } | null;
    throw new Error(payload?.detail ?? "Token Factory could not compile the policy.");
  }
  return (await response.json()) as PolicyCompileResponse;
}

export async function validatePolicyDraft(policy: Policy): Promise<PolicyValidationResponse> {
  const response = await fetch(`${API_BASE_URL}/api/policies/validate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ policy }),
  });
  if (!response.ok) {
    const payload = (await response.json().catch(() => null)) as { detail?: string } | null;
    throw new Error(payload?.detail ?? "RuleBranch could not test the generated draft.");
  }
  return (await response.json()) as PolicyValidationResponse;
}
