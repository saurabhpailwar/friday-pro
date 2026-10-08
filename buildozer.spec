[app]
title = FRIDAY Pro
package.name = fridaypro
package.domain = com.saurabh.fridaypro
source.dir =.
version = 6.2.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
permissions = RECORD_AUDIO,CALL_PHONE,READ_CONTACTS,INTERNET
android.api = 33
android.minapi = 21
