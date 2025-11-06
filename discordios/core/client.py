import logging
import discord
from ..models.config import MobileConfig
from ..handlers.identify import create_identify_handler
from ..utils.validators import validate_platform
from ..exceptions.errors import InvalidDeviceError

logger = logging.getLogger(__name__)

_original_identify = discord.gateway.DiscordWebSocket.identify


def setup_mobile_status(platform='ios', config=None):
    if not validate_platform(platform):
        raise InvalidDeviceError(platform)
    
    if isinstance(platform, str):
        platform = platform.lower()
    
    if config is None:
        config = MobileConfig(device=platform)
    
    identify_func = create_identify_handler(config)
    discord.gateway.DiscordWebSocket.identify = identify_func
    
    logger.info(f"Applied mobile status: {config.device.value}")
    
    return identify_func


def apply_mobile_status(platform='ios', **kwargs):
    config = MobileConfig(device=platform, **kwargs)
    
    return setup_mobile_status(platform, config)


def reset_status():
    discord.gateway.DiscordWebSocket.identify = _original_identify
    logger.info("Reset to original Discord status")
