import tkinter as tk

encrypted_messages = []  # List to store encrypted messages

def caesar_cipher(text, shift, encrypt=True):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine the case (uppercase or lowercase)
            is_upper = char.isupper()
            char = char.lower()

            # Apply the Caesar cipher shift
            if encrypt:
                char = chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
            else:
                char = chr((ord(char) - shift - ord("a")) % 26 + ord("a"))

            # Convert back to uppercase if the original character was uppercase
            if is_upper:
                char = char.upper()

        result += char

    return result

def encrypt_text():
    global original_message  # Use the global variable
    message = entry_message.get()
    shift = int(entry_shift.get())
    encrypted_message = caesar_cipher(message, shift, encrypt=True)
    encrypted_messages.append(encrypted_message)  # Append to the list
    label_result.config(text=f"Encrypted Message: {encrypted_message}")

def decrypt_text():
    shift = int(entry_shift.get())
    if encrypted_messages:
        encrypted_message = encrypted_messages[-1]  # Use the last encrypted message
        decrypted_message = caesar_cipher(encrypted_message, shift, encrypt=False)
        label_result.config(text=f"Decrypted Message: {decrypted_message}")
    else:
        label_result.config(text="No encrypted messages available")

# GUI setup
app = tk.Tk()
app.title("Caesar Cipher Encryption GUI")

# Widgets
label_message = tk.Label(app, text="Enter Message:")
entry_message = tk.Entry(app)

label_shift = tk.Label(app, text="Enter Shift Value:")
entry_shift = tk.Entry(app)

btn_encrypt = tk.Button(app, text="Encrypt", command=encrypt_text)
btn_decrypt = tk.Button(app, text="Decrypt", command=decrypt_text)

label_result = tk.Label(app, text="Result will be displayed here.")

# Layout
label_message.grid(row=0, column=0, padx=10, pady=10)
entry_message.grid(row=0, column=1, padx=10, pady=10)

label_shift.grid(row=1, column=0, padx=10, pady=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

btn_encrypt.grid(row=2, column=0, pady=10)
btn_decrypt.grid(row=2, column=1, pady=10)

label_result.grid(row=3, columnspan=2, pady=10)

# Run the GUI
app.mainloop()




