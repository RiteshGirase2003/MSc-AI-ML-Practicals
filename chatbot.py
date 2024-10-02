# Slip : 7 Write a Python program to implement Simple Chatbot.


class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "how are you?": "I'm just a computer program, but thanks for asking!",
            "what is your name?": "I'm a simple chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!",
            "help": "You can ask me about my functions, or just say 'bye' to exit."
        }

    def get_response(self, user_input):
        if user_input not in self.responses:
            return "i am sorry i can't find answer"
        else:
            return self.responses[user_input]
        # return self.responses.get(user_input, "I'm sorry, I don't understand that.")

    def chat(self):
        print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input.lower())
            print("Chatbot:", response)
            if user_input.lower() == "bye":
                break

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
