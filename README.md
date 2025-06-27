# Vkvideo-dl
Vkvideo-dl - это утилита для быстрого потокового скачивания видео с ВК.

[![Windows](https://custom-icon-badges.demolab.com/badge/Windows-0078D6?logo=windows11&logoColor=white)](#)
[![License: Unlicense](https://img.shields.io/github/license/Alexey-Proger/vkvideo-dl)](https://github.com/Alexey-Proger/vkvideo-dl/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/Alexey-Proger/vkvideo-dl)](https://github.com/Alexey-Proger/vkvideo-dl/releases/latest)
> [!WARNING]
> **Данный материал предоставляется автором для ознакомления.**
>
> Автор не поддерживает пиратство и всё, что-либо связанное с этим.
---
## 💻 Требования для запуска:
- Windows 10 или новее
- Установленный Microsoft Edge или Google Chrome
---
## 🚀 Использование
1. Скачайте [последний релиз программы](https://github.com/Alexey-Proger/vkvideo-dl/releases)
2. Запустите его
3. Следуйте инструкциям в консоли
4. Готово!

> [!NOTE]
> Также Вы можете залогиниться в ВК для скачивания некоторых непубличных видео.
> Приложение и разработчик НЕ собирают данные вашего аккаунта ВК.
---
## 🔨 Сборка из исходников
1. Установите зависимости, используя команду:
    ```shell
    pip install -r requirements.txt
    ```
2. Установите pyinstaller:
    ```shell
    pip install pyinstaller
    ```
3. Соберите скрипт:
    ```shell
    pyinstaller --onefile vkvideo-dl.py
    ```
