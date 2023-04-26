import tkinter as tk

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('MyBot')
trainer = ListTrainer(chatbot)
trainer.train('chat.txt')

def get_response(msg):
    return str(chatbot.get_response(msg))

root = tk.Tk()
root.title('Chatbot GUI')
root.geometry('400x500')



output_box = tk.Text(root, height=20, width=50)
output_box.pack()

input_box = tk.Text(root, height=2, width=50)
input_box.pack()


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


send_button = tk.Button(root, text='Send', command=send_message)
send_button.pack()


def show_login():
    login_window = tk.Toplevel()
    login_window.title('Login')
    login_window.geometry('300x150')

    username_label = tk.Label(login_window, text='Username:')
    username_label.pack()

    username_entry = tk.Entry(login_window)
    username_entry.pack()

    password_label = tk.Label(login_window, text='Password:')
    password_label.pack()

    password_entry = tk.Entry(login_window, show='*')
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Check if the credentials are correct
        if username == 'admin' and password == 'password':
            login_window.destroy()
            root.deiconify()
        else:
            error_label = tk.Label(login_window, text='Invalid username or password')
            error_label.pack()

    login_button = tk.Button(login_window, text='Login', command=login)
    login_button.pack()

    root.withdraw()
root.mainloop()