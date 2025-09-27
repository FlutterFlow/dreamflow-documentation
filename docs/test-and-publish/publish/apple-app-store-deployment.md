---
slug: /deployment/apple-app-store-deployment
title: Apple App Store Deployment
description: Learn how to deploy your apps to the Apple App Store using Dreamflow.
tags: [Apple App Store, Deployment, Dreamflow, iOS]
sidebar_position: 3
toc_max_heading_level: 4
keywords: [Apple App Store, Deployment, Dreamflow, iOS]
---

# Apple App Store Deployment

Dreamflow allows you to deploy your apps directly to the Apple App Store from within the platform. This guide covers all the necessary prerequisites, a step-by-step deployment process, and common troubleshooting tips.

:::info[Prerequisites]
- Ensure you have [**set an app launcher icon**](pre-checks-publishing.md#add-app-launcher-icon).
- Create an [**Apple account**](https://appleid.apple.com/account?appId=632&returnUrl=https%3A//developer.apple.com/account/).
- [**Purchase an Apple Developer membership**](https://developer.apple.com/programs/enroll/). Learn more about the program and enrollment process [**here**](https://developer.apple.com/programs/).
- Ensure your app bundle identifier is correct, as it cannot be changed after publishing. To update the bundle identifier, you can use the [**change_app_package_name**](https://pub.dev/packages/change_app_package_name) package or simply ask the AI agent.
- It's recommended to [**test your app on a real device**](../test/test-on-mobile-device.md) before deployment.

:::

## 1. Create a Bundle Identifier

A **Bundle Identifier (ID)** is a unique string that identifies your app within the Apple ecosystem, typically formatted in reverse domain name notation like `com.example.myapp`.

To create a Bundle ID, visit the [**Certificates, IDs & Profiles**](https://developer.apple.com/account/resources/identifiers/list) page, add a new **App ID**, and provide these details:

1. **Bundle ID:** Define any name in the reverse domain notation.
2. **Description:** Add a brief description of your app.
3. **Capabilities:** Select the necessary app capabilities. Ensure you select **Push Notifications** if your app uses them, and **Sign In with Apple** if your app includes that feature.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/wwXpmj4dWdkSmWizMORd?embed&show_copy_link=true"
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

## 2. Add new app

App Store Connect is the platform used for submitting apps, managing app metadata, and much more. To add a new app, open the [App Store Connect](https://appstoreconnect.apple.com/) and then follow the official steps outlined [here](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app).

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/En7WfaghJEomWPuNzwaq?embed&show_copy_link=true"
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

## 3. Add Apple App ID to Dreamflow

An App ID is used by Apple to identify your app and associate it with your development team.

To add your App ID in Dreamflow, open [App Store Connect](https://appstoreconnect.apple.com/) > My Apps, copy the **Apple ID** from the **App Information** section, then go to **Dreamflow > Publish > iOS** and paste it into the **App Store App ID** field.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/A4dmkvttUV5um4d7zR1y?embed&show_copy_link=true"
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

## 4. Generate API key and add to Dreamflow

To generate your API Key, go to [**App Store Connect**](https://appstoreconnect.apple.com/) > **Users and Access** > **Integrations > [Team Keys](https://appstoreconnect.apple.com/access/integrations/api)**. If you haven't added a key before, you will see a **Request Access** button. For further details, watch a [demo](https://youtu.be/L2BpgVog4so?si=yS9r_PBeORgd6Uhp&t=240) here.

Generate a new API key by selecting **Add (+)**, entering a name, and assigning the **App Manager** role. Once the key is generated, download it and upload it to **Dreamflow** **> Publish > iOS > ASC Private Key (.p8)**.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/1NjbxSUW1IPpYHiVoiNK?embed&show_copy_link=true"
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

## 5. Add issuer ID to Dreamflow

Copy the **Issuer ID** from [**App Store Connect**](https://appstoreconnect.apple.com/) by navigating to **Users and Access** > **Integrations > [Team Keys](https://appstoreconnect.apple.com/access/integrations/api)**, and then paste it into **Dreamflow** **> Publish > iOS > ASC Issuer ID**.


<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/thInLV2e3oSn0ZVY6bAV?embed&show_copy_link=true"
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

## 6. Add Key ID to Dreamflow

Open the [App Store Connect](https://appstoreconnect.apple.com/) > **Users and Access** > **Integrations > [Team Keys](https://appstoreconnect.apple.com/access/integrations/api)**. Find the row for the API Key you generated [here](#4-generate-api-key-and-add-to-dreamflow), select **Copy Key ID,** and then paste it into **Dreamflow** **> Publish > iOS > ASC Key ID**.


<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/cAgczPgrJSuirZJswsdn?embed&show_copy_link=true"
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

## 7. Deploy

To deploy your app from Dreamflow, navigate to **Publish > iOS**, specify the **Bundle ID** and **Version Code**, and then click **Submit Build to App Store**.

Once deployed, you will receive an email from App Store Connect that a new build has been added to your app.

![app-store-deployment.avif](imgs/app-store-deployment.avif)


:::info

- If another deployment is already in progress, deploying a new build will cancel the previous one.
- It may take a few minutes for the request to process. Once completed, the status will be updated to **Submitted**.

:::

## 8. Submit your app for App Store approval

From [**App Store Connect**](https://appstoreconnect.apple.com/), select **My Apps** and choose your app. Select **Prepare for Submission**, add the app assets and metadata, and then click **Add for Review**.

![add-for-review.avif](imgs/add-for-review.avif)

Your app will now be reviewed by Apple. For additional information on Apple's review guidelines, please see [this link](https://developer.apple.com/app-store/review/guidelines/).

## FAQs


<details>
<summary>
Invalid App Store Icon. The App Store Icon in the asset catalog in 'Runner.app' can't be transparent nor contain an alpha channel.
</summary>
<p>
You need to update your App Launcher Icon (under Settings & Integrations --> General) with an image that isn't transparent and/or doesn't contain an alpha channel.
</p>
</details>
