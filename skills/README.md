# Orion Guide

A skill for **ChatGPT, Codex, or Claude** that complements the [Orion MCP connector](https://docs.runorion.com/mcp/overview). Your assistant uses relevant context about your work to ask Orion better questions, prepare Knowledge Base pages, and request metrics, dashboards, slide decks, and workflows. It checks the results and brings them back into your conversation.

The skill lives in your assistant. Orion provides the connected data analysis and saved deliverables. Product guidance comes from the Orion documentation linked in the skill; available actions depend on your connected tools and account permissions.

Read the [Orion Guide documentation](https://docs.runorion.com/mcp/orion-guide) for installation, the onboarding prompt, and examples of what to create.

## Get started

1. [Connect Orion through MCP](https://docs.runorion.com/mcp/setup) and authenticate with your Orion account. The server URL is `https://g.runorion.com/mcp`.
2. Add the skill using the instructions below.
3. Paste the starter prompt into your assistant, ideally in a conversation with relevant context about your work.

Without an Orion connection, the assistant can still prepare a brief and a question to paste into Orion.

### Claude

[Download the ZIP](orion-guide-skill.zip?raw=true) without unzipping it. In **Customize → Skills**, choose **+ → Create skill → Upload a skill**, upload the ZIP, and enable it. Skills require code execution and may need to be enabled by your organization. See [Claude's installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### ChatGPT

Download [SKILL.md](orion-guide/SKILL.md?raw=true) and add it to a project for your Orion work. Add the project instruction: **"Read the attached SKILL.md and use Orion Guide when helping me with Orion."** The skill is entirely contained in that one file. See the [ChatGPT quickstart](https://learn.chatgpt.com/docs/quickstart).

Use an Orion connection if your workspace exposes its tools. Adding the file does not establish the connection.

### Codex

Save [SKILL.md](orion-guide/SKILL.md) at `~/.agents/skills/orion-guide/SKILL.md` for personal use, or `.agents/skills/orion-guide/SKILL.md` in your repository. No additional skill files are required. Connect Orion's MCP server separately, then invoke the skill with **`$orion-guide`** in your prompt. See [Codex skill locations and invocation](https://learn.chatgpt.com/docs/build-skills).

## Starter prompt

Explicitly request Orion Guide for your first session using the prompt below. Installed skills can also be selected automatically for matching requests, but selection is not guaranteed. In ChatGPT's project-file setup, keep the project instruction above so the assistant knows to read the file.

```text
Use Orion Guide to help me get my first useful result from Orion.

Use relevant context you can actually access about my work and goals to
draft a short brief. Show me what you would share and where before
transferring it. Leave out unrelated personal or other clients' information.

Find the right Orion project and recommend a useful question its data
could answer. Once we agree on the question and context, use Orion to
answer it and show me the result here. If my goal calls for a metric,
dashboard, slide deck, or workflow, help me create that in Orion.

Save reusable context if I approve, and tell me if I need to enable
Knowledge Base pages for the project. Ask only for missing details
needed to proceed.
```

Already know what you want? Ask directly: "Build a customer health dashboard in Orion using our existing metrics," or "Turn this validated analysis into a workflow that runs Mondays at 8 a.m. America/New_York." Include your preferences when you have them; Orion can help you choose the remaining settings.
