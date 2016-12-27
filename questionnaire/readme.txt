50
調查問卷程序說明 python 3.4
腳本由 questionnaire.py（主程序） 及 question.txt 調查問卷內容文本構成
主要功能：
1.自定義帶固定格式的問卷內容，
2.實現單選題點選自動下一題，最後一題多選帶有提交按鈕，點提交后打印出所有題目對應的選項的
數據結構說明：
1.提交問卷后存儲的數據結構為 字典，其中題號為key,所選選項為value 多選題的value為只包含0和1的數組，1為勾選，0為未選
2.question.txt 格式為 題目 選項1 選項2 選項3 ...（都以空格作為分隔）