"""
Manages negotiation sessions per user
"""

from typing import Dict, Optional
from chat.negotiation_engine import NegotiationEngine
from products.models import Product
import uuid


class SessionManager:
    """
    Manages active negotiation sessions.
    In production, store this in Redis or database.
    For now, using in-memory dictionary.
    """
    
    def __init__(self):
        self.sessions: Dict[str, NegotiationEngine] = {}
    
    def create_session(self, user_id: str, product_id: int) -> str:
        """Create new negotiation session"""
        session_id = str(uuid.uuid4())
        product = Product.objects.get(pk=product_id)
        self.sessions[session_id] = NegotiationEngine(product)
        return session_id
    
    def get_session(self, session_id: str) -> Optional[NegotiationEngine]:
        """Get existing session"""
        return self.sessions.get(session_id)
    
    def end_session(self, session_id: str):
        """End and cleanup session"""
        if session_id in self.sessions:
            del self.sessions[session_id]
    
    def get_active_sessions_count(self) -> int:
        """Get number of active sessions"""
        return len(self.sessions)


# Global session manager instance
session_manager = SessionManager()
