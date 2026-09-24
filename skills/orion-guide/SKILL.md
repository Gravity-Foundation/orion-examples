---
name: orion-guide
description: Help users get started with Orion, ask questions about their data, share useful background, create reports and dashboards, or improve existing work through the Orion connection.
---

# Orion Guide

Version: 2026-09-24

Help the user use Orion in a way that fits their goal and experience. They can start with a question, explore what is possible, create something, or improve existing work. Use the parts of this guide that help with their request.

Use this skill in ChatGPT, Codex, Claude, or another assistant to help the user work with Orion. Send Orion their request and the background information it needs. Let Orion decide how to do the analysis and build the result unless the user has asked for a particular approach.

The Orion tools available in this conversation explain what they can do and what information they need. Follow those instructions, and consult the relevant [Orion documentation](https://docs.runorion.com/mcp/orion-guide) when needed. This file contains the complete skill. Tool names and field names below are for the assistant; explain them to the user only when it helps them take the next step.

## Meet the user where they are

If they have a clear request, act on it. Answer their question, ask Orion to build what they want, or continue their existing analysis. Do not make them complete setup questions, write a background summary, or save a metric first unless the task needs it.

If they are exploring, help them discover what Orion can do with their data. Ask Orion what questions it can answer, or look at existing projects, metrics, and recommendations for ideas. Suggest useful possibilities and let the user choose the direction. They do not need to choose a final format before exploring.

Use the project and Orion conversation already chosen for the task. Otherwise, use `list_projects` to find the right project or ask which one they mean. Ask for missing information when it changes what to do next. Let Orion handle analysis and settings questions it can resolve. Avoid asking the user to repeat information they have already given.

If a tool requires `user_id`, use the signed-in user's ID when the connection provides it. Otherwise, match the user's known identity against `list_users`. The list alone does not tell you who is signed in; ask if you cannot tell which person is the user.

If you cannot use Orion's tools, help the user [check the connection](https://docs.runorion.com/mcp/setup), work in Orion directly, or write a request they can paste there. Choose what helps with their goal, and be clear about what has and has not been done.

## Bring useful context

Use relevant information you can actually access in this conversation, memory, or materials the user asks you to read. Orion may benefit from knowing what decision they are making, how their business defines a metric, which data to use, the dates to cover, or who will read the result. Include what matters for this request. A short question may already be enough.

Keep the user's definitions and make clear which ideas are suggestions. Include the relevant text or a summary when sending the request: files attached in ChatGPT, Claude, or Codex are not automatically sent to Orion, and Orion may not be able to open a link. Do not claim access to the user's entire history or include unrelated personal details, credentials, or other clients' information.

If the user wants help introducing their work to Orion, a short summary can help them review what will be sent and to which project. If they already asked you to use specific material in Orion, go ahead and use it for that request. Before including other background they have not asked to share, show it to them and let them choose what to include.

Background information can stay in the conversation. If the user wants Orion to use it again, explain relevant options: a project Knowledge Base page for definitions and ways of calculating results, Company Information for facts everyone in the organization should know, or project memory for a recurring preference. Ask who should have access when that is unclear. Using information to answer one question does not mean the user wants it saved for others.

When the user wants to save or change a Knowledge Base page, look for an existing page and read it before editing. Use the available wiki tools, keep unrelated content, and report whether the change was saved or sent for review.

A saved page is not necessarily used by the chosen project. Check whether the project includes it directly or through an organization or group default. If it does not, and no tool can change that setting, guide the user to Project Settings → Knowledge Base. Include the approved information in the current request so Orion can use it meanwhile. A folder name does not tell you who can access its pages. See [Knowledge Base guidance](https://docs.runorion.com/knowledge-base/creating-pages).

## Help them ask, explore, and iterate

Use `ask_orion` to ask questions or request something that no other available tool can create directly. Describe what the user wants and any requirements they have given. Let Orion choose the queries and steps needed to produce the result. Continue the conversation for follow-ups, corrections, and changes of direction.

Existing metrics or analyses may already answer the question. If you use them, check what they measure and which dates their data covers. A calculation run today can still use old data. Repeated runs may recalculate the same period, so their results do not necessarily show change over time. Keep dates, units, definitions, and sources clear. If figures disagree or evidence is missing, explain and investigate the gap.

For example, a user might ask, "Why did contribution change last quarter?" Start with that question and the background they have provided. If they later want to compare customer groups, present the findings, or track the result, help them take that next step.

Respond to Orion's status using the instructions provided with its tools:

- **Still working or timed out:** Use the returned conversation ID with `get_conversation_history`, waiting at least 30 seconds between checks. Orion may keep working after a timeout. Before sending the request again, check the conversation and whether the requested result has already been saved. If you cannot keep waiting, explain what is pending and retain the conversation ID so the work can be checked later.
- **Needs the user's answers (a checkpoint):** Show Orion's questions. Send the answers in `checkpoint_answers` with the exact question or assumption IDs, and repeat the answers in `message`. A normal chat reply alone does not record them. If the questions or IDs are missing, retrieve them if possible or direct the user to answer in Orion. Do not guess what the user approved.
- **Offers Full Analysis:** If the response includes `can_escalate: true`, explain that Full Analysis may take longer and ask whether to continue. After the user agrees, call `continue_with_full_analysis` with the exact question and IDs Orion returned. A consent message sent to `ask_orion` does not switch modes. If Full Analysis is unavailable, explain that limitation.
- **Message recorded:** Orion saved the message but did not start an analysis. Explain the reason it returned.

If Orion asks for confirmation before saving or building something, relay that request. Do not assume every task needs the same confirmation.

## Support their choice of output

Use the format the user asks for. If they are unsure, explain useful options or let Orion recommend one. They can choose a chat answer, metric, dashboard, slide deck, report, or workflow without creating the others first.

Useful options include:

- A [metric](https://docs.runorion.com/metrics/overview) for a saved calculation that returns a value or table.
- A [Dashboard](https://docs.runorion.com/dashboards/overview) for exploring related values with Orion's filters, charts, and tables.
- A slide deck or report for presenting and sharing findings; a webpage can suit a custom HTML presentation.
- A [workflow](https://docs.runorion.com/workflows/create) for repeating an analysis or refreshing outputs, manually or on a requested schedule.

Say **save it in Orion** when that is what the user wants. Creating a chart in ChatGPT or Claude does not also save it in Orion. Orion's interactive Dashboard and a webpage report are different formats, even if they look similar. Request the one the user needs and clarify if unclear. Use a template to guide the appearance while keeping the requested features.

When checking an Orion Dashboard, its saved type should be `interactive_dashboard`. The type `html_dashboard` identifies a webpage, even if it contains buttons or dropdowns. A workflow that produces an Orion Dashboard needs an `interactive` report step linked to a saved dashboard that it uses on each run. Let Orion set up that link; changing the format name alone is not enough. If Orion cannot provide the requested format, explain and discuss alternatives.

Pass along the user's preferences for who can see the result, when it should run, which timezone to use, and who should be notified. Leave settings they have not specified for Orion to recommend or ask about. Use Orion's tools to record any answers it needs. Do not add your own confirmation step for work the user has already requested.

Before running an existing workflow, check whether it will send anything to other people and whether the user has asked for that. If they want notifications turned off, check the recipients and notification steps. Leaving the notification condition blank means it can notify on every run; it does not turn email off. See [workflow settings](https://docs.runorion.com/workflows/manage).

When changing existing work, say what should change and what still needs to stay the same. Give Orion room to make the changes needed. Avoid broad instructions such as "Preserve everything exactly" when that would keep the problem in place. Only require a particular metric, layout, or format to stay unchanged when the task depends on it.

## Bring back a useful result

Answer the question or show what was created. Explain where the information came from and any gaps that affect how the user can use it. Share links returned by Orion's tools. Check that a saved result does what the user requested; a message saying it was created is not enough to prove that. For a dashboard, check the saved format and requested filters. If you could not open it and test the filters, say so.

Use the available tools to read saved metrics, dashboards, reports, or workflows. To read the results of a workflow run, use its run ID with `get_workflow_run_reports`, then read each relevant report with `get_workflow_report_content`. Check the run's status too: one report being available does not mean the whole run succeeded.

When testing filters, check that affected numbers match the selected data. Try filters together and use Clear to reset them where available. Calculate weighted rates from totals rather than averaging row percentages. Make clear when a card or written summary still describes all the data instead of the selected data. See [Filter and Explore](https://docs.runorion.com/dashboards/explore).

Be clear about what has happened: Orion may have proposed something, saved it, run it, or sent it to someone. These are different outcomes. If it needs an answer, show its question. If work is waiting or cannot continue, explain why and what can happen next. Do not invent numbers, IDs, links, or successful actions.

Continue when the user wants to explore or improve the result. Offer a next step when it helps. A useful answer can also be the end of the task; there is no need to always suggest saving information, creating another report, or scheduling future runs.
