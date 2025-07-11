# gemini-dev-lab


Gemini CLI Web UI

A simple, self-hosted web interface to interact with the gemini-cli command-line tool. This project provides a web form to send prompts to the Gemini API and displays the results directly on the page, turning your command-line tool into a private web application.

This project is designed to be extremely lightweight and is perfect for running in cloud development environments like GitHub Codespaces.

Features

Simple Web Interface: A clean, no-frills UI to enter prompts and see results.

Backend Integration: Uses Python's subprocess module to call the gemini-cli tool running on the server.

Preserves Formatting: Displays the raw text output from the CLI, preserving line breaks and code blocks.

Easy to Deploy: Runs anywhere Python and gemini-cli are installed, with special convenience for GitHub Codespaces.

Self-Contained: No external databases or complex dependencies are required.

Technology Stack

Backend: Python 3 with the Flask web framework.

Frontend: Plain HTML and CSS.

Core Engine: The gemini-cli tool.

Environment: Optimized for GitHub Codespaces.

Getting Started

Follow these instructions to get the project up and running in your own environment.

Prerequisites

Python 3: Ensure you have Python 3.x installed.

Gemini CLI: You must have the gemini-cli tool installed and authenticated with your API key. You can test this by running gemini "hello" in your terminal. If this command works, you are ready.

Installation & Setup

Clone or Create the Project Files:
Create a project directory and the necessary files.

Generated bash
mkdir gemini-web-ui
cd gemini-web-ui
touch app.py
mkdir templates
touch templates/index.html
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Populate the Files:
Copy the code from the original guide into app.py and templates/index.html.

Install Dependencies:
This project only requires Flask.

Generated bash
pip install Flask
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Run the Application:
Execute the main Python script.

Generated bash
python3 app.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

The server will start, typically on http://127.0.0.1:3000.

Running in GitHub Codespaces

If you are running this in a GitHub Codespace:

After running python3 app.py, Codespaces will automatically detect the running service on port 3000.

A notification will appear in the bottom-right corner of VS Code. Click "Open in Browser".

Alternatively, go to the PORTS tab in the terminal panel, find port 3000, and click the globe icon (Open in Browser) to access the web UI.

How It Works

User Interaction: A user visits the web page and submits a prompt through an HTML form.

Flask Backend: The Flask application receives the prompt via a POST request.

Subprocess Call: The backend executes the gemini command as a system subprocess, passing the user's prompt as an argument (e.g., subprocess.run(['gemini', prompt], ...)).

Capture Output: The application captures the standard output (the text response) from the gemini-cli command.

Render Response: The captured text is sent back to the index.html template, which then renders it for the user to see.

Project Structure
Generated code
gemini-web-ui/
├── app.py          # The main Flask application logic
├── templates/
│   └── index.html  # The HTML template for the web interface
└── README.md       # This file
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END
Future Improvements

This is a minimal implementation. Here are some ideas for extending its functionality:

AJAX for No Page Reload: Use JavaScript (fetch API) to submit the form asynchronously for a smoother, chatbot-like experience.

Streaming Responses: Implement response streaming to show the text as it's being generated.

Conversation History: Add a session-based mechanism to store and display the conversation history.

Error Handling: Provide more user-friendly error messages (e.g., if the Gemini API key is invalid or the service is down).

Model Selection: Add a dropdown to select different Gemini models if your CLI supports it.
