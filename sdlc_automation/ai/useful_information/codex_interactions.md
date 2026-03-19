How do you call codex element where you ask the user to choose an option?

It’s usually called a **multiple-choice prompt** or **choice question**.

If you mean the Codex UI/tooling element specifically, it’s the `request_user_input` prompt with `options`.

----------

Can you set up local automation automatically if i give you a spec and what would be the codex element name?

Yes. If you give me a spec, I can turn it into a Codex automation setup.

The Codex element names are:

- `request_user_input` for asking the user to choose an option
- `::automation-update{...}` for proposing or updating an automation

If you mean the clickable choice UI specifically, it’s `request_user_input` with `options`.

If you want, send the spec plus:
- what it should do
- when it should run
- which workspace(s) it should use

and I’ll map it into the automation format.


----------

`::automation-update{...}` is a special Codex directive, not a normal code syntax. It tells the app to create, suggest, or modify an automation in the UI.

What it can do:
- `mode="suggested create"`: propose a new automation
- `mode="suggested update"`: propose changes to an existing automation
- `mode="view"`: open an existing automation for inspection

Common fields:
- `id`: required for `view` and `suggested update`
- `name`: short human-friendly automation name
- `prompt`: what the automation should do
- `rrule`: the schedule
- `cwds`: workspace paths it should apply to
- `status`: usually `ACTIVE` or `PAUSED`

Example:
```text
::automation-update{mode="suggested create" name="Daily report" prompt="Summarize Sentry errors" rrule="FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0" cwds="/path/to/project" status="ACTIVE"}
```

A few important constraints:
- The prompt should describe the task only, not the schedule or workspace details.
- The schedule is handled by `rrule`.
- The directive should be on its own line.
- If the user asks to look at an existing automation, `mode="view"` is the right one.

If you want, I can also show you:
1. the exact format I’d use for your own spec
2. how it differs from `request_user_input`
3. a few real examples for recurring checks, summaries, or alerts

----------

In which format do you prefer Codex directive communication?

Use the raw directive syntax, on its own line, with no extra prose around it.

Preferred format:
- `::automation-update{...}` for automation create/update/view
- `::code-comment{...}` for review findings
- One directive per line
- Use double quotes for string values
- Keep values single-line
- Use exact field names expected by the directive

Example:
```text
::automation-update{mode="suggested create" name="Daily report" prompt="Summarize Sentry errors" rrule="FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0" cwds="/path/to/project" status="ACTIVE"}
```

If you are giving me a spec instead of a finished directive, plain English is fine. I can convert it into the correct directive format.

----------

How do you use Codex rrule in combination with the ::automation-update{...}, which one to create first and how to link them?

`rrule` is not a separate Codex object you create and then connect later. It is just a field inside `::automation-update{...}`.

So the order is:

1. If needed, ask the user for a choice with `request_user_input`
2. Take that answer and put it into the `rrule` field
3. Emit `::automation-update{...}` with the full automation definition

There is no special “link” syntax. The linkage is simply:
- `request_user_input` collects the choice
- `::automation-update{...}` consumes that choice as `rrule`

Examples:
- New automation: create one `::automation-update{mode="suggested create" ... rrule="..." ...}`
- Existing automation: use `mode="suggested update"` with the existing `id`, and replace `rrule` there

Local reference: [useful_information/codex_interactions.md](/C:/Workspace/Automation/sdlc/useful_information/codex_interactions.md#L30)

If you want, I can show the exact 2-step pattern for “ask user for schedule, then create automation.”

----------

Yes to "If you want, I can show the exact 2-step pattern for “ask user for schedule, then create automation.”".

The pattern is:

1. Ask the user for the schedule choice.
2. Map that answer to an `rrule`.
3. Put that `rrule` into `::automation-update{...}`.

Example flow:

```text
# Step 1: collect the schedule choice
request_user_input(
  question="When should this automation run?",
  options=[
    { label: "Weekly Monday 9:00", value: "FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0" },
    { label: "Weekly Friday 17:00", value: "FREQ=WEEKLY;BYDAY=FR;BYHOUR=17;BYMINUTE=0" },
  ]
)

# Step 2: create the automation using the selected rrule
::automation-update{mode="suggested create" name="Weekly report" prompt="Summarize Sentry errors" rrule="<selected rrule>" cwds="/path/to/project" status="ACTIVE"}
```

If you are updating an existing automation, the only difference is that you include the existing `id` and use `mode="suggested update"`:

```text
::automation-update{mode="suggested update" id="123" name="Weekly report" prompt="Summarize Sentry errors" rrule="<selected rrule>" cwds="/path/to/project" status="ACTIVE"}
```

So the link is just the selected value:
- `request_user_input` produces the choice
- that choice becomes the `rrule` field in `::automation-update{...}`

If you want, I can turn that into a reusable template you can copy for your own automations.

----------

Tell me about how to set up local or branch model of operation, project selection, model, reasoning level, plan mode on/off (If on, how to automatically switch to plan mode), processing speed.

Assuming by “branch” you mean a git branch or worktree:

- `Local` vs `cloud`: Codex CLI runs locally from your terminal and works in the selected directory. Codex web/app runs tasks in a sandboxed cloud environment connected to your GitHub repo. [Codex CLI](https://developers.openai.com/codex/cli), [Codex web](https://developers.openai.com/codex/cloud)
- `Project selection`: local = start Codex inside the repo root or target directory. Cloud = connect GitHub, then pick the repo/environment; the docs describe this as choosing the repo, setup steps, and tools Codex should use. [Codex CLI](https://developers.openai.com/codex/cli), [Codex web](https://developers.openai.com/codex/cloud)
- `Branch/worktree setup`: there is not a separate “branch mode” knob in Codex. The practical setup is to create a branch or worktree first, then run Codex there. That’s an inference from the docs, which call out built-in worktree and git support. [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)
- `Model`: in the current CLI docs, `/model` switches between GPT-5.4, GPT-5.3-Codex, and other available models. The latest model guide says GPT-5.4 is the default for important work, with smaller/faster variants where available. [Codex CLI](https://developers.openai.com/codex/cli), [Using GPT-5.4](https://developers.openai.com/api/docs/guides/latest-model)
- `Reasoning level`: lower reasoning is faster, higher reasoning is more thorough. GPT-5.2-Codex supports `low`, `medium`, `high`, and `xhigh`; GPT-5.4 also supports `none` as the lowest-latency setting. [GPT-5.2-Codex](https://developers.openai.com/api/docs/models/gpt-5.2-codex), [Using GPT-5.4](https://developers.openai.com/api/docs/guides/latest-model)
- `Plan mode`: I did not find a documented Codex “plan mode” toggle. The closest product-level control is the approval-mode workflow in the CLI, or starting a task in a no-changes/suggest-style flow. There is no documented automatic switch into a separate plan mode from a directive. [Codex CLI](https://developers.openai.com/codex/cli)
- `Processing speed`: fastest is usually local + smaller model + low reasoning + low verbosity. Cloud is better for background or parallel work, but it adds orchestration overhead. [Using GPT-5.4](https://developers.openai.com/api/docs/guides/latest-model), [Codex web](https://developers.openai.com/codex/cloud)

If you want, I can turn this into a concrete setup recommendation for one of these:
1. local CLI workflow
2. branch/worktree workflow
3. cloud PR workflow

----------

Can you give me a full prompt for special Codex directive that would create a automation with all of the parameters mentioned in this conversation?

The prompt field should stay task-focused; `rrule` and `cwds` are separate, and I did not find a dedicated plan-mode toggle in `::automation-update`. The local note also says not to put schedule or workspace details in `prompt`, so the prompt below only carries the behavior rules.

```text
::automation-update{mode="suggested create" name="Codex operating profile" prompt="Prefer the fastest reliable available model for routine work, raise reasoning only when the task is complex or ambiguous, keep outputs concise and low-latency, and when requirements are incomplete switch into planning behavior and do not edit files until the missing decision is resolved; once the request is complete, proceed to execution." rrule="<RRULE>" cwds="C:/Workspace/Automation/sdlc" status="ACTIVE"}
```

Replace `<RRULE>` with the schedule you want. Branch/worktree and project selection come from the workspace you point `cwds` at and whatever is already checked out there.

Sources: [Codex CLI](https://developers.openai.com/codex/cli), [Codex web](https://developers.openai.com/codex/cloud), [Using GPT-5.4](https://developers.openai.com/api/docs/guides/latest-model), [GPT-5.2-Codex](https://developers.openai.com/api/docs/models/gpt-5.2-codex), [local directive notes](/C:/Workspace/Automation/sdlc/useful_information/codex_interactions.md#L30)

----------

Give me <RRULE> example.

`<RRULE>` example: `weekly Monday at 09:00`.

Another valid shape is: `every 6 hours`.

If you want, I can plug one into the full `::automation-update{...}` template for you.

----------

Optimize prompt so that there is a model, and reasoning level involved:

::automation-update{mode="suggested create" name="Codex operating profile" prompt="Prefer the fastest reliable available model for routine work, raise reasoning only when the task is complex or ambiguous, keep outputs concise and low-latency, and when requirements are incomplete switch into planning behavior and do not edit files until the missing decision is resolved; once the request is complete, proceed to execution." rrule="<RRULE>" cwds="C:/Workspace/Automation/sdlc" status="ACTIVE"}

This is the cleaner version. It makes model and reasoning preference explicit, but `::automation-update` still only carries instructions; actual runtime model switching is handled in the Codex client, not inside the automation directive. [Codex CLI](https://developers.openai.com/codex/cli)

```text
::automation-update{mode="suggested create" name="Codex operating profile" prompt="Prefer GPT-5.4 for general reasoning and planning, and GPT-5.3-codex for code-heavy or tool-heavy work. Default to reasoning.effort=medium; use low for simple tasks and high or xhigh only when the task is complex, ambiguous, or high-risk. Keep responses concise and low-latency. If requirements are incomplete, pause in planning behavior, do not edit files, and ask for the missing decision before proceeding. Once the request is complete, execute directly." rrule="FREQ=HOURLY;INTERVAL=1" cwds="C:/Workspace/Automation/sdlc" status="ACTIVE"}
```

Current docs: GPT-5.4 is the default general-purpose model, GPT-5.3-Codex is optimized for agentic coding, and the CLI supports switching models and reasoning levels via `/model`. [Using GPT-5.4](https://developers.openai.com/api/docs/guides/latest-model), [GPT-5.3-Codex](https://developers.openai.com/api/docs/models/gpt-5.3-codex), [Codex CLI](https://developers.openai.com/codex/cli)

----------

What are all the variables that can be used inside ::automation-update{}

In the Codex directive format available here, the attributes you can use inside `::automation-update{...}` are:

- `mode`
  Valid values: `view`, `suggested update`, `suggested create`
- `id`
  Required for `mode="view"` and `mode="suggested update"`
- `name`
  Used for create/update
- `prompt`
  Used for create/update
- `rrule`
  Used for create/update
- `cwds`
  Used for create/update
  Can be a comma-separated string or a JSON-array string
- `status`
  Used for create/update
  Typically `ACTIVE` or `PAUSED`

Practical rules:
- `suggested create`: use `name`, `prompt`, `rrule`, `cwds`, `status`; omit `id`
- `suggested update`: use `id`, `name`, `prompt`, `rrule`, `cwds`, `status`
- `view`: `id` is required; other fields are optional

Example shapes:

```text
::automation-update{mode="suggested create" name="Daily report" prompt="Summarize Sentry errors" rrule="FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0" cwds="C:/Workspace/Automation/sdlc" status="ACTIVE"}
```

```text
::automation-update{mode="suggested update" id="123" name="Daily report" prompt="Summarize Sentry errors" rrule="FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0" cwds="C:/Workspace/Automation/sdlc" status="ACTIVE"}
```

```text
::automation-update{mode="view" id="123"}
```

There are no documented first-class fields here for `model`, `reasoning`, `branch`, `project selection`, `plan mode`, or `processing speed`. If you want those behaviors, they have to be expressed inside `prompt`, not as separate directive attributes.

----------

Is there ::automation-create{} and ::automation-delete{} and what are their options if they exist?

I do not have evidence that `::automation-create{}` or `::automation-delete{}` exist as supported Codex directives.

What is defined in this environment is a single directive:

- `::automation-update{...}`

Its supported attributes are:

- `mode`
  Values: `view`, `suggested create`, `suggested update`
- `id`
  Required for `view` and `suggested update`
- `name`
- `prompt`
- `rrule`
- `cwds`
- `status`

So, in practice:

- create: `::automation-update{mode="suggested create" ...}`
- update: `::automation-update{mode="suggested update" id="..." ...}`
- inspect/open: `::automation-update{mode="view" id="..."}`

I do not see a documented delete directive or delete-specific option inside `::automation-update{...}`. If you need “delete” behavior, that appears to be handled outside this directive surface, likely in the UI rather than via a special `::automation-delete{}` command.

Example create:
```text
::automation-update{mode="suggested create" name="Daily report" prompt="Summarize Sentry errors" rrule="FREQ=HOURLY;INTERVAL=1" cwds="C:/Workspace/Automation/sdlc" status="ACTIVE"}
```

Example update:
```text
::automation-update{mode="suggested update" id="123" name="Daily report" prompt="Summarize Sentry errors" rrule="FREQ=HOURLY;INTERVAL=1" cwds="C:/Workspace/Automation/sdlc" status="PAUSED"}
```

Sources: [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan), [local automation note](/C:/Workspace/Automation/sdlc/useful_information/codex_interactions.md#L30)

What I found and what’s missing: the public OpenAI docs I checked confirm that the Codex app has automations, but they do not document a public directive list for `::automation-create{}` or `::automation-delete{}`. The only directive schema available in this environment is `::automation-update{...}`.

----------