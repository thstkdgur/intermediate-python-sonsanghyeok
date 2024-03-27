import tkinter as tkt
from tkinter.filedialog import *

window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+800+300')
window.resizable(0,0)

# window.iconbitmap("C:\\Users\\user\\Documents\\카카오톡 받은 파일\\memo.ico")
photo = tkt.PhotoImage(file="C:\\Users\\user\\Documents\\카카오톡 받은 파일\KakaoTalk_20240326_192953043.png")
window.iconphoto(False, photo)

#텍스트 창 만들기 
text_area = tkt.Text(window)
#공백 설정하기 
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
#텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W)

# def new_file():
#     pass
# def save_file():
#     pass
# def maker():
#     pass

#새 파일
def new_file():
    text_area.delete(1.0, tkt.END)

#저장
def save_file():
    #파일 저장 물어보기
    f = asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text files', 'txt')])
    text_save = str(text_area.get(1.0 , tkt.END))
    f.write(text_save)
    f.close()

#만든이
def maker():
    help_view = tkt.Toplevel(window)
    help_view.geometry('300x50+850+400')
    help_view.title('만든 이')
    lb = tkt.Label(help_view, text = '\n손상혁')
    lb.pack()

#메뉴 생성
menuMaker = tkt.Menu(window)
#첫번째 메뉴 만들기 
first_menu = tkt.Menu(menuMaker, tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)
#메뉴 바 추가 
menuMaker.add_cascade(label='파일', menu=first_menu)
#메뉴 구성
window.config(menu = menuMaker)

first_menu.add_separator()
#종료 옵션 추가하기
first_menu.add_command(label='종료', command=window.destroy)

#두번째 메뉴 추가 
second_menu = tkt.Menu(menuMaker, tearoff=0)
#세부 메뉴 추가, 함수 연결
second_menu.add_command(label = '만든 이', command = maker)
#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)


window.mainloop() # 창 실행!


#새 파일 누르면 새 파일 만들기, 저장 누르면 윈도우에 저장, 만든이 누르면 이름, 창이나 텍스트 만들기
