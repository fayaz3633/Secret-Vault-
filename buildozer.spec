[app]
title = Secret Vault
package.name = secretvault
package.domain = org.fayaz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# تمام ضروری لائبریریز جو آپ کی ایپ کو چاہیے
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,cryptography,pyjnius

orientation = portrait
fullscreen = 0

# اینڈرائیڈ کی نئی سیٹنگز (API 33)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# فائل مینیجر کے لیے ضروری اجازتیں (Permissions)
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE, CAMERA
android.manifest.intent_filters = [ {"name": "android.intent.action.VIEW", "categories": ["android.intent.category.DEFAULT"] } ]

android.sdk_path = 
android.ndk_path = 
p4a.bootstrap = sdl2
log_level = 2

[buildozer]
bin_dir = ./bin
