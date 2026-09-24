# Orion MCP operations

Read the section relevant to the current task. These are tool and product details, not a required sequence for every Orion request. Connected tool descriptions take precedence if their contracts differ.

## Identity and scope

If a tool requires `user_id`, use authenticated identity or match the user's known identity against `list_users`. That list does not identify the caller by itself; ask if ambiguous. Resolve the target project before sending data or requests, reusing the project already established when appropriate.

## Running requests and confirmations

- **Still running:** Use the returned conversation ID with `get_conversation_history`, waiting at least 30 seconds between polls. Continue until a result, checkpoint, failure, or the client's wait limit. If stopping, report pending work with its ID.
- **Checkpoint:** Show the questions and send the user's answers in `checkpoint_answers` with the exact question or assumption IDs. Also restate the answers in `message`; text alone does not register them. If a response mentions a card but omits its questions or IDs, retrieve them if possible or direct the user to the checkpoint in Orion. Do not guess IDs or approvals.
- **Full Analysis offered:** When `can_escalate` is true, explain that it may take longer and ask whether to continue. After explicit agreement, call `continue_with_full_analysis` with the exact question and IDs from the handoff. Do not send a consent message to `ask_orion`. If escalation is unavailable, explain the limitation.
- **Recorded:** The message was saved without starting analysis. Explain the returned reason.
- **Timeout:** Check the conversation and relevant object list before retrying. Work may continue after the client times out. Retain the conversation ID and report uncertain completion as pending; do not duplicate creation requests.

Orion may preview an analysis or output and require confirmation before saving or building it. Follow the actual response instead of assuming every operation has the same gate. A proposal or failed dry run is not a created object.

## Knowledge Base changes

For an authorized write, search for a matching page and read it before editing. Use `create_wiki_page` or `update_wiki_page` when available, preserving unrelated content. Creation may apply immediately; updates may apply or become review requests. Report the returned status and verify saved content with `get_wiki_page` when possible. On a permission error, provide the draft for an authorized user instead of retrying the same write.

Saving a page does not by itself enable it for a project. Check whether it is enabled or included as a Global or Group Default. If not, and no tool can enable it, direct the user to Project Settings → Knowledge Base to select and save it. Include the approved context in the current analysis request while enablement is pending.

A Knowledge Base folder is organization, not proof of private access. Match shared context to its intended audience. See [Knowledge Base](https://docs.runorion.com/knowledge-base/creating-pages) and [project settings](https://docs.runorion.com/core-concepts/projects).

## Saved outputs and workflows

Use `list_metrics`/`get_metric`, `list_artifacts`/`get_artifact`, or `list_workflows`/`get_workflow` to inspect the relevant saved object. Match its returned ID and check the content and settings that matter to the request. Use `ask_orion` for creation when no dedicated tool is exposed; do not invent tool names.

For generated workflow outputs, use the run ID from `run_workflow` or `get_workflow_runs`, then `get_workflow_run_reports` and `get_workflow_report_content`. Check run status as well as outputs: one available report does not prove the whole run succeeded.

Inspect a workflow's delivery settings before running it and obtain missing authorization if it sends outputs to others. Honor existing authorization; do not infer permission to schedule or share from an onboarding request. If the user requests notifications disabled, check recipients and notification steps: a blank notification condition means notify on every run, not disabled email. See [workflow settings](https://docs.runorion.com/workflows/manage) and [delivery](https://docs.runorion.com/workflows/outputs).

## Native dashboards

When the requested result is a native Dashboard, its saved artifact type is `interactive_dashboard`. A `webpage`/`html` report (`html_dashboard` artifact) remains a webpage even if it contains JavaScript controls. If the requested type is unavailable, explain the limitation and discuss alternatives instead of silently substituting one.

For a native Dashboard workflow output, ask Orion to create or reuse the native dashboard seed and attach its actual returned reference to an `interactive` report step. Verify the saved seed reference and report format; changing only the format string is insufficient. Let Orion author the supported schema rather than inventing IDs or storage paths.

When checking requested filters, compare affected cards against the selected population, including combined filters and Clear where available. Weighted rates should use pooled numerators and denominators. Intentionally unfiltered cards and narrative based on the full dataset should be identified. Correct unfiltered totals or successful execution alone do not verify filter behavior. If the browser is unavailable, report the checks that remain unverified. See [Filter and Explore](https://docs.runorion.com/dashboards/explore).
