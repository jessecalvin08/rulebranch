# RuleBranch build roadmap

## Working pace

Assumption: 10 to 15 hours per week as a solo builder. The quality bar is a small, reliable, visibly polished demonstration—not a broad agent-security platform.

## Milestone 0: Nebius access

**Exit condition:** Token Factory account has the hackathon promo credit redeemed, and the account can create a key.

- Wait for the promo-code email after the submitted credit form.
- Create or log into Token Factory with the chosen Google/GitHub account.
- Redeem the code and confirm the visible balance.
- Create an API key only after access is confirmed; store it privately.
- Run one minimal structured-output request manually before integrating it into the app.

## Milestone 1: Deterministic local proof (Days 1-3)

**Goal:** RuleBranch works without any model or cloud dependency.

- Create the React + FastAPI project skeleton.
- Define the policy and trace schemas.
- Build four simulated tools: `read_file`, `write_file`, `run_tests`, and `http_request`.
- Implement deny-by-default policy evaluation.
- Create the sample repository with a fake `.env` canary and README injection fixture.
- Write twelve fixed tests: normal, denied, approval, and recovery cases.

**Exit condition:** Local tests prove that the policy engine makes correct decisions and the trace captures every attempted action.

## Milestone 2: Token Factory intelligence (Week 1)

**Goal:** Nemotron makes an essential, validated contribution.

- Add the Token Factory client behind a backend service.
- Compile plain-language policy text to typed policy JSON with strict schema validation.
- Generate candidate test cases in structured JSON; retain a fixed hand-written suite as the ground truth.
- Track model name, latency, input/output token data if available, and estimated cost per generation.

**Exit condition:** A normal policy reliably becomes an editable typed draft; invalid output is safely rejected.

## Milestone 3: Coding-agent harness and first Sandbox run (Week 2)

**Goal:** One full attack path runs in an isolated Nebius environment.

- Implement the included coding agent with the four tool adapters.
- Integrate the Contree/Token Factory Sandbox SDK only for controlled sample runs.
- Submit one baseline task with the README-injection fixture.
- Store operation status, logs, artifact metadata, trace, and resource data.

**Exit condition:** The project can show one Token Factory Sandbox execution and replay the same test against the same policy.

## Milestone 4: Product interface and comparison (Week 3)

**Goal:** A first-time judge understands the finding without inspecting source code.

- Build policy entry/review, test-suite selection, run status, trace timeline, and baseline/repair comparison screens.
- Add a small repair workflow that changes only policy configuration or the tool wrapper—never an uncontrolled code patch.
- Make all loading, blocked, failure, and empty states understandable.

**Exit condition:** A visitor can go from policy to a clear violation and comparison result in one guided flow.

## Milestone 5: Evidence and demo readiness (Week 4)

**Goal:** Results are credible and reproducible.

- Expand to a frozen benchmark: 10 normal, 10 boundary, 10 adversarial, 5 recovery, and 5 regression cases.
- Add per-run metrics and JSON export.
- Add documentation, setup scripts, a visible MIT license, and a secret scan.
- Test the local setup in a clean clone.

**Exit condition:** The same test IDs run on baseline and repair configurations, and the dashboard explains the measured difference.

## Milestone 6: Release and submission (Final week)

**Goal:** Judges can evaluate the project without help.

- Deploy a free, accessible demonstration with only synthetic data.
- Create the public GitHub repository and validate all links.
- Record the under-three-minute YouTube video using the storyboard in the hackathon checklist.
- Complete Devpost project details, technology explanation, feedback, screenshots, and final submission rehearsal.

**Exit condition:** A clean-browser user can open the demo, understand the value, view evidence, and reach the repository/video.

## Go/no-go rule

If the local deterministic runner and one controlled Token Factory Sandbox test are not working by the end of Week 2, freeze scope immediately:

- keep a single sample repository;
- keep only `allow` and `deny` policies;
- use a fixed hand-written test suite;
- defer automated repairs, Tavily, additional agents, login, and deployment enhancements.

The smallest demonstrable loop is more valuable than a broad incomplete platform.
