"""Helper utility functions"""

from ..models.enums import DeviceType, Platform


def get_device_info(platform):
    """
    Get device information for a platform
    
    Args:
        platform: str or DeviceType - Platform to get info for
    
    Returns:
        dict - Device information
    
    Example:
        info = get_device_info('ios')
        print(info['os'])  # 'iOS'
    """
    if isinstance(platform, str):
        platform = platform.upper()
    elif isinstance(platform, DeviceType):
        platform = platform.name
    else:
        platform = 'IOS'
    
    return Platform.get(platform)


def format_device_name(platform):
    """
    Format device name for display
    
    Args:
        platform: str or DeviceType - Platform to format
    
    Returns:
        str - Formatted device name with icon
    
    Example:
        name = format_device_name('ios')
        print(name)  # '📱 iPhone'
    """
    info = get_device_info(platform)
    return f"{info['icon']} {info['device']}"


def get_all_devices():
    """
    Get information for all available devices
    
    Returns:
        dict - All device information
    
    Example:
        devices = get_all_devices()
        for name, info in devices.items():
            print(f"{name}: {info['device']}")
    """
    return Platform.get_all()


def compare_devices(device1, device2):
    """
    Compare two devices
    
    Args:
        device1: str or DeviceType - First device
        device2: str or DeviceType - Second device
    
    Returns:
        bool - True if devices are the same
    """
    info1 = get_device_info(device1)
    info2 = get_device_info(device2)
    return info1['device'] == info2['device']