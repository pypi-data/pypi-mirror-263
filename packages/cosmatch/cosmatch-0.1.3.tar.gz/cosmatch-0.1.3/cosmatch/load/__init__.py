from .data_loader import Retriever
from .data_loader import PS1, Gaia

from .data_loader import CatalogLoader
from .data_loader import CSC2, DESI

from .data_loader import clear_downloaded_files, download_vizier_catalog

from ..settings import local_package_path
import os

if not os.path.exists(local_package_path('downloaded_catalogues')):
    os.makedirs(local_package_path('downloaded_catalogues'))

__all__ = [
    'Retriever',
    'PS1',
    'Gaia',

    'CatalogLoader',
    'CSC2',
    'DESI',

    'clear_downloaded_files',
    'download_vizier_catalog',
]
