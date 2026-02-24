# AI-Agent

Buddy is a command-line AI assistant built using Google Gemini (genai SDK) that helps users manage their daily tasks efficiently. It can add, display, and complete todos, check the current time, perform calculations, and even provide weather updates — all through natural language interaction.

This project demonstrates how to integrate LLM tools with Python functions to create a smart, tool-enabled conversational assistant

Features:
✅ Add new tasks to a todo list
📋 View all pending tasks
🎉 Mark tasks as completed
🕐 Get current system time
🌦️ Get weather information (basic logic)
➗ Perform mathematical calculations
💬 Natural language interaction powered by Gemini

Tech Stack:
*Python
*Google Gemini API (google-genai SDK)
*File handling for persistent todo storage
*Tool calling with LLM integration

How It Works:
1.The Gemini model is initialized using genai.Client.
2.Custom Python functions are registered as tools.
3.The AI automatically decides when to call a tool.
4.Tasks are stored locally in a text file (todos.txt).
5.The assistant responds conversationally.
