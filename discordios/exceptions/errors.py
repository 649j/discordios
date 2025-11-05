"""Custom exceptions for DiscordiOS"""


class DiscordiOSException(Exception):
    """Base exception for DiscordiOS"""
    
    def __init__(self, message="An error occurred in DiscordiOS"):
        self.message = message
        super().__init__(self.message)


class InvalidDeviceError(DiscordiOSException):
    """Raised when an invalid device type is provided"""
    
    def __init__(self, device, valid_devices=None):
        self.device = device
        self.valid_devices = valid_devices or ['ios', 'android', 'desktop']
        message = (
            f"Invalid device: '{device}'. "
            f"Valid options: {', '.join(self.valid_devices)}"
        )
        super().__init__(message)


class GatewayError(DiscordiOSException):
    """Raised when there's an error with the Discord gateway"""
    
    def __init__(self, message="Gateway error occurred"):
        super().__init__(message)


class ConfigurationError(DiscordiOSException):
    """Raised when there's a configuration error"""
    
    def __init__(self, message="Configuration error occurred"):
        super().__init__(message)


class ValidationError(DiscordiOSException):
    """Raised when validation fails"""
    
    def __init__(self, field, message=None):
        self.field = field
        if message is None:
            message = f"Validation failed for field: {field}"
        super().__init__(message)