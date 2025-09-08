---
slug: /workspace/content-panel
title: Content Panel 
# description: 
# tags: 
sidebar_position: 3
# keywords: 
---

# Content Panel

The Content Panel is the central workspace area where you can view and edit your application code, preview your app, and access debugging information. It provides a comprehensive development environment with multiple views and tools to help you build and test your applications.

## Overview

The Content Panel consists of three main sections that work together to provide a complete development experience:

- **Code Editor**: View and edit your Flutter app source code. 
- **App Preview**: The application is running in real-time for you to test any logic or UI changes quickly. 
- **Debug Console**: Monitor any debug or print information once you run the app.

:::info[Editor Modes]

The content panel integrates with three main editor modes accessible via the top toolbar:
- **Preview Mode**: Shows only the app preview with device frame styling. Ideal for focused visual development and testing.
- **Code Mode**: Displays only the Monaco code editor without preview. Perfect for intensive coding sessions.
- **Split Mode**: Shows both preview and code editor side-by-side with adjustable split ratio. 
:::

## Code Editor

The Code Editor is located on the left side of the Content Panel and provides a powerful environment for writing and editing your Flutter code.



:::tip
You can swap the positions of the preview and code editor by clicking on this icon at the top right of your Content Panel.
// todo image
:::

The Code editor is built on **Monaco Editor** (the same editor that powers VS Code) and provides a full-featured coding experience. It includes syntax highlighting, auto-completion, and IntelliSense for Dart/Flutter development. The editor supports multi-file editing with tabs, real-time collaboration features, and integrates seamlessly with the platform's live preview system. It also includes advanced features like go-to-definition, find references, and code formatting that you'd expect from a professional IDE.



## App Preview

The App Preview panel is the central component of Dreamflow's environment, providing real-time preview of Flutter applications with advanced inspection and editing capabilities.

The panel displays a real-time preview of your Flutter app running in **debug mode**, with instant updates as you make code changes. The preview runs in a WebView container and supports hot reload for immediate feedback during development.

### Inspect Mode
Inspect mode provides an interactive way to explore and modify your Flutter widgets visually. When enabled, hovering over widgets in the preview reveals their boundaries with colored overlays, making it easy to understand widget layout and hierarchy. This visual feedback helps developers quickly identify and understand the structure of their UI components.

Selecting a widget with a click automatically synchronizes the [Widget Tree](#) and [Property Panel](#) to display detailed information about that widget, maintaining the highlight until another selection is made. This seamless integration between the preview and development panels streamlines the workflow for analyzing and modifying widgets. The context menu, accessed through right-click, offers powerful widget-specific actions including property editing, adding context to agent, code navigation, and other operations, enabling rapid iterations on your Flutter application's user interface.

### Hot Reload and Hot Restart
Dreamflow provides integrated hot reload and hot restart capabilities that allow you to quickly test code changes without losing your development context. These essential Flutter development tools are accessible through dedicated buttons in the content panel toolbar.

**Hot Reload (⚡)** applies your code changes instantly while preserving the current application state. This is ideal for UI modifications, styling updates, and minor code changes. The operation typically completes in under 250ms and maintains your app's navigation stack, variables, and user interactions.

**Hot Restart (↶)** completely restarts your Flutter app with all code changes applied, resetting the application state. Use this for structural changes, when hot reload fails, or after fixing compilation errors. The system intelligently prevents restart attempts when compilation errors are detected.


### Additional Features
Additionally it has other features: 

#### Multi-Device Preview

Choose from four preview modes to test your app across different form factors:
- Phone (iPhone 16 Pro Max - 390x844)
- Tablet (iPad Pro 13" - 834x1194)
- Desktop (1920x1080 landscape)
- Expanded (full-width preview without device frame)

#### Interactive Zoom & Pan

The preview supports zoom levels from 30% to 300% with smooth panning capabilities. Zoom preferences are automatically saved and restored between sessions.

#### Theme Support

Preview both light and dark themes for your Flutter app. 



## Debug Console

The Debug Console is a dedicated output panel in Dreamflow that displays real-time logs and debug information from your Flutter application. This includes:

- Print statements from your Dart code
- Flutter framework messages 
- Hot reload notifications
- Build process output
- Error messages and stack traces

