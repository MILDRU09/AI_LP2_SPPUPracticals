def show_menu():
    print("\n📋 You can ask me the following things:")
    print("1. Say 'hi' or 'hello' → Greeting")
    print("2. Ask 'hours' or 'time' → Store timings")
    print("3. Ask 'location' → Store location")
    print("4. Ask 'products' → View available items")
    print("5. Type 'order' → Check order status")
    print("6. Type 'help' → Show menu again")
    print("7. Type 'bye' → Exit chatbot\n")


def chatbot():
    print("🤖 Chatbot: Hello! Welcome to our store.")
    show_menu()   # show menu at start
    
    while True:
        user = input("You: ").lower()

        if user in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Thank you! Have a nice day 😊")
            break

        elif "hi" in user or "hello" in user:
            print("🤖 Chatbot: Hello! How can I assist you?")

        elif "time" in user or "hours" in user:
            print("🤖 Chatbot: We are open from 9 AM to 9 PM.")

        elif "location" in user:
            print("🤖 Chatbot: We are located in the city center.")

        elif "product" in user:
            print("🤖 Chatbot: We sell clothes, shoes, and accessories.")

        elif "order" in user:
            order_id = input("Enter your order ID: ")
            print(f"🤖 Chatbot: Order {order_id} is being processed.")

        elif "help" in user:
            show_menu()

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Type 'help' to see options.")

# Run chatbot
chatbot()