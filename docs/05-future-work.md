# RuleBranch future work

This is intentionally separate from the hackathon MVP. These ideas must not delay the core RuleBranch proof: policy -> test -> isolated run -> trace -> comparison.

## P1: After the core demo works

### More policy capabilities

- Time, cost, and token budgets per agent run.
- Approval workflow with expiring approval receipts.
- Data classification rules for canaries, credentials, customer records, and source code.
- Policy inheritance: project defaults plus task-specific restrictions.
- Visual policy-diff view between baseline and repair branches.

### Better agent coverage

- GitHub pull-request agent adapter using a fake local Git server.
- MCP tool-manifest importer and tool-poisoning checks.
- Multi-step permission-chain analysis: individually permitted actions that combine into a forbidden data flow.
- Regression-test generation from prior violations.
- Test packs aligned to published agent-security threat categories.

### Better evidence

- Signed, tamper-evident trace receipts.
- HTML/PDF compliance-style reports.
- Historical comparison charts across policy versions.
- CI integration that fails a pull request when a safety test regresses.

## P2: Product expansion

### Framework and platform support

- Adapters for common agent frameworks.
- Workspace/project management with role-based access.
- Bring-your-own repository and container images.
- Private deployment mode for teams that cannot send code externally.
- Public REST API and command-line interface.

### Richer execution

- Parallel sandbox branches for comparing multiple policy repairs.
- Automatic minimal repair suggestions with mandatory user review.
- Performance and cost optimization across multiple model tiers.
- Scheduled safety regression runs.

## P3: Research directions

- A public benchmark measuring whether policies preserve useful task completion while blocking prompt-injection-driven tool misuse.
- Comparative evaluations of policies, agent prompts, tool wrappers, and sandbox restrictions.
- Human-readable explanations of composed-action risks without revealing sensitive trace content.
- Privacy-preserving evaluation datasets built from canaries and synthetic repositories.

## Ideas explicitly rejected for the hackathon MVP

| Idea | Why it is deferred |
| --- | --- |
| Real GitHub/Gmail/WhatsApp access | Adds credentials, privacy risk, and unreliable external dependencies |
| Universal connector marketplace | Broad platform work does not prove the central safety loop |
| Enterprise billing/SSO/multi-tenancy | Not needed for a judge to evaluate the product |
| Model fine-tuning | Consumes budget and does not improve the first proof of value |
| Autonomous repair of real code | High risk and unnecessary for a safety-testing demonstration |
| Physical AI integration | Does not match the selected coding-agent track or current solo scope |
