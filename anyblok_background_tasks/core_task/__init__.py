"""Blok declaration example
"""
from typing import TYPE_CHECKING

from anyblok.blok import Blok

if TYPE_CHECKING:
    from types import ModuleType
    from typing import Callable


class Core_task(Blok):
    """Core_task's Blok class definition"""

    version = "0.1.0"
    author = "Pierre Verkest"
    required = ["anyblok-core", "anyblok-mixins"]

    @classmethod
    def import_declaration_module(cls) -> None:
        """Python module to import in the given order at start-up"""
        from . import tasks  # noqa

    @classmethod
    def reload_declaration_module(
        cls, reload: "Callable[[ModuleType], None]"
    ) -> None:
        """Python module to import while reloading server (ie when
        adding Blok at runtime
        """
        from . import tasks  # noqa

        reload(tasks)
