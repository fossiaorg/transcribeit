from typing import Type, Callable, Any


def singleton(cls: Type[Any]) -> Callable[..., Any]:
    instances = {}

    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance