from __future__ import annotations

from django_cachekey import __version__


def test_version():
    assert __version__ == "0.1.0dev0"
