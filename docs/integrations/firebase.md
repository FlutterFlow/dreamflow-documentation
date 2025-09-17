---
slug: /integrations/firebase
title: Firebase
description: Learn how to connect your Dreamflow app with Firebase to enable powerful backend features such as authentication, real-time databases, analytics, and more.
tags: [Firebase, Integration, Dreamflow, Backend]
sidebar_position: 1
toc_max_heading_level: 4
keywords: [Firebase, Integration, Dreamflow, Backend]
---

# Firebase

Dreamflow makes it easy to integrate [Firebase](https://firebase.google.com/) into your app with a guided, step-by-step setup. This process connects your project to Firebase, generates all necessary configuration, and even creates ready-to-use client code and database rules with AI.

By integrating Firebase, you gain access to services such as Authentication, Firestore Database, Cloud Storage, Hosting and more, giving your app a secure backend for managing users, data, and serverless logic.

## 1. Connection

The first step is to connect Dreamflow with your Google account so it can create new Firebase projects or link to existing ones.

To connect Dreamflow with Firebase, open the **Firebase** tab in Dreamflow, then click **Connect to Firebase**. When the OAuth window appears, sign in with your Google account, review, and approve the requested permissions. These permissions allow Dreamflow to create Firebase projects, manage configurations, and deploy security rules.

Once complete, Dreamflow will confirm the connection with a **Connected** status.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/Iu2hoVYZN1EV5IscOzNy?embed&show_copy_link=true"
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


## 2. Project Setup

After connecting your Google account, the next step is to set up a Firebase project, which will serve as the backend for your app. You can do this in two ways:

- **Select an existing Firebase project:** Choose from the list of your existing Firebase projects.

    ![select-from-existing-project](imgs/select-from-existing-project.avif)
- **Create a new Firebase project:** Let Dreamflow automatically create and configure a new Firebase project for you.

    ![create-new-project](imgs/create-new-project.avif)

Once the project is linked, you need to specify the following:

- **Target Platforms:** Choose every platform you want to support (Web, iOS, Android, macOS, Linux, Windows). Web is always enabled by default, so your app can be previewed inside Dreamflow. Selecting the right platforms ensures Firebase generates configs for each build target.
- **Bundle ID:** Enter a unique **Bundle ID** (e.g., `com.yourcompany.appname`). This must match the app identifier in your platform-specific builds (iOS bundle ID, Android package name). If you skip this, Firebase cannot configure services for mobile apps.

When these details are set, click **Configure Firebase** to complete the setup.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/Ux3hDEIPtZ1qaVHtIKnf?embed&show_copy_link=true"
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

Behind the scenes, Dreamflow uses the **FlutterFire CLI** to handle the configuration. This process generates a `firebase_options.dart` file containing project-specific credentials such as API keys, app ID, and messaging sender ID. These credentials ensure your app is properly connected to Firebase services.

:::

:::warning

Once configured, changing the **Bundle ID** later will require reconfiguring Firebase and may break existing builds. Choose carefully before proceeding.

:::

## 3. Generate Client Code

Once your Firebase project is linked and configured, click **Generate with Agent** to automatically add the code needed to access Firebase services. This step automates a complete Firebase integration tailored to your app, wiring up authentication, Firestore, state management, and updating the existing app logic with little to no manual effort.

:::info

- This step is optional, but we strongly recommend doing it. It saves significant development time by scaffolding schemas, services, and security rules automatically to ensure your Firebase integration is both secure and production-ready from the start.
- The generated code is fully editable and serves as a starting point for customization.

:::

![generate-client-code.avif](imgs/generate-client-code.avif)

### What happens during code generation?

When you click **Generate with Agent**, Dreamflow performs several background steps, including (but not limited to):

- **Firebase Configuration Files**
    - Creates and updates core Firebase files such as `firebase.json`, `firestore.rules`, `firestore.indexes.json`, and `firebase_options.dart`.
    - These files define how your app connects to Firebase, which services are enabled, and enforce security rules and query indexes.
- **Firestore Schema & Services**
    - Generates a `firestore_data_schema.dart` file to define collections and documents.
    - Implements a `firebase_service.dart` repository class to handle Firestore operations (CRUD, queries, synchronization).
    - Adds indexes and security rules to enforce per-user access control.
- **Authentication System**
    - Creates an `auth_service.dart` for sign-in/sign-out logic.
    - Adds an `auth_wrapper.dart` to manage authentication state across the app.
    - Updates `main.dart` to initialize Firebase and route users based on authentication state.
- **App Screens**
    - Updates app pages to fetch and display live data from Firestore instead of hardcoded values.
    - Adds authentication screens to handle user sign-in and sign-up flows.
- **Dependencies & Compilation**
    - Updates `pubspec.yaml` with required Firebase dependencies.
    - Resolves version conflicts and ensures successful compilation.
    

:::info[Enable Services in Firebase Console]

After Dreamflow generates code for Firebase services, you must enable those services in the Firebase Console for them to function correctly. For example:

- **Authentication:** Enable required sign-in methods such as Email/Password or Social Sign-in.
- **Firestore Database:** Activate Firestore in the console to store and retrieve data.
- **Firebase Storage:** Enable Storage to handle file uploads and downloads.

:::

## 4. Deploy to Firebase

The final step is to deploy the generated schemas, indexes, and rules to Firebase so they become active in your project. For example, in a habit tracker app, Dreamflow deploys rules that allow only the authenticated user to modify their habits collection.

To deploy to Firebase:

1. In the **Actions** panel, go to **Deploy to Firebase**. Under **Deployment Target**, select the Firebase service you want to deploy to (default is *Firestore*).
2. Click **Deploy Changes**.

:::info

- Until you deploy, rules and schemas only exist in Dreamflow and are not sent to Firebase.
- Dreamflow uses the Firebase CLI to push security rules, indexes, and any additional configurations (e.g., Auth, Storage) to Firebase.

:::

:::warning

This step is critical for security, as without rules, your Firestore may be open to anyone.

::::

![deploy-to-firebase.avif](imgs/deploy-to-firebase.avif)

