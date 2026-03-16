import csv
from typing import Any, Dict, List, TypeVar, cast

T = TypeVar("T", bound=Dict)


#
def from_csv(filename: str) -> List[T]:
    """
    Читает CSV файл и возвращает List[Dict].

    Args:
        filename: Путь к CSV файлу

    Returns:
        Список словарей из CSV строк
    """
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return cast(List[T], list(reader))


K = TypeVar("K", bound=Dict[str, Any])


#
def to_csv(content: List[K], filename: str, fieldnames: List[str] | None = None):
    """
    Сохраняет список словарей в CSV файл.

    Args:
        content: Список словарей (List[Dict])
        filename: Имя выходного CSV файла
        fieldnames: Список имён колонок (если None — берёт из первого словаря)
    """
    if not content:
        print("Список пуст — ничего не сохраняем")
        return

    # Определяем заголовки
    if fieldnames is None:
        fieldnames = list(content[0].keys())

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Заголовки
        writer.writerows(content)  # Данные
