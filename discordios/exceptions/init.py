"""Exception definitions"""

from .errors import (
    DiscordiOSException,
    InvalidDeviceError,
    GatewayError,
    ConfigurationError,
    ValidationError
)

__all__ = [
    'DiscordiOSException',
    'InvalidDeviceError',
    'GatewayError',
    'ConfigurationError',
    'ValidationError',
]