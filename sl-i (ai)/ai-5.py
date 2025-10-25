def get_chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()

    if any(greet in user_input_lower for greet in ["hello", "hi", "hey"]):
        return (
            "👋 Hello there! I'm your virtual assistant for MyOnlineStore. "
            "How can I help you today? You can ask about orders, shipping, or returns."
        )

    elif any(phrase in user_input_lower for phrase in ["order status", "where is my order", "track my order"]):
        return "📦 Sure! Please provide your 5-digit order number, and I’ll check the latest status for you."

    elif any(word in user_input_lower for word in ["shipping", "delivery", "how long"]):
        return (
            "🚚 Our standard shipping takes 3-5 business days. "
            "Express delivery options are also available at checkout. "
            "You can learn more on our Shipping Policy page."
        )

    elif any(word in user_input_lower for word in ["return", "refund", "exchange"]):
        return (
            "↩️ You can return unused items within 30 days for a full refund or exchange. "
            "Please visit our Returns Portal to start the process."
        )

    elif any(word in user_input_lower for word in ["talk to human", "speak to a person", "agent"]):
        return "👩‍💼 Connecting you to a human agent... Please hold on for a moment."

    elif user_input_lower.isdigit() and len(user_input_lower) == 5:
        return f"✅ Thank you! Your order #{user_input_lower} is currently *In Transit* and will arrive in 2–3 business days. You can also check your email for a tracking link."

    else:
        return (
            "❓ I'm sorry, I didn’t quite get that. "
            "Could you please rephrase or ask about orders, shipping, or returns?"
        )


if __name__ == "__main__":
    print("🤖 Welcome to MyOnlineStore Chatbot! (Type 'exit' to quit)")
    while True:
        user_input = input("👤: ")
        if user_input.lower() == "exit":
            print("🤖: Goodbye! Have a great day! 👋")
            break
        response = get_chatbot_response(user_input)
        print(f"🤖: {response}")