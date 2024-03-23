#!/bin/env python3

__all__ = ('Client', 'JsonManager', 'my_id')

__version__ = '0.1.7'
VERSION = __version__

from .client import Client, my_id
from .json_manager import JsonManager
