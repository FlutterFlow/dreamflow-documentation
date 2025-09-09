---
slug: /deployment/google-playstore-deployment
title: Google Play Store Deployment
description: Learn how to deploy your apps to the Google Play Store using Dreamflow.
tags: [Google Play Store, Deployment, Dreamflow, Android]
sidebar_position: 3
toc_max_heading_level: 4
keywords: [Google Play Store, Deployment, Dreamflow, Android]
---

# Google Play Store Deployment

Dreamflow allows you to deploy your apps directly to the Google Play Store from within the platform. This guide covers all the necessary prerequisites, a step-by-step deployment process, and common troubleshooting tips.

:::info[Prerequisites]

- Register for a [**Google Play Developer account**](https://play.google.com/console/signup).
- Ensure you have set an app launcher icon. If not, add an app icon to the Dreamflow assets, then use the [**flutter_launcher_icons**](https://pub.dev/packages/flutter_launcher_icons) package or ask the AI agent to set it up for you.
- Ensure your app package name is correct, as it cannot be changed after deployment. To verify it, open `android/app/build.gradle` and check the `applicationId`. To update the package name, you can use the [**change_app_package_name**](https://pub.dev/packages/change_app_package_name) package or simply ask the AI agent.
- It's recommended to [**test your app on a real device**](../test/test-on-mobile-device.md) before deployment.

:::

## 1. Creating app on Google Play Store

To create a new app in the Google Play Store, start by opening the [Google Play Console](https://play.google.com/console) and clicking the **Create app** button. Enter the **App name**, select the app type, and choose whether the app will be **Free** or **Paid**. After that, accept the **Declarations**, and finally click **Create app** to proceed.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/364L2UfaOKcHiJH5GIAv?embed&show_copy_link=true"
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

## 2. Set up your app

To provide the app details required by the Google Play Store, go to the **Set up your app** section within your newly created app. Expand the **View tasks** list, then click on each task and complete the required information step by step.

![setup-android-app-in-play-console.avif](imgs/setup-android-app-in-play-console.avif)

## 3. Adding service account credentials

To enable Dreamflow to deploy your app to the Google Play Store, you need to add service account credentials.

### 3.1 Creating a Service Account

To create the Service Account, you can follow the instructions from [here](https://developers.google.com/android-publisher/getting_started). To help you get started quickly, here are the exact steps you need to follow:

1. If you haven't set up Firebase in your app, you'll need to [create a Google Cloud Project](https://developers.google.com/android-publisher/getting_started#creating).
2. Then, head over to the [Google Play Developer API page](https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/) in Google Cloud Console and click **Enable**.
    
    ![enable-play-api](imgs/enble-play-developer-api.avif)
    
3. In Google Cloud Console, go to [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts), click + **CREATE SERVICE ACCOUNT,** and follow the steps as shown below.
    
    <div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/v4qg6mfKvbKGKISqJZg8?embed&show_copy_link=true"
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

    
4. Now, download the JSON key file by clicking **ADD Key > Create new key > select JSON > CREATE**. Keep this file secure.
    
    <div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/ZMZFspS0ZI3xIc0bSago?embed&show_copy_link=true"
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

5. In **Google Play Console**, go to [Users & Permissions](https://play.google.com/console), click **Invite new users**, and add your service account email with these permissions:
    - "Edit and delete draft apps"
    - "Release to production..."
    - "Release apps to testing tracks"
    - "Manage testing tracks and edit tester lists"

    <div style={{
        position: 'relative',
        paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
        height: 0,
        width: '100%'}}>
        <iframe 
            src="https://demo.arcade.software/PLVogskcfVTMqJk4nfig?embed&show_copy_link=true"
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

### 3.2 Uploading service account credentials to Dreamflow

To upload your service account credentials in Dreamflow, go to **Publish > Android**. Under **Google Play Credentials**, click **Upload .json** and select the `.json` file you downloaded in step 4.

![upload-json-file.avif](imgs/upload-json-file.avif)

## 4. Deploy to Google Play Store

For first-time deployment, you need to create an initial release manually in Google Play Console. After that, Dreamflow can handle all subsequent deployments.

### 4.1 Downloading AAB file

In DreamFlow, set the **Google Play Track** to **Internal**, enter the **Bundle ID** and **Version Code**, then click **Submit Build to Google Play**. Wait a few minutes and click **Check Deployment Status**.

Once the build is complete, click **Download AAB File** button (in the **App Bundle** section). If the button is still disabled, wait a bit longer and try again.

:::info

Even if the build status appears as FAILURE, you can still download the AAB file.

:::

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/pBlnRQnHLQRjSFWJTtHw?embed&show_copy_link=true"
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

### 4.2 Upload AAB file to Internal testing track

In Google Play Console, create an **Internal Testing** track and upload the **.aab** file.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/PJt1oXAVn7Wpvjb6zYCb?embed&show_copy_link=true"
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

:::info
After the internal testing track is set up, DreamFlow can handle all future deployments directly.
:::

### 4.3 Deploy from Dreamflow

To deploy your app from Dreamflow, navigate to **Publish > Android**, set the **Track** to Internal, and update the **version code.** If your app is still in draft mode (not yet available on the Play Store), set **Submit as Draft** (under **Deployment Flags)** to **True**, and then click **Deploy to Play Store**.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/lryE56z4DG52mIeJLwhn?embed&show_copy_link=true"
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

:::info

- If another deployment is already in progress, deploying a new build will cancel the previous one.
- It may take a few minutes for the request to process. Once completed, you will get a pop-up saying *Your app is being deployed to Google Play.*

:::

### 4.4 Verify deployment

To verify that the app is deployed to Play Console:

1. Open the **Internal testing** in [Google Play Console](https://play.google.com/console).
2. Under the **Releases** section, find your release and click on the **Show Summary** button.
3. See the **Version Codes** number is increased.

![verify-deployment.avif](imgs/verify-deployment.avif)

### 4.5 Deploy to production

To promote your app to production, open your **Internal testing** track in Google Play Console and complete the release. Once the internal release is finalized, click **Promote Release > Production**.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(50.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/8TQoQjPZEetKsEptLJ2w?embed&show_copy_link=true"
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

For all future deployments, set the **Google Play Track** to **Prod** in Dreamflow and deploy directly from there.

![deploy-to-prod-from-dreamflow.avif](imgs/deploy-to-prod-from-dreamflow.avif)

## Deployment Flags

### Submit as draft

While deploying, if your app is still in draft mode, meaning it is not available on the Play Store yet, you may encounter an error message stating, 'Only releases with the status draft may be created on a draft app.'

To resolve this, enable this option, and you'll see that the release will be created as a draft. You'll then need to manually roll out the app.

### Changes not sent for review

If you face an error that says '*Changes cannot be sent for review automatically*', enable this option and retry deployment.

## FAQs

<details>
<summary>
Why am I getting an "Invalid Package Name" error?
</summary>
<p>
This happens when your package name already exists or doesn’t meet validation requirements. Make sure your package name is unique and not already used by another app on Google Play Store. Note that the package name cannot be changed after deployment.
</p>
</details>

<details>
<summary>
What should I do if I see "The service account does not have permission to perform this action"?
</summary>
<p>
This means your service account doesn’t have the correct permissions. In Google Play Console, ensure the account has these permissions:

- *Edit and delete draft apps*
- *Release to production...*
- *Release apps to testing tracks*
- *Manage testing tracks and edit tester lists*
</p>
</details>





<details>
<summary>
Why does my first upload fail with a message like "You need to use a different package name"?

</summary>
<p>
For the initial deployment, you must manually [**download the .aab file**](#41-downloading-aab-file) and [**upload it to internal testing track**](#42-upload-aab-file-to-internal-testing-track) in Google Play Console. Once the initial track is set up, Dreamflow will handle all subsequent deployments automatically.
</p>
</details>


