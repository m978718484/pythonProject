import sys
import tkinter
import tkinter.messagebox
import tkinter.font


class Window():
    def __init__(self):
        self.root = tkinter.Tk()
        self.currentIndex = 0
        self.data = []
        self.content = []
        self.select = {}
        ft = tkinter.font.Font(family = 'Fixdsys',size = 15,weight = tkinter.font.BOLD)
        self.label = tkinter.Label(font = ft)
        self.label.place(x=2,y=2)
        self.frame = tkinter.Frame(self.root,)
        self.frame.place(x=10, y=30)

        self.v = tkinter.StringVar()
        self.v.set("0")
        self.v1 = []
        self.Load_data()

    def Set_Content(self,index):
        currentshow = self.content[index]
        self.label['text'] = currentshow[0] 
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.v.set("0")
        for text,value in currentshow[1]:
            if self.currentIndex == len(self.content) -1:
                var = tkinter.IntVar()
                c = tkinter.Checkbutton(self.frame, text=text,variable=var,command=self.last)
                c.pack(anchor='w')
                self.v1.append(var)
                ButtonCov = tkinter.Button(self.root, text='提 交', command=self.Conv)
                ButtonCov.place(x=200, y=300)
            else:
                r = tkinter.Radiobutton(self.frame, text=text,variable=self.v, value=value,command=self.next)
                r.pack(anchor='w')

    def Load_data(self):
        all_the_text = open('question.txt').read()
        self.data = all_the_text.split('\n')
        for i in range(0,len(self.data)):
            temp = self.data[i].split(' ')
            temp_row = []
            temp_row.append(temp[0])
            MODES = []
            for x in range(1,len(temp)):
                MODES.append((temp[x],x))
            temp_row.append(MODES)
            self.content.append(temp_row)
        # print (self.content)
        self.Set_Content(self.currentIndex)
        self.currentIndex = self.currentIndex + 1

    def next(self):
        self.select[self.currentIndex] = self.v.get()
        self.Set_Content(self.currentIndex)
        self.currentIndex = self.currentIndex + 1

    def last(self):
        temp = map((lambda var: var.get()), self.v1)
        self.select[self.currentIndex] = list(temp)

    def Conv(self):
        if 1 not in self.select[self.currentIndex]:
            tkinter.messagebox.showinfo('信息提示', '最少选择1项')
        else:
            tkinter.messagebox.showinfo('信息提示', '问卷调查结束，按确定退出系统')
            print(self.select)   
            sys.exit(0)




    def mainloop(self):
        self.root.minsize(800, 350)
        self.root.maxsize(1000, 500)
        self.root.title('调查问卷')
        self.root.mainloop()



# if __name__ == "__main__":
#     window = Window()
#     window.mainloop()
