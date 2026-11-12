[app]
# (str) Title of your application
title = SKYNET

# (str) Package name
package.name = skynet

# (str) Package domain (must be in reverse DNS format)
package.domain = org.skynet.app

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (comma separated)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
# Aqui dizemos que o app precisa do python3 e do kivy para funcionar
requirements = python3,kivy

# (str) Orientation of the app
orientation = portrait

# (int) Fullscreen mode
fullscreen = 0

# (int) Android API to use
# API 33 é o Android 13, a mais estável para compilação via GitHub Actions
android.api = 33

# Aceita as licenças do SDK no ambiente não interativo do GitHub Actions
android.accept_sdk_license = True

# (int) Minimum Android API
android.minapi = 21

# (list) Android architectures to build for
# arm64-v8a é o padrão para quase todos os celulares modernos
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = False

# (list) Permissions
# Se você for adicionar funções de internet ou arquivos no futuro, adicione aqui
android.permissions = INTERNET

[buildozer]
# (int) Log level (0 = error, 1 = warn, 2 = info)
log_level = 2

# (int) Warn on root
warn_on_root = 1
