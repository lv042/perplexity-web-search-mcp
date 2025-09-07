import logging
from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

mcp = FastMCP("perplexity-sonar-mcp")
logger.info("MCP server initialized")
