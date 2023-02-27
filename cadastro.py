import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]
lista_codigos = []

janela = tk.Tk()

#Função

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionartipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))

#Titulo da janela
janela.title('Ferramenta de cadastro de materiais')

lable_descricao = tk.Label(text='Descrição do Material')
lable_descricao.grid(row=1, column=0, padx=10, pady= 10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady= 10, sticky='nswe', columnspan=4)

lable_tipo_unidade = tk.Label(text='Tipo da unidade do Material')
lable_tipo_unidade.grid(row=3, column=0, padx=10, pady= 10, sticky='nswe', columnspan=2)

combobox_selecionartipo = ttk.Combobox(values=lista_tipos)
combobox_selecionartipo.grid(row=3, column=2, padx=10, pady= 10, sticky='nswe', columnspan=2)

lable_quant = tk.Label(text='Quantidade na unidade de Material')
lable_quant.grid(row=4, column=0, padx=10, pady= 10, sticky='nswe', columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady= 10, sticky='nswe', columnspan=2)

botao_confirm = tk.Button(text= "Confirme o código", command=inserir_codigo)
botao_confirm.grid(row=5, column=1, padx=10, pady= 10, sticky='nswe', columnspan=2)

janela.mainloop()

print(lista_codigos)
