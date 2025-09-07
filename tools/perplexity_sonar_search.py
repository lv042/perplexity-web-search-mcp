import os
import httpx
import logging
from enum import Enum
from mcp_server import mcp

logger = logging.getLogger(__name__)

class PerplexityModel(str, Enum):
    SONAR = "sonar"
    SONAR_PRO = "sonar-pro"
    SONAR_DEEP_RESEARCH = "sonar-deep-research"
    SONAR_REASONING = "sonar-reasoning"
    SONAR_REASONING_PRO = "sonar-reasoning-pro"

def _call_perplexity_api(query: str, model: str = PerplexityModel.SONAR_PRO) -> str:
    """Helper function to call Perplexity API."""
    logger.debug(f"Calling Perplexity API with model: {model}")
    
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        logger.error("PERPLEXITY_API_KEY not set")
        return "Error: PERPLEXITY_API_KEY environment variable not set"
    
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": query}]
    }
    
    try:
        with httpx.Client() as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            logger.info(f"API call successful for query: {query[:50]}...")
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"API call failed: {str(e)}")
        return f"Error: {str(e)}"

@mcp.tool()
def perplexity_sonar_search(query: str, model: PerplexityModel = PerplexityModel.SONAR) -> str:
    """Search using Perplexity Sonar API for real-time information."""
    logger.info(f"Search request: {query[:50]}...")
    return _call_perplexity_api(query, model)
