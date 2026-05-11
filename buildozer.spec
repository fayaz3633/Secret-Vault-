[app]
title = Secret Vault
package.name = secretvault
package.domain = org.yourname.vault
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0.0
requirements = python3,kivy,cryptography,pyjnius,plyer,android
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.api = 30
android.minapi = 23
android.ndk = 23b
android.permissions = USE_BIOMETRIC, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.allow_backup = True
android.gradle_dependencies = 'androidx.biometric:biometric:1.1.0'
# optional
icon = icon.png
presplash = splash.png
