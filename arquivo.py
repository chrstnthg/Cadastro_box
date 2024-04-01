import csv
import tkinter as tk

def gravar_contato():
    with open("dados.csv","a") as arquivo_dados:
        escritor=csv.writer(arquivo_dados)
        escritor.writerow([entry_nome.get(), entry_telefone.get(), entry_email.get()])

    print("\n Dados gravados com sucesso")

janela = tk.Tk()

janela.geometry("320x320")


label_nome = tk.Label(janela, text= "Nome: ")
label_telefone = tk.Label(janela, text= "Telefone: ")
label_email = tk.Label(janela, text= "E-mail: ")

entry_nome = tk.Entry(janela)
entry_telefone = tk.Entry(janela)
entry_email = tk.Entry(janela)



button_gravar = tk.Button(text="Gravar Contato", command=gravar_contato)

label_nome.config(font=("Arial", 16))
label_nome.place(x=10, y=10)
entry_nome.place(x=10, y=40, width=300, height=30)

label_telefone.config(font=("Arial", 16))
label_telefone.place(x=10, y=80)
entry_telefone.place(x=10, y=110, width=300, height=30)

label_email.config(font=("Arial", 16))
label_email.place(x=10, y=160)
entry_email.place(x=10, y=190, width=300, height=30)

button_gravar.place(x=10, y=240, width=300, height=60)

janela.mainloop()

