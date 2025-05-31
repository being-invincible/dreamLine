# Dreamline Project Setup in VS Code with Virtual Environment

![image](https://github.com/user-attachments/assets/9314f841-e4bf-44ac-9790-db3b55bcd1f2)

# Dreamline Project Setup in VS Code with Virtual Environment

## 1. Create Project Directory

First, create a new folder for your project:

```bash
mkdir chatbot-app
cd chatbot-app
```# Chatbot Project Setup in VS Code with Virtual Environment

## 1. Create Project Directory

First, create a new folder for your project:

```bash
mkdir chatbot-app
cd chatbot-app
```

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
openai==1.51.0
pandas==2.2.2
PyPDF2==3.0.1
Pillow==10.4.0
```

## 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## 6. Create Project Files

Create the main application file `chatbot_app.py` (copy the code from the artifact above).

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

Add this code at the top of your `chatbot_app.py` file to load environment variables:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

Then update the requirements.txt to include python-dotenv:

```txt
solara==1.38.0
openai==1.51.0
pandas==2.2.2
PyPDF2==3.0.1
Pillow==10.4.0
python-dotenv==1.0.0
```

Install the new dependency:

```bash
pip install python-dotenv
```

## 11. Project Structure

Your final project structure should look like this:

```
chatbot-app/
├── venv/                 # Virtual environment (created automatically)
├── chat_history/         # Chat storage (created automatically)
├── uploads/              # File uploads (created automatically)
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── chatbot_app.py       # Main application
└── README.md            # Project documentation (optional)
```

## 12. Run the Application

Make sure your virtual environment is activated and run:

```bash
python chatbot_app.py
```

The application will start and display a URL (usually `http://localhost:8765`) where you can access your chatbot.

## 13. VS Code Debugging Setup (Optional)

Create `.vscode/launch.json` for debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Chatbot App",
            "type": "python",
            "request": "launch",
            "program": "chatbot_app.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

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
2. Try uploading different file types (PDF, Excel, images)
3. Test the chat functionality
4. Explore the chat history feature
5. Customize the UI or add new features as needed

Your chatbot application is now ready for development and testing!

## 2. Create Virtual Environment

Create a new virtual environment:

```bash
# For Windows
python -m venv venv

# For macOS/Linux
python3 -m venv venv
```

## 3. Activate Virtual Environment

### Windows (Command Prompt):
```bash
venv\Scripts\activate
```

### Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```

### macOS/Linux:
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt when activated.

## 4. Create Requirements File

Create a `requirements.txt` file with the following content:

```txt
solara==1.38.0
openai==1.51.0
pandas==2.2.2
PyPDF2==3.0.1
Pillow==10.4.0
```

## 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## 6. Create Project Files

Create the main application file `chatbot_app.py` (copy the code from the artifact above).

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

Add this code at the top of your `chatbot_app.py` file to load environment variables:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
```

Then update the requirements.txt to include python-dotenv:

```txt
solara==1.38.0
openai==1.51.0
pandas==2.2.2
PyPDF2==3.0.1
Pillow==10.4.0
python-dotenv==1.0.0
```

Install the new dependency:

```bash
pip install python-dotenv
```

## 11. Project Structure

Your final project structure should look like this:

```
chatbot-app/
├── venv/                 # Virtual environment (created automatically)
├── chat_history/         # Chat storage (created automatically)
├── uploads/              # File uploads (created automatically)
├── .env                  # Environment variables
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── chatbot_app.py       # Main application
└── README.md            # Project documentation (optional)
```

## 12. Run the Application

Make sure your virtual environment is activated and run:

```bash
python chatbot_app.py
```

The application will start and display a URL (usually `http://localhost:8765`) where you can access your chatbot.

## 13. VS Code Debugging Setup (Optional)

Create `.vscode/launch.json` for debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Chatbot App",
            "type": "python",
            "request": "launch",
            "program": "chatbot_app.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "PYTHONPATH": "${workspaceFolder}"
            }
        }
    ]
}
```

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
2. Try uploading different file types (PDF, Excel, images)
3. Test the chat functionality
4. Explore the chat history feature
5. Customize the UI or add new features as needed

Your chatbot application is now ready for development and testing!
