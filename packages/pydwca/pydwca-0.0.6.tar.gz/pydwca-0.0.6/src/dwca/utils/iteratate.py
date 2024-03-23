from typing import Iterator, TypeVar

T = TypeVar('T')


def iterate_with_bar(iterator: Iterator[T], **kwargs) -> T:
    try:
        from tqdm import tqdm
        return tqdm(iterator, **kwargs)
    except ImportError:
        return iterator
