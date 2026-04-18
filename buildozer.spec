[app]
title = My Kivy App
package.name = mykivyapp
package.domain = org.example
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools = 33.0.2
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
p4a.branch = develop
p4a.local_recipes =
android.gradle_dependencies =
android.sdk_path = /home/runner/android-sdk
