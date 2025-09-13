import logging
from mcp_server import mcp

logger = logging.getLogger(__name__)

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """
    Writes hello world.

    :param name: str:  (Default value = "World")

    """
    logger.info(f"Greeting request for: {name}")
    return f"Hello, {name}! 👋"
