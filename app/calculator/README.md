# SwixKnife Calculator App

To build it for Android, you’ll need:

    android-sdk 33
    android-ndk 25c
    openjdk 17

    pythonforandroid from develop branch
    buildozer from master branch
    pyjnius from master branch

The stable versions are too old, we used some new features in here.

Build for the first time takes a long time, read buildozer, python for android and kivy’s documentation;

To build for debug:

    buildozer android debug

After debug build, to install and test it via adb:

    buildozer android deploy run logcat

To build for release:

    buildozer android release
