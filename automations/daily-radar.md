# Daily Opportunity Radar — prompt template

Read AGENTS.md, private/profile.json, private/workspace.json, private/opportunity_os.md, and private/memory/daily-radar.md first. Use the user's timezone and output language.

Check today's Daily Report before creating one. Read fresh completed briefs, active signals, career packets, and verified approaching deadlines. Conduct only the targeted verification needed for today's digest. Queue substantial new research for Research Executor rather than pretending it was completed.

Prepare at most one digest for the local calendar day. Lead with what the user may not know and why it changes a decision. Include up to three human decisions, each with evidence, a recommended choice, a verified deadline if applicable, and a link to the completed packet. Keep the distinction between agent-completed work and personal actions clear. Suppress repeats unless evidence, price, timing, or action changed. If there is no meaningful change, record No Action and follow the configured quiet policy.

Archive to the configured Daily Reports database, reusing today's report. Default to inbox delivery. Do not send email from this template. If the user has requested email preparation, draft the exact recipient, subject, body, and attachments for approval, set Sent Email=false and Delivery Reason=Awaiting human approval, then stop before sending.

Write timestamped memory including the report ID/path, items surfaced, dedup keys, delivery state, next checkpoints, and any failed archive step. Report concrete failures without marking the digest sent.
