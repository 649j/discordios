"""
DiscordiOS - Make your Discord bot appear as a mobile device
"""

__version__ = "1.0.1"
__author__ = "B3nderServices"
__license__ = "MIT"
__url__ = "https://github.com/B3nderServices/DiscordiOS"

from .core.client import apply_mobile_status, setup_mobile_status, reset_status

from .models.enums import DeviceType, Platform
from .models.config import MobileConfig

from .exceptions.errors import (
    DiscordiOSException,
    InvalidDeviceError,
    GatewayError,
    ConfigurationError
)

from .utils.helpers import get_device_info, format_device_name
from .utils.validators import validate_platform

__all__ = [
    'apply_mobile_status',
    'setup_mobile_status',
    'reset_status',
    
    'DeviceType',
    'Platform',
    'MobileConfig',

    'DiscordiOSException',
    'InvalidDeviceError',
    'GatewayError',
    'ConfigurationError',
    
    'get_device_info',
    'format_device_name',
    'validate_platform',
    
    '__version__',
]