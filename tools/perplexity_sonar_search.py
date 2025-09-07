import os
import httpx
from mcp_server import mcp

def _call_perplexity_api(query: str, model: str = "sonar-pro") -> str:
    """Helper function to call Perplexity API."""
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
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
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def perplexity_sonar_search(query: str, model: str = "sonar") -> str:
    """Search using Perplexity Sonar API for real-time information."""
    return _call_perplexity_api(query, model)
