"""
@Author: Fabio Casagrande Hirono
================================
Models:
-------
    xxx
    Available classes:
    ---------------------
        >>> TestSetup
        >>> AirfoilGeom
        >>> FrequencyVars
        >>> xxx
    For further information, check the class specific documentation.
"""

from .TestSetup import TestSetup
from .AirfoilGeom import AirfoilGeom
from .FrequencyVars import FrequencyVars

__all__ = [  # Classes
    'TestSetup',
    'AirfoilGeom',
    'FrequencyVars']
