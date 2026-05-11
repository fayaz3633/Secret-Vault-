[app]
title = VIP Vault
package.name = vipvault
package.domain = org.fayyaz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Requirements (صرف پائتھن کی لائبریریاں)
requirements = python3, kivy, kivymd, cryptography, pyjnius

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# Android specific (اینڈرائیڈ کی خاص لائبریریاں یہاں آئیں گی)
android.permissions = USE_BIOMETRIC, USE_FINGERPRINT, INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.gradle_dependencies = 'androidx.security:security-crypto:1.1.0-alpha06', 'androidx.biometric:biometric:1.1.0'

[buildozer]
log_level = 2
warn_on_root = 1
