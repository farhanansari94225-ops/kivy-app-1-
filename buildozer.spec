[app]
title = My Kivy App
package.name = myapp
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
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
