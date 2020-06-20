import json
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pygame

with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

pergunta = [v for v in data[0].values()]
resposta = [v for v in data[1].values()]

resp = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3, 1, 0, 2, 3, 0, 0, 2, 2, 2, 1]

resp_user = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 20:
        x = random.randint(0, 19)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def play_music():
    # Inicializando o mixer PyGame
    pygame.mixer.init()

    # Iniciando o Pygame
    pygame.init()

    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)


def mostra_resultado(pontos):
    lblPergunta.destroy()
    resp1.destroy()
    resp2.destroy()
    resp3.destroy()
    resp4.destroy()
    lblimagem = Label(
        root,
        background="#ffffff",
        border=0,
    )
    lblimagem.pack(pady=(50, 30))
    lblresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    lblresulttext.pack()

    if pontos == 20:
        img = PhotoImage(file="vencedor.png")
        lblimagem.configure(image=img)
        lblimagem.image = img
        lblresulttext.configure(text=f"Parabéns! Você fez {pontos} pontos e acertou todas as perguntas!"
                                     "\nCom isso, demonstrou estar muito bem informado!"
                                     "\nJuntos somos mais fortes no combate ao Covid-19!", fg='#008000', font=' Consolas 20 bold')

    elif 10 <= pontos <= 19:
        img = PhotoImage(file="ok.png")
        lblimagem.configure(image=img)
        lblimagem.image = img
        lblresulttext.configure(text=f"Você foi bem! Fez {pontos} pontos.\n Atualize-se mais, pois sua ajuda será muito importante"
                                     "\npara o combate ao Covid-19!", fg='#002699', font='Consolas 20 bold')
    else:
        img = PhotoImage(file="virus.png")
        lblimagem.configure(image=img)
        lblimagem.image = img
        lblresulttext.configure(text=f"Poxa, que pena! Você fez apenas {pontos} pontos.\nPrecisa se atualizar bastante,"
                                     "\npara que possamos juntos\ncombater o Covid-19!", fg='#cc0000', font='Consolas 20 bold')


def calc():
    global indexes, resp_user, resp
    x = 0
    pontos = 0
    for i in indexes:
        if resp_user[x] == resp[i]:
            pontos += 1
        x += 1
    print(pontos)
    mostra_resultado(pontos)


ques = 1


def selecionado():
    global radiovar, resp_user
    global lblPergunta, resp1, resp2, resp3, resp4
    global ques
    x = radiovar.get()
    resp_user.append(x)
    radiovar.set(-1)
    if ques < 20:
        lblPergunta.config(text=pergunta[indexes[ques]])
        resp1['text'] = resposta[indexes[ques]][0]
        resp2['text'] = resposta[indexes[ques]][1]
        resp3['text'] = resposta[indexes[ques]][2]
        resp4['text'] = resposta[indexes[ques]][3]
        ques += 1
    else:
        calc()


def main():
    mainmenu = Menu(root)

    root.configure(menu=mainmenu)

    submenu = Menu(mainmenu, tearoff=0)
    mainmenu.add_cascade(label="Opções", menu=submenu)
    submenu.add_command(label="Info", command=info)
    submenu.add_command(label="Sair", command=sair)


def sair():
    saida = messagebox.askyesno(title="Sair", message="Deseja realmente sair do jogo?")
    if saida > 0:
        root.destroy()
        return


def info():
    messagebox.showinfo(title="Equipe Innovatis", message="Allan Carlos"
                                                          "\nAndré Felipe"
                                                          "\nJean Nunes")


def inicia_quiz():
    global lblPergunta, resp1, resp2, resp3, resp4
    lblPergunta = Label(
        root,
        text=pergunta[indexes[0]],
        font=("Consolas bold", 18),
        fg='#00802b',
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblPergunta.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    resp1 = Radiobutton(
        root,
        text=resposta[indexes[0]][0],
        font=("Times bold", 13),
        value=0,
        variable=radiovar,
        command=selecionado,
        background="#ffffff",
    )
    resp1.pack(pady=5)

    resp2 = Radiobutton(
        root,
        text=resposta[indexes[0]][1],
        font=("Times bold", 13),
        value=1,
        variable=radiovar,
        command=selecionado,
        background="#ffffff",
    )
    resp2.pack(pady=5)

    resp3 = Radiobutton(
        root,
        text=resposta[indexes[0]][2],
        font=("Times bold", 13),
        value=2,
        variable=radiovar,
        command=selecionado,
        background="#ffffff",
    )
    resp3.pack(pady=5)

    resp4 = Radiobutton(
        root,
        text=resposta[indexes[0]][3],
        font=("Times bold", 13),
        value=3,
        variable=radiovar,
        command=selecionado,
        background="#ffffff",
    )
    resp4.pack(pady=5)


def start_clicado():
    lblimagem.destroy()
    lbltext.destroy()
    lblInstrucao.destroy()
    lblRegras.destroy()
    btStart.destroy()
    gen()
    inicia_quiz()
    play_music()


root = tkinter.Tk()
root.title("Corona Quiz By Innovatis Games")
root.iconbitmap('logo.ico')
root.geometry("1000x700+10+10")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="logo.png")

lblimagem = Label(
    root,
    image=img1,
    background="#ffffff",
)
lblimagem.pack(pady=(40, 0))

lbltext = Label(
    root,
    text="Corona Quiz",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
lbltext.pack(pady=(0, 50))

img2 = PhotoImage(file="start.png")

btStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=start_clicado,
)
btStart.pack()

lblInstrucao = Label(
    root,
    text="Bem-vindo ao Corona Quiz!\nClique em Start para iniciar o jogo!",
    background="#ffffff",
    font=("Consolas bold", 16),
    justify="center",
)
lblInstrucao.pack(pady=(10, 70))

lblRegras = Label(
    root,
    text="Este quiz contém 20 perguntas.\n"
         "Para ganhar, você terá que acertar todas elas.\n"
         "Tenha certeza ao clicar em uma resposta,\npois será sua opção final. Pense antes de selecionar!",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="#FACA2F",
)
lblRegras.pack()

main()

root.mainloop()
