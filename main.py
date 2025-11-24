import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

me = 0
pc = 0

score_label = tk.Label(root, text=f"You: {me}  Computer: {pc}", font=('Arial', 14))
score_label.pack(pady=20)

result_label = tk.Label(root, text="Pick one!", font=('Arial', 12))
result_label.pack()


def play(choice):
    global me, pc
    options = ['r', 'p', 's']
    computer = random.choice(options)

    moves = {'r': 'Rock 🪨', 'p': 'Paper 📃', 's': 'Scissors ✂️'}

    if choice == computer:
        result = "Tie!"
    elif (choice == 'r' and computer == 's') or (choice == 'p' and computer == 'r') or (
            choice == 's' and computer == 'p'):
        result = "You win!"
        me += 1
    else:
        result = "Computer wins!"
        pc += 1

    result_label.config(text=f"{result}\nYou: {moves[choice]}  Computer: {moves[computer]}")
    score_label.config(text=f"You: {me}  Computer: {pc}")


button_frame = tk.Frame(root)
button_frame.pack(pady=30)

tk.Button(button_frame, text="🪨 Rock", command=lambda: play('r'), width=10).pack(pady=5)
tk.Button(button_frame, text="📃 Paper", command=lambda: play('p'), width=10).pack(pady=5)
tk.Button(button_frame, text="✂️ Scissors", command=lambda: play('s'), width=10).pack(pady=5)

root.mainloop()
