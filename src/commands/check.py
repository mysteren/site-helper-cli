import sys
from typing import List, TypedDict, cast

import requests

from src.services.csv import from_csv, to_csv
from src.services.fs import get_asset_path


class UrlRow(TypedDict):
    url: str


class UrlStatusRow(TypedDict):
    url: str
    status: str


def check_pages(params: str):
    data = _loadData(f"{params}_pages.local.csv")
    print(f"Данные: {data}")

    # Проверяем статусы ссылок
    result_data = check_url_statuses(data)

    # Сохраняем в новый CSV файл
    output_filename = f"{params}_pages_with_status.local.csv"
    to_csv(
        cast(list[dict[str, str]], result_data),
        get_asset_path(output_filename),
        fieldnames=["url", "status"],
    )
    print(f"Результаты сохранены в {output_filename}")


def _loadData(filename: str):
    data: List[UrlRow] = from_csv(get_asset_path(filename))
    return data


def check_url_statuses(data: List[UrlRow]) -> List[UrlStatusRow]:
    """
    Проверяет HTTP статус каждой ссылки (следует редиректам) и возвращает
    данные с колонкой статуса.

    Args:
        data: Список словарей с URL-адресами

    Returns:
        Список словарей с url и status
    """
    result: List[UrlStatusRow] = []
    total = len(data)
    bar_width = 40

    for i, row in enumerate(data):
        url = row.get("url", "")
        if not url:
            status = "EMPTY_URL"
        else:
            try:
                response = requests.get(url, timeout=10, allow_redirects=True)
                status = str(response.status_code)
            except requests.exceptions.Timeout:
                status = "TIMEOUT"
            except requests.exceptions.RequestException as e:
                status = f"ERROR: {type(e).__name__}"

        result.append({"url": url, "status": status})

        # Прогресс-бар
        progress = (i + 1) / total if total > 0 else 1
        filled = int(bar_width * progress)
        bar = "=" * filled + " " * (bar_width - filled)
        percent = int(progress * 100)
        sys.stdout.write(f"\r[{bar}] {percent}% ({i + 1}/{total})")
        sys.stdout.flush()

    sys.stdout.write("\n")

    return result
