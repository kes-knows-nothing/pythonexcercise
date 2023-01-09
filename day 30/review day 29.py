from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import json
import pyperclip

# 2-1 입력 내용 저장 버튼 기능 구현

def add():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="안내", message="빈칸을 모두 입력해주십시오.")
    else:
        try:
            with open("data.json", "r") as file_data:
                data = json.load(file_data)
        except FileNotFoundError:
            with open("data.json", "w") as file_data:
                json.dump(new_data, file_data, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file_data:
                json.dump(data, file_data, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="안내", message="입력 정보가 저장되었습니다.")

# 2-2 랜덤 비밀번호 생성

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# 3-2 찾기 기능 구현

def search():
    website = website_entry.get()
    email = email_entry.get()
    try:
        with open("data.json") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showwarning(title="경고", message="데이터를 저장 후에 다시 시도해주세요.")
    else:
        password = data[website]["password"]
        if website in data:
            messagebox.showinfo(title="안내", message=f"해당 사이트의\n이메일: {email}\n비밀번호: {password}입니다.")
        else:
            messagebox.showerror(title="에러 메시지", message="해당 데이터를 찾을 수 없습니다.")


# 한글로 만들어보는 비밀번호 생성기

# 1.UI 작성

# 1-1 화면 생성
window = Tk()
window.title("비밀번호 생성기")
window.config(padx=20, pady=20)

# 1-2 그림 파일 불러오고 배치하기
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# 1-3 레이블, 엔트리, 버튼 배치
website_label = Label(text="웹사이트")
website_label.grid(row=1, column=0)
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1)
email_label = Label(text="이메일 주소")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "kestrel@email.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_label = Label(text="비밀번호")
password_label.grid(row=3, column=0)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)
password_gen_button = Button(text="랜덤 비밀번호 생성", command=random_password, width=20)
password_gen_button.grid(row=3, column=2)
add_button = Button(text="입력 내용 저장", width=35, command=add)
add_button.grid(row=4, column=1, columnspan=2)

# 3-1 찾기 버튼 추가
search_button = Button(text="찾기", width=20, command=search)
search_button.grid(row=1, column=2)
# 2. 버튼 기능 구현
# 3. 찾기 기능 구현

window.mainloop()