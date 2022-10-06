import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd
import time
import threading


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('icon.ico')
        self.resizable(width=False, height=False)
        self.title('READ-SCAN-WORD')
        self.geometry('400x300')
        self.openfilename = None
        self.create_widgets()

    def create_widgets(self):
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)
        self.file_menu = Menu(self.menu_bar, tearoff=0,)
        self.file_menu.add_command(label="เปิดไฟล์", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="ปิดโปรแกรม", command=self.quit)
        self.menu_bar.add_cascade(label="ไฟล์", menu=self.file_menu)
        Label(self, text='ชื่อไฟล์ :').grid(column=0, row=0, padx=5, pady=5)
        self.filename = StringVar()
        self.filename.set('')
        self.labelfile = Label(self, textvariable=self.filename, borderwidth=2,
                               relief="sunken", width=40, anchor='w')
        self.labelfile.grid(column=1, row=0)
        self.btnProcess = Button(
            self, text='ประมวลผลนับคำ', command=self.process)
        self.btnProcess.grid(column=0, row=1, padx=5, pady=5)
        self.pgbar = ttk.Progressbar(
            self, orient='horizontal', length=200, mode='determinate')
        self.pgbar.grid(column=0, row=2, columnspan=2,
                        sticky='W', padx=5, pady=5)
        self.textprogress = Label(self, text='')
        self.textprogress.grid(column=1, row=2, padx=5, pady=5, sticky='s')

        self.result = StringVar()
        self.result.set('aaa\t999\nbbbb\t999\n...\nxxx\t99\nyyyy\t99\n...')
        self.frame = LabelFrame(self, text='คำที่ปรากฏมากที่สุด 10 อันดับ')
        self.frame.grid(column=0, row=3, columnspan=2,
                        padx=5, pady=5, sticky='w')
        Label(self.frame, textvariable=self.result, anchor="e").grid(
            column=0, row=0, padx=5, pady=5)

    def quit(self):
        self.showBeforeExit = messagebox.askquestion(
            "ยืนยันการปิดโปรแกรม", "คุณต้องการปิดโปรแกรมใช่หรือไม่")
        # ถ้าตอบ yes จะทำการปิดโปรแกรม
        self.destroy() if self.showBeforeExit == 'yes' else None

    def open_file(self):
        self.openfilename = fd.askopenfilename(
            filetypes=[('ไฟล์ข้อความ .txt', '*.txt')])
        print(self.openfilename)
        self.filename.set(self.openfilename)

    def process(self):
        if self.openfilename == None or self.openfilename == '':
            messagebox.showerror('เกิดข้อผิดพลาด', 'กรุณาระบุไฟล์ก่อนประมวลผล')
            self.open_file()

        else:
            threading.Thread(target=self.StartProcess).start()

    def StartProcess(self):
        f = open(self.openfilename, "r", encoding="utf-8")
        data = f.read()
        word = data.split()
        dicts = dict()
        max_file_txt = len(word)
        count = max_file_txt
        for i in word:
            dicts[i] = word.count(i)
            time.sleep(0.01)
            count -= 1
            if count != 0:
                self.pgbar['value'] = (
                    max_file_txt - count) / max_file_txt * 100
                self.textprogress['text'] = f'{( max_file_txt - count)+1}/{max_file_txt}'

        dicts_ten = list(dicts.items())[0:10]
        dicts_ten = dict(dicts_ten)
        list_dic = list(dicts_ten.items())
        list_dic = sorted(list_dic, key=lambda x: x[1], reverse=True)
        print(list_dic)
        self.result.set(f'{list_dic[0][0]}\t{list_dic[0][1]}\n{list_dic[1][0]}\t{list_dic[1][1]}\n{list_dic[2][0]}\t{list_dic[2][1]}\n{list_dic[3][0]}\t{list_dic[3][1]}\n{list_dic[4][0]}\t{list_dic[4][1]}\n{list_dic[5][0]}\t{list_dic[5][1]}\n{list_dic[6][0]}\t{list_dic[6][1]}\n{list_dic[7][0]}\t{list_dic[7][1]}\n{list_dic[8][0]}\t{list_dic[8][1]}\n{list_dic[9][0]}\t{list_dic[9][1]}')
        f.close()
        if self.result.set != 'aaa\t999\nbbbb\t999\n...\nxxx\t99\nyyyy\t99\n...':
            messagebox.showinfo('ประมวลผล', 'ประมวลผลเสร็จสิ้น')
            self.pgbar['value'] = 0
            self.textprogress['text'] = ''


if __name__ == "__main__":
    app = App()
    app.mainloop()