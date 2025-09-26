---
slug: /publish/pre-checks-before-publishing
title: Pre-checks Before Publishing
description: Ensure your app is ready for launch with this detailed guide on essential pre-publishing checks.
tags: [Pre-checks, Publishing, Deployment]
sidebar_position: 1
keywords: [Pre-checks, Publishing, Deployment, Dreamflow]
---

# Pre-checks Before Publishing
Before publishing your app, it’s important to run through a checklist to ensure quality, compliance, and readiness for release. These pre-checks help confirm that your app works as expected, meets platform requirements, and provides a smooth user experience.

Here’s a comprehensive list of these prechecks:

1. **Functionality Testing**: [Test the app manually](../test/test-on-mobile-device.md) across devices to verify that every feature behaves correctly, user interactions respond as intended, and no crashes or unexpected errors occur.
2. **Get Feedback**: Gather feedback from users or testers to receive valuable insights and potential areas of improvement before the public release.
3. **Optimizations & Enhancements**: Review your app’s overall performance and make sure all assets are optimized. This includes, but is not limited to:
    - Making sure images are properly sized and compressed to reduce load times.
    - Minimizing large files, unused assets, or unnecessary dependencies.
    - Checking that animations and transitions run smoothly without lag.
    - Enable caching strategies where appropriate.
4. **User Interface (UI)**: Review UI consistency across different devices, screen sizes, and resolutions.
5. **Accessibility Checks**: Use Flutter’s [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget on images and buttons to provide meaningful descriptions for assistive technologies. Verify that TalkBack (Android) and VoiceOver (iOS) correctly interpret UI elements. Check color contrast with Flutter’s theming system and ensure that navigation using gestures or keyboard input remains accessible across all screens.
6. **Security Measures**: Safeguard user data by using HTTPS for all network requests, encrypting sensitive information, and following best practices for authentication and storage. Ensure compliance with legal standards like GDPR or CCPA, if applicable.
7. **Compliance with Store Guidelines**: Carefully review submission policies for both [Apple’s App Store](https://developer.apple.com/app-store/review/guidelines/) and [Google Play Store](https://play.google/developer-content-policy/). Pay attention to metadata, privacy policies, restricted content rules, and minimum functionality requirements.
8. **Localization and Internationalization**: If your app targets users in multiple countries, consider [adding multi-language](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization) support.
9. **License and Third-Party Attributions**: Adhere to licenses and include necessary attributions for third-party libraries and assets.
10. **Prepare Marketing Assets**: Prepare all the necessary marketing assets, such as screenshots, app icons, and promotional text.
11. **Error Logging & Monitoring**: Integrate crash reporting and analytics (e.g., Firebase Crashlytics, Sentry) before release. Try triggering test crashes in debug or staging builds to confirm reports are collected correctly.
12. **Offline & Poor Network Support**: Validate app behavior with no connectivity and high-latency/packet-loss scenarios. Provide cached content, retry/backoff for API calls, and clear offline states.


## Add App Launcher Icon

An **app launcher icon** is the small image that represents your app on a device’s home screen. It’s the first visual element users see, so having a clear and properly designed icon is important for branding and user experience.

When you create a new app in Dreamflow, it sets a default Dreamflow logo as the launcher icon. To give your app a unique identity, you should replace this with your own custom icon. Follow the steps below to update the launcher icon:

1. Go to the [**Assets**](../../workspace/modules-panel/assets.md) module in Dreamflow and upload your icon image. For best results, use a square, high-resolution source image (i.e., **1024×1024 px**) to ensure your app icon looks sharp across all devices and sizes.
2. Update the code to use the new app icon. Dreamflow uses the [`flutter_launcher_icons`](https://pub.dev/packages/flutter_launcher_icons) package to set launcher icons for both platforms. You can either:
    - Ask the Agent to do it automatically, or
    - Do it manually by updating the `image_path` in your `pubspec.yaml` file to point to the newly uploaded app icon.

Here is the example configuration in `pubspec.yaml` file:

```jsx
flutter_launcher_icons:
  android: true
  ios: true
  image_path: assets/images/app_icon.png
  remove_alpha_ios: true
```

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/xzNj2YwPUvpxlrNQCv1r?embed&show_copy_link=true"
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

- The Agent can’t generate a launcher icon image for you; you need to upload your own image file in the **Assets** module.
- The app icon is generated during native builds (Android/iOS) before deployment. However, if you want to verify that it’s configured correctly, [**download**](../test/test-on-mobile-device.md#download-code-and-run) the project, run the following command in the terminal, then run the app on a device and check device’s home screen to confirm the new icon appears.

```jsx
flutter pub run flutter_launcher_icons
```
:::

### Platform-Specific Icon Configuration

If you want to use different icons for Android and iOS, you can set platform-specific paths. This is useful if your design team provides unique assets for each platform.

To do so, upload separate icons for each platform to assets module, then update your `pubspec.yaml` as shown below:

```yaml
flutter_launcher_icons:
  android: true
  ios: true
  image_path_android: assets/images/app_icon_android.png
  image_path_ios: assets/images/app_icon_ios.png
  remove_alpha_ios: true

```

- **`image_path_android`**: Path to the Android app icon.
- **`image_path_ios`**: Path to the iOS app icon.

### Adaptive Icons for Android

Android supports [**adaptive icons**](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons), which allow your app icon to adapt to different shapes (circle, square, squircle, etc.). 

To setup adaptive icons, you can either use this [online tool](https://icon.kitchen/) or use these [resources](#adaptive-icon-resources) to create one. and then provide both a **background** and **foreground** layer in `pubspec.yaml` file.

Here is the example configuration:

```jsx
flutter_launcher_icons:
  android: true
  ios: true
  image_path: "assets/icons/app_icon.png"

  # For adaptive icon support:
  adaptive_icon_background: "assets/icons/icon_bg.png"   # image or solid color ("#FFFFFF")
  adaptive_icon_foreground: "assets/icons/icon_fg.png"   # your logo / symbol image
  adaptive_icon_foreground_inset: 16   # optional padding percentage (default is 16)

```

- `adaptive_icon_background`: A solid color or image asset to use as the background layer.
- `adaptive_icon_foreground`: An image asset to use as the foreground (your logo or symbol).
- `adaptive_icon_foreground_inset` (optional): A padding percentage for the foreground layer.

:::info

- Both `adaptive_icon_background` and `adaptive_icon_foreground` must be set for adaptive icons to be generated.
- If you do not specify adaptive layers, `flutter_launcher_icons` will fall back to generating legacy (non-adaptive) icons.

:::


#### Adaptive Icon Resources

See the following resources for more information on Android adaptive icons.

##### Create Adaptive Icon

- [Create app icons in Android Studio](https://developer.android.com/studio/write/create-app-icons#create-adaptive)
- [Figma template](https://material.uplabs.com/posts/adaptive-icon-sticker-sheet) (requires login)
- [Bjango templates](https://github.com/bjango/Bjango-Templates) include adaptive icons
- [Adobe XD template](https://github.com/faizmalkani/adaptive-icon-template-xd)

##### Adaptive Icon Fundamentals

- [Understanding Android Adaptive Icons](https://medium.com/google-design/understanding-android-adaptive-icons-cee8a9de93e2)
- [Designing Adaptive Icons](https://medium.com/google-design/designing-adaptive-icons-515af294c783)
- [Implementing Adaptive Icons](https://medium.com/google-developers/implementing-adaptive-icons-1e4d1795470e)

