import json
import tkinter
from tkinter import *
from tkinter import messagebox
import random

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

pergunta = [v for v in data[0].values()]
resposta = [v for v in data[1].values()]

resp = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

resp_user = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 10:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(pontos):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if pontos == 10:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Parabéns!\nDemonstrou grande conhecimento\nsobre o Covid-19!")
    elif 4 <= pontos < 9:
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Muito bom!\n Mas ainda pode melhorar!")
    else:
        img = PhotoImage(file="imagem05.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Poxa, que pena!\nVocê precisa se atualizar mais\nsobre o Covid-19!")


def calc():
    global indexes, resp_user, resp
    x = 0
    pontos = 0
    for i in indexes:
        if resp_user[x] == resp[i]:
            pontos += 1
        x += 1
    print(pontos)
    showresult(pontos)


ques = 1


def selected():
    global radiovar, resp_user
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    resp_user.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text=pergunta[indexes[ques]])
        r1['text'] = resposta[indexes[ques]][0]
        r2['text'] = resposta[indexes[ques]][1]
        r3['text'] = resposta[indexes[ques]][2]
        r4['text'] = resposta[indexes[ques]][3]
        ques += 1
    else:
        calc()


def mquit():
    mexit = messagebox.askyesno(title="Sair", message="Deseja realmente sair do jogo?")
    if mexit > 0:
        root.destroy()
        return


def info():
    messagebox.showinfo(title="Equipe Innovatis", message="Allan Carlos M. Ribeiro"
                                                          "\nAndré Felipe P. da Silva"
                                                          "\nJean Nunes de O. Silva")


def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=pergunta[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=resposta[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=resposta[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=resposta[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=resposta[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Corona Quiz By Innovatis Games")
root.iconbitmap('quiz.ico')
root.geometry("700x700")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="imagem06.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(40, 0))

labeltext = Label(
    root,
    text="Corona Quiz",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Bem-vindo ao Corona Quiz!\nClique em Start para iniciar o jogo!",
    background="#ffffff",
    font=("Consolas", 14),
    justify="center",
)
lblInstruction.pack(pady=(10, 70))

lblRules = Label(
    root,
    text="Este quiz contém 10 perguntas.\n"
         "Para ganhar, você terá que acertar todas elas.\n"
         "Tenha certeza ao clicar em uma resposta,\npois será sua opção final. Pense antes de selecionar!",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="#FACA2F",
)
lblRules.pack()

mainmenu = Menu(root)

root.configure(menu=mainmenu)

submenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Opções", menu=submenu)
submenu.add_command(label="Info", command=info)
submenu.add_command(label="Sair", command=mquit)

root.mainloop()
