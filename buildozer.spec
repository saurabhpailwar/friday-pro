[app]
title = FRIDAY Pro
package.name = fridaypro
package.domain = com.saurabh.fridaypro
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 6.2.1
requirements = python3,kivy,android,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = develop
