[app]

# (str) Title of your application
title = AutoRing

# (str) Package name
package.name = autoring

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyjnius,plyer

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android >= presplash support)
# Supported formats are: #RRGGBB, #AARRGGBB, red, blue, green, black, white...
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = RECORD_AUDIO, MODIFY_AUDIO_SETTINGS, WAKE_LOCK

# (int) Android API to use
#android.api = 27

# (int) Minimum API required
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public (False)
#android.private_storage = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) Android blacklist filenames
#android.blacklist_filenames = addons-3.0.0.zip,blacklist.txt

# (list) Android whitelist filenames
#android.whitelist_filenames =

# (str) Path to Android AARs to copy into libs/armeabi
#android.add_aars =

# (list) Android argument to pass to `apkbuilder`
#android.apkbuilder_args =

# (str) Android bootstrap (e.g. sdl2, service, webview)
p4a.bootstrap = sdl2

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Full name including package path of the Java class that implements PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra XML to write directly inside the <manifest> element of AndroidManifest.xml
#android.manifest_extra =

# (str) Extra XML to write directly inside the <manifest><application> element of AndroidManifest.xml
#android.manifest_application_extra =

# (str) Full name including package path of the Java class that implements PythonService
#android.service_class_name = org.kivy.android.PythonService

# (bool) Indicate whether the screen should stay on
#android.wakelock = False

# (list) Android app dependencies in the format:
#android.add_dependency_com.android.support:support-v4:19.0.1,android.arch.core:common:1.1.0

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies' is enabled
#android.enable_androidx = False

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (list) Add compile options
#android.add_compile_options =

# (list) Gradle repositories to add {name:value}
#android.gradle_repositories =

# (list) packaging options to add {name:value}
#android.add_packaging_options =

# (str) Path to a custom build.gradle file
#android.custom_build =

# (list) Android plugins to add
#android.add_plugins =

# (str) API key for Google Analytics (used only if 'android.gradle_dependencies' is enabled)
#android.google_services.json =

# (bool) Indicate whether your application includes OpenCV functionality
#android.use_opencv = False

# (bool) Allow android logcat to display log messages in a notification
#android.notification_logcat = True

# (list) Android gradle arguments
#android.gradle_args =

# (str) Reference to a custom AndroidManifest.xml file
#android.manifest_file =

# (bool) Enable the force build all recipes option
#android.force_build_all = False

# (str) Packaging to use (e.g. "aab", "apk" or "both")
#android.packaging = "apk"

# (bool) Enable the android arm64 build
#android.arm64 = True

# (bool) Enable the android x86 build
#android.x86 = False

# (bool) Enable the android x86_64 build
#android.x86_64 = False

# (str) Android resource files to copy directly to the APK
#android.resources =

# (str) Path to a JSON file containing the 'Play Services' API keys
#android.play_services_json =

# (str) Path to a directory containing 'Play Services' AARs
#android.play_services_aar_dir =

# (list) extra command to pass when building with Gradle
#android.extra_cmds =

# (str) Buildozer log level
log_level = 2

# (bool) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

# -------------------------------------------------------------------
# List as sections
# You can define all the "list" as [section:key].
# Each line will be considered as a option to the list.
# Let's take [app] / source.exclude_patterns.
# Instead of doing:
# [app]
# source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
# This can be translated into:
# [app:source.exclude_patterns]
# license
# data/audio/*.wav
# data/images/original/*
# -------------------------------------------------------------------

# -------------------------------------------------------------------
# Profiles
# You can extend section / key with a profile
# For example, you want to deploy a demo version of your application without
# HD content. You could first change the title to add "(demo)" in the name
# and extend the excluded directories to remove the HD content.
# [app@demo]
# title = My Application (demo)
# [app:source.exclude_patterns@demo]
# images/hd/*
# Then, invoke the command line with the "demo" profile:
# buildozer --profile demo android debug
# -------------------------------------------------------------------
