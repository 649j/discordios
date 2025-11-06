import logging
from ..models.config import MobileConfig

logger = logging.getLogger(__name__)


class GatewayPayload:
    """Handles creation of Discord gateway payloads"""
    
    def __init__(self, config=None):
        """
        Initialize gateway payload handler
        
        Args:
            config: MobileConfig - Configuration for the device
        """
        self.config = config or MobileConfig()
    
    def build_payload(self, websocket):
        """
        Build IDENTIFY payload
        
        Args:
            websocket: DiscordWebSocket instance
        
        Returns:
            dict - Complete IDENTIFY payload
        """
        payload = {
            'op': websocket.IDENTIFY,
            'd': {
                'token': websocket.token,
                'properties': self.config.get_properties(),
                'compress': self.config.compress,
                'large_threshold': self.config.large_threshold,
                'v': self.config.api_version
            }
        }
        
        # Add shard info
        if websocket.shard_id is not None and websocket.shard_count is not None:
            payload['d']['shard'] = [websocket.shard_id, websocket.shard_count]
        
        # Add presence
        state = websocket._connection
        if state._activity is not None or state._status is not None:
            payload['d']['presence'] = {
                'status': state._status,
                'game': state._activity,
                'since': 0,
                'afk': False
            }
        
        # Add intents
        if state._intents is not None:
            payload['d']['intents'] = state._intents.value
        
        return payload
    
    def create_identify(self):
        """
        Create an identify function for Discord gateway
        
        Returns:
            Async function that sends IDENTIFY payload
        """
        config = self.config
        
        async def identify(self):
            """Send IDENTIFY payload with mobile device properties"""
            
            # Create gateway handler
            gateway = GatewayPayload(config)
            payload = gateway.build_payload(self)
            
            # Call hooks and send
            await self.call_hooks('before_identify', self.shard_id, initial=self._initial_identify)
            await self.send_as_json(payload)
            self._initial_identify = False
            
            logger.info(f"Sent IDENTIFY with device: {config.device.value}")
        
        return identify


def create_identify_function(config):
    """
    Create an identify function with the given config
    
    Args:
        config: MobileConfig - Device configuration
    
    Returns:
        Async function for gateway identification
    """
    gateway = GatewayPayload(config)

    return gateway.create_identify()
