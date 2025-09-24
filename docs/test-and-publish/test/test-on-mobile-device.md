---
slug: /test/test-on-mobile-device
title: Testing App on Mobile Devices
description: Learn how to test your Dreamflow app on mobile devices.
tags: [Test, Mobile Device, Android, iOS]
sidebar_position: 2
keywords: [Dreamflow, Test, Mobile Device, Android, iOS]
---

# Testing App on Mobile Devices
Testing your app on mobile devices is essential to ensure it performs as expected in real-world scenarios. You can do this by downloading the code and running it locally on your machine.

:::info[Prerequisites]
Downloading the code is only available with a [**paid subscription**](https://dreamflow.app/pricing).
:::

## Android Setup

To test your app on an Android device or emulator, you first need to set up your development environment, install Flutter, and configure your target device. Instructions for each platform are available here: [**Windows**](https://docs.flutter.dev/get-started/install/windows/mobile), [**Mac**](https://docs.flutter.dev/get-started/install/macos/mobile-android), [**Linux**](https://docs.flutter.dev/get-started/install/linux/android).

To setup an Android physical device, first enable Developer Options and USB Debugging in your Android device. Navigate to **Settings > About phone**, tap **Build number** seven times to activate Developer Options, then go to **Settings > System > Developer options** and enable **USB debugging**.

Connect your device to your computer via USB, authorizing the connection if prompted. Verify the setup by running `flutter devices` in Android Studio’s terminal; your device should appear in the list of connected devices.

:::info

For more detailed guidance, refer to the [**Android Flutter documentation**](https://docs.flutter.dev/get-started/install/windows/mobile#configure-your-target-android-device).

:::

## iOS Setup

For app testing on an iOS device or simulator, you need a Mac with Xcode installed. Follow [**these instructions**](https://docs.flutter.dev/get-started/install/macos/mobile-ios) to set up your Mac.

To setup a physical iOS device, you must configure your **Apple Developer account** and set up **code signing** in Xcode. First, add your **Apple ID** by opening **Xcode > Preferences > Accounts**, clicking **"+"**, selecting **Apple ID**, and signing in.

Next, assign your project to a development team. Open your project in Xcode, select the **Runner** project, go to **Signing & Capabilities**, and choose your **Apple Developer team** in the **Team** dropdown. If your team is not listed, ensure that your Apple ID has been properly added to Xcode.

Finally, configure code signing to allow your app to run on a real device. Ensure **"Automatically manage signing"** is enabled. Xcode will attempt to create and download a **provisioning profile** for your project. If issues arise, you may need to manually create a provisioning profile in the **Apple Developer Certificates, Identifiers & Profiles** section. Once created, download and double-click the provisioning profile to install it in Xcode.

:::info

For more detailed guidance, refer to the [**iOS Flutter documentation**](https://docs.flutter.dev/get-started/install/macos/mobile-ios#configure-your-target-ios-device).

:::

## Download Code and Run

To download your app code, click on your project name and select the **Download Code** option.

![download-code.avif](imgs/download-code.avif)

Once downloaded, open the project in your preferred IDE and run your app on either a real device or an emulator by following the instructions below:

- For **VS Code**:
    1. Go to the **View** menu > select **Terminal** from the dropdown.
    2. Run the command `flutter pub get`.
    3. Now, enter the command `flutter run`. VS Code will build and run your app. You'll see the output in the terminal, and the app should launch in the selected emulator or physical device.
- For **Android Studio**:
    1. Open the terminal within Android Studio by clicking **View** > **Tool Windows** > **Terminal**.
    2. Run the command `flutter pub get`.
    3. Click the green "Run" button (a right-facing triangle) located in the top toolbar. Choose the target device (emulator or physical device) where you want to run the app. Android Studio will build and run your app. You'll see the output in the "Run" panel at the bottom, and the app should launch in the selected emulator or device.

:::info
If you encounter a version compatibility issue with Flutter, you can resolve it by upgrading to the latest version. Simply execute the `flutter upgrade` command in your terminal. To verify your current Flutter version, use the `flutter --version` command.
:::

## Building APK File

You can build APK files locally to test your app on Android devices or prepare it for release on the Google Play Store.

:::info[Prerequisites]

Before building an APK, make sure your [**Android setup**](#android-setup) is complete and the [**app runs**](#download-code-and-run) successfully.

:::

#### Building a Debug APK (for Local Testing)

Debug APKs are useful for quickly installing your app on a device without signing or optimization. To build a debug APK:

1. Open a terminal in your project root.
2. Run the following command.
    ```jsx
    flutter build apk --debug
    ```
    
3. The APK will be generated at:
    
    ```jsx
    build/app/outputs/flutter-apk/app-debug.apk
    ```
    
4. Now, you can either directly install it on your device:
    
    ```jsx
    flutter install
    ```
    or manually copy the APK to any device and install it.
    

:::warning

Debug APKs are not optimized and should not be uploaded to the Play Store.

:::

**Build App for Release**

Dreamflow lets you [deploy apps directly to the Google Play Store](../publish/google-playstore-deployment.md) from within the platform. If you prefer to publish manually, you’ll first need to **sign your app** with a keystore and then **build a release APK or App Bundle**. Release builds are fully optimized, securely signed, and ready for distribution on the Play Store.

You can follow the official Flutter documentation for detailed steps:

- [Sign the app](https://docs.flutter.dev/deployment/android#sign-the-app)
- [Build the app for release](https://docs.flutter.dev/deployment/android#build-the-app-for-release)

## Building an IPA File

You can’t generate a debug `.ipa` file. Debug builds are only for local development and testing, and once your [iOS setup](#ios-setup) is complete, you can [run](#download-code-and-run) them directly on your device.

**Build App for Release**

Dreamflow lets you [deploy apps directly to the App Store](../publish/apple-app-store-deployment.md) from within the platform. If you prefer to create an IPA file for manual distribution (e.g., via TestFlight or the App Store), you’ll need to build a release IPA. This requires proper **code signing** with your Apple Developer account. Follow the official guide for detailed steps on [build and release for iOS](https://docs.flutter.dev/deployment/ios).