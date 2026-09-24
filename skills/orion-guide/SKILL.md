---
name: orion-guide
description: Help users set up and use Orion through its MCP connector. Use when users ask about Orion onboarding, bringing business context into Orion, analyzing data with Orion, or creating Orion metrics, dashboards, slide decks, and workflows.
---

# Orion Guide

Version: 2026-09-24

Installation and examples: [Orion Guide documentation](https://docs.runorion.com/mcp/orion-guide).

You are the user's assistant in ChatGPT, Codex, Claude, or another MCP client. These instructions guide your work in that assistant. Send Orion the task-specific context and requests it needs through MCP; keep this skill in the host assistant.

Help the user turn what their assistant already knows about their work into useful context and a result from Orion: an answer, metric, dashboard, slide deck, or workflow. Start with their immediate request; someone asking for a dashboard does not need onboarding again.

Orion is an AI data analyst. The MCP connection provides access to Orion; this skill guides how to use it. Use the connected tool descriptions as the authority for available operations and parameters, and the linked Orion docs for product behavior and setup. Consult the relevant page when needed rather than loading the whole documentation site. If Orion tools are unavailable, prepare a concise context brief and analysis prompt the user can paste into Orion, and point to [MCP setup](https://docs.runorion.com/mcp/setup). Do not claim to have connected, saved, or analyzed anything.

## Start with the user's work

Use relevant context actually available in this conversation, accessible memory, and materials the user supplies or asks you to consult. Do not imply access to their entire chat history. Extract the user's role, business or project, decision to make, important definitions, known data sources, and preferred output. Leave out unrelated personal details, credentials, and information from other clients or projects.

If the goal is unclear, suggest two or three specific questions based on that context and recommend one. Ask only for missing details that change the next action, usually the target project and the question or decision. If little context exists, ask what they want to understand and which Orion project to use; do not start with a long questionnaire.

Use `list_projects` to find the relevant project, or reuse a project already established in this conversation. Resolve ambiguity before sending context or analysis requests. If a tool needs `user_id`, use authenticated identity or match the user's known identity against `list_users`. That list does not identify the caller by itself; ask if ambiguous. Inspect relevant existing metrics and Knowledge Base pages before proposing new definitions. Read selectively, scoped to the task.

## Prepare useful context

For onboarding or context transfer, draft a short brief from what is known. For a direct question or creation request, include the needed context in that request without a separate onboarding step. Useful context includes:

- **Purpose and audience:** the business or project, the user's role, and the decision this analysis supports.
- **Definitions and data:** relevant entities, metric formulas, filters, time periods, and source documents or known tables. Preserve established definitions from Orion, dbt, Looker, or supplied documentation; flag conflicts rather than silently replacing them.
- **Output:** the question to answer, useful breakdowns, and the desired table, chart, or narrative.
- **Sources and gaps:** where the context came from, its date when known, and assumptions or missing definitions that need resolution.

When preparing context for Orion, preserve the business definitions the user provides and link to supporting documents. Clearly label suggestions and anything that needs confirmation.

When gathering background from memory or other materials for onboarding, show what you propose to send and which project will receive it, and let the user approve. If the user already asked you to use specific material in Orion, proceed within that scope. Using context for one analysis does not authorize publishing it as shared knowledge; clarify the audience when needed. Include the relevant text or summary in the request: Orion does not automatically receive files attached to the host assistant, and a source link alone may be inaccessible.

## Put context where Orion can use it

| Context | Destination |
| --- | --- |
| This question's objective, audience, and temporary assumptions | Include in the `ask_orion` message for the selected project. |
| Reusable definitions, methodology, or business background | A focused Knowledge Base page, then enable it for the relevant project. |
| Company facts intended for every project and user | Draft Company Information for an admin to add in Orion. |
| A recurring preference within a project | An explicit request to Orion to remember it, when requested by the user. |

For an authorized Knowledge Base write, search for a matching page first. Read it before editing and preserve unrelated content. Use `create_wiki_page` or `update_wiki_page` when exposed and permitted. Creation applies immediately; updates may apply immediately or become a review request. Report the actual result and verify saved content with `get_wiki_page` when available. On a permission error, provide the draft for an authorized user instead of retrying the same write.

**Saving a Knowledge Base page does not by itself enable it for a project.** Check whether it is enabled or included as a Global or Group Default. If it is not, and no tool can enable it, direct the user to Project Settings → Knowledge Base, select the page, and save. Include the approved brief in the analysis message while enablement is pending. Do not claim future conversations have the page in context before that is confirmed.

A Knowledge Base folder is organization, not proof of private access. Keep client-specific context out of company-wide settings and default pages. Use the relevant [Knowledge Base](https://docs.runorion.com/knowledge-base/creating-pages) and [project settings](https://docs.runorion.com/core-concepts/projects) guidance when placement or access needs clarification.

## Get the first useful answer

Reuse an existing metric when it answers the question. Inspect its definition, results, and freshness: a recent execution timestamp does not prove the underlying data is current. Historical execution results may be refresh snapshots rather than a time series. Check units, denominators, and grain before comparing values. If results conflict with a Knowledge Base definition or benchmark, surface the discrepancy and investigate; do not force results to match. If the requested date range or breakdown is missing, use `ask_orion` with the project ID, approved context, question, and desired output. Continue the same conversation for follow-ups.

For example: "Using this project's definition of an active account, compare the last four complete weeks with the preceding four, broken down by customer segment. Show the values and changes, identify the largest contributors, and state the definition, dates, sources, and data gaps. Return a concise explanation and chart-ready table."

If the user asks what's possible, inspect existing metrics and recommendations, or ask Orion which questions the connected data supports. Offer a few grounded options. If data or configuration is missing, report the specific blocker and the next action in Orion; do not manufacture an answer or promise to connect data sources through tools that are not exposed.

Handle Orion's response according to its status and the connected tool instructions:

- **Still running:** Check `get_conversation_history` using the returned conversation ID, waiting at least 30 seconds between polls. Continue until a result, checkpoint, failure, or the client's wait limit; report pending work with its ID if you must stop. Do not submit duplicate requests.
- **Checkpoint:** Show the questions and send the user's answers in `checkpoint_answers` with the exact question or assumption IDs. Also restate those answers in `message`; text alone does not register them. If the response refers to a card but omits its questions or IDs, retrieve them if possible, otherwise direct the user to the checkpoint in Orion. Do not guess IDs or approvals.
- **Full Analysis offered:** If `can_escalate` is true, explain that it may take longer and ask whether to continue. After explicit agreement, use `continue_with_full_analysis` with the exact question and IDs from the handoff. Do not send a consent message to `ask_orion`. If escalation is unavailable, explain the limitation.
- **Recorded:** The message was saved without starting analysis. Explain the returned reason.

## Create the output the user needs

Honor the user's requested format. Otherwise recommend the smallest useful output based on who will use it and how. Creation can be the first task: ask Orion to perform the analysis and build the requested output in the same conversation.

| User's need | Ask Orion to create | Include in the request |
| --- | --- | --- |
| Keep tracking a value or table | [Metric](https://docs.runorion.com/metrics/overview) | Definition, numerator/denominator, grain, filters, date window, visualization, and requested refresh cadence. Reuse validated analysis logic or an existing matching metric. |
| Explore several related numbers | [Dashboard](https://docs.runorion.com/dashboards/overview) | Audience, decisions, KPI tiles, chart breakdowns, useful filters, and reporting period. A dashboard needs a workflow to refresh on a recurring schedule. |
| Present findings in a meeting | [Slide deck](https://docs.runorion.com/chat/running-analyses) | Audience, decision, story, approximate slide count, reporting period, and any supplied template or style. |
| Repeat an analysis or deliverable | [Workflow](https://docs.runorion.com/workflows/create) | Validated notebook or metrics, rolling date window, output format, schedule and timezone, visibility, and any explicitly requested recipients or notification conditions. |

Use `ask_orion` for creation when dedicated creation tools are absent. Continue the existing `conversation_id` so Orion can reuse the analysis. Specify **saved in Orion** when that is intended; a chart or deck built only in the host assistant is a different deliverable. Do not invent `create_metric`, `create_dashboard`, or other tools.

For example: "Build a native Orion Dashboard from this analysis for our customer success team: utilization and activation KPIs, an account comparison, and working segment and region filters that recalculate the relevant cards. Show the data as-of date and definitions. Keep it private; no schedule or notifications."

For a dashboard request, specify Orion's native **Dashboard**, whose saved artifact type is `interactive_dashboard`. A `webpage`/`html` report (`html_dashboard` artifact) is a different output, even if it contains JavaScript tabs or dropdowns. Use that format when the user explicitly requests a webpage. Treat an HTML template as visual guidance and adapt it to native dashboard components; it must not silently select the artifact type. If the native capability is unavailable, explain the limitation instead of substituting a webpage.

For a workflow's native Dashboard output, ask Orion to create or reuse the native dashboard seed and attach its actual returned reference to an `interactive` report step. Read back the saved workflow and check the seed reference as well as the report format; changing only the format string is insufficient. Use the connected tools and current workflow schema as the authority, and never invent seed IDs or storage paths.

When revising an existing output, enumerate what must stay fixed: for example, metric definitions and IDs, source and Knowledge Base references, reporting periods, validated calculations, branding, and existing visibility, schedule and delivery settings. Avoid blanket instructions such as "Preserve everything exactly" when correcting an implementation. Explicitly allow the artifact type, seed, data bindings and layout instructions to change as needed to meet the user's request, while preserving unrelated outputs. Read the current object rather than copying stale counts or settings from earlier prompts.

Verify dashboard behavior separately from successful creation. Filters must recalculate applicable KPIs, charts and tables over the selected population; weighted rates use pooled numerators and denominators. Identify intentionally unfiltered cards and narrative based on the full dataset. Check the saved artifact type, then exercise individual filters, combined filters and Clear against independently aggregated source results. If browser interaction cannot be checked, mark it unverified and give the user the specific remaining checks. Correct unfiltered totals or a successful workflow run alone do not verify interactivity. See [Filter and Explore](https://docs.runorion.com/dashboards/explore).

For metrics, Orion dry-runs the calculation and requests confirmation before saving. Present the preview and relay the user's response through the supported checkpoint or confirmation mechanism. For workflows, start from an analysis or metrics that have been validated; Orion performs an end-to-end dry run before saving. Do not call a proposal or failed dry run a created object.

Carry out creation already authorized by the user. Ask only for missing choices that matter, such as an ambiguous metric definition, timezone for a requested schedule, or delivery audience. Honor requested schedules and delivery; do not add them to a one-off deliverable. For a workflow prepared for review, request schedule **None** and no notification recipients or steps, and verify those settings. A blank notification condition means notify on every run; it does not disable email. If the tools cannot create the requested state, leave a concrete draft and explain the remaining step. See [workflow settings](https://docs.runorion.com/workflows/manage) and [delivery](https://docs.runorion.com/workflows/outputs).

Verify the saved result through `list_metrics`/`get_metric`, `list_artifacts`/`get_artifact`, or `list_workflows`/`get_workflow`, as available. Match the returned ID and inspect the content and settings. Return the actual link when provided, plus any pending confirmation, failed run, or manual step. A workflow definition, a completed run, and a delivered output are separate outcomes.

For a workflow's generated output, use the run ID returned by `run_workflow`, or find it with `get_workflow_runs`. Then use `get_workflow_run_reports` to find the output IDs and `get_workflow_report_content` to read them. Check run status as well as outputs: one available report does not prove the whole run succeeded.

If a creation request times out, inspect the conversation and relevant object list before retrying. Work may continue after the client times out. If completion is still unclear, report it as pending or unverified and retain the conversation ID; do not duplicate the creation request.

## Bring the result back into the assistant

Present the answer in the current chat. Check Orion's source notes before reusing its claims: a value quoted from a Knowledge Base page is not a queried result, and an inferred data date stays unverified. When useful, render a chart or table using returned data and the host assistant's capabilities. Preserve dates, units, filters, definitions, and source references. Label a chart recreated in the assistant accordingly; do not imply it is a live embedded Orion dashboard. Never invent missing values or chart configurations. Share only Orion URLs returned by tools.

Close with the finding or created deliverable, any material limitation, what context was saved or is still pending, and one useful next action. Inspect an existing workflow's delivery behavior before running it; obtain missing authorization if it sends outputs to others. Do not schedule, share, or send results merely because the user requested onboarding.

For additional setup, consult the relevant docs rather than recreating a product manual: [data sources](https://docs.runorion.com/connecting-data-sources), [Company Information](https://docs.runorion.com/configuration/company-information), [metrics](https://docs.runorion.com/metrics/overview), and [workflows](https://docs.runorion.com/workflows/create).
