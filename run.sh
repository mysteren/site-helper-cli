#!/bin/bash

# Получаем директорию, где находится этот скрипт
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Переходим в директорию проекта
cd "$SCRIPT_DIR" || {
    echo "Ошибка: не удалось перейти в директорию $SCRIPT_DIR"
    exit 1
}

# Запускаем Python модуль, передавая все аргументы ($@)
python -m src.main "$@"
