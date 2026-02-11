---
slug: /prompting-effectively
title: Prompting Effectively
description: Best practices for writing clear, structured prompts in Dreamflow to get accurate, efficient, and maintainable code from the Agent.
tags: [ai]
sidebar_position: 1
keywords: [dreamflow prompting, ai prompting best practices, coding agent prompts, dreamflow agent, prompting, architectural prompting, ai-assisted development]
---

# Prompting Effectively

Dreamflow’s agent is most effective when you treat it like a **collaborative developer**, not a one-shot code generator. Clear prompts, resolved ambiguity, and small scopes lead to better code, lower credit usage, and more predictable results.

Many coding prompts requests contain hidden ambiguity. A prompt like “Create this UI” or “Add favorites feature” can imply different data sources, navigation patterns, persistence, UX behavior, and architecture. If you do not specify these, the agent has to guess, which can lead to extra code, mismatched behavior, more back-and-forth iterations, and higher credit usage due to unnecessary generation.

This guide explains how to prompt effectively, based on real research and practical experimentation with coding agents.

### Ask Clarifying Questions

A reliable way to improve outcomes is to instruct the agent to ask clarifying questions before writing code. For example:

```jsx
Before writing any code, analyze my request. 
If there is any ambiguity in scope, behavior, data, or implementation, ask clarifying questions first. 
Do not proceed until I answer.
```

This approach works because human engineers naturally ask clarifying questions before writing code, and coding agents produce better results when they follow the same discipline.

In practice, this keeps you firmly in control of architectural decisions while preventing the agent from inventing or assuming requirements. As a result, the final implementation aligns much more closely with your original intent, both in structure and behavior.

:::tip[Reduced Credit Usage]

Clarifying questions can reduce credit usage because the agent spends less effort exploring multiple interpretations. When your requirements are precise, the agent can focus its effort on what you actually want rather than implementing assumed features or alternate paths.

:::

### Keep Tasks Context Aware

The agent produces the best results when it knows **exactly which part of the app you’re referring to** and **what kind of change you want to make**. Vague prompts force the agent to scan and infer intent, which increases ambiguity and the chance of incorrect changes.

Instead of starting with a big or vague request and refining it later, aim to provide clear context and scope in your very first prompt so the task is well-defined from the beginning.

Whenever possible, explicitly identify the widget or section you want to modify. You can do this in the following ways:

#### Add Widget to Agent

A strong workflow is to [add widget to agent](../workspace/agent-panel.md#add-to-agent) first, then prompt the agent. This anchors the task to a specific part of the widget tree and removes guesswork.

For example, after adding the Text widget to the agent’s context, you can write a prompt such as:

*"Animate this widget on load with a quick count-up effect. 
The animation should start from 0 and increment smoothly to the final value."*

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/ennIBbg31xRoLOpOL8wU?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

Here’s another example prompt describing the behavior (and not just appearance) the agent should implement on the attached widget:

*"Update the arrow and percentage badge color to change dynamically based on the value. 
Use green for positive growth and red for negative growth. 
Don’t change the rest of the card’s styling."*


<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/UTrMKHgveSs3f629cpvu?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

#### Add Screenshot to Agent

[Adding screenshot](../workspace/agent-panel.md#screenshot-mode) gives the agent a holistic view of the UI, including layout structure, spacing, visual hierarchy, colors, and relative positioning. This reduces the need for the agent to infer how different widgets relate to each other, which can be difficult to express precisely using text alone.

Using a screenshot is often more effective when:

- The change affects multiple widgets at once.
- The task is more visual, such as alignment, spacing, animation flow, or theming.
- You want the agent to understand the overall context of the screen.

Once the screenshot is added, clearly describe the desired behavior or change you want the agent to implement, and reference visual elements directly from the screenshot. For example:

*"Using the attached screenshot as context, add a Light / Dark mode toggle button to the top-right area of the dashboard header. 
The toggle should switch the entire app theme between light and dark modes, including background colors, cards, text, charts, and sidebar.
Persist the user’s theme preference across sessions, and keep the existing layout and spacing unchanged."*

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/HR64H4OmwefAX3JOTxA1?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

#### Add Image to Agent

Instead of making design changes manually, you can let the agent interpret the image and apply the updates for you. Images work especially well when the goal is to **match a visual design** rather than modify the behavior of a specific widget. The agent can infer layout, spacing, typography, color usage, hierarchy, and component styling directly from the image and apply those changes.

After [adding the image](../workspace/agent-panel.md#image-attachments), describe **what the image represents** and **how it should be applied**. Be explicit about what should change and what should remain untouched. For example:

*"Use the attached design image as the source of truth for the dashboard cards.
Update spacing, typography, border radius, and shadow styles to match the image.
Do not change layout structure outside the cards or existing business logic."*

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/KSwH8nvw2p1QWU5uFZrC?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

#### Use Follow-Up Thread

The **Follow-up** thread builds on the agent’s existing understanding of the task.

This is ideal when:

- You are refining or adjusting a change the agent just made
- You want to tweak behavior, styling, or logic without re-explaining context

Because the agent retains prior context, follow-ups are faster and require less repetition. This works best for incremental improvements within the same feature or UI area.

![followup-thread.avif](imgs/followup-thread.avif)


## Ask for a Plan

Large changes often fail because the agent starts implementing before constraints are clear. Asking for a plan first helps you catch scope creep early, confirm the right approach, and avoid unnecessary edits.

Use this pattern:

```jsx
Before writing code:
1) Propose a step-by-step plan.
2) List the exact files you will modify or create.
3) Call out any assumptions and any missing requirements.
4) Identify risks or tradeoffs (if any).
Do not implement until I confirm.
```

:::tip
- Ask for a short plan (5–10 steps) and a clear “what changes where” file list.
- Ask the agent to separate “must do” steps from “nice to have.”
- If the agent needs to refactor, it should ask first.
:::

Example follow-up after the plan:

```jsx
Ok, go ahead. But keep changes minimal and only touch the listed files. If you need to touch any additional file, stop and ask first.
```

This reduces unexpected edits and keeps you in control of the change.

## Use an “Options First” Pattern for Decisions

Ask the agent to propose options rather than guessing. This prevents lock-in to an approach you did not choose and makes tradeoffs explicit.

For example, after attaching a screenshot of the current screen to the agent, you can use a prompt like the following:

```jsx
I want to add offline caching for this screen.

Propose 2 approaches:
A) SharedPreferences
B) SQLite

For each approach, include:
- Pros/cons
- Complexity (low/medium/high)
- Performance considerations
- Migration impact (if any)
- Which files would change
- A recommended option with reasoning

Do not implement until I choose.
```

Optional refinement (keeps the conversation efficient):

```jsx
Keep the comparison under 12 bullet points total.
End with: "My recommendation: A or B"
```

This keeps decisions explicit and reduces rewrites later.

## Define Acceptance Criteria Like a Test

When you specify acceptance criteria precisely, the agent makes fewer assumptions and produces code that matches your intent.

For example:
```jsx
Acceptance criteria:
- Tapping the "Subscriptions" card navigates to subscriptions screen
- If API returns empty list, show an empty state with CTA
- If API errors, show retry button and preserve previous data
- No changes to other dashboard cards
```

If you can’t describe “done,” the agent can’t reliably hit it.

## Handle Multi-Step Work With Checkpoints

Dreamflow agent support **[Restore Checkpoint](../workspace/agent-panel.md#restore-checkpoint)**, which lets you revert your entire project to the exact state it was in before a specific prompt was executed. Because of this safety net, you can structure larger tasks into controlled steps instead of attempting everything at once.

For such tasks, ask the agent to stop at checkpoints. This keeps the work reviewable and prevents the agent from building too far ahead on a wrong assumption.

For example:

```jsx
Implement in checkpoints:
Checkpoint 1: Create files + folder structure only
Checkpoint 2: Implement models + repository
Checkpoint 3: Implement UI + states
Checkpoint 4: Add tests

After each checkpoint:
- Summarize what changed
- List files touched/created
- Call out any assumptions
- Wait for my confirmation before continuing
```


## Avoid Confidence-Based Instructions

Avoid prompts like “If you are less than 95% confident, ask questions.” A model’s self-assessed confidence is not a dependable signal of correctness. Instead, make clarification the rule whenever ambiguity exists, without relying on confidence thresholds.

:::tip[Characteristics of a Good Prompt]
- Goal and scope: what you want, and what you explicitly do not want
- Where it belongs: feature/module name, folder location, or the file(s) to modify
- Data and persistence: mock vs backend, and whether it must persist across sessions
- UX rules: loading, empty, error states, and any visual indicators
:::

## Prompting for Architecture

Dreamflow can go beyond prototypes when you prompt with architectural intent. The key is to treat the agent as a fast implementer that follows your system design, not as a tool that invents your system design.

### Think Like an Architect

If you do not specify architecture, the agent will infer one. Inference is where inconsistency and refactor-heavy codebases come from. Start by choosing your architecture, core libraries, and folder conventions, then have the agent implement within those boundaries.

Include specifics such as:

- Architectural pattern (layered, feature-based, clean architecture)
- State management (Provider, Riverpod, BLoC)
- Routing (GoRouter, Navigator 2.0)
- Networking (Dio, http)
- Data modeling (Freezed, json_serializable)
- Storage (SharedPreferences, SQLite, Supabase/Firebase)

### Scaffold Structure Before Writing Code

A strong pattern is to have the agent set up the project shape first.

Example prompt:

*"Create a task management app using feature-based architecture and BLoC for state management. Use GoRouter for navigation, Dio for networking, Freezed for data models, and SharedPreferences for local storage. Create the folders and files and update pubspec.yaml, but do not write any implementation code yet."*

This gives you a clean structure you can review before any logic is added.

### Separate Architecture from Implementation

Treat architecture and implementation as two different steps:

1. Structure and dependencies
2. Feature-by-feature implementation

This reduces churn because structure decisions are expensive to change later, while implementation can iterate quickly once the foundation is correct.


### Use Project Rules

If you find yourself repeating architectural constraints in prompts, define them once as [Project Rules](../workspace/agent-panel.md#project-rules).

- Put global rules in a root `AGENTS.md` so they apply everywhere
- Put feature-specific rules in nested `AGENTS.md` files so they apply only when working in that folder
- Keep root rules short to avoid bloating context and slowing responses

With strong rules in place, your prompts can stay short while still producing consistent, production-ready output.

### Video Guide

To dive deeper into prompting the agent effectively, watch this video.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://www.youtube.com/embed/eFtTpmtIujo"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>