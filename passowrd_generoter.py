import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x600")

        self.password_var = tk.StringVar()
        self.password_var.set("")

        # Label for displaying generated password
        self.password_label = tk.Label(root, textvariable=self.password_var,font=("Arial", 14))
        self.password_label.pack(pady=10)

        # Entry field for specifying password length
        self.length_label = tk.Label(root, text=" Enter Password Length:",bg='lightblue',font=15)
        self.length_label.pack(pady=6)
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=6)

        # Button for generating password
        self.generate_button = tk.Button(root, text="Generate Password",bg='orange',font=15, command=self.generate_password)
        self.generate_button.pack(pady=5)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())

            if password_length <= 0:
                raise ValueError("Password length must be a positive integer")

            # Define character sets for password generation
            characters = string.ascii_letters + string.digits + string.punctuation

            # Generate random password
            password = ''.join(random.choice(characters) for _ in range(password_length))

            # Update password label with the generated password
            self.password_var.set(password)
        except ValueError as e:
            self.password_var.set("Error: " + str(e))
        except Exception as e:
            self.password_var.set("Error")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
