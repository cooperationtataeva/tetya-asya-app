[app]
title = Тетя Ася
package.name = tetyaasyaapp
package.domain = com.tetyaasya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Включаем Kivy и все необходимые инструменты для работы с logo.png и скруглениями углов
requirements = kivy==2.3.1, sdl2_image, pillow

orientation = portrait
fullscreen = 1

# Разрешаем приложению открывать ваши ссылки в браузере телефона
android.permissions = INTERNET

# Фиксируем стабильные версии Android API
android.api = 33
android.minapi = 24
android.ndk_api = 24
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 0
