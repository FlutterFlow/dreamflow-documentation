---
slug: /workspace/theme
title: Theme 
description: Learn how to manage colors, typography, and style constants in Dreamflow’s Theme panel to create a consistent, cohesive design across your app.
tags: [theme, dreamflow, flutter]
sidebar_position: 3
keywords: [dreamflow theme, app theme, dark mode, light mode, colors, typography, style]
---


# Theme
The **Theme** panel in Dreamflow provides a centralized way to manage the visual identity of your app. Instead of hardcoding styles in multiple places, you can define colors, typography, and style values once and reuse them consistently across your project. This ensures your app maintains a polished, cohesive look while making design updates faster and easier.

## Colors

Colors define the overall mood and branding of your app. In Dreamflow, colors are grouped into three categories:

- **Brand Colors**: Represent your brand’s primary palette (e.g., primary, secondary, accent). Use these to give your app its unique identity.
- **Utility Colors**: These are functional colors that support layout and contrast.
- **Semantic Colors**: Contextual colors that represent meaning within the app for states like errors or warnings.

:::info

Each brand color includes a **hex value** (e.g., `#7C4DFF`) and an **opacity setting** so you can fine-tune how they appear in your design.

:::

### Dark Mode

Dreamflow makes it easy to design and preview your app in both **Light Mode** and **Dark Mode**. In the Theme panel, you can select **Dark Mode** from the dropdown. Set your colors for dark mode, then switch the mode in the Preview canvas to instantly see your design in action.

:::info
When you switch modes, Dreamflow automatically applies the corresponding color palettes, allowing you to check readability, contrast, and overall aesthetics in real time.
:::

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/OKojpnMFTASQci348sSe?embed&show_copy_link=true"
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

### Best Practices

To get the most out of Dreamflow’s color system, keep these guidelines in mind:

- **Maintain contrast**: Always ensure sufficient contrast between foreground (text/icons) and background colors for accessibility.
- **Be consistent**: Use brand colors consistently for key elements such as buttons and text so users quickly learn their meaning.
- **Leverage semantic colors**: Don’t reinvent error, warning, or success colors; stick to semantic definitions for clarity.
- **Test both modes**: Always check your design in **Light Mode** and **Dark Mode** to ensure readability and visual harmony.
- **Avoid color overload**: Use a limited palette so your app feels cohesive rather than chaotic.

## Typography

Typography in Dreamflow ensures that text styles remain consistent throughout your app. It is divided into categories that map to different use cases:

- **Display**: Large, prominent text for headers, hero sections, or landing screens.
- **Headline**: Sub-headers or secondary emphasis text.
- **Title**: Standard section titles and key labels.
- **Body**: Paragraphs, descriptions, and content-heavy areas.
- **Label**: Smaller text for buttons, captions, or UI labels.

Each category can be customized to align with your design system.

## Style Constants

Style constants define reusable design values across your app, helping you maintain consistency in both light and dark modes.

- **Light Mode Colors**: Default color set when your app is displayed in light mode.
- **Dark Mode Colors**: Color overrides for dark mode.
- **Font Sizes**: Centralized definitions for text sizing.