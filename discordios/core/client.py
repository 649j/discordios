import logging
import discord
from ..models.config import MobileConfig
from ..handlers.identify import create_identify_handler
from ..utils.validators import validate_platform
from ..exceptions.errors import InvalidDeviceError

logger = logging.getLogger(__name__)

_original_identify = discord.gateway.DiscordWebSocket.identify


def setup_mobile_status(platform='ios', config=None):
    # Validate platform
    if not validate_platform(platform):
        raise InvalidDeviceError(platform)
    
    # Convert string to lowercase
    if isinstance(platform, str):
        platform = platform.lower()
    
    # Create config if not provided
    if config is None:
        config = MobileConfig(device=platform)
    
    # Create and apply the identify function
    identify_func = create_identify_handler(config)
    discord.gateway.DiscordWebSocket.identify = identify_func
    
    logger.info(f"Applied mobile status: {config.device.value}")
    
    return identify_func


def apply_mobile_status(platform='ios', **kwargs):
    """
    Apply mobile status to Discord bot
    
    Args:
        platform: str or DeviceType - 'ios', 'android', or 'desktop'
        **kwargs: Additional arguments passed to MobileConfig
    
    Example:
        apply_mobile_status('ios')
        apply_mobile_status('android', compress=True)
        bot = discord.Client(intents=discord.Intents.default())
    """
    
    # Create config with kwargs
    config = MobileConfig(device=platform, **kwargs)
    
    return setup_mobile_status(platform, config)


def reset_status():
    """
    Reset to original Discord status
    
    Example:
        reset_status()
        bot = discord.Client(intents=discord.Intents.default())
    """
    discord.gateway.DiscordWebSocket.identify = _original_identify
    logger.info("Reset to original Discord status")






