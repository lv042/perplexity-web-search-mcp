import os
import httpx
import logging
from typing import Optional
from enum import Enum
from mcp_server import mcp

logger = logging.getLogger(__name__)

class PerplexityModel(str, Enum):
    """Available Perplexity Sonar models for different use cases."""
    SONAR = "sonar"
    SONAR_PRO = "sonar-pro"
    SONAR_DEEP_RESEARCH = "sonar-deep-research"
    SONAR_REASONING = "sonar-reasoning"
    SONAR_REASONING_PRO = "sonar-reasoning-pro"

class SearchMode(str, Enum):
    """Search mode options for Perplexity API."""
    WEB = "web"
    ACADEMIC = "academic"

def _call_perplexity_api(query: str, model: str = PerplexityModel.SONAR, search_mode: str = SearchMode.WEB, 
                        recency_filter: Optional[str] = None, city: Optional[str] = None, country: Optional[str] = None) -> str:
    """Helper function to call Perplexity API.

    Args:
        query: The search query to send to Perplexity API
        model: The Perplexity model to use (default: PerplexityModel.SONAR)
        search_mode: The search mode to use (default: SearchMode.WEB)
        recency_filter: Time filter for results (e.g., 'week', 'day')
        city: City name for location-based search
        country: Two letter ISO country code

    Returns:
        str: The response content from Perplexity API or error message

    Raises:
        httpx.TimeoutException: If the API request times out
        Exception: For other API-related errors
    """
    logger.debug(f"Calling Perplexity API with model: {model}, search_mode: {search_mode}")
    
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
        "messages": [{"role": "user", "content": query}],
        "search_mode": search_mode
    }
    
    if recency_filter:
        payload["search_recency_filter"] = recency_filter
    
    if city or country:
        payload["web_search_options"] = {"user_location": {}}
        if city:
            payload["web_search_options"]["user_location"]["city"] = city
        if country:
            payload["web_search_options"]["user_location"]["country"] = country
    
    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            logger.info(f"API call successful for query: {query[:50]}...")
            return response.json()["choices"][0]["message"]["content"]
    except httpx.TimeoutException:
        logger.error("API call timed out")
        return "Error: Request timed out"
    except Exception as e:
        logger.error(f"API call failed: {str(e)}")
        return f"Error: {str(e)}"

@mcp.tool()
def web_search(query: str, model: PerplexityModel = PerplexityModel.SONAR, 
               recency_filter: Optional[str] = None, city: Optional[str] = None, country: Optional[str] = None) -> str:
    """Search the web using Perplexity Sonar API for real-time information.

    Args:
        query: The search query or question to ask Perplexity
        model: The Perplexity model to use. Options: "sonar", "sonar-pro", 
               "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro"
               (default: "sonar")
        recency_filter: Time filter for results (e.g., 'week', 'day')
        city: City name for location-based search
        country: Two letter ISO country code

    Returns:
        str: The search results and answer from Perplexity API
    """
    logger.info(f"Web search request: {query[:50]}...")
    return _call_perplexity_api(query, model, SearchMode.WEB, recency_filter, city, country)

@mcp.tool()
def web_search_academic(query: str, model: PerplexityModel = PerplexityModel.SONAR,
                       recency_filter: Optional[str] = None, city: Optional[str] = None, country: Optional[str] = None) -> str:
    """Search academic sources using Perplexity Sonar API for scholarly information.

    Args:
        query: The search query or question to ask Perplexity
        model: The Perplexity model to use. Options: "sonar", "sonar-pro", 
               "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro"
               (default: "sonar")
        recency_filter: Time filter for results (e.g., 'week', 'day')
        city: City name for location-based search
        country: Two letter ISO country code

    Returns:
        str: The search results from academic sources via Perplexity API
    """
    logger.info(f"Academic search request: {query[:50]}...")
    return _call_perplexity_api(query, model, SearchMode.ACADEMIC, recency_filter, city, country)
