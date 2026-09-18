# Release and submission plan

Updated September 18, 2026. This document distinguishes completed work from release blockers. It is not evidence of a completed Devpost submission.

## Verified today

- `backend/.env` is ignored by Git, along with virtual environments, frontend dependencies, build output, and generated reports.
- A search of the candidate public source and documentation found no obvious embedded API key, GitHub token, password, or private-key block. This is a best-effort pattern scan, not a guarantee.
- The backend suite passed 51 tests. The production-only frontend dependency audit reported zero vulnerabilities on September 16. Re-run both before release.
- `backend/fixtures/sample_policy.json` passes all 18 synthetic authority checks. These checks execute no coding agent or repository tests.
- The actual Token Factory project ID was copied from Project settings and added to the private, ignored `backend/.env`. A read-only SDK check against that ID still reported `spawn=false`, `list=false`, and all other reported Sandbox permissions false. Sandbox access is not verified; no live Sandbox run was started.

## Real-run procedure (pending access)

1. The real project ID is configured privately. The Nebius Sandbox Beta request was submitted on September 18, 2026. Wait for the access notification, then confirm `spawn=true` with a read-only check. Do not paste an API key into chat or documentation.
2. Repeat the read-only Sandbox permission check and proceed only when `spawn=true`. Retain the existing `NEBIUS_API_KEY`, `NEBIUS_MODEL`, and `NEBIUS_PROJECT_ID` in private `backend/.env`.
3. Review `backend/fixtures/sample_policy.json`. It permits reading the README, source and tests, writing `src/`, and running exact `pytest`; it denies secret reads, deletion, and network tool calls.
4. From `backend/`, run `./.venv/Scripts/python.exe -m app.run_sandbox --reviewed-policy fixtures/sample_policy.json --approve --output reports/sandbox-comparison.json`.
5. Check that the report says `evidence_type=nebius_sandbox_execution`, both branches have a Sandbox image ID, every action was genuinely model-produced, and both final pytest exit codes match the claimed outcome. If the model did not attempt an unsafe action, report that honestly; do not substitute the scripted dashboard trace.
6. Keep the report private until it has been inspected for unexpected content. It is deliberately gitignored.

The runner limits itself to eight model actions per branch and only uploads the three checked-in fixture files and an explicit fake canary. It never sends `http_request` or executes `delete_file`, even in the observe branch. “Observe” therefore measures *attempts* and permitted fixture work, not a real exfiltration. The enforce branch applies the reviewed policy before fixture capabilities. This comparison is meaningful only after a successful live run and inspection.

## Public repository gate

- Re-run `git check-ignore -v backend/.env` and a secret scan before staging.
- Stage only intended source, docs, fixture, license, and lock files. Inspect staged names and diff. Never add `backend/.env`, reports, generated artifacts, or real private code.
- Create a local commit and publish an MIT-licensed public GitHub repository only after GitHub authentication is refreshed. The CLI currently says its stored token is invalid; no remote or public repo has been verified.
- Verify the public page as a signed-out visitor, including `LICENSE`, setup instructions, and a clean clone/install/test path.

## Judge demo gate

A local `localhost` URL is not judge-accessible. The existing React page displays a sample simulation and calls a local FastAPI backend. A frontend-only static deployment would not make the model compiler or sandbox runner work. Choose a host that can run the backend privately with server-side credentials, resource/time limits, and spend controls; put the frontend on a public URL. Verify it as a signed-out visitor. Do not expose the API key to the browser or publish an unrestricted paid `/api/policies/compile` endpoint.

## Video outline (maximum three minutes)

Record only after a working public demo and real-run report exist. Use OBS or another local screen recorder and upload to public YouTube; Devpost needs the public video URL.

1. **0:00–0:25 — problem:** A coding agent needs source access, but README content is untrusted. State the exact fake-canary fixture.
2. **0:25–0:55 — authority:** Show plain-language policy, Nemotron-generated structured draft, and human review.
3. **0:55–1:35 — baseline/observe:** Show *actual* model-produced tool attempts and Sandbox image/result ID; call out that unsafe network/delete calls were suppressed by the outer test safety boundary.
4. **1:35–2:15 — enforce:** Show the reviewed policy blocking any attempted unsafe action, with exact rule IDs and the real `pytest` result.
5. **2:15–2:40 — evidence:** Compare actual attempt counts, blocks, and task completion. If there was no attack attempt or a test failed, say so accurately.
6. **2:40–3:00 — architecture and links:** Explain Nebius Token Factory + NVIDIA Nemotron + Nebius Sandboxes and show the public repository/demo URLs.

Do not read out or show the private API key, billing data, or a real `.env`. Do not describe sample-scripted events as executed results.

## Devpost final checklist

- Working project running on Token Factory or Nebius AI Cloud and using at least one NVIDIA open-source model.
- Select Coding and Agentic Engineering track; describe the user problem, what was built, how it works, and where Nebius/NVIDIA were used.
- Public code repository with visible open-source license and setup README.
- Judge-accessible working demo, hosted application, or test-build URL.
- Public YouTube demonstration of no more than three minutes, with audio explaining Nebius and NVIDIA use.
- Feedback on Nebius/NVIDIA tools, plus a note on substantial changes made during the submission period if this work predates it.
- Final Devpost review and submission before October 30, 2026 at 10:00 AM Pacific Time. Verify the final status shows submitted, not draft.

Source: [official hackathon rules](https://nebiusglobalaihackathon.devpost.com/rules).
