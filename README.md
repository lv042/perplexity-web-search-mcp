# 🔍 Perplexity Web-Search MCP

> **Supercharge your AI assistant with real-time web search and academic research capabilities**

An MCP (Model Context Protocol) server that integrates Perplexity's powerful Sonar API, giving your AI assistant access to current information from the web and scholarly sources.

## ✨ Features

- 🌐 **Real-time web search** - Get current information from across the internet
- 🎓 **Academic search** - Access peer-reviewed papers and scholarly sources  
- 📍 **Location-aware results** - Filter by city and country
- ⏰ **Time-filtered search** - Get recent results (day, week, etc.)
- 🧠 **Multiple AI models** - Choose from various Perplexity Sonar models
- 🔌 **Universal compatibility** - Works with any MCP-compatible system

## 🤖 Compatible AI Systems

This MCP server works seamlessly with:
- **Claude** (Anthropic)
- **Amazon Q Developer**
- **Google Gemini**
- **OpenAI Codex**
- **Any MCP-compatible AI assistant**

## 🚀 Exemplary Amazon Q Developer Setup

Here's how to properly integrate this MCP server with Amazon Q Developer:

### 1. Locate your Amazon Q agent configuration
```bash
~/.aws/amazonq/cli-agents/dev.json
```

### 2. Add the sonar MCP server to your configuration
```json
{
  "$schema": "https://raw.githubusercontent.com/aws/amazon-q-developer-cli/refs/heads/main/schemas/agent-v1.json",
  "name": "dev",
  "description": "",
  "mcpServers": {
    "sonar": {
      "command": "/Users/your-username/SoftwareProjects/perplexity_sonar_mcp/.venv/bin/python",
      "args": ["/Users/your-username/SoftwareProjects/perplexity_sonar_mcp/main.py"],
      "cwd": "/Users/your-username/SoftwareProjects/perplexity_sonar_mcp",
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-api-key-here"
      }
    }
  },
  "tools": [
    "fs_read",
    "fs_write",
    "execute_bash",
    "use_aws",
    "@sonar"
  ]
}
```

### 3. Usage Example
```bash
[dev] > Web search: "Is AI a bubble?"

🛠️  Using tool: web_search from mcp server sonar
 ⋮
 ● Running web_search with the param:
 ⋮  {
 ⋮    "name": "web_search",
 ⋮    "arguments": {
 ⋮      "query": "Is AI a bubble?"
 ⋮    }
 ⋮  }

Allow this action? Use 't' to trust (always allow) this tool for the session. [y/n/t]: y

 ⋮
 ● Completed in 9.990s

> Based on current market analysis, AI is widely considered to be in a bubble phase...
```

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
