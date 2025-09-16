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