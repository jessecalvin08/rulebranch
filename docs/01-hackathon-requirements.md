# Hackathon requirements and submission checklist

## Official requirement summary

RuleBranch must satisfy all of the following:

1. Run on **Nebius Token Factory** or **Nebius AI Cloud**.
2. Use at least one NVIDIA open-source model.
3. Fit a hackathon track. RuleBranch will enter **Coding and Agentic Engineering**.
4. Provide a working project, test build, or hosted demo that judges can access free of charge through the judging period.
5. Publish the source code in a public repository with an open-source license and clear setup instructions.
6. Submit a public YouTube demonstration video of three minutes or less.
7. Explain how Nebius Token Factory/AI Cloud and NVIDIA models were used.
8. Supply required project description, category, platform feedback, repository, demo, and video on Devpost.

The official rules evaluate viable submissions using four equally weighted criteria:

| Criterion | What RuleBranch must visibly prove |
| --- | --- |
| Technological implementation | A real Token Factory model call and an isolated Sandbox execution; schema validation; deterministic enforcement; inspectable traces |
| Design | A complete flow from policy entry to finding, repair, and comparison—not only scripts or raw logs |
| Potential impact | A realistic developer problem: coding agents can be induced to misuse tools or access secrets |
| Quality of the idea | A focused, non-obvious workflow: authority-to-tests compilation plus reproducible before/after evidence |

Source: [Official rules](https://nebiusglobalaihackathon.devpost.com/rules).

## Dates

| Milestone | Date |
| --- | --- |
| Submission period | August 26 to October 30, 2026 |
| Submission deadline | October 30, 2026, 10:00 AM Pacific Time |
| Winners announced | Around January 11, 2027 |

Because the project is being built in India, add the deadline to the calendar in local time as well. Do not rely on a last-minute timezone conversion.

## Credits and onboarding

Current evidence from the Devpost welcome email:

- The separate Token Factory credit form was submitted on September 14, 2026.
- The confirmation page says that a promo code will be emailed.
- The Devpost activation code shown in the email was `NEBIUS-DEVPOST-GLOBAL26`.
- The email also advertises a further $25 Token Factory credit through the Nebius Builders Program, plus training, office hours, and community access.

Use the first $25 credit for the essential proof of technology. Treat the additional credit as helpful but not guaranteed until it is visibly active in the account.

## Submission checklist

### Build and technology

- [ ] RuleBranch makes a live runtime call to Nebius Token Factory.
- [ ] At least one NVIDIA open-source model performs an essential job, not a cosmetic label.
- [ ] At least one controlled coding-agent scenario executes through Token Factory Sandboxes.
- [ ] The project has a clear selected track: Coding and Agentic Engineering.
- [ ] The core result is reproducible using synthetic data and no private credentials.

### Repository

- [ ] Public GitHub repository created.
- [ ] MIT license visible at repository root.
- [ ] README explains setup, environment variables, architecture, and demo data.
- [ ] `.env.example` has placeholders only.
- [ ] No API keys, secrets, personal tokens, or private data appear in Git history.
- [ ] Test cases, policy schema, sample repository, and expected results are included.

### Demo and Devpost

- [ ] Hosted demo or test build remains reachable without payment.
- [ ] Public YouTube video is less than three minutes.
- [ ] Video shows the product working on screen, not only slides.
- [ ] Devpost description explains the user problem, product, technology use, and result.
- [ ] Screenshots make the policy, violation trace, and branch comparison understandable.
- [ ] Feedback on Nebius and NVIDIA tools is completed.
- [ ] Any reused pre-existing work is disclosed with the changes made during the submission period.

## Three-minute video outline

| Time | On-screen proof |
| --- | --- |
| 0:00-0:20 | The danger: a coding agent can follow an injected README instruction and cross a permission boundary |
| 0:20-0:45 | Write the plain-language policy; show Nemotron's editable structured output |
| 0:45-1:20 | Baseline sandbox run; show the agent's attempted secret read or network upload |
| 1:20-1:50 | RuleBranch trace identifies the exact policy rule and blocks the action |
| 1:50-2:20 | Repair branch reruns the same suite; safety improves while normal tasks still pass |
| 2:20-2:45 | Architecture: Token Factory, NVIDIA Nemotron, deterministic policy engine, Sandboxes |
| 2:45-3:00 | Final measurable result and repository/demo links |

## Sources to recheck before submission

- [Hackathon overview](https://nebiusglobalaihackathon.devpost.com/)
- [Official rules](https://nebiusglobalaihackathon.devpost.com/rules)
- [Hackathon resources](https://nebiusglobalaihackathon.devpost.com/resources)
- [Schedule](https://nebiusglobalaihackathon.devpost.com/details/dates)
