# fortune.py

def main():
    name = "Jainendra Tripathy"
    admission_no = "21je0417"

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

    if mood == "happy":
        print(f"✨ Your fortune: Great things await you, {name}! Keep smiling. ✨")
    elif mood == "sad":
        print("✨ Your fortune: Tough times don't last, but tough people do. ✨")
    elif mood == "neutral":
        print("✨ Your fortune: Balance is key. Enjoy the calm. ✨")
    else:
        print("Sorry, I don't have a fortune for that mood... yet!")

if __name__ == "__main__":
    main()
