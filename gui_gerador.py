import tkinter as tk
from tkinter import ttk
from random import randint



def on_gerar_senha():
    """Função para gerar senhas"""
    parcial = []
    senha = []

    caracteres = ('!', '@', '#', '$', '%', '*', '&', '(', ')', '?')
    números = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    alfamaiu = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'X', 'Y', 'Z', 'W')
    alfaminu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'x', 'y', 'z', 'w')
    

    if carac_var.get():
        parcial.append(caracteres)
    if maiu_var.get():
        parcial.append(alfamaiu)
    if minu_var.get():
        parcial.append(alfaminu)
    if num_var.get():
        parcial.append(números)

    if not (carac_var.get() or maiu_var.get() or minu_var.get() or num_var.get()):
        status_var.set("Escolha uma opção")
        return

    try:
        tamanho = int(tam_senha.get())
    except:
        status_var.set('Escolha uma opção')
        return

    for i in range(tamanho):
        var = randint(0, len(parcial) - 1)
        if len(parcial[var]) == 10:
            dez = randint(0, 9)
            senha.append(parcial[var][dez])
        if len(parcial[var]) == 26:
            vinte = randint(0, 25)
            senha.append(parcial[var][vinte])
    
    final = ''
    final = final.join(senha)
    status_var.set(final)



#Aqui eu crio a janela principal.
root = tk.Tk()

#Aqui eu crio o título
root.title('Gerador de Senhas')

#Aqui eu determino o tamanho da janela
root.geometry('500x300+300+300')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#Aqui eu bloqueio o redimensionamento da janela
root.resizable(False, False)

#Aqui eu crio um painel para comportar o motrador de senhas
status = ttk.LabelFrame(root, text="Sua senha:")
status.grid(row=0, column=0, sticky=tk.W + tk.E)

#Aqui eu crio o painel que vai mostrar as senhas
status_var = tk.StringVar()
ttk.Label(status, textvariable=status_var).grid(row=0, column=0, sticky=tk.W + tk.E)

#Aqui eu crio um título para o Spinbox
ttk.Label(root, text="Qual é o tamanho da sua senha?\n" \
"Escolha um número de 5 a 20").grid(row=1, column=0, sticky='nsew')

#Aqui eu crio a caixa de seleção de tamanho de senha.
tam_senha = tk.StringVar(value=12)
ttk.Spinbox(root, textvariable=tam_senha, from_=5, to=20, increment=1).grid(
    row=2, column=0, sticky='nsew')


#Aqui eu crio o painel para mostrar as opções de senha
conf = ttk.LabelFrame(root, text="O que você quer na sua senha?")
conf.grid(row=3, column=0, sticky=tk.W + tk.W)

#Aqui eu crio um loop para preencher os espaços
for i in range(5):
    conf.rowconfigure(i, weight=1)

#Aqui eu crio o checkbutton para caracteres especiais
carac_var = tk.BooleanVar(value=False)
ttk.Checkbutton(conf,variable=carac_var, text="Você que símbolos especiais na sua senha?").grid(
    row=0, column=0, sticky=tk.W, padx=10
)

#Aqui eu crio o checkbutton para letras maiúsculas
maiu_var = tk.BooleanVar(value=False)
ttk.Checkbutton(conf, variable=maiu_var, text="Você quer letras maiúsculas na sua senha?").grid(
    row=1, column=0, sticky=tk.W, padx=10
)

#Aqui eu crio o checkbutton para letras minúsculas
minu_var = tk.BooleanVar(value=False)
ttk.Checkbutton(conf, variable=minu_var, text="Você quer letras minúsculas na sua senha?").grid(
    row=2, column=0, sticky=tk.W, padx=10
)

#Aqui eu crio o checkbutton para números
num_var = tk.BooleanVar(value=False)
ttk.Checkbutton(conf, variable=num_var, text="Você quer números na sua senha?").grid(
    row=3, column=0, sticky=tk.W, padx=10
)

gerar_button = ttk.Button(root, text="Gerar Senha", command=on_gerar_senha
                        ).grid(row=99, column=0, sticky='nsew')

root.mainloop()