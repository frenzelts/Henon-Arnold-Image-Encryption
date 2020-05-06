import tkinter as tk
from tkinter import filedialog as fd
import os
import encrypt

def chooseImg(event=None):
    filename = fd.askopenfilenames(title='Choose images')
    for i in filename:
        listFilenames.append(i)
        choose_entry.insert(tk.INSERT, i+'\n')

def chooseDestination(event=None):
    output_entry.delete(0, tk.END)
    path = fd.askdirectory(title='Select output destination')
    output_entry.insert(tk.INSERT, path)

def beginEncryption(event=None):
    for i in listFilenames:
        showBar(i, listFilenames.index(i), len(listFilenames), progressText)
        encrypt.encrypt(i, output_entry.get())
    progressText.set("Encryption finished. ("+str(len(listFilenames))+"/"+str(len(listFilenames))+")")
    listFilenames.clear()
    choose_entry.delete(1.0, tk.END)
    output_entry.delete(0, tk.END)

def showBar(filename, index, length, progressText):
    progressText.set("Encrypting "+os.path.basename(filename)+" ("+str(index)+"/"+str(length)+")")
    app.update_idletasks()    

app = tk.Tk()
listFilenames = []
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(3, weight=1)

#Choose
choose_label = tk.Label(app, text="Choose images to be encrypted", font=('Helvetica', 10))
choose_label.grid(row=0, column=0, padx=(8,0), pady=(10,5), sticky='wn')
choose_entry = tk.Text(app, width=0, height=0)
choose_entry.grid(row=1, column=0, sticky='wens', padx=(10,5), rowspan=3)
add_button = tk.Button(app, text ="Add", command=chooseImg)
add_button.grid(row=1, column=1, sticky='wen', padx=(5,10))
clear_button = tk.Button(app, text ="Clear", command=chooseImg)
clear_button.grid(row=2, column=1, sticky='wes', padx=(5,10), pady=(5,0))

#Output
output_label = tk.Label(app, text="Choose output destination", font=('Helvetica', 10))
output_label.grid(row=4, column=0, padx=(8,0), pady=(10,5), sticky='wn')
output_entry = tk.Entry(app)
output_entry.grid(row=5, column=0, sticky='wen', padx=(10,5))
output_button = tk.Button(app, text="Select folder", command=chooseDestination)
output_button.grid(row=5, column=1, sticky='wen', padx=(5,10))

#Key
key_label = tk.Label(app, text="Input shared key: ", font=('Helvetica', 10))
key_label.grid(row=6, column=0, padx=(8,0), pady=(5,5), sticky='wn')
key_entry = tk.Text(app, width=0, height=0)
key_entry.grid(row=7, column=0, sticky='wen', padx=10, columnspan=2)

#Progress
progressText = tk.StringVar()
progress_label = tk.Label(app, textvariable=progressText, font=('Helvetica', 9))
progress_label.grid(row=8, column=0, sticky='swn', padx=(7,0), pady=(20,10))

#Encrypt
encrypt_button = tk.Button(app, text ="Encrypt", command=beginEncryption)
encrypt_button.grid(row=8, column=1, sticky='senw', padx=(0,10), pady=(20,10))

app.title("Image Encryption")
app.geometry('%sx%s' % (int(app.winfo_screenwidth()/4), int(app.winfo_screenheight()/3)))
app.resizable(width=False, height=False)

app.mainloop()