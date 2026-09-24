# Orion Coach

A skill for **ChatGPT, Codex, or Claude** that complements the [Orion MCP connector](https://docs.runorion.com/mcp/overview). Your assistant uses relevant context about your work to ask Orion better questions, prepare Knowledge Base pages, and request metrics, dashboards, slide decks, and workflows. It checks the results and brings them back into your conversation.

The skill lives in your assistant. Orion provides the connected data analysis and saved deliverables. Product guidance comes from the Orion documentation linked in the skill; available actions depend on your connected tools and account permissions.

## Get started

1. [Connect Orion through MCP](https://docs.runorion.com/mcp/setup) and authenticate with your Orion account. The server URL is `https://g.runorion.com/mcp`.
2. Add the skill using the instructions below.
3. Paste the starter prompt into your assistant, ideally in a conversation with relevant context about your work.

Without an Orion connection, the assistant can still prepare a brief and a question to paste into Orion.

### Claude

[Download the ZIP](orion-coach-skill.zip?raw=true) without unzipping it. In **Customize → Skills**, choose **+ → Create skill → Upload a skill**, upload the ZIP, and enable it. Skills require code execution and may need to be enabled by your organization. See [Claude's installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### ChatGPT

Download [SKILL.md](orion-coach/SKILL.md?raw=true) and add it to a project for your Orion work. Add the project instruction: **"Read the attached SKILL.md and follow Orion Coach when helping me with Orion."** See the [ChatGPT quickstart](https://learn.chatgpt.com/docs/quickstart).

Use an Orion connection if your workspace exposes its tools. Adding the file does not establish the connection.

### Codex

Save [SKILL.md](orion-coach/SKILL.md) at `~/.agents/skills/orion-coach/SKILL.md` for personal use, or `.agents/skills/orion-coach/SKILL.md` in your repository. Connect Orion's MCP server separately, then ask Codex to **use Orion Coach**. See [Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

## Starter prompt

```text
Use Orion Coach to help me get my first useful result from Orion.

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

Already know what you want? Ask directly: "Build a customer health dashboard in Orion using our existing metrics. Keep it private," or "Turn this validated analysis into a workflow that runs Mondays at 8 a.m. America/New_York with no email notifications."

## Maintaining the download

`orion-coach/SKILL.md` is the source of truth. After editing it, update its version date and regenerate the ZIP from the repository root:

```bash
python3 -m zipfile -c skills/orion-coach-skill.zip skills/orion-coach
```

The archive should contain the `orion-coach/` folder with `SKILL.md` inside. Keep any copies distributed through the Orion docs in sync with the reviewed skill. Installation does not enable automatic updates; users replace their installed copy to get a new version.
