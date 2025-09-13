# Perplexity Sonar MCP

MCP server for Perplexity Sonar integration providing web and academic search capabilities.

## Installation

### With uv (recommended)
```bash
uv sync
```

### With pip
```bash
pip install -e .
```

## MCP Configuration

Add to your MCP client configuration:

**With uv:**
- Transport Type: STDIO  
- Command: uv  
- Arguments: run main.py

**With Python:**
- Transport Type: STDIO  
- Command: python  
- Arguments: main.py

## Environment Setup

Set your Perplexity API key:
```bash
export PERPLEXITY_API_KEY="your-api-key-here"
```

## Usage

### With uv
```bash
uv run python main.py
```

### With Python
```bash
python main.py
```

## Requirements

- Python >=3.10
- `PERPLEXITY_API_KEY` environment variable

## Tools

### `hello_world`
Basic example tool for testing MCP functionality.

### `web_search`
Search the web using Perplexity Sonar API for real-time information.

**Parameters:**
- `query` (required): The search query or question
- `model` (optional): Perplexity model - "sonar", "sonar-pro", "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro" (default: "sonar")
- `recency_filter` (optional): Time filter for results (e.g., 'week', 'day')
- `city` (optional): City name for location-based search
- `country` (optional): Two letter ISO country code

### `web_search_academic`
Search academic sources using Perplexity Sonar API for scholarly information. Prioritizes peer-reviewed papers and academic journals.

**Parameters:**
- `query` (required): The search query or question
- `model` (optional): Perplexity model - "sonar", "sonar-pro", "sonar-deep-research", "sonar-reasoning", "sonar-reasoning-pro" (default: "sonar")
- `recency_filter` (optional): Time filter for results (e.g., 'week', 'day')
- `city` (optional): City name for location-based search
- `country` (optional): Two letter ISO country code

## Configuration

Set your Perplexity API key:
```bash
export PERPLEXITY_API_KEY="your-api-key-here"
```
