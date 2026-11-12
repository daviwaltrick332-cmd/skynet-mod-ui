# 🌌 SKYNET Android Control Panel

Este projeto é uma interface de demonstração para Android desenvolvida em **Python** utilizando o framework **Kivy**. O objetivo é criar um painel de controle moderno, com design escuro e elementos interativos (switches e sliders).

## 🚀 Como gerar o APK (Instruções de Build)

Este projeto utiliza o **GitHub Actions** para compilar o código Python em um arquivo `.apk` instalável, eliminando a necessidade de instalar o Linux ou o Buildozer localmente.

### Passo a Passo:

1. **Subir os arquivos:** Certifique-se de que o `main.py`, `buildozer.spec` e a pasta `.github/workflows/` estão no repositório.
2. **Acessar Actions:** No menu superior do GitHub, clique na aba **Actions**.
3. **Selecionar Workflow:** No menu lateral esquerdo, clique em **"Build SKYNET Android APK"**.
4. **Iniciar Build:** Clique no botão **Run workflow** $\rightarrow$ **Run workflow**.
5. **Aguardar:** O processo leva cerca de 20 minutos para baixar o Android SDK/NDK e compilar o app.
6. **Baixar APK:** Quando o processo terminar (check verde), clique na execução e baixe o arquivo `skynet-debug-apk` na seção **Artifacts**.

## 📱 Instalação no Celular

1. Extraia o arquivo `.zip` baixado do GitHub.
2. Transfira o arquivo `.apk` para o seu dispositivo Android.
3. Abra o arquivo no celular.
4. **Importante:** Como o app não foi baixado da Play Store, o Android solicitará que você autorize a **"Instalação de fontes desconhecidas"** nas configurações de segurança.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework UI:** Kivy
- **Compilador:** Buildozer
- **CI/CD:** GitHub Actions
- **Alvo:** Android API 33 (arm64-v8a)

## ⚠️ Aviso Legal

Este aplicativo é uma **demonstração de interface (UI)**. Os botões e sliders alteram apenas estados internos do aplicativo e não possuem a capacidade de ler memória de outros processos, modificar jogos ou burlar sistemas de segurança.
