from tkinter import *
import rc4

def encrypt():
    text = entry_text.get().encode()
    key = entry_key.get().encode()
    cipher_text = rc4.crypt(key, text)
    result_entry.delete("1.0", END)
    result_entry.insert("1.0", cipher_text)

def decrypt():
    try:
        cipher_text = bytes.fromhex(result_entry.get("1.0", END).strip())
        key = entry_key.get().encode()
        decrypted_hex = rc4.crypt(key, cipher_text)
        decrypted_bytes = bytes.fromhex(decrypted_hex)
        plain_text = decrypted_bytes.decode(errors="ignore")
        entry_plain.delete("1.0", END)
        entry_plain.insert("1.0", plain_text)
    except ValueError:
        result_entry.delete("1.0", END)
        result_entry.insert("1.0", "Помилка у форматі шифротексту")

# Інтерфейс
root = Tk()
root.title("Шифратор для RC4")
root.geometry("700x500")
root.configure(bg="#F0F0F0")

Label(root, text="Введіть текст від 1 до 49:", font=("Arial", 12)).pack(pady=5)
entry_text = Entry(root, font=("Arial", 12), width=50)
entry_text.pack(pady=5)

Label(root, text="Ключ максимум 49 символів:", font=("Arial", 12)).pack(pady=5)
entry_key = Entry(root, font=("Arial", 12), width=50)
entry_key.pack(pady=5)

Label(root, text="Розшифрований текст:", font=("Arial", 12)).pack(pady=5)
entry_plain = Text(root, height=5, width=50, font=("Arial", 12))
entry_plain.pack(pady=5)

Label(root, text="Зашифрований:", font=("Arial", 12)).pack(pady=5)
result_entry = Text(root, height=5, width=50, font=("Arial", 12))
result_entry.pack(pady=5)

frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

Button(frame_buttons, text="Зашифрувати", font=("Arial", 12), command=encrypt).grid(row=0, column=0, padx=10)
Button(frame_buttons, text="Розшифрувати", font=("Arial", 12), command=decrypt).grid(row=0, column=1, padx=10)
Button(root, text="Вихід", font=("Arial", 12), width=15, command=root.quit).pack(pady=10)

root.mainloop()
