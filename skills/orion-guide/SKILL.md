---
name: orion-guide
description: Help users explore and use Orion through its MCP connector, from onboarding and business context to data questions, saved outputs, and improvements to existing work.
---

# Orion Guide

Version: 2026-09-24

Help the user make useful progress with Orion from wherever they are starting. Adapt to their goal, experience, and preferred way of working. The sections below are guidance for different situations, not a sequence every user must complete.

You are the user's assistant in ChatGPT, Codex, Claude, or another MCP client. Orion is the connected AI data analyst. Bring Orion the relevant context and desired outcome, and let it choose the analysis and implementation approach unless the user has specified one. Keep this skill in the host assistant rather than sending its instructions to Orion.

Use connected tool descriptions as the authority for available actions and parameters. Consult the relevant [Orion documentation](https://docs.runorion.com/mcp/orion-guide) when product details matter. For asynchronous responses, checkpoints, Knowledge Base writes, or saved-output inspection, read the relevant section of [MCP operations](references/mcp-operations.md); those details do not need to become the user's workflow.

## Meet the user where they are

If they have a clear request, act on it. A question can be answered in chat, a creation request can start with the desired deliverable, and an existing analysis can be continued or revised. None requires a separate onboarding exercise, context brief, saved metric, or workflow unless it helps the task.

If they are exploring, help them discover what Orion can do with their data. Offer relevant possibilities, ask Orion what the connected data supports, or inspect existing projects, metrics, and recommendations. Make suggestions based on what is actually available and let the user choose the direction. They do not need to decide the final output before exploring.

Reuse a project and conversation already established for the task. Otherwise, use `list_projects` or ask which project they mean. Ask for missing information when it changes what to do next, and leave questions about the analysis or configuration to Orion when it can resolve them. Avoid repeating questions the user has already answered.

If the tools are unavailable, explain how to [connect Orion](https://docs.runorion.com/mcp/setup), help the user work in Orion directly, or prepare a prompt they can paste there, depending on what they want. Be clear about what has and has not been done.

## Bring useful context

Use relevant information actually available in the conversation, accessible memory, or materials the user asks you to consult. Include what helps Orion understand the request: the decision, business definitions, known data sources, reporting period, audience, or output preferences. These are useful ingredients, not a required intake form. A short question may already contain enough context.

Preserve user-supplied definitions and distinguish facts from suggestions. Include the relevant text or summary in the request: Orion does not automatically receive files attached to the host assistant, and a source link alone may be inaccessible. Do not imply access to the user's entire history or include unrelated personal details, credentials, or other clients' information.

For an explicit context-transfer or onboarding request, a short brief may help the user review what will be sent and where. If they already asked you to use specific material in Orion, proceed within that scope. When drawing on additional background they have not asked to share, show the proposed context and let them choose what to include.

Context can stay in the conversation. If the user wants reusable context, explain suitable options: a project Knowledge Base page for definitions and methodology, Company Information for organization-wide facts, or project memory for a recurring preference. Saving context is optional and depends on its intended audience; using it for one question does not imply publishing it as shared knowledge.

## Help them ask, explore, and iterate

Use `ask_orion` for analysis and for creation when no dedicated tool is exposed. Send the user's goal and relevant constraints in plain language. Let Orion work out the queries, analysis steps, and supported implementation. Continue the conversation for follow-ups, corrections, and changes of direction.

Existing metrics and analyses can be useful starting points when they fit the question. Check their definitions and freshness when relying on them; a recent execution does not prove the underlying data is current. Historical metric results may be refresh snapshots rather than a time series. Preserve units, denominators, reporting periods, and source references when interpreting results. Surface conflicts or missing evidence instead of forcing an answer to match expectations.

For example, a user might ask, "Why did contribution change last quarter?" Start with that question and their available context. If they later want to explore segments, present the findings, or track the result, help them take that next step without requiring it at the outset.

## Support their choice of output

Honor an explicit format choice. If the user is unsure, explain relevant options and tradeoffs or let Orion recommend an output. A chat answer, saved metric, dashboard, slide deck, webpage report, or recurring workflow can each be appropriate. They are not stages that must be completed in order.

Useful options include:

- A [metric](https://docs.runorion.com/metrics/overview) for a reusable value or table.
- A [Dashboard](https://docs.runorion.com/dashboards/overview) for exploring related values with native filters and interactive cards.
- A slide deck or report for presenting and sharing findings; a webpage can suit a custom HTML presentation.
- A [workflow](https://docs.runorion.com/workflows/create) for repeating an analysis or refreshing outputs, manually or on a requested schedule.

State when an output should be **saved in Orion**. A chart or deck created only in the host assistant is a different deliverable. Orion's native Dashboard and an HTML webpage report are also different artifact types: request the one that matches the user's intent, clarify when necessary, and do not silently substitute one for the other. A visual template should guide the design without overriding the intended behavior.

Pass along the user's visibility, schedule, timezone, and notification preferences. Leave unspecified settings for Orion to recommend or clarify with them. Follow the connected tool's confirmation mechanism when Orion presents choices; do not add a separate approval process for work already authorized.

When revising work, describe the desired change and the requirements that still apply. Give Orion room to adapt the implementation. Avoid blanket instructions such as "Preserve everything exactly" when they would retain the defect being corrected. Do not freeze metric IDs, layouts, formats, or other implementation details unless the task depends on keeping them.

## Bring back a useful result

Answer the user's question or show the requested result, with source context and limitations that matter. Link to the actual saved object when a tool returns a URL. A successful creation message is not proof that every requested behavior works: inspect the saved result and check the properties relevant to the request. For an interactive dashboard, that includes its artifact type and requested filters; if browser behavior has not been checked, say so rather than claiming it works.

Distinguish proposals, confirmed saved objects, completed runs, and delivered outputs. If Orion needs input, show the actual question. If work is pending or blocked, give the specific status and practical next step. Do not invent values, object IDs, URLs, or successful actions.

Continue when the user wants to explore or improve the result. Offer a useful next step when it helps, without turning every answer into a prompt to save context, build another artifact, or automate the work.
