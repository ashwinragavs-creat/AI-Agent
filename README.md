# AI-Agent

from google import genai
from google.genai import types
from datetime import datetime

client = genai.Client(api_key="AIzaSyCNB9GT-KtsBdO_6nfbeyKmS3HVE4R3HVY")
TODO_FILE = "todos.txt" 

def add_todo(task: str) -> str:
    """Add a task to the todo list file."""
    with open(TODO_FILE, "a") as f:
        f.write(f"[ ] {task}\n")
    return f"✅ Added: {task}"

def show_todos() -> str:
    """Show all todos from file."""
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.read().strip()
        return tasks if tasks else "📋 No tasks yet!"
    except FileNotFoundError:
        return "📋 No tasks yet!"
    
def complete_todo(task_number: int) -> str:
    """Mark a task as complete in file."""
    with open(TODO_FILE, "r") as f:
        lines = f.readlines()
    lines[task_number-1] = lines[task_number-1].replace("[ ]", "[✓]")
    with open(TODO_FILE, "w") as f:
        f.writelines(lines)
    return f"🎉 Completed task {task_number}!"

def get_time() -> str:
    return datetime.now().strftime("🕐 %H:%M:%S")

def get_weather(city: str) -> str:
    city_lower = city.lower()
    if city_lower in weather_data:
        return f"Weather in {city}: {weather_data[city_lower]}"
    return f"Weather in {city}: 🌡️ 22°C (default)"

def calculate(expression: str) -> str:
    """Calculate a math expression and return the result."""
    try:
        return f"The answer is: {eval(expression)}"
    except:
        return "Sorry, I couldn't calculate that."


chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction="You are Buddy, a friendly assistant that manages todos!",
        tools=[add_todo, show_todos, complete_todo, get_time,get_weather,calculate]
    )
)

print("🤖 Buddy is ready! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        break
    response = chat.send_message(user_input)
    print(f"Buddy: {response.text}\n")


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
