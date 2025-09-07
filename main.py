import logging
from mcp.server.fastmcp import FastMCP
from tools import hello_world

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("perplexity-sonar-mcp")
logger.info("Perplexity Sonar MCP server initialized")

# Register tools
mcp.tool()(hello_world)

if __name__ == "__main__":
    logger.info("Starting Perplexity Sonar MCP server...")
    mcp.run()
