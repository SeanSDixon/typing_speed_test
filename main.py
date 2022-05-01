import tkinter as tk
from tkinter import Canvas, PhotoImage
from PIL import ImageTk, Image
from data import *


list_of_word = paragraph.split(" ")
correct_words = []
incorrect_words = []


def stop():
    exit()


def start():
    # Listening to Key Function
    def onkeypress(event):
        word = test_entry.get()
        print(word)
        test_entry.delete(0, tk.END)
        word = word.lstrip()

        if word in list_of_word:
            correct_words.append(word)
        elif word not in list_of_word:
            incorrect_words.append(word)

    def finished():
        test_text.destroy()
        test_entry.destroy()

        score = len(correct_words)

        finishing_label = tk.Label(text="TEST COMPLETE", font=("Helvetica BOLD", 25))
        finishing_label.pack()

        wpm_label1 = tk.Label(text="\nYou typed", font=("Helvetica", 20))
        wpm_label2 = tk.Label(text=f"\n{score}", font=("Helvetica BOLD", 30))
        wpm_label3 = tk.Label(text="\nWords Per Minute!", font=("Helvetica", 20))
        wpm_label1.pack()
        wpm_label2.pack()
        wpm_label3.pack()

        incor_label1 = tk.Label(text="\nUnfortunately, you spelt these words wrong:\n", font=("Helvetica", 14))
        incor_label2 = tk.Label(text=f"{', '.join(incorrect_words)}\n", font=("Helvetica", 17))
        incor_label3 = tk.Label(text="So they did not count :(", font=("Helvetica", 14))
        incor_label1.pack()
        incor_label2.pack()
        incor_label3.pack()

    # Clearing Window
    canvas.destroy()
    desc_label.destroy()
    heading_label.destroy()
    start_button.destroy()
    exit_button.destroy()

    # Setting Up GUI
    window.after(60000, finished)

    test_text = tk.Label(text=paragraph, font=("Helvetica", 15), )
    test_text.pack()

    test_entry = tk.Entry(width=40, font=("Helvetica", 15),)
    test_entry.pack(pady=60)
    test_entry.focus()
    test_entry.insert(0, " ")
    test_entry.bind("<space>", onkeypress)



window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(height=600, width=600)
window.config(pady=30, padx=30)

# Logo
canvas = tk.Canvas(height=270, width=451, bg="black")
canvas.grid(row=1, column=1)
logo = ImageTk.PhotoImage(Image.open("typing_logo.png"))
canvas.create_image(227, 137, image=logo)

# Labels
heading_label = tk.Label(text="The Typing Speed Test", font=("Helvetica bold", 30), pady=15)
heading_label.grid(row=0, column=1)

desc_label = tk.Label(text="\nWelcome!!!\nClick Start when you are ready.\nOnce you click start, a paragraph will appear "
                           "as well as an entry bar.\nYour goal is to type as many of the words as you can in 60 Seconds.\n"
                           , font=("Helvetica", 13))
desc_label.grid(row=2, column=1)

# Buttons
start_button = tk.Button(command=start, text="Start", font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
start_button.place(x=50, y=485)

exit_button = tk.Button(command=stop, text="Exit", font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
exit_button.place(x=310, y=485)

window.mainloop()