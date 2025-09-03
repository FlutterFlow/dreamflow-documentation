---
slug: /test/test-on-mobile-device
title: Testing App on Mobile Devices
description: Learn how to test your DreamFlow app on mobile devices.
tags: [Test, Mobile Device, Android, iOS]
sidebar_position: 2
keywords: [DreamFlow, Test, Mobile Device, Android, iOS]
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

For app testing on an iOS device or simulator, you need a Mac with Xcode. Follow [**these instructions**](https://docs.flutter.dev/get-started/install/macos/mobile-ios) to set up your Mac.

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

- If your device is not listed in the **Flutter Device Selection** dropdown, make sure you have properly completed the [**Android**](#android-setup) and [**iOS**](#ios-setup) setup.
- If you encounter a version compatibility issue with Flutter, you can resolve it by upgrading to the latest version. Simply execute the `flutter upgrade` command in your terminal. To verify your current Flutter version, use the `flutter --version` command.

:::