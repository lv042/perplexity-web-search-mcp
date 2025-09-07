from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("perplexity-sonar-mcp")

@mcp.tool()
def hello_world(name: str = "World") -> str:
    """Say hello to someone.

    Args:
        name: Name to greet (defaults to "World")
    """
    return f"Hello, {name}! 👋 Change #2"

if __name__ == "__main__":
    mcp.run()
