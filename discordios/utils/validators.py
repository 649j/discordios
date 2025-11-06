from ..models.enums import DeviceType
from ..models.config import MobileConfig


def validate_platform(platform):
    """
    Validate if a platform is valid
    
    Args:
        platform: str or DeviceType - Platform to validate
    
    Returns:
        bool - True if valid, False otherwise
    
    Example:
        if validate_platform('ios'):
            print("Valid platform!")
    """
    if isinstance(platform, DeviceType):
        return True
    
    if isinstance(platform, str):
        valid = ['ios', 'android', 'desktop']
        return platform.lower() in valid
    
    return False


def validate_config(config):
    """
    Validate a MobileConfig object
    
    Args:
        config: MobileConfig - Configuration to validate
    
    Returns:
        bool - True if valid, False otherwise
    """
    if not isinstance(config, MobileConfig):
        return False
    
    # Check required attributes
    required = ['device', 'compress', 'large_threshold', 'api_version']
    return all(hasattr(config, attr) for attr in required)


def validate_device_type(device):
    """
    Validate device type
    
    Args:
        device: any - Value to validate as device type
    
    Returns:
        bool - True if valid DeviceType
    """
    return isinstance(device, DeviceType)


def validate_api_version(version):
    """
    Validate API version
    
    Args:
        version: int - API version to validate
    
    Returns:
        bool - True if valid version
    """

    return isinstance(version, int) and version > 0
