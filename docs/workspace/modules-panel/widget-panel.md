---
slug: /workspace/widget-tree
title: Widget Tree 
description: Learn about the Widget Tree panel in Dreamflow, a powerful hierarchical view that displays and helps you manage your Flutter app's widget structure
tags: [widgets, ui, widget-tree, flutter, dreamflow, components]
keywords: [widget tree, flutter widgets, ui components, widget hierarchy, widget management, widget structure, dreamflow interface, widget navigation, widget properties, widget selection]
sidebar_position: 1

---

# Widget Tree

The Widget Tree panel is a powerful hierarchical view that displays the complete structure of your Flutter app's widget tree, providing comprehensive tools for navigation, inspection, and modification of your UI components.

**Hierarchical Tree View**: Displays your app's widget structure as an expandable tree, showing the parent-child relationships between widgets. Each node represents a widget with its type, properties, and children clearly visible.

**Real-Time Synchronization**: The tree automatically updates in real-time as you make changes to your code, reflecting the current state of your running Flutter app.

**Widget Selection**: Click on any widget in the tree to select it, which automatically highlights the corresponding widget in the preview panel and updates the property panel with its details.

![Widget Tree Panel](../imgs/widget-tree.png)

*The Widget Tree panel displays a hierarchical view of the selected page/screen, showing the complete widget tree including the Scaffold structure and any custom widgets used within it.*


:::info[View Modes]

**Consolidated View**: Hides structural widgets or Modifiers like `Expanded`, `Padding` to provide a cleaner, more focused view of your actual UI components.

**Detailed View**: Shows every widget in the tree, including all structural and layout widgets, giving you complete visibility into the widget hierarchy.
<p></p>
![Widget Tree View Modes](../imgs/widget-tree-view-mode.png)


:::


## Widget Management

Right-click on any widget to access a comprehensive context menu with options for:
- Adding new widgets
- Wrapping existing widgets
- Copying, cutting, and pasting widgets
- Taking screenshots for AI context
- Navigating to component definitions
- Removing widgets

### Add Widget
Insert new widgets into your tree by selecting a parent widget and choosing from a categorized catalog of available widgets (Framework, Project, Dependencies). For structural widgets like Scaffold, you will see a list of property-specific widgets that can be added as children.


<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/Xb10bs310XYTGNS6Uf1H?embed&show_copy_link=true"
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


Here's a quick demo to show you can add a widget to a Column:

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/3eXOPIUfeFG3StCJv5H4?embed&show_copy_link=true"
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

:::tip[Right-Click to Add Widget]
For quick access to widget options, right-click on any existing widget to open the context menu. This provides an alternative way to add new widgets to your layout.
:::

### Wrap Widget
Wrap existing widgets with containers, padding, or other layout widgets to modify their behavior without changing their core functionality.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/2Hdtm30YQkY9xy4zFhKv?embed&show_copy_link=true"
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

### Clipboard Operations
The context menu provides standard clipboard operations (cut, copy, paste) that allow you to move and duplicate widgets across your layout tree. You can use either the context menu options or familiar keyboard shortcuts:

- **Cut**: Ctrl/Cmd + X
- **Copy**: Ctrl/Cmd + C  
- **Paste**: Ctrl/Cmd + V

These operations enable efficient widget reuse and layout restructuring without having to recreate widgets from scratch.

### Go to Code
The "Go to Code" and "Go to Component" features provide quick navigation from the widget tree to the underlying [code implementation](../content-panel.md#code-editor). You can access these features by hovering over a widget in the tree and right-clicking on the widget to use the context menu options.

- **Go to Code**: Jumps to the Code Editor and highlights the code for the selected widget
- **Go to Component**: For custom project widgets, opens the component file with the relevant widget code highlighted

This makes it easy to inspect and modify widget code directly from the visual layout editor.
 
