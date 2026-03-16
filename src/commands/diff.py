from typing import List, TypedDict

from src.services.fs import get_asset_path
from src.services.url import extract_uri, normalize_uri

from ..services.csv import from_csv, to_csv


class UrlRow(TypedDict):
    url: str


def get_diff(params: str):
    db = _loadData(f"{params}_db.csv")
    wm = _loadData(f"{params}_wm.csv")

    dbUrlsSet = {_format_url_row(row)["url"] for row in db}
    wmUrlsSet = {_format_url_row(row)["url"] for row in wm}

    missing = dbUrlsSet - wmUrlsSet

    count = len(missing)

    print(f"Количество  страниц не в индексе: {count}")

    # 🔥 СОХРАНЯЕМ через to_csv
    if missing:
        _save_missing_urls(missing, f"{params}_missing.csv")

    return


def _format_url_row(row: UrlRow) -> UrlRow:
    return {"url": normalize_uri(extract_uri(row["url"]))}


def _save_missing_urls(missing: set[str], filename: str):
    """Специально для set[str] → CSV с колонкой 'url'."""
    urls_list = [{"url": url} for url in sorted(missing)]
    to_csv(urls_list, get_asset_path(filename), fieldnames=["url"])


def _loadData(filename: str):
    data: List[UrlRow] = from_csv(get_asset_path(filename))
    return data
