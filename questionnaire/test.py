from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font

class App1(ttk.Frame):
    def createWidgets(self):
        #text variables
        self.i_height = StringVar()
        self.i_weight = StringVar()
        self.o_bmi = StringVar()

        #labels
        self.label1 = ttk.Label(self, text="Enter your weight:").grid(row=0, column=0, sticky=W)
        self.label2 = ttk.Label(self, text="Enter your height:").grid(row=1, column=0, sticky=W)
        self.label3 = ttk.Label(self, text="Your BMI is:").grid(row=2, column=0, sticky=W)

        #text boxes
        self.textbox1 = ttk.Entry(self, textvariable=self.i_weight).grid(row=0, column=1, sticky=E)
        self.textbox2 = ttk.Entry(self, textvariable=self.i_height).grid(row=1, column=1, sticky=E)
        self.textbox3 = ttk.Entry(self, textvariable=self.o_bmi).grid(row=2, column=1, sticky=E)

        #buttons
        self.button1 = ttk.Button(self, text="Cancel/Quit", command=self.quit).grid(row=3, column=1, sticky=E)
        self.button1 = ttk.Button(self, text="Ok", command=self.calculateBmi).grid(row=3, column=2, sticky=E)

    def calculateBmi(self):
        try:
            self.weight = float(self.i_weight.get())
            self.height = float(self.i_height.get())
            self.bmi = self.weight / self.height ** 2.0
            self.o_bmi.set(self.bmi)
        except ValueError:
            messagebox.showinfo("Error", "You can only use numbers.")
        finally:
            self.i_weight.set("")
            self.i_height.set("")

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

class App2(ttk.Frame):
    def create_widgets(self):
        """Create the widgets for the GUI"""
        #1 textbox (stringvar)
        self.entry= StringVar()
        self.textBox1= ttk.Entry(self, textvariable=self.entry).grid(row=0, column=1)

        #5 labels (3 static, 1 stringvar)
        self.displayLabel1 = ttk.Label(self, text="feet").grid(row=0, column=2, sticky=W)
        self.displayLabel2 = ttk.Label(self, text="is equivalent to:").grid(row=1, column=0)
        self.result= StringVar()
        self.displayLabel3 = ttk.Label(self, textvariable=self.result).grid(row=1, column=1)
        self.displayLabel4 = ttk.Label(self, text="meters").grid(row=1, column=2, sticky=W)

        #2 buttons
        self.quitButton = ttk.Button(self, text="Quit", command=self.quit).grid(row=2, column=1, sticky=(S,E))
        self.calculateButton = ttk.Button(self, text="Calculate", command=self.convert_feet_to_meters).grid(row=2, column=2, sticky=(S,E))

    def convert_feet_to_meters(self):
        """Converts feet to meters, uses string vars and converts them to floats"""
        self.measurement = float(self.entry.get())
        self.meters = self.measurement * 0.3048
        self.result.set(self.meters)

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

class BMIApp(object):

  def __init__(self, master):
  	self.master = master
  	self.currentIndex = 0
  	self.data = []
  	self.content = []
  	self.select = {}
  	ft = tkinter.font.Font(family = 'Fixdsys',size = 15,weight = tkinter.font.BOLD)
  	self.question_label = ttk.Label(master,text="中華人民共和國",font = ft)
  	self.question_label.pack()
  	self.question_label.place(x=2,y=2)
  	self.frame = ttk.Frame(master,)
  	self.frame.place(x=10, y=30)
  	self.v =IntVar()
  	self.v.set(-1)
  	self.v1 = []
  	self.Load_data()

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
  	self.Set_Content(self.currentIndex)
  	self.currentIndex = self.currentIndex + 1
  	
  def next(self):
  	print(self.v.get())
  	self.select[self.currentIndex] = self.v.get()
  	self.Set_Content(self.currentIndex)
  	self.currentIndex = self.currentIndex + 1

  def Set_Content(self,index):
  	currentshow = self.content[index]
  	self.question_label['text'] = currentshow[0]
  	for widget in self.frame.winfo_children():
  		widget.destroy()
  	self.v.set(-1)
  	for text,value in currentshow[1]:
  		if self.currentIndex == len(self.content) -1:
  			var = IntVar()
  			c = ttk.Checkbutton(self.frame, text=text,variable=var,command=self.last)
  			c.pack(anchor='w')
  			self.v1.append(var)
  		else:
  			r = ttk.Radiobutton(self.frame, text=text,variable=self.v, value=value,command=self.next)
  			r.pack(anchor='w')
  	if self.currentIndex==len(self.content)-1:
  		ButtonCov = ttk.Button(self.master, text='提 交', command=self.Conv)
  		ButtonCov.pack()
  		ButtonCov.place(x=200, y=300)


  def last(self):
  		temp = map((lambda var: var.get()), self.v1)
  		self.select[self.currentIndex] = list(temp)

  def Conv(self):
  	if 1 not in self.select[self.currentIndex]:
  		tkinter.messagebox.showinfo('信息提示', '最少选择1项')
  	else:
  		tkinter.messagebox.showinfo('信息提示', '问卷调查结束，按确定退出系统')
  		print(self.select)
    # -----------------------------------------------------------------------------------
    # # heading label
    # self.heading_label = ttk.Label(master, text="BMI Calculator")
    # self.heading_label.pack()

    # weight input
    # self.weight_entry = ttk.Entry(master)
    # self.weight_entry.pack()
    # self.weight_entry.insert(0,"Weight in kg") 

    # # height input
    # self.height_entry = ttk.Entry(master)
    # self.height_entry.pack()
    # self.height_entry.insert(0,"Height in m")

    # # submit button
    # self.submit_button = ttk.Button(master, text="Compute!", command=self.calc_bmi)
    # self.submit_button.pack()

  # def calc_bmi(self):
  #   # compute and show bmi to 2 decimal places
  #   bmi = int(self.weight_entry.get()) / (float(self.height_entry.get()) * float(self.height_entry.get()))
  #   messagebox.showinfo(title="Your BMI", message="{0:.2f}".format(bmi))
  # ----------------------------------------------------------------------------------------------------------

def button1_click():
    root = Tk()
    app = App1(master=root)
    app.mainloop()

def button2_click():
    root = Tk()
    app = App2(master=root)
    app.mainloop()
def button3_click():
	root = Tk()
	app = BMIApp(master=root)


def main():
    window = Tk()
    button1 = ttk.Button(window, text="bmi calc", command=button1_click).grid(row=0, column=1)
    button2 = ttk.Button(window, text="feet conv", command=button2_click).grid(row=1, column=1)
    button3 = ttk.Button(window, text="xxxx", command=button3_click).grid(row=2, column=1)
    window.mainloop()

if __name__ == '__main__':
    main()