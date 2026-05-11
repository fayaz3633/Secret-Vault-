[app]

# (str) Title of your application
title = Secret Vault

# (str) Package name
package.name = secretvault

# (str) Package domain (needed for android packaging)
package.domain = org.fayaz

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# MD Icons اور دیگر ضروری لائبریریز شامل ہیں
requirements = python3,kivy,kivymd,pillow,cryptography,pyjnius

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA

# (int) Target Android API, should be as high as possible.
# ہم نے اسے 33 پر سیٹ کیا ہے تاکہ نیا سسٹم اسے قبول کرے
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (leave empty to download)
android.ndk_path =

# (str) Android SDK directory (leave empty to download)
android.sdk_path =

# (str) ANT directory (leave empty to download)
android.ant_path =

# (bool) If True, then skip trying to update the SDK
# اسے ہم نے خودکار طریقے سے لائسنس قبول کرنے کے لیے True کیا ہے
android.accept_sdk_license = True

# (str) Android entry point, default is to use start.py
android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to exclude for the build
# android.exclude_exts =

# (list) List of Java files to add to the android project
# android.add_java_src =

# (list) Android AAR archives to add
# android.add_aars =

# (str) python-for-android branch to use, if not master
# p4a.branch = master

# (str) The directory in which python-for-android should look for your own recipes (if any)
# p4a.local_recipes =

# (str) The directory in which python-for-android should look for your own builds
# p4a.hook =

# (str) The bootstrap to use for android builds
p4a.bootstrap = sdl2

# (int) Log level (2 = depth output)
# اسے 2 پر رکھا ہے تاکہ اگر کوئی مسئلہ ہو تو ہمیں تفصیل مل سکے
log_level = 2

# (bool) Show screen orientation choices
android.show_choices = False

[buildozer]

# (str) Path to build artifacts (default is ./.buildozer)
bin_dir = ./bin

