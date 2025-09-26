---
slug: /workspace/properties-panel
title: Properties Panel
description: Learn about Dreamflow's Properties Panel that provides comprehensive property editing for Flutter widgets with specialized editors and real-time visual feedback
tags: [properties, widgets, ui, development, flutter]
sidebar_position: 4
keywords: [properties panel, widget properties, property editing, flutter development, dreamflow interface, development environment, visual editing, property editors]
---

# Properties Panel 

The Properties Panel allows you to edit widget properties in real-time, providing both easy-to-use visual editors and flexible code-based editing capabilities.

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
        frameBorder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>


:::tip[Quick Access from Widget Tree]
The Properties Panel can be quickly accessed by double  clicking any widget in the Widget Tree. The panel will automatically update to show the properties of the selected widget.
:::

:::note[Switching to Code]
To switch from the visual property editor to a code-based property editor, hover near the property and click the "Switch to Code View" button. You can also cmd+click this button to jump to the specific line in the code editor where the property is defined.
:::


## Adding Hidden Properties
Some properties for widgets are hidden by default. However, any property that's accessible in the underlying widget can be set from the property panel. 
If you are looking for a hidden property, you can search for it or add it using the "+ Add Property" button at the top of the Property panel. 


## Modifiers

Modifiers refer to wrapper widgets that can be added around existing Flutter widgets to modify their behavior, appearance, or layout. Think of them as "decorators" that wrap around your base widgets. They are Flutter widgets that wrap around other widgets to modify their:
- **Layout behavior** (positioning, sizing, constraints)
- **Visual appearance** (colors, borders, shadows, opacity)
- **Interactive behavior** (gestures, focus, accessibility)
- **Animation properties** (transitions, transformations)

:::note[Modifiers in the Widget Tree]
Modifier widgets are hidden from the "Simplified View" in the [**widget tree**](modules-panel/widget-panel.md#nodes-widgets).
:::


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
        frameBorder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>



