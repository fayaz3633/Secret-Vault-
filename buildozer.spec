[app]
title = VIP Vault
package.name = vipvault
package.domain = org.fayyaz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# تمام ضروری لائبریریاں یہاں سیٹ کر دی ہیں
requirements = python3, kivy==2.2.1, kivymd==1.1.1, cryptography, pyjnius, sdl2_image, sdl2_ttf, sdl2_mixer, sdl2

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# اینڈرائیڈ کے پکے ورژن (تاکہ یلو وارننگ نہ آئے)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# ان لائنوں کو ہم نے خالی چھوڑا ہے تاکہ گٹ ہب خود راستہ ڈھونڈے
android.sdk_path = 
android.ndk_path = 

[buildozer]
log_level = 2
warn_on_root = 1
