# Opportunity OS

**A personal opportunity system that researches, prepares, and remembers—so you can make better decisions.**

Opportunity OS turns your goals and background into an agent-assisted workspace for career opportunities, company research, startup ideas, and an optional investment research lane. It combines a private personal profile, Notion databases, reusable workflows, and personalized scheduled tasks.

The agent does the research and prepares the evidence. You make the decisions and approve external actions.

## Start here

1. **Fork or download this repository.** Keep the reusable template separate from your private working data.
2. Open the folder in your preferred coding agent. Codex desktop is the reference setup; another agent works if it can read files, research current sources, and access your Notion workspace.
3. Paste this into a new chat:

   ```text
   Help me set up my personal Opportunity OS from this repository.
   Read START_HERE.md, AGENTS.md, and prompts/onboarding.md.
   Interview me in short rounds, then generate my private profile, workspace
   configuration, and personalized automation prompts. Ask about what I want
   to achieve before recommending workflows. Mark missing facts as unknown.
   Prepare my Notion workspace after I choose its destination. Run one manual
   test before proposing schedules. Show the final schedule manifest before
   enabling anything. Do not send messages or submit applications.
   ```
4. Follow [START_HERE.md](START_HERE.md). Prefer a career-only pilot before enabling more lanes.

No programming is needed for the basic workflow. Notion access and scheduling are configured in your own agent account. This repository does not install a scheduler, connect accounts, or publish a prebuilt Notion template automatically.

## What it does

| Workflow | Agent completes | You decide |
| --- | --- | --- |
| Daily Opportunity Radar | Checks fresh evidence, removes duplicates, prepares one concise digest | Which opportunities deserve attention |
| Research Executor | Completes one focused strategy packet and archives it | Whether the evidence changes a decision |
| Career Preparation | Matches roles against verified facts; drafts application packets | Which role to pursue and whether to submit |
| Weekly Review | Reviews outcomes and proposes changes to priorities and cadence | Whether to adopt those changes |

Read the [research loop](workflows/research-loop.md), [career workflow](workflows/career-preparation.md), and [approval policy](workflows/approval-and-execution.md) for the operating details.

## Personalization is the product

There is no universal career path, watchlist, geography, schedule, or preferred language here. Onboarding collects your goals, actual qualifications, constraints, evidence, notification preferences, and permission boundaries. It then creates:

- `private/profile.json`: your facts, goals, preferences, and their provenance.
- `private/workspace.json`: your own Notion destinations and local paths.
- `private/automation-manifest.json`: proposed tasks, schedules, timezone, and permissions.
- `private/automations/*.md`: fully resolved prompts for your selected workflows.
- `private/memory/`: prior work, checkpoints, and run history.

These files are ignored by Git. Ignore rules are a convenience, not encryption; review staged files before pushing. Your Notion sharing settings also determine who can read archived personal information.

## Repository map

```text
START_HERE.md             Setup and first-run acceptance checks
AGENTS.md                 Shared operating rules for the agent
prompts/onboarding.md     Guided interview and configuration workflow
config/                   Portable JSON examples
notion/database-schema.md Database blueprint and provisioning instructions
automations/              Task specifications and copy-ready prompt bodies
workflows/                Research, career, review, and approval playbooks
examples/                 Fictional example for learning the workflow
scripts/check_setup.py    Offline configuration and privacy checks
```

## Scheduling and tools

First run each prompt manually. Then create scheduled tasks through your agent's supported scheduling interface and confirm the saved prompt, timezone, enabled status, and required tool access. Templates are specifications, not a portable scheduler configuration. Local scheduled work needs the local project available; see [setup guidance](START_HERE.md#scheduling).

Notion is the reference archive, but research can still finish locally when the connection is unavailable. Email and mailbox connections are optional; no email connector is required to use the starter.

## Open source and license

Released under the **[MIT License](LICENSE)**. You may use, copy, modify, distribute, sublicense, and sell copies of this template, provided you retain the copyright and license notice. Contributions are welcome under the same license; see [CONTRIBUTING.md](CONTRIBUTING.md).

The template is provided without warranty. The license does not grant rights to third-party source material, product names, or connected services. Keep your personal data out of public contributions. Research outputs are decision support; investment, legal, immigration, and eligibility conclusions require appropriate verification.

## Design principles

- Complete agent-doable work instead of assigning research homework.
- Prefer decision-relevant evidence over more news.
- Check prior work before researching again.
- Distinguish confirmed facts, interpretations, and unknowns.
- Preserve human approval for messages and external submissions.
- Remember outcomes without silently changing goals or authority.

Built from a personal workflow and generalized for other people's goals. This is an independent project, not an official OpenAI or Notion product.
