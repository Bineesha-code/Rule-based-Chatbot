# Task-8
# Rule-based Chatbot
# Author: Bineesha K P
# Date: 25-06-2025

def chatbot():
    print("Hy! I am Bitu the Chatbot!. (Type 'exit' to end the chat)")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Bitu: Hello there! How can I help you?")
        elif user_input in ["how are you?", "how are you"]:
            print("Bitu: I'm doing great.Thank You!")
        elif user_input in ["what is your name?", "your name"]:
            print("Bitu: I am Bitu, your friendly chatbot.")
        elif user_input in ["bye", "exit"]:
            print("Bitu: Goodbye! Have a nice day.")
            break
        else:
            print("Bitu: Sorry, I didn't understand that.")

chatbot()
