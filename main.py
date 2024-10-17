import tkinter as tk
from tkinter import ttk
import os
import platform

# Cria a janela principal
root = tk.Tk()

# Define o título da janela
root.title("Analise de Sistemas")

# Define o tamanho da janela (1200x900)
root.geometry("1400x900")

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
    "Desktop": ["Monitor", "Teclado", "Mouse"],
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

# Função para realizar a pesquisa e análise
def realizar_pesquisa():
    selected_option = select_box.get()
    selected_service = related_select_box.get()
    if selected_option == "Notebook" and selected_service == "Portas USB":
        # Realiza uma análise do sistema para obter informações sobre as portas USB
        usb_info = "\n".join(os.popen("lsusb" if platform.system() == "Linux" else "systeminfo").readlines())
        textarea.delete(1.0, tk.END)
        textarea.insert(tk.END, f"Resultado da Análise para {selected_service}:\n{usb_info}")
    else:
        textarea.delete(1.0, tk.END)
        textarea.insert(tk.END, "Selecione 'Notebook' e 'Portas USB' para realizar uma análise.")
    update_clear_button_state()

# Função para limpar o textarea
def limpar_textarea():
    textarea.delete(1.0, tk.END)
    update_clear_button_state()

# Atualiza o estado do botão de limpar
def update_clear_button_state():
    if textarea.get(1.0, tk.END).strip():
        clear_button.config(state=tk.NORMAL)
    else:
        clear_button.config(state=tk.DISABLED)

# Cria um botão para realizar a pesquisa
search_button = tk.Button(header_frame, text="Pesquisar", width=15, bd=0, relief='flat', bg='#FFFFFF', activebackground='#E0E0E0', command=realizar_pesquisa)
search_button.pack(side='left', padx=10, ipady=5)

# Cria um botão para limpar o textarea
clear_button = tk.Button(header_frame, text="Limpar", width=15, bd=0, relief='flat', bg='#FFFFFF', activebackground='#E0E0E0', command=limpar_textarea, state=tk.DISABLED)
clear_button.pack(side='right', padx=10, ipady=5)

# Adiciona o efeito de cursor pointer ao passar o mouse sobre os botões
def on_enter(e):
    e.widget.config(cursor="hand2")

def on_leave(e):
    e.widget.config(cursor="")

search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)
clear_button.bind("<Enter>", on_enter)
clear_button.bind("<Leave>", on_leave)

# Cria um campo de texto (textarea) abaixo do header
textarea = tk.Text(root, width=100, height=20, bd=0, relief='solid', font=('JetBrains Mono', 16))
textarea.pack(pady=10, padx=10, fill='both', expand=True)

# Executa o loop principal
root.mainloop()
