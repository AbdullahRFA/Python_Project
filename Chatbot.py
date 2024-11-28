responses = {
    #About Owner
    "who created you": "Abdullah Nazmus-Sakib, student of JU at CSE department",
    # Greetings
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How can I assist you today?",
    "hey": "Hey! What's up?",
    "good morning": "Good morning! Hope you have a great day ahead.",
    "good evening": "Good evening! How can I assist you?",

    # Status inquiries
    "how are you": "I'm just a bot, but I'm doing fine! How about you?",
    "what's up": "Not much, just here to help you!",
    "how's it going": "Everything is going well! How can I assist you?",

    # Gratitude
    "thank you": "You're welcome! Let me know if there's anything else I can do.",
    "thanks": "Anytime! I'm here to help.",
    "thanks a lot": "You're very welcome!",

    # Farewells
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Take care! See you soon.",
    "see you later": "Catch you later!",
    "take care": "You too! Stay safe.",

    # Basic questions
    "what is your name": "I am your friendly chatbot. What's your name?",
    "who are you": "I'm a chatbot created to assist you with your queries.",
    "where are you from": "I'm from the cloud, living in your device!",
    "what can you do": "I can chat with you, answer questions, and assist you with information.",

    # Common small talk
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "tell me a fun fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
    "do you like me": "Of course! I enjoy chatting with you.",
    "do you have any hobbies": "I love learning new things and helping people like you!",
    "are you human": "Nope, I'm a bot, but I try to be helpful and friendly.",

    # Weather-related
    "what's the weather like": "I'm not connected to live weather data right now, but you can check a weather app for that!",
    "is it going to rain": "I'm not sure, but carrying an umbrella is always a good idea.",
    
    # Food-related
    "what should I eat": "How about trying something new today? Maybe pizza or pasta?",
    "do you like pizza": "I can't eat, but pizza sounds delicious!",
    "can you cook": "I can't cook, but I can find you some great recipes!",

    # Time-related
    "what time is it": "I'm not sure of the current time. You can check your device for that!",
    "what day is it": "You can check your calendar for that! But I hope it's a good day.",

    # Help-related
    "can you help me": "Of course! What do you need help with?",
    "i need help": "Sure! Please tell me what you need assistance with.",
    "how do i": "Can you tell me more about what you're trying to do? I'll do my best to help.",

    # Technology-related
    "what is python": "Python is a programming language known for its simplicity and versatility.",
    "how do i learn programming": "You can start with online resources like Codecademy, freeCodeCamp, or YouTube tutorials.",
    "what is ai": "AI, or Artificial Intelligence, refers to systems that can perform tasks that typically require human intelligence, like learning and problem-solving.",

    # Fun
    "sing a song": "La la la! 🎵 I'm not a great singer, but I can try!",
    "dance": "I can't dance, but I can play some music for you!",
    "tell me something": "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to heat expansion!",

    # Personal questions
    "do you have a family": "Not really, but I consider everyone I chat with as a friend!",
    "do you sleep": "Nope, I’m available 24/7 to help you!",
    "do you know me": "I know that you're awesome because you're chatting with me!",

    # Miscellaneous
    "why is the sky blue": "The sky appears blue because of the way Earth's atmosphere scatters sunlight.",
    "what is love": "Love is a beautiful emotion that connects people. It's also a complex topic for a bot like me!",
    "can you solve math problems": "Sure! Ask me a math question, and I'll try my best.",
}

while True:
    try:
        question = input("\nMessage or Query for Chatbot (type 'exit' to quit): ").strip().lower()
        
        # Exit condition
        if question == "exit":
            print("\nGoodbye! Have a great day!\n")
            break
        
        # Respond to the user's question
        if question in responses:
            print(f"\n{responses[question]} \n")
        else:
            print("\nI don't know the answer to that. Please try asking something else!\n")
    
    except Exception as e:
        print("An unexpected error occurred:", e)