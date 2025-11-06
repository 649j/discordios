from ..models.enums import DeviceType
from ..models.config import MobileConfig


def validate_platform(platform):
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
    
    required = ['device', 'compress', 'large_threshold', 'api_version']
    return all(hasattr(config, attr) for attr in required)


def validate_device_type(device):
    return isinstance(device, DeviceType)


def validate_api_version(version):
    return isinstance(version, int) and version > 0



