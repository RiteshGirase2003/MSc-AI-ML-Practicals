# Slip : 7 Write a Python program to implement Simple Chatbot.

import re

# Predefined responses based on regex patterns
responses = {
    r'hi|hello|hey': "Hello! How can I assist you today?",
    r'bye|goodbye|see you': "Goodbye! Have a great day!",
    r'how are you': "I'm a bot, but I'm doing great! How about you?",
    r'(.*) your name': "I am a simple chatbot built with Python.",
    r'(.*)help(.*)': "Sure! I can assist you with simple queries. Ask me anything!",
    r'what (.*) (weather|temperature|climate)': "I can't check the weather right now, but you can try checking a weather app.",
    r'(.*)(time|date)': " time 12 pm"
}

# Function to match user input with regex patterns
def chatbot_response(user_input):
    # Iterate over the patterns and responses
    for key, value in responses.items():
        if re.search(key, user_input, re.IGNORECASE):  # Case-insensitive matching
            return value
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Simulate a chatbot conversation
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        # Get the chatbot's response
        print("Chatbot:", chatbot_response(user_input))
