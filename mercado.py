import customtkinter as ctk

proxima_linha = 4 # Começa na 4 porque as 0, 1, 2 e 3 já estao ocupadas
lista_de_widgets = []
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("600x600") # o tamanho da janela 
root.title("Minha Lista")

# --- FUNÇÕES ---
def acao_adicionar():
    global proxima_linha # Avisa que vamos mudar o valor da variável global
    
    nome = entrada_item.get()
    preco = entrada_preco.get()
    
    if nome != "" and preco != "":
        # Criando os 3 widgets da linha
        lbl_nome = ctk.CTkLabel(master=root, text=nome)
        lbl_preco = ctk.CTkLabel(master=root, text=f"R$ {preco}")
        check = ctk.CTkCheckBox(master=root, text="Comprado")
        
        # Posicionando cada um na sua coluna
        lbl_nome.grid(row=proxima_linha, column=0, pady=2)
        lbl_preco.grid(row=proxima_linha, column=1, pady=2)
        check.grid(row=proxima_linha, column=2, pady=2) # Você precisará de uma 3ª coluna
        
        # Guardamos a linha inteira em uma lista para remover depois
        item_completo = {"nome": lbl_nome, "preco": lbl_preco, "check": check}
        lista_de_widgets.append(item_completo)
        
        proxima_linha += 1 # Pula para a próxima linha para o próximo item
        
        # Limpa os campos
        entrada_item.delete(0, ctk.END)
        entrada_preco.delete(0, ctk.END)

def acao_remover():
    # isoo cria a lista ou sla tambem 
    itens_para_manter = []
    
    for item in lista_de_widgets:
        # Se o checkbox estiver marcado (valor 1)
        if item["check"].get() == 1:
            # Deleta os widgets da tela
            item["nome"].destroy()
            item["preco"].destroy()
            item["check"].destroy()
        else:
            # Se não estiver marcado, guardamos para continuar na lista
            itens_para_manter.append(item)
    
    # Atualizamos a lista global 
    lista_de_widgets[:] = itens_para_manter
# --- WIDGETS ---

# 1. Título 
label_titulo = ctk.CTkLabel(master=root, 
                            text="Lista de Compras",
                            font=ctk.CTkFont(size=40, weight="bold"))
label_titulo.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

# 2. Campo de Entrada
entrada_item = ctk.CTkEntry(master=root,
                            placeholder_text="Nome do item...",
                            width=300)
entrada_item.grid(row=1, column=0, columnspan=2, pady=10)

# No setor de WIDGETS
entrada_preco = ctk.CTkEntry(master=root, placeholder_text="Preço (R$)...", width=100)
entrada_preco.grid(row=1, column=1, pady=10, padx=10) # Colocando ao lado do nome
# 3. Botão Adicionar (Coluna 0)
btn_add = ctk.CTkButton(master=root, 
                        text="Adicionar", 
                        command=acao_adicionar)
btn_add.grid(row=2, column=0, padx=10, pady=10, sticky="ew") # sticky="ew" faz ele esticar

# 4. Botão Remover 
btn_del = ctk.CTkButton(master=root, 
                        text="Remover", 
                        fg_color="red",
                        hover_color="#990000",
                        command=acao_remover)
btn_del.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

root.mainloop()