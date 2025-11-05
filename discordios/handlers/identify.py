"""Identification handler for Discord gateway"""

import logging
from ..models.config import MobileConfig

logger = logging.getLogger(__name__)


class IdentifyHandler:
    """Handles Discord gateway identification"""
    
    def __init__(self, config):
        """
        Initialize identify handler
        
        Args:
            config: MobileConfig - Device configuration
        """
        self.config = config
    
    def build_base_payload(self, websocket):
        """Build base identification payload"""
        return {
            'op': websocket.IDENTIFY,
            'd': {
                'token': websocket.token,
                'properties': self.config.get_properties(),
                'compress': self.config.compress,
                'large_threshold': self.config.large_threshold,
                'v': self.config.api_version
            }
        }
    
    def add_shard_info(self, payload, websocket):
        """Add shard information to payload"""
        if websocket.shard_id is not None and websocket.shard_count is not None:
            payload['d']['shard'] = [websocket.shard_id, websocket.shard_count]
    
    def add_presence(self, payload, websocket):
        """Add presence information to payload"""
        state = websocket._connection
        if state._activity is not None or state._status is not None:
            payload['d']['presence'] = {
                'status': state._status,
                'game': state._activity,
                'since': 0,
                'afk': False
            }
    
    def add_intents(self, payload, websocket):
        """Add intents to payload"""
        state = websocket._connection
        if state._intents is not None:
            payload['d']['intents'] = state._intents.value
    
    def build_full_payload(self, websocket):
        """Build complete identification payload"""
        payload = self.build_base_payload(websocket)
        self.add_shard_info(payload, websocket)
        self.add_presence(payload, websocket)
        self.add_intents(payload, websocket)
        return payload
    
    async def send_identify(self, websocket):
        """Send identification to Discord gateway"""
        payload = self.build_full_payload(websocket)
        
        await websocket.call_hooks('before_identify', websocket.shard_id, initial=websocket._initial_identify)
        await websocket.send_as_json(payload)
        websocket._initial_identify = False
        
        logger.info(f"Sent IDENTIFY with device: {self.config.device.value}")


def create_identify_handler(config):
    """
    Create an identify function with the given config
    
    Args:
        config: MobileConfig - Device configuration
    
    Returns:
        Async function for gateway identification
    """
    handler = IdentifyHandler(config)
    
    async def identify(self):
        """Identify function to be patched into Discord websocket"""
        await handler.send_identify(self)
    
    return identify