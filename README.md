# Project - Dreamline

This reimagined app concept was made possible with [Solara](https://solara.dev/) (From prototype to high quality web application in pure Python). The idea is to have a custom platform which can use different AI models as a plugin from which users can quickly switch between each other for their particular use-case, in a rich web applicaiton all built with Python (No Html or JavaScript).

![image](https://github.com/user-attachments/assets/9314f841-e4bf-44ac-9790-db3b55bcd1f2)

PS: Not just a generic chatbot application that integrates AI Apis like a typical streamlit app. 

# Dreamline Project Setup in VS Code with Virtual Environment

## 1. Create Project Directory

First, create a new folder for your project:

## 2. Create Virtual Environment

Create a new virtual environment:

```bash
# For Windows
python -m venv dreamlineapp

# For macOS/Linux
python3 -m venv dreamlineapp
```

## 3. Activate Virtual Environment

### Windows (Command Prompt):
```bash
dreamlineapp\Scripts\activate
```

### Windows (PowerShell):
```bash
dreamlineapp\Scripts\Activate.ps1
```

### macOS/Linux:
```bash
source dreamlineapp/bin/activate
```

You should see `(venv)` at the beginning of your command prompt when activated.

## 4. Create Requirements File

Create a `requirements.txt` file with the following content:

```txt
solara==1.38.0
openai==1.54.4
pandas==2.2.2
python-dotenv==1.0.0
```

## 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## 6. Create Project Files

Create the main application file `main.py` (copy the code from the artifact above).

## 7. Create Environment File

Create a `.env` file to store your API key:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

**Important**: Replace `your-openai-api-key-here` with your actual OpenAI API key.

## 8. Create .gitignore File

Create a `.gitignore` file to exclude sensitive files:

```gitignore
# Virtual environment
venv/
env/

# Environment variables
.env

# Chat history (optional - remove if you want to commit chat data)
chat_history/
uploads/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE files
.vscode/settings.json
.idea/

# OS files
.DS_Store
Thumbs.db
```

## 9. VS Code Setup

### Open Project in VS Code:
```bash
code .
```

### Install VS Code Extensions:
1. **Python** (by Microsoft) - Essential for Python development
2. **Python Debugger** (by Microsoft) - For debugging support
3. **Pylance** (by Microsoft) - Advanced Python language support

### Configure Python Interpreter:
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "Python: Select Interpreter"
3. Choose the interpreter from your virtual environment:
   - Windows: `.\venv\Scripts\python.exe`
   - macOS/Linux: `./venv/bin/python`

## 10. Update chatbot_app.py for Environment Variables

Add this code at the top of your `loadEnv.py` file to load environment variables:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```
Run this to load the .env variables into your environment.

## 11. Project Structure

Your final project structure should look like this:

```
chatbot-app/
├── dreamlineapp/         # Virtual environment (created automatically)
├── chat_history/         # Chat storage (created automatically)
├── uploads/              # File uploads (created automatically)
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── main.py               # Main application
├── loadEnv.py            # .env varible loader
└── README.md             # Project documentation (optional)
```

## 12. Run the Application

Make sure your virtual environment is activated and run:

```bash
solara run main.py
```

The application will start and display a URL (usually `http://localhost:8765`) where you can access your chatbot.


## Troubleshooting

### Common Issues:

1. **Virtual Environment Not Activating:**
   - Make sure you're in the correct directory
   - Try using the full path to the activation script

2. **Import Errors:**
   - Ensure virtual environment is activated
   - Verify all packages are installed: `pip list`

3. **API Key Issues:**
   - Check that your `.env` file is in the project root
   - Verify the API key is correct and has the right format

4. **VS Code Not Using Correct Python:**
   - Press `Ctrl+Shift+P` and select "Python: Select Interpreter"
   - Choose the interpreter from your `venv` folder

### Helpful VS Code Commands:

- `Ctrl+Shift+P`: Command Palette
- `Ctrl+`` `: Toggle Terminal
- `F5`: Start Debugging
- `Ctrl+F5`: Run Without Debugging

## Getting Your OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new secret key
5. Copy and paste it into your `.env` file

**Important**: Never commit your `.env` file to version control!

## Next Steps

Once everything is set up:

1. Test the application by running it
2. Test the chat functionality
3. Explore the chat history feature - future updates with DB
4. Customize the UI or add new features as needed

Your chatbot application is now ready for development and testing!
