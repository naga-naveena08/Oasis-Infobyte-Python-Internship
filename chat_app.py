import datetime

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def chat_application():
    print("=== Simple Chat Application ===")
    print("Two users can chat here. Type 'bye' to end the conversation.\n")
    
    chat_history = []
    message_count = 0
    
    while True:
        msg1 = input(f"[{get_time()}] User1: ")
        
        if msg1.lower() == 'bye':
            print(f"[{get_time()}] User1 has left the chat.")
            chat_history.append(f"[{get_time()}] User1: bye")
            break
        
        chat_history.append(f"[{get_time()}] User1: {msg1}")
        message_count += 1
        
        msg2 = input(f"[{get_time()}] User2: ")
        
        if msg2.lower() == 'bye':
            print(f"[{get_time()}] User2 has left the chat.")
            chat_history.append(f"[{get_time()}] User2: bye")
            break
        
        chat_history.append(f"[{get_time()}] User2: {msg2}")
        message_count += 1
    
    print(f"\nChat ended. Total messages exchanged: {message_count}")
    
    show_history = input("Do you want to see the full chat history? (y/n): ")
    if show_history.lower() == 'y':
        print("\n=== Chat History ===")
        for line in chat_history:
            print(line)
    
    print("\nThank you for using the Chat Application!")

chat_application()
