#* imports
import tkinter as tk

#* Function to center our window
def center_window(root,width,height):
    # get our screen with and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate the middle x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    # set the geometry of our window.
    # (width x height + x coord + y coord)
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

#* Setup the tkinter window
def application():
    window = tk.Tk()
    window.title("Friendly Chat")
    window.geometry("700x900")
    window.configure(bg="#181825")

    #* Make the window a fixed size
    window.resizable(False, False)

    #* Center the window
    center_window(window,700,900)

    #* Create an input field for typing a message
    input_box = tk.Entry(
        window,
        width=30,
        bg="#1e1e2e",
        fg="#ced0d6",
        borderwidth=0,
        font=("Arial", 24))

    input_box.place(rely=0.95,relx=0.4,anchor="center")

    #* Create a button to send the message
    send_button = tk.Button(
        window,
        text="Send :)",
        width=10,
        bg="#4f4165",
        fg="#ced0d6",
        borderwidth=0,
        font=("Arial", 16)
    )

    send_button.place(rely=0.95,relx=0.9,anchor="center")

    #* Keep the application running
    window.mainloop()


application()