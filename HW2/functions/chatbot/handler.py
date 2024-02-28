import sys
import datetime
import re
import random

# Function to generate FIGlet text
def generate_figlet(input_text):
    # Simulated response for demonstration purposes
    return f"Generated FIGlet for: {input_text}"

# Function to handle user queries
def handle_request(request):
    query = request.lower()

    # Respond to queries based on keywords
    if 'figlet for name' in query:
        response = generate_figlet("ChatBot")
    elif 'figlet for date' in query:
        current_date = datetime.datetime.now().date()
        response = generate_figlet(str(current_date))
    elif 'figlet for time' in query:
        current_time = datetime.datetime.now().time()
        response = generate_figlet(str(current_time))
    elif 'name' in query:
        response = random.choice(["Hello, my name is ChatBot", 
                                  "You can call me ChatBot", 
                                  "Hello, I am ChatBot"])
    elif 'date' in query:
        current_date = datetime.datetime.now().date()
        response = random.choice(["Current date is: " + str(current_date),
                                  "Today's date is: " + str(current_date),
                                  "At this moment the date reads as " + str(current_date)])
    elif 'time' in query:
        current_time = datetime.datetime.now().time()
        response = random.choice(["Time is: " + str(current_time),
                                  "Right now the clock shows " + str(current_time),
                                  "Current time is: " + str(current_time)])
    elif 'figlet' in query:
        pattern = r"figlet for (.*)"
        match = re.search(pattern, query)
        if match:
            response = generate_figlet(match.group(1))
        else:
            response = "Write figlet query in format: figlet for <text>"
    else:
        response = """I apologize, I didn't understand your question.
                      Please try again with the following questions:
                      1. What is your name?
                      2. What is the current time?
                      3. Generate figlet for Hello World"""

    return response

if __name__ == "__main__":
    input_text = sys.stdin.read().strip()
    print(handle_request(input_text))
