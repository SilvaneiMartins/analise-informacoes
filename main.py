import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()

# Define o título da janela
root.title("Minha Aplicação Desktop")

# Define o tamanho da janela (900x700)
root.geometry("1200x900")

# Torna a janela não redimensionável
root.resizable(False, False)

# Define a cor de fundo da janela
root.configure(bg='#CCCCCC')

# Cria um frame para o header
header_frame = tk.Frame(root, bg='#CCCCCC')
header_frame.pack(fill='x', pady=10)

# Cria um componente de seleção (select) no header
options = [
    "Desktop",
    "Notebook",
    "Rede Local", 
    "OS Macbook",
    "OS Windows",
    "Mobile iOS", 
    "Pesquiar Usb", 
    "Mobile Android",
]
select_box = ttk.Combobox(header_frame, values=options, width=40)
select_box.set("Selecione uma opção")
select_box.pack(side='left', padx=10, ipady=7)

# Cria um segundo componente de seleção relacionado ao primeiro
related_options = {
    "Desktop": ["Monitor", "Teclado", "Mouse",],
    "Notebook": ["Carregador", "Mouse Sem Fio", "Adaptador HDMI", "Informações do Notebook", "Portas USB"],
    "Rede Local": ["Roteador", "Switch", "Cabo Ethernet", "PC na Rede", "Traveco de Pacode"],
    "OS Macbook": ["Atualização de Sistema", "Configuração iCloud", "Assistência Técnica", "Senhas", "Falhas", "Desbloquear", "Descobrir Senha"],
    "OS Windows": ["Atualização de Sistema", "Instalação de Drivers", "Assistência Técnica", "Senhas", "Falhas", "Desbloquear", "Descobrir Senha"],
    "Mobile iOS": ["Carregador", "Fone de Ouvido", "Capa Protetora", "Portas Abertas", "Desbloquear", "Descobrir Senha"],
    "Pesquiar Usb": ["Pen Drive", "Qtde Dispositivo", "Pesquisar Informações", "Pesquisar Documentos"],
    "Mobile Android": ["Carregador", "Fone de Ouvido", "Capa Protetora", "Portas Abertas", "Desbloquear", "Descobrir Senha"],
}
related_select_box = ttk.Combobox(header_frame, width=40)
related_select_box.set("Selecione um serviço")
related_select_box.pack(side='left', padx=10, ipady=7)

# Atualiza o segundo select com base no primeiro
def update_related_options(event):
    selected_option = select_box.get()
    if selected_option in related_options:
        related_select_box['values'] = related_options[selected_option]
        related_select_box.set("Selecione um serviço")
    else:
        related_select_box['values'] = []
        related_select_box.set("")

select_box.bind("<<ComboboxSelected>>", update_related_options)

# Cria um botão para realizar a pesquisa
search_button = tk.Button(header_frame, text="Pesquisar", width=15, bd=0, relief='flat', bg='#FFFFFF', activebackground='#E0E0E0')
search_button.pack(side='left', padx=10, ipady=5)

# Adiciona o efeito de cursor pointer ao passar o mouse sobre o botão
def on_enter(e):
    search_button.config(cursor="hand2")

def on_leave(e):
    search_button.config(cursor="")

search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

# Executa o loop principal
root.mainloop()
