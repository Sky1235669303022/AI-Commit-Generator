# Smart Commit Generator

## 📖 Overview

This project is an AI-powered tool that generates professional Git commit messages from code changes. It uses the Google AI Studio API to analyze a code diff and create a concise, standardized commit message.

## ✨ Features

-   Analyzes code changes (diff) to understand their purpose.
-   Generates commit messages in a standardized format (e.g., `feat:`, `fix:`).
-   Simple web-based user interface.

## 🚀 Getting Started

### **Prerequisites**

-   Python 3.8 or higher
-   A Google AI Studio API key

### **Installation**

1.  Clone the repository:
    `git clone https://github.com/your_username/smart-commit-generator.git`
    `cd smart-commit-generator`
2.  Install the required libraries:
    `pip install -r requirements.txt`

### **Configuration**

1.  Get your API key from [Google AI Studio](https://aistudio.google.com/).
2.  Set your API key as an environment variable in your terminal:
    `set GEMINI_API_KEY="YOUR_API_KEY_HERE"`

### **Usage**

1.  Start the backend server:
    `python app.py`
2.  Open the `frontend/index.html` file in your browser to use the application.