# 導入tkinter模塊
import tkinter
# 導入tkinter.messagebox模塊 消息框
import tkinter.messagebox
# 導入tkinter.font模塊 字體
import tkinter.font

# 創建Window類，相當於創建一個調查問卷應用
class Window():
    # 初始化控件及存放數據相關的變量
    def __init__(self):
        # 實例化TK類，可以理解為用於數據展示的窗體
        self.root = tkinter.Tk()
        # 用於記住當前答到的第幾個調查問卷題
        self.currentIndex = 0
        # 將question.txt所有內容按行存儲到這個數組中
        self.data = []
        # 用於存放更細化的每一行數據拆分，self.content  = [[題目1，(選項1,1)，(選項2,2)，... ]，[題目2,(選項1,1)，(選項2,2)，...] 
        self.content = []
        # 存儲選擇的結果，沒選一題執行 self.select[當前題號] = 選擇第幾個答案
        self.select = {}
        # 創建一個字體實例
        ft = tkinter.font.Font(family = 'Fixdsys',size = 15,weight = tkinter.font.BOLD)
        # 創建用於顯示問卷題的Label,并設置字體為ft
        self.label = tkinter.Label(font = ft)
        # Label所在窗體的位置
        self.label.place(x=2,y=2)
        # 創建一個Frame對象，用於存放顯示選項
        self.frame = tkinter.Frame(self.root,)
        # Frame對象在窗體的位置
        self.frame.place(x=10, y=30)
        # 用於記住單選題的選項狀態
        self.v = tkinter.StringVar()
        # 設置單選項的初始值為未選中狀態
        self.v.set("0")
        # 用於記住多選題的選項狀態
        self.v1 = []
        # 調用 加載問卷題目及選項 方法
        self.Load_data()

    # 每答完一題顯示下一個問卷題目的方法
    def Set_Content(self,index):
        # 獲取當前題目及選項
        currentshow = self.content[index]
        # 將當前的題目賦值給self.label
        self.label['text'] = currentshow[0] 
        # 遍歷self.frame所有選項，就是那些Radiobutton
        for widget in self.frame.winfo_children():
            # 清空上一個題目的選項
            widget.destroy()
        # 設置當前題目單選項的初始值為未選中狀態
        self.v.set("0")
        # 遍歷題目的選項數組
        for text,value in currentshow[1]:
            # 如果當前題目是最後一個題目
            if self.currentIndex == len(self.content) -1:
                # 定義一個臨時的tkinter.IntVar，用於初始化checkbutton多選題的值
                var = tkinter.IntVar()
                # 在self.frame里創建Checkbutton多選題的選項，并綁定點選事件到self.last方法
                c = tkinter.Checkbutton(self.frame, text=text,variable=var,command=self.last)
                # 將Checkbutton放到self.frame上面
                c.pack(anchor='w')
                # 全局self.v1添加當前多選題的選項值，開始時為0
                self.v1.append(var)
                # 因為最後一題，需要創建一個按鈕來執行提交動作，統計答題的結果，綁定點擊事件到self.Conv方法
                ButtonCov = tkinter.Button(self.root, text='提 交', command=self.Conv)
                # ButtonCov在窗體的位置
                ButtonCov.place(x=200, y=300)
            # 如果當前題目不是最後一個題目
            else:
                # 在self.frame里創建Radiobutton單選題的選項，并綁定點選事件到self.next方法
                r = tkinter.Radiobutton(self.frame, text=text,variable=self.v, value=value,command=self.next)
                # 將r放到self.frame上面
                r.pack(anchor='w')
    # 加載問卷題目及選項
    def Load_data(self):
        # 讀取問題內容到all_the_text
        all_the_text = open('question.txt').read()
        # 處理all_the_text，并放到self.data數組裏面
        self.data = all_the_text.split('\n')
        # 循環訪問self.data數組
        for i in range(0,len(self.data)):
            # 創建臨時數組，并把當前的數據拆分后賦給它
            temp = self.data[i].split(' ')
            # 創建臨時數組 temp_row
            temp_row = []
            # -----------------------------------------------------------
            # 虛線之間的代碼沒法註釋，數據處理過程，都是最基礎的代碼
            temp_row.append(temp[0])
            MODES = []
            for x in range(1,len(temp)):
                MODES.append((temp[x],x))
            temp_row.append(MODES)
            self.content.append(temp_row)
            # 虛線之間的代碼沒法註釋，只要知道虛線內步驟執行完后 self.content 數據格式為：[[題目1，(選項1,1)，(選項2,2)，... ]，[題目2,(選項1,1)，(選項2,2)，...] 
            #-------------------------------------------------------------
        # 將第一題展示到介面上
        self.Set_Content(self.currentIndex)
        # 當前題目指向下一題下標
        self.currentIndex = self.currentIndex + 1

    # 跳轉下一題方法
    def next(self):
        # 將當前題的選項保存到self.select變量
        self.select[self.currentIndex] = self.v.get()
        # 加載下一個題目到介面
        self.Set_Content(self.currentIndex)
        # 當前題目指向下一題下標
        self.currentIndex = self.currentIndex + 1
    # 保存多選題選項值，每一個Checkbutton點擊都會執行該法
    def last(self):
        # 映射獲取多選題的選中狀態
        temp = map((lambda var: var.get()), self.v1)
        # 將映射轉變為list并賦給self.select
        self.select[self.currentIndex] = list(temp)
    # 提交按鈕點擊事件
    def Conv(self):
        # 如果多選題未選，提示必須要選一個選項
        if 1 not in self.select[self.currentIndex]:
            # 彈框提醒
            tkinter.messagebox.showinfo('信息提示', '最少选择1项')
        else:
            # 彈框提醒
            tkinter.messagebox.showinfo('信息提示', '问卷调查结束，按确定退出系统')
            # 打印問卷結果
            print(self.select)   
            # 退出系統
            sys.exit(0)
    # 彈出窗體事件
    def mainloop(self):
        # 設置窗體的大小的最小值
        self.root.minsize(800, 350)
        # 設置窗體的大小的最大值
        self.root.maxsize(1000, 500)
        # 設置窗體的標題
        self.root.title('调查问卷')
        # 呼出窗體
        self.root.mainloop()
