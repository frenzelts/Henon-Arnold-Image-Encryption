import tkinter as tk
from tkinter import filedialog as fd
import os
import encrypt as e
import decrypt as d
import threading as thread

class MainApplication:
    def __init__(self, app, flag):
        self.flag = flag
        self.app = app
        if self.flag == 'e':
            self.choose_label_text = "Select images to be encrypted"
            self.encrypt_text = "Encrypt"
        else:
            self.choose_label_text = "Select images to be decrypted"
            self.encrypt_text = "Decrypt"
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(3, weight=1)
        self.app.title("Image "+self.encrypt_text+"ion - SKRIPSI FRENZEL")
        self.app.geometry('%sx%s' % (int(self.app.winfo_screenwidth()/4), int(app.winfo_screenheight()/3)))
        self.app.resizable(width=False, height=False)
        self.listFilenames = []
        #Choose
        self.choose_label = tk.Label(self.app, text=self.choose_label_text, font=('Helvetica', 10))
        self.choose_label.grid(row=0, column=0, padx=(8,0), pady=(10,5), sticky='wn')
        self.choose_entry = tk.Text(self.app, width=0, height=0)
        self.choose_entry.grid(row=1, column=0, sticky='wens', padx=(10,5), rowspan=3)
        self.choose_entry.config(state=tk.DISABLED)
        self.add_button = tk.Button(self.app, text ="Add", command=self.chooseImg)
        self.add_button.grid(row=1, column=1, sticky='wen', padx=(5,10))
        self.clear_button = tk.Button(self.app, text ="Clear", command=lambda:[self.choose_entry.config(state=tk.NORMAL), self.choose_entry.delete(1.0, tk.END), self.choose_entry.config(state=tk.DISABLED), self.listFilenames.clear()])
        self.clear_button.grid(row=2, column=1, sticky='wes', padx=(5,10), pady=(5,0))

        #Output
        self.output_label = tk.Label(self.app, text="Choose output destination", font=('Helvetica', 10))
        self.output_label.grid(row=4, column=0, padx=(8,0), pady=(10,5), sticky='wn')
        self.output_entry = tk.Entry(self.app)
        self.output_entry.grid(row=5, column=0, sticky='wen', padx=(10,5))
        self.output_entry.config(state=tk.DISABLED)
        self.output_button = tk.Button(self.app, text="Select folder", command=self.chooseDestination)
        self.output_button.grid(row=5, column=1, sticky='wen', padx=(5,10))

        #Key
        self.key_label = tk.Label(self.app, text="Input shared key: ", font=('Helvetica', 10))
        self.key_label.grid(row=6, column=0, padx=(8,0), pady=(5,5), sticky='wn')
        self.key_entry = tk.Entry(app, width=0)
        self.key_entry.grid(row=7, column=0, sticky='wen', padx=10, columnspan=2)

        #Progress
        self.progressText = tk.StringVar()
        self.progress_label = tk.Label(self.app, textvariable=self.progressText, font=('Helvetica', 9))
        self.progress_label.grid(row=8, column=0, sticky='swn', padx=(7,0), pady=(20,10))
        print(thread.active_count())

        #Encrypt
        self.encrypt_button = tk.Button(self.app, text=self.encrypt_text, command= lambda: thread._start_new_thread(self.beginEncryption, (self.listFilenames,)))
        self.encrypt_button.grid(row=8, column=1, sticky='senw', padx=(0,10), pady=(20,10))

    def chooseImg(self):
        filename = fd.askopenfilenames(title='Choose images')
        for i in filename:
            self.listFilenames.append(i)
            self.choose_entry.config(state=tk.NORMAL)
            self.choose_entry.insert(tk.INSERT, i+'\n')
            self.choose_entry.config(state=tk.DISABLED)

    def chooseDestination(self):
        self.output_entry.delete(0, tk.END)
        path = fd.askdirectory(title='Select output destination')
        self.output_entry.config(state=tk.NORMAL)
        self.output_entry.insert(tk.INSERT, path)
        self.output_entry.config(state=tk.DISABLED)

    def beginEncryption(self, listFilenames):
        self.changeButtonState(tk.DISABLED)
        self.changeTextBoxState(tk.DISABLED)
        for i in listFilenames:
            self.showBar(i, listFilenames.index(i), len(listFilenames))
            if self.flag == 'e':
                e.encrypt(i, self.output_entry.get())
            else:
                d.decrypt(i, self.output_entry.get())
        self.progressText.set(self.encrypt_text+"ion finished. ("+str(len(listFilenames))+"/"+str(len(listFilenames))+")")
        self.clearAllText()
        self.changeButtonState(tk.NORMAL)

    def showBar(self, filename, index, length):
        self.progressText.set(self.encrypt_text+"ing "+os.path.basename(filename)+" ("+str(index)+"/"+str(length)+")")
        self.app.update_idletasks()    

    def changeButtonState(self, s):
        self.add_button.config(state=s)
        self.clear_button.config(state=s)
        self.output_button.config(state=s)
        self.encrypt_button.config(state=s)

    def changeTextBoxState(self, s):
        self.output_entry.config(state=s)
        self.choose_entry.config(state=s)
        self.key_entry.config(state=s)

    def clearAllText(self):
        self.changeTextBoxState(tk.NORMAL)
        self.listFilenames.clear()
        self.choose_entry.delete(1.0, tk.END)
        self.output_entry.delete(0, tk.END)
        self.key_entry.delete(0,tk.END)
        self.changeTextBoxState(tk.DISABLED)
        self.key_entry.config(state=tk.NORMAL)

class IntroApplication:
    def __init__(self, app):
        self.app = app
        self.btn_encrypt = tk.Button(self.app, text="Encrypt", command=lambda:self.start_main('e'))
        self.btn_encrypt.pack()
        self.btn_decrypt = tk.Button(self.app, text="Decrypt", command=lambda:self.start_main('d'))
        self.btn_decrypt.pack()
    
    def start_main(self, flag):
        self.app.destroy()
        new_app = tk.Tk()
        main_app = MainApplication(new_app, flag)
        new_app.mainloop()

app = tk.Tk()
intro_app = IntroApplication(app)
app.mainloop()