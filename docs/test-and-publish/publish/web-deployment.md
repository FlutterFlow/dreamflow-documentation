---
slug: /deployment/web-deployment
title: Web Deployment
description: Learn how to deploy your apps to the Web using Dreamflow.
tags: [Web, Deployment, Dreamflow]
sidebar_position: 4
toc_max_heading_level: 4
keywords: [Deployment, Dreamflow, Web]
---

# Web Deployment

Dreamflow makes it easy to take your app live on the web with minimal setup. You can quickly publish apps for testing, demos, or full production use, directly from your browser.

Dreamflow offers two flexible options:

- **One-Click Deployment:** Instantly publish your app to the web in just seconds, perfect for previews and prototypes.
- **Custom Web Deployment:** Gain more control over the deployment process, with configuration options tailored for production-ready apps.

## One-Click Deployment

With **One-Click Deployment**, you can instantly publish your app to the web without any additional setup. Dreamflow automatically builds and hosts your project under a shareable Dreamflow URL.

To deploy your app, navigate to **Publish > Web** and click **One-Click Deployment**. Dreamflow will automatically build and host your app at a unique subdomain (e.g., `https://<unique-id>.share.dreamflow.app`).

![one-click-deployment.avif](imgs/one-click-deployment.avif)

If you make changes to your project, click **Update Deployment** to publish the latest version. You can click **Unpublish** to remove the app from its live URL whenever you no longer want it accessible.

![update-unpublish-deployment.avif](imgs/update-unpublish-deployment.avif)

:::info[Key Benefits]

- **Fastest way to go live:** No configuration or hosting setup needed. Everything happens directly in Dreamflow.
- **Shareable link:** Easily share your app with teammates, testers, or clients.
- **Quick iteration:** Update deployments as you make changes, ensuring your live app always reflects the latest build.
- **Full control:** Unpublish when you’re ready to stop sharing or move to a custom deployment.

:::

:::warning
1-click web deployment doesn’t allow customizing `index.html`. For example, you can’t add a custom favicon. If you need a full control, you can use your own hosting solution.
:::

## Custom Deployment

(Coming soon)