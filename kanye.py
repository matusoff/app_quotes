from tkinter import *
import requests


def get_quote():
    quote = requests.get(url="https://api.kanye.rest")
    quote.raise_for_status()
    quotes = quote.json()
    canvas.itemconfig(quote_text, text=quotes["quote"])
    

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"PROJECTS\100days_of_code\API_module\quotes\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "normal"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"PROJECTS\100days_of_code\API_module\quotes\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()