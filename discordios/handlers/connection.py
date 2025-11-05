"""Connection management"""

import logging

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages Discord gateway connection state"""
    
    def __init__(self):
        """Initialize connection manager"""
        self.connected = False
        self.session_id = None
        self.sequence = None
        self.device = None
    
    def set_connected(self, status, device=None):
        """
        Set connection status
        
        Args:
            status: bool - Connection status
            device: str - Device name (optional)
        """
        self.connected = status
        if device:
            self.device = device
        
        status_str = 'connected' if status else 'disconnected'
        logger.info(f"Connection: {status_str}")
    
    def set_session(self, session_id, sequence):
        """
        Set session information
        
        Args:
            session_id: str - Discord session ID
            sequence: int - Message sequence number
        """
        self.session_id = session_id
        self.sequence = sequence
        logger.debug(f"Session updated: {session_id[:8]}...")
    
    def get_info(self):
        """Get connection information"""
        return {
            'connected': self.connected,
            'session_id': self.session_id,
            'sequence': self.sequence,
            'device': self.device
        }
    
    def reset(self):
        """Reset connection state"""
        self.connected = False
        self.session_id = None
        self.sequence = None
        logger.info("Connection state reset")
    
    def is_ready(self):
        """Check if connection is ready"""
        return self.connected and self.session_id is not None
    
    def __repr__(self):
        return f"ConnectionManager(connected={self.connected}, device={self.device})"