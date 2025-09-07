import logging
from mcp_server import mcp

logger = logging.getLogger(__name__)

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """Say hello to someone.

    Args:
        name: Name to greet (defaults to "World")
    """
    logger.info(f"Greeting request for: {name}")
    return f"Hello, {name}! 👋"
