import csv
import tkinter as tk
from tkinter import messagebox


def gravar_contato():

    if entry_nome.get().strip() == "" or entry_fone.get().strip() == "" or entry_email.get().strip() == "":
        messagebox.showerror("Erro ao gravar", "Todos os campos devem ser preenchidos")

    else:
        with open("dados.csv", "a", newline="") as arquivo_dados:
            escritor = csv.writer(arquivo_dados)
            escritor.writerow([entry_nome.get().strip(), entry_fone.get().strip(), entry_email.get().strip()])
            messagebox.showinfo("Sistema contatos", "Contato cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_fone.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_nome.focus_set()

    ler_contatos()


def ler_contatos():
    with open("dados.csv", "r") as arquivo_dados:
        leitor = csv.reader(arquivo_dados)
        lista_contatos.delete(0, tk.END)# limpar a lista
        for linha in leitor:
            lista_contatos.insert("end", linha[0])


janela = tk.Tk()

janela.geometry("580x300")

label_nome = tk.Label(janela, text="Nome:")
label_fone = tk.Label(janela, text="Telefone:")
label_email = tk.Label(janela, text="E-mail:")
label_contatos = tk.Label(janela, text="Contatos")

entry_nome = tk.Entry(janela)
entry_fone = tk.Entry(janela)
entry_email = tk.Entry(janela)

button_gravar = tk.Button(text="Gravar Contato", command=gravar_contato)

lista_contatos = tk.Listbox(janela, selectmode="single")

label_nome.config(font=("Arial", 16))
label_nome.place(x=10, y=10)
entry_nome.config(font=("Arial", 16))
entry_nome.place(x=10, y=40, width=300, height=30)

label_contatos.config(font=("Arial", 16))
label_contatos.place(x=320, y=10)

label_fone.config(font=("Arial", 16))
label_fone.place(x=10, y=80)
entry_fone.config(font=("Arial", 16))
entry_fone.place(x=10, y=110, width=300, height=30)

label_email.config(font=("Arial", 16))
label_email.place(x=10, y=150)
entry_email.config(font=("Arial", 16))
entry_email.place(x=10, y=180, width=300, height=30)

button_gravar.config(font=("Arial", 16))
button_gravar.place(x=10, y=230, width=300, height=60)

lista_contatos.config(font=("Arial", 16))
lista_contatos.place(x=320, y=40, width=250)

ler_contatos()

janela.mainloop()


