import pyautogui
import time
import os
import tkinter as tk
import pandas

# 1920 1080
width, height = pyautogui.size()

x1 = int(width * 454 / 1920)
y1 = int(height * 625 / 1080)

x2 = int(width * 916 / 1920)
y2 = int(height * 780 / 1080)

x3 = int(width * 930 / 1920)
y3 = int(height * 780 / 1080)

mode = 'null'

def MainCode():

    global mode, output_label, x1, y1, x2, y2, x3, y3
    if mode == '0':
        dataFrame = pandas.read_csv("Data")
        data = dataFrame.values
        l = len(data)

        time.sleep(5)
        for i in range(0, l):
            pyautogui.click(x1, y1)
            time.sleep(1.5)
            str = data[i]
            for j in range(0, len(str[0])):
                ch = str[0][j]
                if ch != '-':
                    pyautogui.press(ch)
            pyautogui.write(str, interval=0.1)

            pyautogui.click(x2, y2)
            time.sleep(2)
            pyautogui.click(x3, y3)
            time.sleep(2)
            pyautogui.press("f5")
            time.sleep(2)

        output_label.config(text = "Done!")

    elif mode == '1':

        path = "Files"
        file_names = [entry[0:-4] for entry in os.listdir(path) if os.path.isfile(os.path.join(path, entry))]

        data = []
        F = open("TextData.txt")
        for S in F:
            if not (S[-1] >= '0' and S[-1] <= '9'):
                S = S[:-1]  # /n is at end
            if file_names.count(S) == 0:
                data.append(S)

        Mising = "Mising: {0}".format(len(data))
        output_label.config(text = Mising)  # print(len(data))
        if len(data) == 0:
            mode = "null2"

        dataFrame = pandas.DataFrame(data)
        dataFrame.to_csv("Data", index=False)

def on_button1_click():
    global mode, output_label
    if mode == 'null':
        output_label.config(text = "Prepare the data first!!!!")
    elif mode == 'null2':
        output_label.config(text="Everything is already done :)")
    else:
        mode = '0'
        MainCode()

def on_button2_click():
    global mode
    mode = '1'
    MainCode()

window = tk.Tk()
window.title("CERTIFICATES")
window.geometry("500x200")
window.configure(bg="red")


button_font = ("Arial", 16)

button1 = tk.Button(window, text="Compile", command=on_button1_click,
                    font=button_font)
button1.pack(pady=10)

button2 = tk.Button(window, text="Prepare the data", command=on_button2_click,
                    font=button_font)
button2.pack(pady=10)


output_label = tk.Label(window, text="")
output_label.pack(pady=10)


window.mainloop()



