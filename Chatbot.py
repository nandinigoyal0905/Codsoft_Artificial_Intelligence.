# Define a function to get the chatbot response based on user input
def get_response(user_input):
    # Convert the user input to lowercase for easier matching
    user_input = user_input.lower()

    # Define some predefined rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "I'm just a computer program, but thanks for asking!"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I can assist you with general information. Just ask me a question."
    elif "age" in user_input:
        return "I'm just a computer program, so I don't have an age."
    elif "name" in user_input:
        return "I don't have a name, but you can call me ChatBot."
    elif "who created you" in user_input:
        return "I was created by a team of developers."
    elif "what can you do" in user_input:
        return "I can answer questions, provide information, and engage in conversations."
    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "how's the weather" in user_input:
        return "I'm not connected to the internet, so I can't provide real-time weather information."
    elif "tell me a fact" in user_input:
        return "Did you know that honey never spoils?"
    elif "favorite color" in user_input:
        return "I don't have preferences, but I think all colors are interesting."
    elif "tell me a story" in user_input:
        return "Once upon a time, in a land far, far away..."
    elif "thank you" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."
    elif "how to contact support" in user_input:
        return "You can contact our support team at support@example.com."
    elif "favorite food" in user_input:
        return "I don't eat, so I don't have a favorite food."
    elif "what's your purpose" in user_input:
        return "My purpose is to assist and provide information to users."
    elif "tell me a riddle" in user_input:
        return "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? (Answer: An echo)"
    elif "how does a computer work" in user_input:
        return "Computers work by processing binary data using a combination of hardware and software."
    else:
        return "I'm sorry, I don't understand that."

# Main conversation loop
print("Chatbot: Hello! How can I assist you?")
while True:
    user_input = input("User: ")
    
    # Exit the loop if the user says goodbye
    if "goodbye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    # Get the chatbot's response
    response = get_response(user_input)
    print("Chatbot:", response)
