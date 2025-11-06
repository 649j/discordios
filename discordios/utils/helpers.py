from ..models.enums import DeviceType, Platform


def get_device_info(platform):
    if isinstance(platform, str):
        platform = platform.upper()
    elif isinstance(platform, DeviceType):
        platform = platform.name
    else:
        platform = 'IOS'
    
    return Platform.get(platform)


def format_device_name(platform):
    info = get_device_info(platform)
    return f"{info['icon']} {info['device']}"


def get_all_devices():
    return Platform.get_all()


def compare_devices(device1, device2):
    info1 = get_device_info(device1)
    info2 = get_device_info(device2)

    return info1['device'] == info2['device']

