# Set up your Opportunity OS

## 1. Keep a reusable template and a private workspace

Fork this repository, or download it if you do not use Git. Open the folder in your agent. All personal configuration and outputs belong in the ignored `private/` directory, not in the example files.

You can ask your agent to initialize `private/profile.json` and `private/workspace.json` from `config/`. It must preserve any existing private files and collect your answers before filling missing facts.

## 2. Run onboarding

Use the prompt in the README. The agent follows `prompts/onboarding.md`, interviewing you in short rounds. Start with your actual outcome—for example, finding a first product engineering internship—not a list of automation tools.

The minimum viable setup is one lane, one research task, and one daily digest. Investment and startup research are optional. You choose the output language; the source language may differ.

## 3. Set up Notion

Connect Notion through a tool available to your agent, or create the databases manually using `notion/database-schema.md`. Choose a private parent page you own. Authorize creation there, then let the agent inspect existing databases before creating anything.

The starter includes a schema blueprint, not a hosted duplicate-template URL or a standalone Notion API installer. The agent must use supported Notion tools and inspect their actual schema and access rules.

Store the resulting data source IDs in `private/workspace.json`. Never use example placeholders as actual IDs. If you skip Notion, the agent can archive under `private/briefs/` and keep a reconciliation queue for later.

## 4. Test once manually

Ask the agent to complete one small research task from your selected lane using `automations/research-executor.md`, followed by a Radar draft using `automations/daily-radar.md`.

Accept the pilot only when:

- The task matches your priorities and confirmed facts.
- The sources are current, direct, and accessible, with uncertain claims labeled.
- The output explains what changes a decision and assigns no research homework.
- Notion contains one brief and no duplicate signal; or a local fallback explicitly records the archive failure.
- Nothing was emailed, submitted, or marked sent.
- The run memory records what would justify reopening the topic.

Run `python3 scripts/check_setup.py` to check JSON syntax, core configuration, manifest bindings, and whether private files are tracked. This is an offline configuration check, not verification of your tools or accounts.

## Scheduling

Ask the agent to turn `automations/specifications.md` into a personalized manifest and resolved prompts under `private/`. Review task names, exact prompts, times, timezone, required tools, and permission limits before enabling them in your scheduler.

For Codex / ChatGPT desktop, use the supported scheduled-task interface or tools. Current official guidance says local scheduled tasks need the computer on, the app running, and the project available. CLI and IDE interfaces can prepare and test prompts but do not provide the Scheduled management interface. Availability depends on the product, plan, and workspace settings. See [official scheduled-task documentation](https://learn.chatgpt.com/docs/automations).

For another agent, use its documented scheduling mechanism. Do not assume these Markdown files install scheduled jobs. Keep the manifest as the reviewable specification, then record the actual scheduler IDs and read back the saved configuration.

Start with weekly research and a weekday Radar if that matches your needs. These are examples, not defaults to enable silently. Review the first few runs before increasing frequency.

## 6. Review after one week

Use `workflows/weekly-review.md`. Ask whether the system found useful opportunities, saved work, and avoided noise. Adjust priorities and cadence explicitly. You can pause a workflow without deleting the archive.

## If something fails

| Problem | Recovery |
| --- | --- |
| Notion connection unavailable | Save the completed packet locally; record the failed archive step and dedup key |
| Browsing unavailable | Label current facts unverified; do not invent freshness or publish a new investment conclusion |
| Missing eligibility evidence | Verify the requirement; label the unknown; ask the user only for personal facts inaccessible to the agent |
| Empty or repetitive Radar | Suppress repeated items; preserve a short run log; lower discovery frequency if needed |
| Missed local scheduled run | Check app/machine/project availability and scheduler run history |
| Email requested | Prepare the exact message and obtain action-specific approval before sending |
