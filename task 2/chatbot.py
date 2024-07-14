import random
import nltk
from nltk.chat.util import Chat, reflections
def greet():
    responses = ["Hello!", "Hi", "Hi There!", "Greetings!"]
    return random.choice(responses)

def goodbye():
    responses = ["Bye :)", "Good Bye :)", "see You Later:)", "Take Care!"]
    return random.choice (responses)

def welcome():
    responses = ["Your Welcome", "Welcome" "No Mention!"]
    return random.choice (responses)

def chatbot_response (user_input):
    if user_input.lower() == "hello" or user_input.lower() == "hi" or user_input.lower() == "hey":
        return greet()
    
    elif user_input.lower() == "how are you":
        return "I'm doing well, thank You!"

    elif user_input.lower() == "what is your name?" or user_input.lower() == "Who are you?" or user_input.lower() == "Who are you":
        return "I'm a chatbot, I'm here to help you"
    
    elif user_input.lower() == "sorry":
        return " It's alright, no worries"
    
    elif user_input.lower() == "bye" or user_input.lower() == "good bye":
        return goodbye()
    
    elif user_input.lower() == "thank You":
        return welcome()
    
    else:
        return " i'm just a basic chatbot. I don't understand what you are looking for.But if I were you,I would go and google it."

def chat():
    print("Welcome to the Chatbot!")
    print("You can start chatting, or type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response (user_input))
            break
        else:
            print("Chatbot: ", chatbot_response (user_input))
            
chat()
