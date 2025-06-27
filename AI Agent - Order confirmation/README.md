# README.md
// filepath: /AI Agent - Order confirmation\README.md

# AI Agent - Order Confirmation

This project is an AI-powered chat agent that helps users confirm their order status using a 6-digit order number. The agent interacts with users, validates order numbers, and fetches order status from a local dataset.

## Features

- Conversational AI agent for order confirmation
- Validates 6-digit order numbers
- Fetches order status from a local JSON file
- Handles chat termination and invalid queries

## Files

- `ai_agent.py`: Main chat agent logic
- `mytools.py`: Tool functions for order status lookup
- `data.json`: Sample order data

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the chat agent:
   ```
   python ai_agent.py
   ```

## Requirements

- Python 3.8+
- See `requirements.txt` for Python packages

## Notes

- The agent uses the [Groq API](https://groq.com/) for AI chat completions. You must provide a valid API key in `ai_agent.py`.
- All responses are in JSON format as per the system prompt.
