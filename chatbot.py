print("🤖 Chatbot: Hello! I am a simple rule-based chatbot.")
print("🤖 Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "name" in user_input:
        print("Bot: I'm a simple rule-based chatbot.")

    elif "help" in user_input:
        print("Bot: Sure! You can ask me about my name, how I am, or say hello.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "bye" in user_input:
        print("Bot: Goodbye! Have a nice day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try something else.")