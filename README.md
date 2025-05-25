# CustomerSupportAgent

## Project Description
This project is a simple command-line customer support agent that simulates interaction with Anthropic's Claude API. It's designed to take a user's query and return a (currently mock) response, demonstrating basic application structure, input handling, and API key management.

The core functionality lies in `src/customer_support_agent/main.py`, which prompts the user for input and calls a function to simulate fetching a response.

## Setup and Configuration

### API Key
To use this agent (even in its current mock state, and especially when connecting to a real API), you need to configure your Claude API key.

1.  Open the file `src/customer_support_agent/main.py`.
2.  Locate the line:
    `CLAUDE_API_KEY = "YOUR_CLAUDE_API_KEY_HERE"`
3.  Replace `"YOUR_CLAUDE_API_KEY_HERE"` with your actual Claude API key.

**Important**: The script includes a reminder and an error check for this placeholder key. If the key is not replaced, the script will print a warning and the `get_claude_response` function will return an error message.

## Running the Agent
To run the customer support agent:

1.  Navigate to the root directory of the project in your terminal.
2.  Execute the script using the following command:
    ```bash
    python src/customer_support_agent/main.py
    ```
3.  The script will then prompt you to enter your query.

## Testing
Unit tests are located in the `tests/` directory and can be run using Python's `unittest` module. From the root project directory, run:
```bash
python -m unittest discover tests
```
