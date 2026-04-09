import sys

from src.commands.check import check_pages

from .commands.diff import get_diff


def main():
    # Проверяем аргументы командной строки
    if len(sys.argv) < 2:
        print("Ошибка: укажите команду!")
        show_help()
        return

    command = sys.argv[1]  # Первый аргумент - команда
    param = sys.argv[2] if len(sys.argv) > 2 else None  # Второй аргумент - параметр

    # Обработка команд
    if command == "diff":
        if param is None:
            print("Ошибка: для команды diff нужен дополнительный параметр!")
            show_help()
        else:
            print(f"Выполняется diff с параметром: {param}")
            get_diff(param)  # Раскомментируйте когда будет готова функция

    elif command == "check":
        if param is None:
            print("Ошибка: для команды <|user_cursor|> нужен дополнительный параметр!")
            show_help()
        else:
            print(f"Выполняется <|user_cursor|> с параметром: {param}")
            check_pages(param)  # Раскомментируйте когда будет готова функция
    else:
        print(f"Неизвестная команда: {command}")
        show_help()


def show_help():
    """Выводит справку по доступным командам."""
    print("Доступные команды:")
    print("- diff <name> - Разница между списками страниц, выдает новый список ")
    print("- check <name> - проверка статусов страниц ")
    print("Использование:  python -m  src.main<команда> <параметр>")


if __name__ == "__main__":
    main()
