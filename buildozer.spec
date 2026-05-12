[app]
title = Secret Vault
package.name = secretvault
package.domain = org.fayaz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ہم نے Kivy کا نیا ورژن ڈال دیا ہے تاکہ پرانے سسٹم سے نہ الجھے
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,cryptography,pyjnius

orientation = portrait
fullscreen = 0

# SDK والی لائن بالکل غائب ہے تاکہ لال ایرر نہ آئے
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# فائل مینیجر کی تمام ضروری اجازتیں
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, CAMERA
android.manifest.intent_filters = [ {"name": "android.intent.action.VIEW", "categories": ["android.intent.category.DEFAULT"] } ]

android.sdk_path = 
android.ndk_path = 
p4a.bootstrap = sdl2
log_level = 2

[buildozer]
bin_dir = ./bin
