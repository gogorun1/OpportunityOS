# Personalized task specifications

Generate only the tasks selected during onboarding. The following are starting points for discussion, not active schedules.

| Task | Suggested pilot cadence | Purpose | Output |
| --- | --- | --- | --- |
| Research Executor | Once or twice weekly | Complete one evidence-backed task | Brief and warranted signals |
| Career Preparation | Twice weekly | Verify roles and prepare selected packets | Tracker and review packets |
| Daily Radar | Weekday morning after research | Consolidate decision-relevant changes | One inbox digest |
| Weekly Review | Once weekly | Assess outcomes and propose adjustments | Short review |

For each selected task produce an exact prompt under private/automations/, then bind it in private/automation-manifest.json. Include workflow, name, prompt_path, IANA timezone, human-readable cadence, enabled=false, required_tools, permission_scope, and scheduler_id=null. Resolve actual local paths and actual Notion mappings during onboarding.

Each prompt must read AGENTS.md, live private/profile.json, private/workspace.json, relevant workflow files, and private/memory/<workflow>.md at the beginning. Create missing memory only in private storage. Append a timestamped result, archive references, and reopening conditions before returning.

The reference memory paths use workflow names such as daily-radar or research-executor. A scheduler-specific memory file may also be maintained when the host requires it; record its path privately and avoid contradictory copies.

Default delivery is the agent inbox and internal Notion archive. Background workers do not send mail. Notify on meaningful changes, completed requested artifacts, failures, or required user action; log unchanged checks quietly where the host permits. A daily digest should not repeat old signals without new decision relevance.

Use supported scheduler tools or UI to activate reviewed tasks. Read back the saved prompt/schedule/timezone and store returned IDs. No scheduler-specific credentials or personal automation exports belong in Git.
