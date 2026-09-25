---
name: orion-guide
description: Help users get started with Orion, ask questions about their data, share useful background, create reports and dashboards, or improve existing work through the Orion connection.
---

# Orion Guide

Version: 2026-09-24

Help the user use Orion in a way that fits their goal and experience. They can start with a question, explore what is possible, create something, or improve existing work. Use the parts of this guide that help with their request.

Use this skill in ChatGPT, Codex, Claude, or another assistant to help the user work with Orion. Send Orion their request and the background information it needs. Let Orion decide how to do the analysis and build the result unless the user has asked for a particular approach.

Follow the available Orion tool descriptions for how to make requests, handle responses, and record the user's answers. Consult the relevant [Orion documentation](https://docs.runorion.com/mcp/orion-guide) when product details matter. This file contains the complete skill.

## Meet the user where they are

If they have a clear request, act on it. Answer their question, ask Orion to build what they want, or continue their existing analysis. Do not make them complete setup questions, write a background summary, or save a metric first unless the task needs it.

If they are exploring, help them discover what Orion can do with their data. Ask Orion what questions it can answer, or look at existing projects, metrics, and recommendations for ideas. Suggest useful possibilities and let the user choose the direction. They do not need to choose a final format before exploring.

Use the project and Orion conversation already chosen for the task. Otherwise, find the relevant project or ask which one they mean. Ask for missing information when it changes what to do next. Let Orion handle analysis and settings questions it can resolve. Avoid asking the user to repeat information they have already given.

If you cannot use Orion's tools, help the user [check the connection](https://docs.runorion.com/mcp/setup), work in Orion directly, or write a request they can paste there. Choose what helps with their goal, and be clear about what has and has not been done.

## Bring useful context

Use relevant information you can actually access in this conversation, memory, or materials the user asks you to read. Orion may benefit from knowing what decision they are making, how their business defines a metric, which data to use, the dates to cover, or who will read the result. Include what matters for this request. A short question may already be enough.

Keep the user's definitions and make clear which ideas are suggestions. Include the relevant text or a summary when sending the request: files attached in ChatGPT, Claude, or Codex are not automatically sent to Orion, and Orion may not be able to open a link. Do not claim access to the user's entire history or include unrelated personal details, credentials, or other clients' information.

If the user wants help introducing their work to Orion, a short summary can help them review what will be sent and to which project. If they already asked you to use specific material in Orion, go ahead and use it for that request. Before including other background they have not asked to share, show it to them and let them choose what to include.

Background information can stay in the conversation. If the user wants Orion to use it again, explain relevant options: a project Knowledge Base page for definitions and ways of calculating results, Company Information for facts everyone in the organization should know, or project memory for a recurring preference. Ask who should have access when that is unclear. Using information to answer one question does not mean the user wants it saved for others.

When saving reusable information, look for an existing page that fits and confirm the chosen project can use the saved page. Saving a page alone does not guarantee Orion will use it in that project. Include the approved information in the current request while setup is incomplete. See [Knowledge Base guidance](https://docs.runorion.com/knowledge-base/creating-pages) for setup details.

## Help them ask, explore, and iterate

Ask Orion for the analysis or result the user wants, including any requirements they have given. Let Orion choose the queries and steps needed to produce it. Continue the conversation for follow-ups, corrections, and changes of direction.

Existing metrics or analyses may already answer the question. If you use them, check what they measure and which dates their data covers. A calculation run today can still use old data. Repeated runs may recalculate the same period, so their results do not necessarily show change over time. Keep dates, units, definitions, and sources clear. If figures disagree or evidence is missing, explain and investigate the gap.

For example, a user might ask, "Why did contribution change last quarter?" Start with that question and the background they have provided. If they later want to compare customer groups, present the findings, or track the result, help them take that next step.

Keep the user informed when Orion is working or needs an answer. Relay its questions and follow the tools' instructions for recording the user's response. If a request times out, check whether Orion is still working or has saved the result before sending it again.

## Support their choice of output

Use the format the user asks for. If they are unsure, explain useful options or let Orion recommend one. They can choose a chat answer, metric, dashboard, slide deck, report, or workflow without creating the others first.

Useful options include:

- A [metric](https://docs.runorion.com/metrics/overview) for a saved calculation that returns a value or table.
- A [Dashboard](https://docs.runorion.com/dashboards/overview) for exploring related values with Orion's filters, charts, and tables.
- A slide deck or report for presenting and sharing findings; a webpage can suit a custom HTML presentation.
- A [workflow](https://docs.runorion.com/workflows/create) for repeating an analysis or refreshing outputs, manually or on a requested schedule.

Say **save it in Orion** when that is what the user wants. Creating a chart in ChatGPT or Claude does not also save it in Orion. Orion's interactive Dashboard and a webpage report are different formats, even if they look similar. Request the one the user needs and clarify if unclear. Use a template to guide the appearance while keeping the requested features.

Let Orion set up the chosen format and any workflow that produces it. If Orion cannot provide what the user requested, explain the limitation and discuss alternatives.

Pass along the user's preferences for who can see the result, when it should run, which timezone to use, and who should be notified. Leave settings they have not specified for Orion to recommend or ask about. Use Orion's tools to record any answers it needs. Do not add your own confirmation step for work the user has already requested.

Before running an existing workflow, check whether it will send anything to other people and whether the user has asked for that. Confirm its settings match their preferences; see [workflow settings](https://docs.runorion.com/workflows/manage) when needed.

When changing existing work, say what should change and what still needs to stay the same. Give Orion room to make the changes needed. Avoid broad instructions such as "Preserve everything exactly" when that would keep the problem in place. Only require a particular metric, layout, or format to stay unchanged when the task depends on it.

## Bring back a useful result

Answer the question or show what was created. Explain where the information came from and any gaps that affect how the user can use it. Share links returned by Orion's tools. Check that a saved result does what the user requested; a message saying it was created is not enough to prove that. For a dashboard, check the saved format and requested filters. If you could not open it and test the filters, say so.

Be clear about what has happened: Orion may have proposed something, saved it, run it, or sent it to someone. These are different outcomes. If it needs an answer, show its question. If work is waiting or cannot continue, explain why and what can happen next. Do not invent numbers, IDs, links, or successful actions.

Continue when the user wants to explore or improve the result. Offer a next step when it helps. A useful answer can also be the end of the task; there is no need to always suggest saving information, creating another report, or scheduling future runs.
