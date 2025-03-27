import random
import json
import os

# 🎲 Function to jumble a word
def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)

# 📂 File paths
word_file = r"C:\Users\292593\Desktop\master\python training\python_code_submit\Python-training\word.txt"
hint_file = r"C:\Users\292593\Desktop\master\python training\python_code_submit\Python-training\hints.txt"

# ✅ Check if files exist before proceeding
if not os.path.exists(word_file) or not os.path.exists(hint_file):
    print("❌ Error: One or more required files are missing!")
    exit()

# 📖 Read words from word.txt
with open(word_file, 'r') as f:
    words = f.read().strip().split(',')

# 📝 Read hints from hints.txt (JSON file)
with open(hint_file, 'r') as f:
    hints = json.load(f)

# 🔀 Shuffle words randomly
random.shuffle(words)

# 🏆 Game variables
score = 0
first_attempts = 0
second_attempts = 0
total_rounds = len(words)

print("\n🎮 Welcome to the **Word Jumble Game!** 🎮")
print("🔹 **Try to guess the correct word.** You have **two attempts**. Type '❌ exit' to quit.\n")

# 🔥 Start the game loop
for word in words:
    jumbled_word = jumble(word.strip())

    print(f"\n🔀 **Jumbled Word:** 🌀 {jumbled_word}")

    # 🏅 First attempt
    user_guess = input("💡 Can you guess? 🎤 ").strip().lower()

    if user_guess == "exit":
        print("👋 Exiting the game... See you next time! 🚀")
        break

    if user_guess == word.lower():
        print("✅ **Correct! (+2 points) 🎉🎊**\n")
        score += 2
        first_attempts += 1
    else:
        # First attempt was **wrong**
        print("❌ **Incorrect! Try again...**")

        # 🛎️ Provide a hint
        if word.strip() in hints:
            print(f"💡 **CLUE:** {hints[word.strip()]}")
        else:
            print("💡 **CLUE:** No hint available.")

        # 🎭 Second attempt
        user_guess = input("🤔 Take a second guess? 🎤 ").strip().lower()

        if user_guess == "exit":
            print("👋 Exiting the game... See you next time! 🚀")
            break

        if user_guess == word.lower():
            print("✅ **Correct! (+1 point) 🎉**\n")
            score += 1
            second_attempts += 1
        else:
            print(f"❌ **Wrong! The correct word was:** {word.strip()} 🚨\n")

# 📊 **Grading System**
max_score = total_rounds * 2  # Maximum possible score (2 points per word)
percentage = (score / max_score) * 100

if percentage >= 80:
    grade = "🏅 A+ 🎖️"
elif percentage >= 60:
    grade = "🥇 A"
elif percentage >= 40:
    grade = "🥈 B+"
elif percentage >= 20:
    grade = "🥉 B"
else:
    grade = "❌ C"

# 🎯 **Final Results**
print("\n🎯 **Game Over!** 🎯")
print(f"🏆 **Total Points:** {score}/{max_score}")
print(f"🥇 **First Attempts:** {first_attempts}")
print(f"🥈 **Second Attempts:** {second_attempts}")
print(f"🎓 **Overall Grade:** {grade}\n")
print("🎉 **Thanks for playing! See you again!** 🚀")
