import socket
import threading
import tkinter as tk

HOST_TARGET = '127.0.0.1'
PORT_TARGET = 1234


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')


def username_select():
    global window
    window = tk.Tk()
    window.title("Friendly Chat")
    window.geometry("400x400")
    window.configure(bg="#101013")
    window.resizable(False, False)
    center_window(window, 700, 900)

    greeting_label = tk.Label(
        window,
        text="Welcome to Friendly Chat!\nPlease enter your username",
        bg="#101013",
        fg="#ffffff",
        font=("Arial", 24)
    )
    greeting_label.place(rely=0.5, relx=0.5, anchor="center")

    username_input_box = tk.Entry(
        window,
        width=30,
        bg="#222329",
        fg="#ffffff",
        borderwidth=0,
        font=("Arial", 24))
    username_input_box.place(rely=0.6, relx=0.5, anchor="center")

    username_submit_button = tk.Button(
        window,
        text="Start Chatting!",
        width=15,
        bg="#222329",
        fg="#ffffff",
        borderwidth=0,
        font=("Arial", 16),
        command=lambda: main(str(username_input_box.get()))
    )
    username_submit_button.place(rely=0.7, relx=0.5, anchor="center")

    window.mainloop()


def main(username):
    global window, message_result_box, message_input_box, client

    window.destroy()

    def update_message_box():
        message_history_list = []
        with open('messagehistory.txt', 'r') as f:
            for line in f:
                message_history_list.append(line)
        message_result_box.delete(1.0, "end")
        for message in message_history_list:
            message_result_box.insert("end", message)

    def receive_messages(client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    print(f"Received message: {message}")  # Debugging line
                    with open('messagehistory.txt', 'a') as f:
                        f.write(f"{message}\n")
                    window.after(0, update_message_box)  # Ensure the update happens in the main thread
                else:
                    print("Connection closed by the server.")
                    break
            except Exception as e:
                print(f"Exception occurred: {e}")  # Debugging line
                break

    def send_messages(client, message):
        if message.strip():  # Only send non-empty messages
            client.send(message.encode('utf-8'))
            message_input_box.delete(0, 'end')  # Clear input box after sending
            with open('messagehistory.txt', 'a') as f:
                f.write(f"Me: {message}\n")
            window.after(0, update_message_box)  # Ensure the update happens in the main thread

    window = tk.Tk()
    window.title("Friendly Chat")
    window.geometry("700x900")
    window.configure(bg="#101013")
    window.resizable(False, False)

    center_window(window, 700, 900)

    message_result_box = tk.Text(
        window,
        width=30,
        height=100,
        bg="#101013",
        fg="#ffffff",
        borderwidth=0,
        font=("Arial", 16),
        wrap="word"
    )
    message_result_box.pack(expand=True, fill="both", side="left")
    update_message_box()

    message_input_box = tk.Entry(
        window,
        width=30,
        bg="#222329",
        fg="#ffffff",
        borderwidth=0,
        font=("Arial", 24))
    message_input_box.place(rely=0.95, relx=0.4, anchor="center")

    send_button = tk.Button(
        window,
        text="Send :)",
        width=10,
        bg="#222329",
        fg="#ffffff",
        borderwidth=0,
        font=("Arial", 16),
        command=lambda: send_messages(client, message_input_box.get())
    )
    send_button.place(rely=0.95, relx=0.9, anchor="center")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"your username is: {username}")

    try:
        client.connect((HOST_TARGET, PORT_TARGET))

        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.start()

        client.send(username.encode('utf-8'))

    except Exception as e:
        print(f"Unable to connect to {HOST_TARGET}:{PORT_TARGET}. Error: {str(e)}")


if __name__ == "__main__":
    username_select()
