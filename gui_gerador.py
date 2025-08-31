import tkinter as tk
from tkinter import ttk

#Aqui eu crio a janela principal.
root = tk.Tk()

#Aqui eu crio o título
root.title('Gerador de Senhas')

#Aqui eu determino o tamanho da janela
root.geometry('500x300+300+300')

#Aqui eu bloqueio o redimensionamento da janela
root.resizable(False, False)

#Aqui eu crio o painel que vai mostrar as senhas
status_var = tk.StringVar()
ttk.Label(root, textvariable=status_var).grid(row=0, column=0, sticky=(tk.W + tk.E))

#Aqui eu crio um título para o Spinbox
ttk.Label(root, text="Qual é o tamanho da sua senha?\n" \
"Escolha um número de 5 a 20").grid(row=1, column=0, sticky=(tk.W + tk.E))

#Aqui eu crio a caixa de seleção de tamanho de senha.
tam_senha = tk.IntVar(value=12)
ttk.Spinbox(root, textvariable=tam_senha, from_=5, to=20, increment=1).grid(
    row=2, column=0, sticky=(tk.W + tk.E)
)


#Aqui eu crio o painel para mostrar as opções de senha
conf = ttk.LabelFrame(root, text="O que você quer na sua senha?")
conf.grid(row=3, column=0, sticky=(tk.W + tk.E))

#Aqui eu crio um loop para preencher os espaços
for i in range(5):
    conf.rowconfigure(i, weight=1)


