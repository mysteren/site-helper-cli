from urllib.parse import urlparse


def extract_uri(full_url: str) -> str:
    """
    Извлекает URI из полного URL (убирает схему и хост).

    Args:
        full_url: Полный URL вида 'https://example.com/path?query#fragment'

    Returns:
        Только URI часть: '/path?query#fragment'
    """
    parsed = urlparse(full_url)
    # Объединяем path + query + fragment без хоста и схемы
    uri_parts = [part for part in (parsed.path, parsed.query, parsed.fragment) if part]
    return "/".join(uri_parts) if uri_parts else "/"


def normalize_uri(uri: str) -> str:
    """
    Корректирует URI: добавляет ведущий слеш '/', если его нет.

    Args:
        uri: URI вида 'path/to/page' или '/path/to/page'

    Returns:
        Нормализованный URI, всегда начинающийся с '/'
    """
    return uri if uri.startswith("/") else f"/{uri}"
