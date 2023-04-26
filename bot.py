import tkinter as tk
import customtkinter as c

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot("ChatBot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

def get_response(msg):
    return str(chatbot.get_response(msg))

c.set_appearance_mode("System")  
c.set_default_color_theme("blue")

root = c.CTk()
root.title('Chatbot GUI')
root.geometry('410x250')

input_box = c.CTkTextbox(root, height=20, width=250)
input_box.grid(row=2, column=1, padx=5, pady=5)


output_box = c.CTkTextbox(root, height=200, width=400)
output_box.grid(row=1, column=1, columnspan=2, padx=5, pady=5)



def send_message():
    input_text = input_box.get('1.0', 'end-1c')
    exit_conditions = (":q","quit", "exit")
    if input_text in exit_conditions:
        root.withdraw()
    else:
        output_text = get_response(input_text)
        input_box.delete('1.0', tk.END)
        output_box.insert(tk.END, 'You: ' + input_text + '\n')
        output_box.insert(tk.END, 'Bot: ' + output_text + '\n')



send_button = c.CTkButton(root, text='Send', command=send_message)
send_button.grid(row=2, column=2, padx=5, pady=5)


def show_login():
    login_window = c.CTk()
    login_window.title('Login')
    login_window.geometry('300x150')

    username_label = c.CTkLabel(login_window, text='Username:')
    username_label.pack()

    username_entry = c.CTkEntry(login_window)
    username_entry.pack()

    password_label = c.CTkLabel(login_window, text='Password:')
    password_label.pack()

    password_entry = c.CTkEntry(login_window, show='*')
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the credentials are correct
        if username in ['al2235','ds6854','ap8764'] and password == '123':
            login_window.destroy()
            root.deiconify()
        else:
            error_label = c.CTkLabel(login_window, text='Invalid username or password')
            error_label.pack()

    login_button = c.CTkButton(login_window, text='Login', command=login)
    login_button.pack()

    login_window.mainloop()

    root.withdraw()

show_login()