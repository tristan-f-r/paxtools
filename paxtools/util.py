__all__ = ['optional']

def optional(value: str, show: bool) -> list[str]:
    return [value] if show else []
