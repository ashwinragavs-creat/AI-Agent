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