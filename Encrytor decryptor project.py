from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import tkinter.font as font

def encode(key, data):
    f = Fernet(key)
    encoded_data = f.encrypt(data)
    return encoded_data

def decode(key, data):
    f = Fernet(key)
    decoded_data = f.decrypt(data)
    return decoded_data

def encrypt_file(key, filename):
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = encode(key, data)
    with open(filename + ".enc", 'wb') as f:
        f.write(encrypted_data)
    res.delete('1.0', END)


def decrypt_file(key, filename):
    with open(filename, 'rb') as f:
        data = f.read()
    decrypted_data = decode(key, data)
    with open(filename[:-4], 'wb') as f:
        f.write(decrypted_data)
    res.delete('1.0', END)

def Result():
    if mode.get() == 1:  # Encrypt
        if file_entry.get():  # If a file is selected
            try:
                encrypt_file(key_var.get().encode(), file_entry.get())
                messagebox.showinfo("Encryption Successful", f"{file_entry.get()} has been encrypted successfully.")
            except Exception as e:
                messagebox.showerror("Encryption Error", f"An error occurred during encryption: {e}")
        elif msg.get("1.0", "end-1c"):  # If a message is provided
            message = msg.get("1.0", "end-1c").encode()  # Encode the message to bytes
            try:
                encoded_result = encode(key_var.get().encode(), message)
                res.delete('1.0', END)
                res.insert('1.0', encoded_result)
            except Exception as e:
                messagebox.showerror("Encryption Error", f"An error occurred during encryption: {e}")
        else:
            messagebox.showinfo('SICURO', 'Please enter a message or select a file to encrypt.')
    elif mode.get() == 2:  # Decrypt
        if file_entry.get():  # If a file is selected
            try:
                decrypt_file(key_var.get().encode(), file_entry.get())
                messagebox.showinfo("Decryption Successful", f"{file_entry.get()} has been decrypted successfully.")
            except Exception as e:
                messagebox.showerror("Decryption Error", f"Incorrect key. Please check the key and try again.")
        elif msg.get("1.0", "end-1c")!="":  # If a message is provided
            message = msg.get("1.0", "end-1c")
            try:
                decoded_result = decode(key_var.get().encode(), message)  # Encode the message to bytes
                res.delete('1.0', END)
                res.insert('1.0', decoded_result)
            except Exception as e:
                messagebox.showerror("Decryption Error", f"Incorrect key. Please check the key and try again.")
        else:
            messagebox.showinfo('SICURO', 'Please enter a message or select a file to decrypt.')
    else:
        messagebox.showinfo('SICURO', 'Please choose either encryption or decryption.')

def browse_file():
    filename = filedialog.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, filename)

def Reset():
    global key
    key = Fernet.generate_key()
    key_var.set(key.decode())  # Update the key in the StringVar
    generated_key_entry.delete(0, END)
    generated_key_entry.insert(0, key.decode())
    msg.delete("1.0", "end")
    res.delete("1.0", "end")
    mode.set(0)
    file_entry.delete(0, END)  # Deselect the file

wn = Tk()
wn.geometry("649x550")
wn.resizable(False, False)
wn.configure(bg='#b1d4eb')
wn.title("SICURO")

key_var = StringVar()
key = Fernet.generate_key()
key_var.set(key.decode())
mode = IntVar()

headingFrame1 = Frame(wn,bg="gray91",bd=5)
headingFrame1.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

headingLabel = Label(headingFrame1, text=" SICURO \n An Encryption and Decryption Tool", fg='grey19', font=('Courier',15,'bold'))
headingLabel.pack()

label1 = Label(wn, text='Enter the Message', font=('Courier',10))
label1.grid(row=1, column=0, padx=10, pady=10, sticky='w')

msg = Text(wn,height=3, width=50, font=('calibre',10,'normal'))
msg.grid(row=1,rowspan=2, column=1, columnspan=2, padx=10, pady=10)

label2 = Label(wn, text='Generated Key:', font=('Courier',10))
label2.grid(row=4, column=0, padx=10, pady=10, sticky='w')

generated_key_entry = Entry(wn, textvariable=key_var, font=('Courier', 10), bg='white', relief='solid', width=44)
generated_key_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='w')
generated_key_entry.insert(0, key.decode())
generated_key_entry.config(state='normal')

label3 = Label(wn, text='Check one of encrypt or decrypt', font=('Courier',10))
label3.grid(row=5, column=0, padx=10, pady=10, sticky='w')

Radiobutton(wn, text='Encrypt', variable=mode, value=1).grid(row=6, column=1, padx=10, pady=10, sticky='w')
Radiobutton(wn, text='Decrypt', variable=mode, value=2).grid(row=6, column=2, padx=10, pady=10, sticky='w')

label4 = Label(wn, text='Result', font=('Courier',10))
label4.grid(row=7, column=0, padx=10, pady=10, sticky='w')

res = Text(wn,height=3, width=50, font=('calibre',10,'normal'))
res.grid(row=7,rowspan=2, column=1, columnspan=2, padx=10, pady=10)

file_entry_label = Label(wn, text='Select File:', font=('Courier',10))
file_entry_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

file_entry = Entry(wn, font=('Courier', 10), bg='white', relief='solid', width=44)
file_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky='w')

browse_btn = Button(wn, text='Browse', bg='lavender blush2', fg='black', width=6, height=1, command=browse_file)
browse_btn['font'] = font.Font(size=9)
browse_btn.place(x=229,y=222)

ShowBtn = Button(wn,text="Show Message",bg='#6bb0ee', fg='black',width=15,height=1,command=Result)
ShowBtn['font'] = font.Font( size=12)
ShowBtn.place(x=247,y=494)

ResetBtn = Button(wn, text='Reset', bg='#6beeaa', fg='black', width=15, height=1, command=Reset)
ResetBtn['font'] = font.Font(size=12)
ResetBtn.place(x=80, y=494)

QuitBtn = Button(wn, text='Exit', bg='#ee6b6e', fg='black', width=15, height=1, command=wn.destroy)
QuitBtn['font'] = font.Font(size=12)
QuitBtn.place(x=416, y=494)

wn.mainloop()
