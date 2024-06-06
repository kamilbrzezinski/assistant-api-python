import tkinter as tk
from tkinter import scrolledtext
from assistant import Assistant


class ChatWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Asystent")

        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(padx=10, pady=10)

        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, state='disabled', width=50, height=20)
        self.chat_display.pack()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(self.input_frame, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.send_button = tk.Button(self.input_frame, text="Zapytaj", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        self.root.bind('<Return>', self.send_message)

        self.assistant = Assistant()

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.display_message("Ty: " + message)
            self.message_entry.delete(0, tk.END)

            response = self.assistant.send_message(message)
            self.display_message("Asystent: " + response)

    def display_message(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.yview(tk.END)
        self.chat_display.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatWindow(root)
    root.mainloop()
