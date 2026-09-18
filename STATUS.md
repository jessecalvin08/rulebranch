# RuleBranch status

Last updated: September 18, 2026

## Current position

The local prototype has a verified live policy-generation call to NVIDIA Nemotron through Nebius Token Factory. A bounded Nebius Sandbox coding-agent runner is implemented, but it has not produced a live execution result: the currently probed project returned no Sandbox permissions and HTTP 403 for image listing. The dashboard still shows only a scripted sample, not measured real agent behavior.

| Item | Status | Notes |
| --- | --- | --- |
| Devpost registration | Complete | Confirmation email received |
| Project direction | Complete | RuleBranch, Coding and Agentic Engineering track |
| Project workspace | Complete | Documentation, MIT license, git ignore rules, and implementation structure created |
| Token Factory credit request | Complete | Jesse redeemed the promo code and activated Token Factory |
| Token Factory account and credit redemption | Needs balance check | Dashboard is active; visible badge currently shows $1 trial, so confirm the separate promotional balance in Billing settings |
| API key | Stored locally | Jesse saved `rulebranch-local-dev` in ignored `backend/.env`; the key value was never shared or inspected |
| Token Factory connection check | Verified | Authenticated model listing works; listing models alone does not prove generation |
| Selected NVIDIA model | Configured and verified | `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B`; corrected a duplicated `NEBIUS_MODEL=` assignment without changing the key |
| JSON policy compiler | Live generation verified | Running API returned `status: compiled`, `response_mode: json_schema`, and 12 rules including 3 local guards on September 14 |
| Generated-policy semantics | Hardened, local checks added | Generated `run_tests` rules must allow exactly `pytest`; the evaluator rejects absolute/traversal paths and protects nested secret/Git paths. A fixed 18-case local matrix now checks the generated draft against the demo's intended authority |
| Local policy evaluator | Unit-tested, simulation only | Checks scripted calls; does not execute a real coding agent, file edit, upload, or repository test |
| Generated-draft test | 18/18 passed, synthetic only | The exact 12-rule draft displayed in Jesse's RuleBranch tab was validated through the local API on September 14: all 5 permitted-operation checks and 13 prohibited/invalid-operation checks passed. No browser focus, Token Factory request, file action, command action, or network action was involved |
| React + FastAPI dashboard | Build passed | Generated drafts are separate from sample traces, edits mark drafts stale, failures are visibly errors, and generated drafts can be tested locally |
| Regression tests | 51 passed | Offline tests cover generation contracts, malformed output, reserved guards, path and test-runner enforcement, the 18-case matrix, API integration, secret-safe errors, and the new Sandbox runner's synthetic-only safety boundary; 2 dependency deprecation warnings |
| Sandbox integration | Beta access requested; not live-verified | Official ConTree SDK installed and pinned; runner creates two branches, asks Nemotron for bounded actions, and measures pytest. The real project ID is configured privately, but a read-only check returned `spawn=false`, `list=false`, and all other reported Sandbox permissions false. A Sandbox Beta request was submitted to Nebius on September 18, 2026; no Sandbox was run. |
| Public repository | Not published | Local commit `4a3f1a5` exists; GitHub CLI token is invalid, and no remote or public repository is verified |
| Public demo | Not deployed | Local-only React + FastAPI; no judge-accessible URL has been verified |
| Demo video | Not recorded/uploaded | Outline prepared in release plan; recording must wait for a truthful working run |
| Devpost submission | Draft only | Complete near deadline after code, demo, video, and repository are ready |

## Next action for Jesse

Do not create or share another API key. The Sandbox Beta request is submitted. Wait for Nebius to notify the project email that access is enabled, then rerun the read-only permission check; the current SDK result is still `spawn=false`. The CLI has an explicit `--approve` gate, but the dashboard does not yet expose a review/approval flow or a live result. The current generated draft passed **18/18** local synthetic checks; that is not a coding-agent result.

Read [the debugging record](docs/07-compilation-debugging.md) for the confirmed causes, verification, limitations, and next steps. The local simulation does not need a Nebius API key.

## Next implementation milestones

1. Confirm or obtain Sandbox execution permission for the configured project; the read-only probe using the actual project ID returned `spawn=false`.
2. Review `backend/fixtures/sample_policy.json` or export/review the latest generated draft, then invoke the CLI's explicit approval gate.
3. Run and debug the two real Nebius Sandbox branches, then verify the recorded agent actions and actual pytest outcomes.
4. Add a dashboard review/approval and live-result flow, or provide a reliable judge test build with the CLI evidence clearly labeled.
5. Publish a secret-scanned public repository and an accessible demo, record/upload the short public video, then complete Devpost submission.
6. Confirm the remaining promotional balance before larger live runs; it has not been measured here.

## Decision log

| Decision | Chosen approach | Reason |
| --- | --- | --- |
| Project name | RuleBranch | Clearer hackathon product story than IntentGraph; avoids a conflicting AI product name |
| Track | Coding and Agentic Engineering | The app tests coding agents that write and test code in isolated sandboxes |
| Primary scenario | Coding agent | Stronger track fit than appointments or media workflow automation |
| Interface | React + FastAPI | A polished web demonstration with Python for AI and policy logic |
| Enforcement | Deterministic rules | A model must not be the sole judge of whether its own actions are safe |
| Demo data | Synthetic sample repository | Safe, repeatable, public, and free of real credentials |

## Important handling rule

Never paste a Nebius API key in chat, screenshots, public documents, GitHub, or source code. The existing key stays in ignored `backend/.env`; only the backend loads it. Debugging did not print or alter it.
