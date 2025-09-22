---
slug: /workspace/assets
title: Assets
description: Discover how to manage images, audio, fonts, and other files in Dreamflow’s Assets panel.
tags: [assets, dreamflow, flutter]
keywords: [assets panel, flutter assets, image management, audio files, font files, resource organization, dreamflow workspace, asset upload, asset usage]
sidebar_position: 3
---

# Assets

The **Assets** panel in Dreamflow is where you manage all the files your app needs, such as images, audio, videos, fonts, and documents. These assets are stored directly in your project, making them easy to reference and reuse across your app.

## Uploading Assets

To upload an asset, click **Upload Assets** and choose a file from your computer, or simply drag and drop it into the panel. Dreamflow will automatically organize the file into the right category (for example, a `.png` will appear under **Images**).

:::info

- You can use the search bar at the top of the Assets Panel to quickly locate files by name.
- Assets are bundled into your project when you publish or export the code.

:::


<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/j9xa6jssFU7pazeWHvNe?embed&show_copy_link=true"
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


## Accessing Assets

Once uploaded, assets can be used directly through the [Properties Panel](../properties-panel.md) or referenced in your generated code (for example: `Image.asset('assets/images/logo.png')`).


<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/4knXrPcj8X2PWRMp5DGx?embed&show_copy_link=true"
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


## Best Practices

- **Optimize image sizes:** Use lightweight formats like `.webp` or `.svg` to improve performance and reduce load times.
- **Use clear, descriptive names:** Give assets meaningful names (e.g., `placeholder.png` instead of `img1.png`) to make them easier to manage.
- **Avoid oversized files:** Keep videos and audio files reasonably small to ensure your app remains fast and responsive.