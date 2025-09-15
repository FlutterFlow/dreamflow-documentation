---
slug: /workspace/properties-panel
title: Properties Panel
description: Learn about Dreamflow's Properties Panel that provides comprehensive property editing for Flutter widgets with specialized editors and real-time visual feedback
tags: [properties, widgets, ui, development, flutter]
sidebar_position: 4
keywords: [properties panel, widget properties, property editing, flutter development, dreamflow interface, development environment, visual editing, property editors]
---

# Properties Panel 

The Properties Panel is a sophisticated interface for editing widget properties in real-time, providing both visual and code-based editing capabilities with intelligent property type detection and specialized editors.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/6AJA10eoZEfsJPrjKyrp?embed&show_copy_link=true"
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



**Real-Time Property Editing**: The panel displays all properties of the currently selected widget and allows you to edit them with immediate visual feedback. Changes are applied instantly to your running app.

**Intelligent Property Editors:** The system automatically detects property types and provides specialized editors:
- **Color Properties:** Color picker with hex input and visual color swatches
- **TextStyle Properties:** Rich text styling editor with font family, size, weight, and color options
- **Padding/Margin:** Visual padding editor with individual side controls
- **Border Radius:** Corner-specific radius controls with visual preview
- **Gradients:** Linear, radial, and sweep gradient editors with color stops
- **Borders:** Border style, width, and color controls
- **Images:** Asset and network image selectors
- **Icons:** Icon picker with search functionality
- **Alignment:** Visual alignment controls
- **Boolean Properties:** Toggle switches for true/false values
- **Enum Properties:** Dropdown menus for predefined options


This makes the Properties Panel a comprehensive tool for visual Flutter development, allowing you to modify any aspect of your UI without writing code manually.

:::tip[Quick Access from Widget Tree]
The Properties Panel can be quickly accessed by clicking any widget in the Widget Tree. The panel will automatically update to show the properties of the selected widget.
:::



### Advanced Functionalities

- **Property Search:** Search functionality to quickly find specific properties within complex widgets.
- **Add Property Button:** Add new properties to widgets that don't have them configured yet.
- **Grouped Properties:** For supported widgets (Container, Text, TextField), properties are organized into logical groups like "Layout", "Styling", "Behavior" for easier navigation.
- **Syntax Highlighting:** For complex expressions and function properties, the panel provides syntax-highlighted code editors.
- **CopyWith Support:** Automatically handles Flutter's copyWith pattern for updating nested properties like TextStyle sub-properties.



## Modifiers


Modifiers refer to wrapper widgets that can be added around existing Flutter widgets to modify their behavior, appearance, or layout. Think of them as "decorators" or "containers" that wrap around your base widgets. They are Flutter widgets that wrap around other widgets to modify their:
- **Layout behavior** (positioning, sizing, constraints)
- **Visual appearance** (colors, borders, shadows, opacity)
- **Interactive behavior** (gestures, focus, accessibility)
- **Animation properties** (transitions, transformations)




### Adding a Modifier

1. Select any widget in the Widget Tree Panel that you want to wrap with a **Modifier** widget.

2. In the Properties Panel, scroll down to the **Modifiers** section at the bottom.

3. Click the **+** button next to "Modifiers" tab to open the Modifier selection menu.

4. Choose from available wrapper widgets such as:
    - **Container** - For padding, margin, decoration, and constraints
    - **Padding** - For adding space around content
    - **Center** - For centering content
    - **Align** - For positioning content
    - **SizedBox** - For setting specific dimensions
    - **Transform** - For rotations, scaling, and translations & other such modifier widgets. 


5. The Modifier widget will be added to your widget hierarchy and its properties will appear in the Modifiers tab section of the Properties panel, where you can edit them immediately.


<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/JPPGJVEhgwSBhviyKmUs?embed&show_copy_link=true"
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



