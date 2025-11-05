"""Device type and platform enumerations"""

from enum import Enum


class DeviceType(Enum):
    """Available device types for Discord mobile emulation"""
    
    IOS = "ios"
    ANDROID = "android"
    DESKTOP = "desktop"
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"DeviceType.{self.name}"


class Platform(Enum):
    """Platform information for each device type"""
    
    IOS = {
        'os': 'iOS',
        'browser': 'Discord iOS',
        'device': 'iPhone',
        'icon': '📱',
        'version': '16.0',
        'user_agent': 'Discord-iOS/1.0'
    }
    
    ANDROID = {
        'os': 'Android',
        'browser': 'Discord Android',
        'device': 'Discord Android',
        'icon': '📱',
        'version': '13.0',
        'user_agent': 'Discord-Android/1.0'
    }
    
    DESKTOP = {
        'os': 'Windows',
        'browser': 'discord.py',
        'device': 'discord.py',
        'icon': '💻',
        'version': '10',
        'user_agent': 'Discord-Desktop/1.0'
    }
    
    @classmethod
    def get(cls, device_type):
        """
        Get platform info for a device type
        
        Args:
            device_type: str or DeviceType
        
        Returns:
            dict - Platform information
        """
        if isinstance(device_type, str):
            device_type = device_type.upper()
        elif isinstance(device_type, DeviceType):
            device_type = device_type.name
        
        try:
            return cls[device_type].value.copy()
        except KeyError:
            return cls.IOS.value.copy()
    
    @classmethod
    def get_all(cls):
        """Get all available platforms"""
        return {
            'ios': cls.IOS.value,
            'android': cls.ANDROID.value,
            'desktop': cls.DESKTOP.value
        }