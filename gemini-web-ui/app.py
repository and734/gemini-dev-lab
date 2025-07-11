# app.py

import subprocess
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the main route for our web page
@app.route('/', methods=['GET', 'POST'])
def index():
    # This variable will hold the result from the Gemini CLI
    result = None
    # This will hold the original prompt to display it back to the user
    prompt = ""

    # Check if the form was submitted (i.e., it's a POST request)
    if request.method == 'POST':
        # Get the prompt from the form's textarea
        prompt = request.form['prompt']

        # --- IMPORTANT ---
        # This is where we call the gemini-cli tool.
        # We use subprocess.run to execute the command.
        # Using a list like ['gemini', prompt] is safer than a single string
        # as it helps prevent shell injection vulnerabilities.
        try:
            # Execute the command: `gemini "your prompt here"`
            # `capture_output=True` captures stdout and stderr.
            # `text=True` decodes them as text (UTF-8).
            # `check=True` will raise an exception if the command returns a non-zero exit code (an error).
            completed_process = subprocess.run(
                ['gemini', prompt], 
                capture_output=True, 
                text=True, 
                check=True
            )
            # Get the standard output from the command
            result = completed_process.stdout
        except subprocess.CalledProcessError as e:
            # If the command fails, show the error message
            result = f"An error occurred:\n{e.stderr}"
        except FileNotFoundError:
            # If the 'gemini' command isn't found
            result = "Error: 'gemini' command not found. Is it installed and in your PATH?"

    # Render the HTML template. Pass the prompt and result to the template.
    # On a GET request, prompt and result will be empty.
    # On a POST request, they will contain the user's data and the AI's response.
    return render_template('index.html', prompt=prompt, result=result)

# This allows the script to be run directly
if __name__ == '__main__':
    # Run the app on host 0.0.0.0 to make it accessible
    # in the Codespace and on port 3000.
    app.run(host='0.0.0.0', port=3000)
    