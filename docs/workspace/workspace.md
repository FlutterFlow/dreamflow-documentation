---
slug: /workspace
title: Workspace
description: Learn about Dreamflow's integrated workspace panels that provide a complete Flutter development environment with specialized tools for building, testing and deploying applications
tags: [workspace, ui, development, flutter]
sidebar_position: 0
keywords: [workspace, panels, modules panel, content panel, properties panel, agent panel, flutter development, dreamflow interface, development environment]
---

# Workspace

The workspace is organized into panels that work together to provide a complete development experience. 

![workspace-overview](./imgs/workspace.avif)

## Core Panels

- **Top Bar**: Central command center for project navigation, panel management, and deployment. Provides access to project settings, undo/redo functionality, panel visibility controls, and deployment actions.

- **[Modules Panel](modules-panel/widget-panel.md)**: Helps users access different functional areas of the platform. Includes Widget Tree (default navigation), Theme (styling), Assets (file management), Firebase (backend services), and Supabase (database integration). The module panel appears on the left side of the screen, and its content is managed through the left-side rail.

- **[Content Panel](../workspace/content-panel.md)**: Main workspace area that displays either the app preview and/or code editor depending on the selected mode (preview, code or split). Features real-time app preview with device frame options, hot reload/restart controls, and integrated code editor with syntax highlighting and auto-complete. The content panel is in the center of the workspace. 

- **[Properties Panel](../workspace/properties-panel.md)**: Comprehensive property editing interface for selected widgets. Provides visual property editors for colors, text styles, padding, borders, gradients, and more. When you double click on a widget in the Widget Tree or the Preview, the Property Panel is automatically displayed to the right of the Content Panel.  

- **[Agent Panel](../workspace/agent-panel.md)**: AI-powered development assistant that helps you build and modify your Flutter app through natural language conversations. Features streaming conversations, context management, screenshot integration, and support for multiple AI models. The agent panel is to the right of the workspace.

- **Bottom Bar**: Provides essential project status and debugging tools:
  - **Refresh Dependencies**: Runs `flutter pub get` to update project packages
  - **Debug Console**: Toggle to view real-time app logs and debugging output
  - **App Status**: Live indicator showing if your app is running, loading, has errors, or is stopped
  - **Analysis Issues**: Quick overview of errors, warnings, and info messages in your code (coming from the code analyzer)


This integrated workspace approach eliminates the need to switch between different tools and provides a cohesive environment for building, testing, and deploying Flutter applications.

## Keyboard Shortcuts

Keyboard shortcuts help you work faster by reducing reliance on the mouse. You can quickly toggle panels, navigate the canvas, edit widgets, and perform common actions with simple key combinations.

To see a list of all keyboard shortcuts, click on your project name and select the **Keyboard Shortcuts** option.

![keyboard-shortcuts.avif](imgs/keyboard-shortcuts.avif)

Dreamflow currently supports the following keyboard shortcuts:

:::info

- `⌘` represents the **Command** key on macOS. On Windows/Linux, use **Ctrl** instead.
- `⌥` represents the **Option** key on macOS (equivalent to **Alt** on Windows/Linux).

:::

#### Panel Layout

- **Reset all Panel widths to default**: `⌥ 0`
- **Toggle Builder Panel visibility**: `⌥ 2`
- **Toggle Details Panel visibility**: `⌥ 3`
- **Toggle Right Agent Panel visibility**: `⌥ 4`
- **Tab forward between Preview, Inspect, and Code**: `⌥ Tab`
- **Tab backwards**: `⌥ Shift Tab`
- **Toggle Split View**: `⌥ S`
- **Toggle Inspect Mode**: `⌥ Shift I`

#### Editing

- **Undo**: `⌘ Z`
- **Redo**: `⌘ Shift Z`
- **Save File**: `⌘ S`
- **Quick Prompt**: `⌘ K`
- **Copy Widget**: `⌘ C`
- **Cut Widget**: `⌘ X`
- **Paste Widget**: `⌘ V`
- **Delete Widget**: *(Shortcut not assigned)*

#### Navigation

- **Show Command Palette**: `⌘ P`
- **Expand/Select Node or Children**: `→`
- **Collapse/Select Node or Children**: `←`
- **Select Next Visible Node**: `↓`
- **Select Previous Visible Node**: `↑`
- **Select Next Sibling**: `⌘ ↓`
- **Select Previous Sibling**: `⌘ ↑`

#### Settings

- **View all Keyboard Shortcuts**: `⌥ /`
- **Toggle Platform Brightness (Light/Dark Mode)**: `⌥ Shift B`
- **Open Feedback Form**: `⌥ F`