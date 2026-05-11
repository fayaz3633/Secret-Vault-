[app]
title = Secret Vault
package.name = secretvault
package.domain = org.fayaz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# صرف ضروری لائبریریز
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,cryptography,pyjnius

orientation = portrait
fullscreen = 0

# یہاں دھیان دیں: صرف .api لکھا ہے، .sdk نہیں
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# یہ دونوں خالی رہیں گے
android.sdk_path = 
android.ndk_path = 

p4a.bootstrap = sdl2
log_level = 2

[buildozer]
bin_dir = ./bin
