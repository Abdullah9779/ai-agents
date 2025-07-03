# AI Agent Assistant

This project is a simple AI agent assistant using LangChain and Groq LLM, with search and Wikipedia tools.

## Features
- Conversational AI agent
- Uses Groq LLM (deepseek-r1-distill-llama-70b)
- Integrates search and Wikipedia tools
- Maintains chat history

## Setup
1. Clone the repository or download the code.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file (if required by your tools).

## Usage
Run the assistant:
```bash
python main.py
```
Type your queries. Type `exit` or `quit` to stop the assistant.

## Files
- `main.py`: Main entry point for the AI agent.
- `tools.py`: Contains tool definitions (e.g., search, Wikipedia).
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Notes
- Make sure you have the necessary API keys or environment variables set in your `.env` file for Groq and any other services.
