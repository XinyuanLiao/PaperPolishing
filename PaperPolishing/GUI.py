import PySimpleGUI as sg
import ChatGPT

sg.theme('default1')  # 设置主题
font = ("Times New Roman", 16)
font1 = ("Helvetica", 20)
layout = [[sg.Text(text='中文或需要润色的英文：', size=(52, 1), font=font1)],
          [sg.Multiline(key="-IN-", size=(75, 10), font=font)],
          [sg.Text(text='润色后的英文及其中文翻译：', size=(50, 1), font=font1)],
          [sg.Multiline(key="-OUT-", size=(75, 10), font=font, default_text=ChatGPT.check_connection())],
          [sg.Text(text='', size=(10, 1)),
           sg.Button("翻译", size=(15, 1), button_color='#a5a7ab', font=font),
           sg.Button("润色", size=(15, 1), button_color='#a5a7ab', font=font),
           sg.Button("清除", size=(15, 1), button_color='#a5a7ab', font=font),
           sg.Button("退出", size=(15, 1), button_color='#a5a7ab', font=font)]
          ]
window = sg.Window("PaperPolishing", layout)  # 设置窗口名称，窗口布局，以及图标
# print(ChatGPT.check_connection())
while True:
    event, values = window.read()
    if event in (None, "退出"):  # 点击“X”或者“退出”按钮时才退出
        break
    if event == "润色":
        tar = ChatGPT.response(values["-IN-"])
        window["-OUT-"].Update(tar)
    if event == "翻译":
        tar = ChatGPT.only_translate(values["-IN-"])
        window["-OUT-"].Update(tar)
    if event == "清除":
        window["-IN-"].Update("")
        window["-OUT-"].Update("")
window.close()
