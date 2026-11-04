# Notion workspace blueprint

Create these databases under a private parent selected by the user. Research Briefs, Opportunity Signals, and Daily Reports form the basic system. Add Career Tracker and Networking Targets only when useful.

This file is a schema, not an installed Notion template. Before creating anything, search the selected parent, fetch existing schemas, and reuse compatible databases. Use actual supported tool syntax, not guessed property IDs. Store data source identifiers and any field-name mappings in private/workspace.json. Credentials belong in the connection manager, never this file.

## Research Briefs

| Property | Type / options |
| --- | --- |
| Brief | Title |
| Date | Date, date-only |
| Lane | Select: Career, Startup, Investment, Event, Mixed |
| Status | Select: Queued, Done, Skipped |
| Priority | Select: High, Medium, Watch |
| Novelty | Select: Known, Useful, New, Non-obvious |
| What You May Not Know | Rich text |
| Trigger | Rich text |
| Decision Needed | Rich text |
| Human Action | Rich text |
| Source | URL |
| Dedup Key | Rich text |
| Sent Email | Checkbox, false by default |

Body: the completed packet from workflows/research-loop.md. A queued brief becomes Done in place. Use the same page for minor updates; create a linked delta packet for a material new event when useful.

## Opportunity Signals

| Property | Type / options |
| --- | --- |
| Signal | Title |
| Date | Date |
| Lane | Select: Career, Startup, Investment, Event |
| Company or Person | Rich text |
| Geography | Rich text |
| Status | Select: New, Watch, Act, Archived |
| Priority | Select: High, Medium, Watch |
| Novelty | Select: Known, Useful, New, Non-obvious |
| Confidence | Select: Low, Medium, High |
| Action | Rich text |
| Source | URL |
| Dedup Key | Rich text |

Create only for a concrete next action or decision threshold. Link the supporting brief in the body. Update the existing company/topic signal when appropriate. News alone is not a signal.

## Career Tracker

| Property | Type / options |
| --- | --- |
| Application | Title |
| Company | Rich text |
| Role URL | URL |
| Location | Rich text |
| Deadline | Date |
| Status | Select: Discovered, Matching, Prepared, Awaiting Approval, Submitted, Interview, Rejected, Withdrawn, Closed |
| Eligibility | Select: Confirmed, Unknown, Not Eligible |
| Fit | Select: Strong, Possible, Weak |
| Packet Path | Rich text |
| Approval Reference | Rich text |
| Submission Receipt | Rich text |
| Dedup Key | Rich text |

Body: verified job requirements, personal evidence match, unknowns, exact packet version, consent answers, approval scope, and subsequent outcome. Submitted requires a real receipt or equivalent verified confirmation.

## Networking Targets

| Property | Type / options |
| --- | --- |
| Target | Title |
| Organization | Rich text |
| Contact Purpose | Rich text |
| Contextual Route | Rich text |
| Status | Select: Research, Ready, Awaiting Approval, Contacted, Closed |
| Source | URL |
| Dedup Key | Rich text |

Only add a target with a specific purpose and evidence-backed route. Prefer relevant events or shared context before cold outreach. A public profile is not proof of willingness to connect.

## Daily Reports

| Property | Type / options |
| --- | --- |
| Report | Title |
| Date | Date, date-only |
| Human Action | Rich text |
| Delivery Status | Select: Draft, Ready, Awaiting Approval, Sent, No Action |
| Sent Email | Checkbox, false by default |
| Delivery Reason | Rich text |
| Dedup Key | Rich text |

Use one report per local calendar day. Include brief links and a short decision summary. An inbox report can be Ready while Sent Email remains false. An email draft awaiting approval uses Delivery Reason = Awaiting human approval. Mark Sent only after the actual email succeeds and store its receipt.

## Verification and recovery

Read back created IDs/properties where needed to bind later operations. Confirm checkbox/date types and that no unintended public sharing was enabled. If archive writes fail, save the full output and desired properties under private/reconciliation/ with the dedup key, failure, and timestamp. Before retrying, search Notion for the key to avoid duplicate pages after partial success.
