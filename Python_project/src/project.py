from tkinter import *
from tkinter import messagebox

# 변수 선언 부분
# 파일 리스트 생성, 이미지 파일 이름 저장
fnameList = ["dog1.png", "dog2.png", "dog3.png", "dog4.png", "dog5.png", "dog6.png", "dog7.png", "dog8.png", "dog9.png"]
num = 0

# 함수 선언 부분
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "png/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    textLabel.configure(text = fnameList[num]) # 이미지가 다음으로 넘어갈 때 텍스트 변경

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file = "png/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    textLabel.configure(text = fnameList[num]) # 이미지가 이전으로 넘어갈 때 텍스트 변경

def myFunc():
    messagebox.showinfo("선택한 강아지", "이 강아지가 가장 마음에 드시는군요~")

# 메인 코드 부분
window = Tk()
window.geometry("700x600")
window.title("강아지 사진 앨범 보기")

heartimage = PhotoImage(file = "png/heart.png")

# 버튼 크기 조정
heartimage = heartimage.subsample(2, 2)

canvas = Canvas(window, width = 50, height = 50)
canvas.pack()

canvas.create_image(28, 25, image = heartimage)
canvas.bind("<Button-1>", lambda e : myFunc())

# 버튼 위젯 생성
btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

# 라벳 위젯으로 이미지 생성
photo = PhotoImage(file = "png/" + fnameList[0])
pLabel = Label(window, image = photo)
textLabel = Label(window, text = fnameList[num]) # 라벨로 텍스트 생성
textLabel2 = Label(window, text = "마음에 드는 강아지가 있으면 하트를 누르세요", font = 23, fg = "blue")

# 버튼 위젯 디스플레이
btnPrev.place(x = 250, y = 100)
btnNext.place(x = 400, y = 100)
textLabel.place(x = 325, y = 100) # 텍스트 위치 설정
textLabel2.place(x = 100, y = 50)

# 이미지 디스플레이
pLabel.place(x = 25, y = 150)

window.mainloop()