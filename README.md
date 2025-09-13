# 🔍 Perplexity Sonar MCP

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
