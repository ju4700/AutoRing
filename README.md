# AutoRing App
AutoRing is an Android application developed using Kivy that automatically adjusts the device's ringtone mode based on ambient noise levels. The app uses the device's microphone to continuously monitor noise levels. When the noise level exceeds a predefined threshold, the app switches the device to normal ring mode and sets the ringtone volume to maximum. Conversely, when the noise level falls below the threshold, the app switches the device to vibrate mode.

![Untitled design](https://github.com/user-attachments/assets/f8eb5fa5-5ea8-44f9-8d66-7a0b05a75cff)

## Features:
Automatically adjusts ringtone mode based on ambient noise levels.
Runs in the background as a service.
Displays a notification when active, indicating the app's status.
Allows users to close the app from the notification panel.

## Requirements:
Android device with microphone capabilities.
Android version supporting required permissions (e.g., microphone access, background service).

## Installation:
To install AutoRing, download the APK file from the releases section and install it on your Android device.

## Permissions:
AutoRing requires the following permissions:
* Microphone access: Used to monitor ambient noise levels.
* Notification access: Allows the app to display notifications.
* Usage:
    Launch the AutoRingtone app.
    Adjust the ambient noise threshold if needed.
    Keep the app running in the background.
    The app will automatically adjust the ringtone mode based on noise levels.
    
# Development:
AutoRing is developed using Python with Kivy for the frontend and utilizes Android APIs via Pyjnius for backend functionalities.

