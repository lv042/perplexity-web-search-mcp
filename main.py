import logging
from mcp_server import mcp
from tools import hello_world, web_search, web_search_academic

# Mark imports as used for MCP registration
_ = hello_world, web_search, web_search_academic

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting Perplexity Sonar MCP server...")
    mcp.run()
