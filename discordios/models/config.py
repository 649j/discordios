"""Configuration management for mobile devices"""

from .enums import DeviceType, Platform


class MobileConfig:
    """Configuration for mobile device emulation"""
    
    def __init__(
        self,
        device=DeviceType.IOS,
        compress=True,
        large_threshold=250,
        api_version=3,
        custom_properties=None
    ):
        """
        Initialize mobile configuration
        
        Args:
            device: DeviceType or str - Device to emulate
            compress: bool - Enable compression
            large_threshold: int - Large guild threshold
            api_version: int - Discord API version
            custom_properties: dict - Custom connection properties
        """
        self.device = self._parse_device(device)
        self.compress = compress
        self.large_threshold = large_threshold
        self.api_version = api_version
        self.custom_properties = custom_properties or {}
        self._platform_info = Platform.get(self.device)
    
    def _parse_device(self, device):
        """Parse device string to DeviceType"""
        if isinstance(device, DeviceType):
            return device
        
        if isinstance(device, str):
            device_lower = device.lower()
            for dt in DeviceType:
                if dt.value == device_lower:
                    return dt
        
        return DeviceType.IOS
    
    def get_properties(self):
        """Get Discord connection properties"""
        properties = {
            '$os': self._platform_info['os'],
            '$browser': self._platform_info['browser'],
            '$device': self._platform_info['device'],
            '$referrer': '',
            '$referring_domain': ''
        }
        
        # Merge custom properties
        properties.update(self.custom_properties)
        
        return properties
    
    def get_platform_info(self):
        """Get platform information"""
        return self._platform_info.copy()
    
    def to_dict(self):
        """Convert config to dictionary"""
        return {
            'device': self.device.value,
            'compress': self.compress,
            'large_threshold': self.large_threshold,
            'api_version': self.api_version,
            'platform_info': self._platform_info
        }
    
    def __repr__(self):
        return f"MobileConfig(device={self.device.value})"
    
    def __str__(self):
        return f"Mobile Config: {self.device.value}"