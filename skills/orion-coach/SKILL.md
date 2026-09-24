---
name: orion-coach
description: Guide ChatGPT, Codex, or Claude in using Orion through MCP to transfer business context, analyze data, and create metrics, dashboards, slides, and workflows. Use when a user wants to get started with Orion or work with Orion from their assistant.
---

# Orion Coach

Version: 2026-09-23

Installation and examples: [Orion Coach docs guide](https://docs.runorion.com/mcp/orion-coach).

You are the user's assistant in ChatGPT, Codex, Claude, or another MCP client. These instructions guide your work in that assistant. Send Orion the task-specific context and requests it needs through MCP; keep this skill in the host assistant.

Help the user turn what their assistant already knows about their work into useful context and a result from Orion: an answer, metric, dashboard, slide deck, or workflow. Start with their immediate request; someone asking for a dashboard does not need onboarding again.

Orion is an AI data analyst. The MCP connection provides access to Orion; this skill guides how to use it. Use the connected tool descriptions as the authority for available operations and parameters, and the linked Orion docs for product behavior and setup. Consult the relevant page when needed rather than loading the whole documentation site. If Orion tools are unavailable, prepare a concise context brief and analysis prompt the user can paste into Orion, and point to [MCP setup](https://docs.runorion.com/mcp/setup). Do not claim to have connected, saved, or analyzed anything.

## Start with the user's work

Use relevant context actually available in this conversation, accessible memory, and materials the user supplies or asks you to consult. Do not imply access to their entire chat history. Extract the user's role, business or project, decision to make, important definitions, known data sources, and preferred output. Leave out unrelated personal details, credentials, and information from other clients or projects.

If the goal is unclear, suggest two or three specific questions based on that context and recommend one. Ask only for missing details that change the next action, usually the target project and the question or decision. If little context exists, ask what they want to understand and which Orion project to use; do not start with a long questionnaire.

Use `list_projects` to find the relevant project. Resolve ambiguity before sending context or analysis requests. If a tool needs `user_id`, resolve the current user's identity from authenticated context or `list_users`; ask if ambiguous, never choose another user by default. Inspect relevant existing metrics and Knowledge Base pages before proposing new definitions. Read selectively, scoped to the task.

## Prepare useful context

Draft a short brief, ideally a few paragraphs, from what is known. Include only fields that help this task:

- **Purpose and audience:** the business or project, the user's role, and the decision this analysis supports.
- **Definitions and data:** relevant entities, metric formulas, filters, time periods, and source documents or known tables. Preserve established definitions from Orion, dbt, Looker, or supplied documentation; flag conflicts rather than silently replacing them.
- **Output:** the question to answer, useful breakdowns, and the desired table, chart, or narrative.
- **Sources and gaps:** where the context came from, its date when known, and assumptions or missing definitions that need resolution.

Distinguish user-supplied facts from proposals. Do not invent table names, business rules, metric definitions, or data availability. For research or slide decks, synthesize the decision-relevant context and retain source references. A hypothetical example stays labeled as an example.

Show the proposed context and destination before transferring information drawn from memory or other materials. If the user already approved the exact content and destination, proceed without asking again. Approval to use context for one analysis does not by itself authorize publishing it as shared knowledge. Confirm the intended audience when shared visibility is unclear.

## Put context where Orion can use it

| Context | Destination |
| --- | --- |
| This question's objective, audience, and temporary assumptions | Include in the `ask_orion` message for the selected project. |
| Reusable definitions, methodology, or business background | A focused Knowledge Base page, then enable it for the relevant project. |
| Company facts intended for every project and user | Draft Company Information for an admin to add in Orion. |
| A recurring preference within a project | An explicit request to Orion to remember it, when requested by the user. |

For an authorized Knowledge Base write, search for a matching page first. Read it before editing and preserve unrelated content. Use `create_wiki_page` or `update_wiki_page` when exposed and permitted. Creation applies immediately; updates may apply immediately or become a review request. Report the actual result and verify saved content with `get_wiki_page` when available. On a permission error, provide the draft for an authorized user instead of retrying the same write.

**Saving a Knowledge Base page does not enable it for a project.** If no tool can enable the page, direct the user to Project Settings → Knowledge Base, select the page, and save. Until enabled, include the approved brief in the analysis message so the first answer can still use it. Do not claim future conversations have the page in context before enablement is confirmed.

A Knowledge Base folder is organization, not proof of private access. Keep client-specific context out of company-wide settings and default pages. Use the relevant [Knowledge Base](https://docs.runorion.com/knowledge-base/creating-pages) and [project settings](https://docs.runorion.com/core-concepts/projects) guidance when placement or access needs clarification.

## Get the first useful answer

Reuse an existing metric when it answers the question. Inspect its definition, results, and freshness: a recent execution timestamp does not prove the underlying data is current. Historical execution results may be refresh snapshots rather than a time series. Check units, denominators, and grain before comparing values. If results conflict with a Knowledge Base definition or benchmark, surface the discrepancy and investigate; do not force results to match. If the requested date range or breakdown is missing, use `ask_orion` with the project ID, approved context, question, and desired output. Continue the same conversation for follow-ups.

For example: "Using this project's definition of an active account, compare the last four complete weeks with the preceding four, broken down by customer segment. Show the values and changes, identify the largest contributors, and state the definition, dates, sources, and data gaps. Return a concise explanation and chart-ready table."

If the user asks what's possible, inspect existing metrics and recommendations, or ask Orion which questions the connected data supports. Offer a few grounded options. If data or configuration is missing, report the specific blocker and the next action in Orion; do not manufacture an answer or promise to connect data sources through tools that are not exposed.

Follow tool responses for completion, checkpoints, and analysis-mode changes. If processing is asynchronous, use the returned conversation or run ID to check progress at the documented interval; do not submit duplicate requests. Relay checkpoint questions and record the user's actual answers using the tool's required fields. A recorded message is not a completed analysis. Escalate to Full Analysis only through the supported tool after the user's explicit agreement when offered; explain if escalation is unavailable.

## Create the output the user needs

Honor the user's requested format. Otherwise recommend the smallest useful output based on who will use it and how. Creation can be the first task: ask Orion to perform the analysis and build the requested output in the same conversation.

| User's need | Ask Orion to create | Include in the request |
| --- | --- | --- |
| Keep tracking a value or table | [Metric](https://docs.runorion.com/metrics/overview) | Definition, numerator/denominator, grain, filters, date window, visualization, and requested refresh cadence. Reuse validated analysis logic or an existing matching metric. |
| Explore several related numbers | [Dashboard](https://docs.runorion.com/dashboards/overview) | Audience, decisions, KPI tiles, chart breakdowns, useful filters, and reporting period. A dashboard needs a workflow to refresh on a recurring schedule. |
| Present findings in a meeting | [Slide deck](https://docs.runorion.com/chat/running-analyses) | Audience, decision, story, approximate slide count, reporting period, and any supplied template or style. |
| Repeat an analysis or deliverable | [Workflow](https://docs.runorion.com/workflows/create) | Validated notebook or metrics, rolling date window, output format, schedule and timezone, visibility, and any explicitly requested recipients or notification conditions. |

Use `ask_orion` for creation when dedicated creation tools are absent. Continue the existing `conversation_id` so Orion can reuse the analysis. Specify **saved in Orion** when that is intended; a chart or deck built only in the host assistant is a different deliverable. Do not invent `create_metric`, `create_dashboard`, or other tools.

For example: "Build an Orion dashboard from this analysis for our customer success team: utilization and activation KPIs, an account comparison, and filters for segment and region. Show the data as-of date and definitions. Keep it private; no schedule or notifications."

For metrics, Orion dry-runs the calculation and requests confirmation before saving. Present the preview and relay the user's response through the supported checkpoint or confirmation mechanism. For workflows, start from an analysis or metrics that have been validated; Orion performs an end-to-end dry run before saving. Do not call a proposal or failed dry run a created object.

Carry out creation already authorized by the user. Ask only for missing choices that matter, such as an ambiguous metric definition, timezone for a requested schedule, or delivery audience. Creation alone does not authorize sharing, scheduled execution, or notifications. If a workflow is being prepared for review, request it with scheduling and notifications disabled; verify that state rather than assuming the request was honored. If the tools cannot create that state, leave a concrete draft and explain the remaining step.

Verify the saved result through `list_metrics`/`get_metric`, `list_artifacts`/`get_artifact`, or `list_workflows`/`get_workflow`, as available. Match the returned ID and inspect the content and settings. Return the actual link when provided, plus any pending confirmation, failed run, or manual step. A workflow definition, a completed run, and a delivered output are separate outcomes.

If a creation request times out, inspect the conversation and relevant object list before retrying. Work may continue after the client times out. If completion is still unclear, report it as pending or unverified and retain the conversation ID; do not duplicate the creation request.

## Bring the result back into the assistant

Present the answer in the current chat. Check Orion's source notes before reusing its claims: a value quoted from a Knowledge Base page is not a queried result, and an inferred data date stays unverified. When useful, render a chart or table using returned data and the host assistant's capabilities. Preserve dates, units, filters, definitions, and source references. Label a chart recreated in the assistant accordingly; do not imply it is a live embedded Orion dashboard. Never invent missing values or chart configurations. Share only Orion URLs returned by tools.

Close with the finding or created deliverable, any material limitation, what context was saved or is still pending, and one useful next action. Inspect an existing workflow's delivery behavior before running it; obtain missing authorization if it sends outputs to others. Do not schedule, share, or send results merely because the user requested onboarding.

For additional setup, consult the relevant docs rather than recreating a product manual: [data sources](https://docs.runorion.com/connecting-data-sources), [Company Information](https://docs.runorion.com/configuration/company-information), [metrics](https://docs.runorion.com/metrics/overview), and [workflows](https://docs.runorion.com/workflows/create).
