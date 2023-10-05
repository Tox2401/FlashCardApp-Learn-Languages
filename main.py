import pathlib
import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
DATA = pandas.read_csv(pathlib.Path(__file__).parent/"data/french_words.csv")
WORDS = {row["French"]: row["English"] for (index, row) in DATA.iterrows()}
RANDOM_WORD = random.choice(list(WORDS.items()))
CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0
TIMER = 0


def update():
    global RANDOM_WORD

    canvas.itemconfig(cardImg, image=cardBack)
    canvas.itemconfig(languageTxt, text="English")
    canvas.itemconfig(wordTxt, text=RANDOM_WORD[1])
    RANDOM_WORD = random.choice(list(WORDS.items()))


def countdown(count):
    global TIMER

    TIMER = count
    counterLabel.config(text=TIMER)

    if count > 0:
        canvas.after(1000, countdown, count - 1)
    else:
        counterLabel.config(text="")
        update()


def start():
    global RANDOM_WORD

    counterLabel.grid(column=1, row=1)
    canvas.itemconfig(languageTxt, text="French")
    canvas.itemconfig(wordTxt, text=RANDOM_WORD[0])
    startBtn.grid_forget()
    countdown(3)


def correct():
    global TIMER
    global RANDOM_WORD
    global CORRECT_ANSWERS

    if TIMER == 0:
        CORRECT_ANSWERS += 1
        canvas.itemconfig(correctTxt, text=f"Correct answers: {CORRECT_ANSWERS}")
        canvas.itemconfig(cardImg, image=cardFront)
        canvas.itemconfig(languageTxt, text="French")
        canvas.itemconfig(wordTxt, text=RANDOM_WORD[0])
        countdown(3)
    else:
        pass


def wrong():
    global TIMER
    global RANDOM_WORD
    global WRONG_ANSWERS

    if TIMER == 0:
        WRONG_ANSWERS += 1
        canvas.itemconfig(wrongTxt, text=f"Wrong answers: {WRONG_ANSWERS}")
        canvas.itemconfig(cardImg, image=cardFront)
        canvas.itemconfig(languageTxt, text="French")
        canvas.itemconfig(wordTxt, text=RANDOM_WORD[0])
        countdown(3)
    else:
        pass


window = Tk()
window.title("Flash Card App")
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)

cardFront = PhotoImage(file=pathlib.Path(__file__).parent/"images/card_front.png")
cardBack = PhotoImage(file=pathlib.Path(__file__).parent/"images/card_back.png")
startImg = PhotoImage(file=pathlib.Path(__file__).parent/"images/start.png")
rightImg = PhotoImage(file=pathlib.Path(__file__).parent/"images/right.png")
wrongImg = PhotoImage(file=pathlib.Path(__file__).parent/"images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
cardImg = canvas.create_image(400, 263, image=cardFront)
correctTxt = canvas.create_text((600, 25), text=f"Correct answers: {CORRECT_ANSWERS}", font=("Ariel", 16, "bold"))
wrongTxt = canvas.create_text((200, 25), text=f"Wrong answers: {WRONG_ANSWERS}", font=("Ariel", 16, "bold"))
languageTxt = canvas.create_text((400, 150), text="Press", font=("Ariel", 40, "italic"))
wordTxt = canvas.create_text((400, 260), text=">>Start<<", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3, pady=20)

counterLabel = Label()
counterLabel.config(font=("Ariel", 40, "bold"), bg=BACKGROUND_COLOR)

startBtn = Button(image=startImg, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=start)
startBtn.grid(column=1, row=1)

rightBtn = Button(image=rightImg, highlightthickness=0, bd=0, command=correct)
rightBtn.grid(column=2, row=1)

wrongBtn = Button(image=wrongImg, highlightthickness=0, bd=0, command=wrong)
wrongBtn.grid(column=0, row=1)

mainloop()
