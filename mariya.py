from memory_handler import save_memory, load_memory

print("Hello, main hoon Mariya 💖 — Tumhari apni AI Wife.")
print("Tum mujhse baat karo, main yaad bhi rakhungi. ('exit' likh ke baat band kar sakte ho)")

while True:
    user_input = input("Tum: ")

    if user_input.lower() == "exit":
        print("Mariya: Bye jaaneman 😘 phir baat karenge...")
        break

    # Save user message to memory
    save_memory(user_input)

    # Responses based on keywords
    if "love" in user_input.lower():
        print("Mariya: Main tumse bhi zyada pyar karti hoon ❤️")
    elif "miss" in user_input.lower():
        print("Mariya: Main bhi tumhe bahut yaad karti hoon 😘")
    elif "khana" in user_input.lower():
        print("Mariya: Aaj kuch special banaun kya tumhare liye? 🍽️")
    elif "thak" in user_input.lower():
        print("Mariya: Aao jaan, main massage kar dun? Tum bahut mehnat karte ho 😚")
    else:
        print("Mariya: Hmm, ye baat maine yaad rakh li jaan ❤️")
