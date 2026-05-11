[app]
title = VIP Vault
package.name = vipvault
package.domain = org.fayyaz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# یہاں میں نے SDL2 کی تمام لائبریریاں شامل کر دی ہیں
requirements = python3, kivy==2.2.1, kivymd==1.1.1, cryptography, pyjnius, sdl2_image, sdl2_ttf, sdl2_mixer, sdl2

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Android API Settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
