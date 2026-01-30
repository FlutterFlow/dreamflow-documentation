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

Many coding prompts requests contain hidden ambiguity. A prompt like “Create this UI” or “Add favorites feature” can imply different data sources, navigation patterns, persistence, UX behavior, and architecture. If you do not specify these, the Agent has to guess, which can lead to extra code, mismatched behavior, more back-and-forth iterations, and higher credit usage due to unnecessary generation.

This guide explains how to prompt effectively, based on real research and practical experimentation with coding agents.

### Ask Clarifying Questions

A reliable way to improve outcomes is to instruct the Agent to ask clarifying questions before writing code. For example:

```jsx
Before writing any code, analyze my request. If there is any ambiguity in scope, behavior, data, or implementation, ask clarifying questions first. Do not proceed until I answer.
```

This approach works because human engineers naturally ask clarifying questions before writing code, and coding agents produce better results when they follow the same discipline.

In practice, this keeps you firmly in control of architectural decisions while preventing the agent from inventing or assuming requirements. As a result, the final implementation aligns much more closely with your original intent, both in structure and behavior.

:::tip[Reduced Credit Usage]

Clarifying questions can reduce credit usage because the Agent spends less effort exploring multiple interpretations. When your requirements are precise, the Agent can focus its effort on what you actually want rather than implementing assumed features or alternate paths.

:::

### Keep Tasks Small and Focused

Dreamflow's AI Agent is strongest when you break the task into small, reviewable steps.

Prefer prompts like:

- “Create the layout for the header and filters.”
- “Add persistence for favorites only.”
- “Wire the provider for this screen.”
- “Implement routing for this flow.”

Avoid one-shot prompts that attempt to build large chunks of the app at once. Smaller tasks are easier to validate and reduce downstream refactors.

### Avoid Confidence-Based Instructions

Avoid prompts like “If you are less than 95% confident, ask questions.” A model’s self-assessed confidence is not a dependable signal of correctness. Instead, make clarification the rule whenever ambiguity exists, without relying on confidence thresholds.

:::tip[Characteristics of a Good Prompt]
- Goal and scope: what you want, and what you explicitly do not want
- Where it belongs: feature/module name, folder location, or the file(s) to modify
- Data and persistence: mock vs backend, and whether it must persist across sessions
- UX rules: loading, empty, error states, and any visual indicators
:::

## Prompting for Architecture

Dreamflow can go beyond prototypes when you prompt with architectural intent. The key is to treat the Agent as a fast implementer that follows your system design, not as a tool that invents your system design.

### Think Like an Architect

If you do not specify architecture, the Agent will infer one. Inference is where inconsistency and refactor-heavy codebases come from. Start by choosing your architecture, core libraries, and folder conventions, then have the Agent implement within those boundaries.

Include specifics such as:

- Architectural pattern (layered, feature-based, clean architecture)
- State management (Provider, Riverpod, BLoC)
- Routing (GoRouter, Navigator 2.0)
- Networking (Dio, http)
- Data modeling (Freezed, json_serializable)
- Storage (SharedPreferences, SQLite, Supabase/Firebase)

### Scaffold Structure Before Writing Code

A strong pattern is to have the Agent set up the project shape first.

Example prompt:

```jsx
Create a task management app using feature-based architecture and BLoC for state management. Use GoRouter for navigation, Dio for networking, Freezed for data models, and SharedPreferences for local storage. Create the folders and files and update pubspec.yaml, but do not write any implementation code yet.
```

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