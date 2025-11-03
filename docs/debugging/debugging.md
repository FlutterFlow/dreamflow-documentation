---
slug: /debugging
title: Debugging
description: Practical guidance for debugging project code with Dreamflow agent.
tags: [debugging]
sidebar_position: 1
keywords: [dreamflow debugging, error tracing, agent prompt, generated code, logging]
---

# Debugging

## Layout Issues

### Overflow Errors

An **Overflow Error** occurs when a widget’s content is too large to fit within the available space on the screen or inside its parent widget.

Flutter tries to render all UI elements within fixed layout constraints, and when a widget exceeds those limits, it triggers an overflow, often shown as yellow and black striped bars on the screen and the error message like this in the debug console:

```
A RenderFlex overflowed by 28 pixels on the bottom.
```

#### Why Overflow Errors Occur

Overflow errors typically happen due to one or more of the following reasons:

- A widget’s **content is larger** than the space provided by its parent (for example, long text inside a `Row` or a large image in a small `Container`).
- Missing **scrollable widgets** like `SingleChildScrollView`, `ListView`, or `Expanded` when content should be scrollable or flexible.
- Hard-coded **widths or heights** that don’t adapt to different screen sizes.
- Nesting layout widgets (like `Row`, `Column`, or `Flex`) without proper constraints (`Expanded`, `Flexible`, etc.).

#### Common Examples

- A `Row` containing multiple `Text` widgets with long strings and no wrapping.
- A `Column` with too many child widgets that extend beyond the screen height.
- Fixed-size containers that don’t resize on smaller devices.

#### How to Fix Overflow Errors

Here are some quick tips to fix overflow errors manually:

- Use **`Expanded`** or **`Flexible`** widgets to make child widgets adapt to available space.
- Wrap overflowing content in a **`SingleChildScrollView`** to make it scrollable.
- Use **`TextOverflow.ellipsis`** or `maxLines` for long text content.
- Avoid fixed widths/heights; use responsive layout helpers like `MediaQuery` or `LayoutBuilder`.

#### Using Agent to Fix Overflow Errors

Dreamflow’s Agent can help you quickly identify and fix overflow errors.

**Here’s how to use it:**

1. [**Take a screenshot**](../workspace/agent-panel.md#screenshot-mode) of your app preview showing the overflow error (yellow/black bars).
2. **Describe the issue to the Agent.** Here’s an example prompt:
    
    ```
    I see an overflow error on the screen. Please check the console to find the widget causing it and adjust the layout to fix it.
    ```

    ![fix-with-agent.avif](imgs/fix-with-agent.avif)

3. The **Agent will analyze the logs**, locate the widget and line number causing the overflow, and automatically adjust layout constraints, for example, by adding `Expanded`, `Flexible`, or scrollable containers where needed.
4. Once the fix is applied, the agent will **rerun the preview,** and you can confirm if the overflow error is resolved.