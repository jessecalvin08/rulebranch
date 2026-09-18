# Nebius Token Factory setup runbook

## Purpose

Use this guide after the promo-code email arrives. It sets up the minimum secure access RuleBranch needs for one live NVIDIA model call and later a controlled Sandbox run.

## Current status

September 14: the account is active and a real policy-generation call succeeded. Jesse's existing key and model setup are complete; do not repeat these steps or overwrite the private configuration. See the [debugging record](07-compilation-debugging.md). An earlier screenshot showed a $1 trial badge; the current remaining promotional balance has not been verified.

## Step 1: Create or sign in to Token Factory

1. Open [tokenfactory.nebius.com](https://tokenfactory.nebius.com).
2. Select **Log in**.
3. Use the same Google or GitHub account consistently for hackathon-related services where practical.
4. Confirm that the Token Factory dashboard opens.

## Step 2: Redeem the promo code

1. Open the promo-code email from Nebius.
2. Follow its redemption link or instructions.
3. Apply the code to the Token Factory account.
4. Confirm the credit balance appears in the dashboard.
5. Take a screenshot of the visible confirmation if desired, but hide any account ID or secret information.

If redemption fails, keep the error screenshot and contact the hackathon manager or Nebius support through the official resources. Do not repeatedly submit the original credit form.

## Step 3: Create an API key

For a new installation only (already completed on Jesse's machine):

1. Select the purple **Get API key** button in the upper-right of Token Factory. The **API keys** item in the left sidebar opens the same area.
2. Create a dedicated key named `rulebranch-local-dev`.
3. Copy the value only into a password manager or directly into the private local configuration file. Do not paste it into chat or take a screenshot of it.
4. In the project folder, duplicate `backend/.env.example` and rename the copy to `backend/.env`.
5. Open `backend/.env` in VS Code and set only the first line at this stage:

```env
NEBIUS_API_KEY=paste-the-private-key-here
```

6. Save the file. It is already excluded from Git by `.gitignore`.
7. Never send the key in chat, email, screenshots, issue trackers, or public repositories.

Leave `NEBIUS_MODEL` empty until the RuleBranch preflight has listed the authenticated model catalog. Do not copy a model identifier from a generic tutorial.

## Step 4: Select the model discovered by RuleBranch

The September 14 preflight returned four NVIDIA/Nemotron-named candidates. This exact model identifier subsequently completed a live policy-generation call:

```env
NEBIUS_MODEL=nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B
```

1. Set the complete line in `backend/.env` exactly once. If the file already contains `NEBIUS_MODEL=`, paste only `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B` after its equals sign, not the entire assignment again.
2. Save the file.
3. Stop the backend with `Ctrl+C` and start it again; `.env` changes require a restart.
4. In the RuleBranch dashboard, select **Compile with Token Factory** once to generate a new draft. This submits an inference request and uses credits; listing models does not prove this step succeeds.

RuleBranch requests named JSON-schema output, validates the draft's structure, and adds local secret, network, and deletion guards. The model assists with translation; its policy still needs human and semantic review. It is not automatically applied to the fixed sample comparison, and no real coding agent is executed.

## Step 5: First live validation

Milestone status:

1. API-key authentication: verified.
2. Nemotron structured policy generation: verified for the synthetic default input. Correct meaning and executability still need checking.
3. A controlled coding-agent fixture in a Nebius Sandbox: not implemented or verified yet.

Keep the model identifier configurable. The implementation will query the authenticated model list or select the identifier displayed in the account rather than relying on a model name copied from an old example.

## Credit-preservation rules

- Develop policy enforcement and unit tests locally first.
- Cache valid structured generations during development.
- Use a smaller suitable Nemotron model for routine policy/test generation.
- Use larger reasoning models only for difficult, final demonstrations.
- Run Sandbox jobs only for controlled milestone proofs and release candidates.
- Record model use and sandbox usage per run in RuleBranch.

## Optional follow-up

The Devpost welcome email also offers the Nebius Builders Program, which may provide an additional $25 in Token Factory credits plus Tavily credits, office hours, and training. Join it after the primary Token Factory credit is redeemed; it is helpful but not required for the first RuleBranch milestone.

## Official references

- [Token Factory quickstart](https://docs.tokenfactory.nebius.com/quickstart)
- [Structured output and JSON](https://docs.tokenfactory.nebius.com/ai-models-inference/json)
- [Sandbox overview](https://docs.tokenfactory.nebius.com/sandboxes/overview)
- [Hackathon resources](https://nebiusglobalaihackathon.devpost.com/resources)
