import tkinter as tk
from tkinter import font, ttk, scrolledtext

COMBINACOES_SEGUROS = {
    frozenset({'Água Sanitária', 'Vinagre'}): False,
    frozenset({'Água Sanitária', 'Detergente'}): True,
    frozenset({'Vinagre', 'Detergente'}): True,
    frozenset({'Água Sanitária', 'Álcool'}): False,
    frozenset({'Vinagre', 'Álcool'}): True,
    frozenset({'Detergente', 'Álcool'}): True,
    frozenset({'Água Sanitária', 'Sabão Líquido'}): True,
    frozenset({'Vinagre', 'Sabão Líquido'}): True,
    frozenset({'Detergente', 'Sabão Líquido'}): True,
    frozenset({'Água Sanitária', 'Desinfetante'}): True,
    frozenset({'Vinagre', 'Desinfetante'}): False,
    frozenset({'Detergente', 'Desinfetante'}): True,
    frozenset({'Água Sanitária', 'Polidor'}): True,
    frozenset({'Vinagre', 'Polidor'}): False,
    frozenset({'Detergente', 'Polidor'}): True,
    frozenset({'Água Sanitária', 'Lustra Móveis'}): True,
    frozenset({'Vinagre', 'Lustra Móveis'}): False,
    frozenset({'Detergente', 'Lustra Móveis'}): True,
    frozenset({'Água Sanitária', 'Limpa Vidros'}): True,
    frozenset({'Vinagre', 'Limpa Vidros'}): True,
    frozenset({'Detergente', 'Limpa Vidros'}): True,
    frozenset({'Água Sanitária', 'Desengordurante'}): True,
    frozenset({'Vinagre', 'Desengordurante'}): True,
    frozenset({'Detergente', 'Desengordurante'}): True,
}

EXPLICACOES = {
    frozenset({'Água Sanitária', 'Vinagre'}): "A combinação de Água Sanitária e Vinagre produz gás cloro, que é tóxico.",
    frozenset({'Água Sanitária', 'Detergente'}): "A combinação de Água Sanitária e Detergente é segura e pode ajudar na limpeza.",
    frozenset({'Vinagre', 'Detergente'}): "A combinação de Vinagre e Detergente é segura e eficiente para limpeza.",
    frozenset({'Água Sanitária', 'Álcool'}): "A combinação de Água Sanitária e Álcool pode produzir vapores tóxicos.",
    frozenset({'Vinagre', 'Álcool'}): "A combinação de Vinagre e Álcool é segura e útil para limpeza.",
    frozenset({'Detergente', 'Álcool'}): "A combinação de Detergente e Álcool é segura e pode ser eficaz na limpeza.",
    frozenset({'Água Sanitária', 'Sabão Líquido'}): "A combinação de Água Sanitária e Sabão Líquido é segura e comum na limpeza.",
    frozenset({'Vinagre', 'Sabão Líquido'}): "A combinação de Vinagre e Sabão Líquido é segura e eficaz para limpeza.",
    frozenset({'Detergente', 'Sabão Líquido'}): "A combinação de Detergente e Sabão Líquido é segura e muito utilizada para limpeza.",
    frozenset({'Água Sanitária', 'Desinfetante'}): "A combinação de Água Sanitária e Desinfetante é segura e potente para desinfecção.",
    frozenset({'Vinagre', 'Desinfetante'}): "A combinação de Vinagre e Desinfetante pode ser perigosa e liberar vapores tóxicos.",
    frozenset({'Detergente', 'Desinfetante'}): "A combinação de Detergente e Desinfetante é segura e eficaz.",
    frozenset({'Água Sanitária', 'Polidor'}): "A combinação de Água Sanitária e Polidor é segura e pode ser útil para limpeza.",
    frozenset({'Vinagre', 'Polidor'}): "A combinação de Vinagre e Polidor pode ser perigosa e liberar vapores tóxicos.",
    frozenset({'Detergente', 'Polidor'}): "A combinação de Detergente e Polidor é segura e eficiente para limpeza.",
    frozenset({'Água Sanitária', 'Lustra Móveis'}): "A combinação de Água Sanitária e Lustra Móveis é segura e pode ser eficaz na limpeza de móveis.",
    frozenset({'Vinagre', 'Lustra Móveis'}): "A combinação de Vinagre e Lustra Móveis pode liberar vapores tóxicos e deve ser evitada.",
    frozenset({'Detergente', 'Lustra Móveis'}): "A combinação de Detergente e Lustra Móveis é segura e eficiente para limpeza de móveis.",
    frozenset({'Água Sanitária', 'Limpa Vidros'}): "A combinação de Água Sanitária e Limpa Vidros é segura e pode ajudar na limpeza de vidros.",
    frozenset({'Vinagre', 'Limpa Vidros'}): "A combinação de Vinagre e Limpa Vidros é segura e eficiente para limpeza de vidros.",
    frozenset({'Detergente', 'Limpa Vidros'}): "A combinação de Detergente e Limpa Vidros é segura e útil na limpeza de vidros.",
    frozenset({'Água Sanitária', 'Desengordurante'}): "A combinação de Água Sanitária e Desengordurante é segura e eficaz para remover gordura.",
    frozenset({'Vinagre', 'Desengordurante'}): "A combinação de Vinagre e Desengordurante é segura e útil para remover gordura.",
    frozenset({'Detergente', 'Desengordurante'}): "A combinação de Detergente e Desengordurante é segura e eficaz na remoção de gordura.",
}

class VerificadorDeMisturaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Mistura de Produtos de Limpeza")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.produtos = [
            'Água Sanitária', 'Vinagre', 'Detergente', 'Álcool', 'Sabão Líquido', 
            'Desinfetante', 'Polidor', 'Lustra Móveis', 'Limpa Vidros', 'Desengordurante'
        ]

        self.criar_widgets()

    def criar_widgets(self):
        self.titulo_font = font.Font(family='Helvetica', size=18, weight='bold')
        self.label_font = font.Font(family='Helvetica', size=14)
        self.button_font = font.Font(family='Helvetica', size=12, weight='bold')
        self.combo_font = font.Font(family='Helvetica', size=12)

        self.instrucao = tk.Label(self.root, text="Selecione dois produtos de limpeza:", font=self.titulo_font)
        self.instrucao.pack(pady=20)

        self.combobox_frame = tk.Frame(self.root)
        self.combobox_frame.pack(pady=10)

        self.produto1_var = tk.StringVar(value=self.produtos[0])
        self.produto1_menu = ttk.Combobox(
            self.combobox_frame, textvariable=self.produto1_var, values=self.produtos, state='readonly', 
            font=self.combo_font, width=25
        )
        self.produto1_menu.grid(row=0, column=0, padx=10)

        self.produto2_var = tk.StringVar(value=self.produtos[1])
        self.produto2_menu = ttk.Combobox(
            self.combobox_frame, textvariable=self.produto2_var, values=self.produtos, state='readonly', 
            font=self.combo_font, width=25
        )
        self.produto2_menu.grid(row=0, column=1, padx=10)

        self.verificar_button = tk.Button(self.root, text="Verificar Mistura", command=self.verificar_mistura, bg='blue', fg='white', font=self.button_font, relief='raised', borderwidth=3)
        self.verificar_button.pack(pady=20)

    def verificar_mistura(self):
        produto1 = self.produto1_var.get()
        produto2 = self.produto2_var.get()

        if produto1 == produto2:
            segura = True
            explicacao = "A mistura de um produto com ele mesmo é sempre segura."
        else:
            combinacao = frozenset([produto1, produto2])
            segura = COMBINACOES_SEGUROS.get(combinacao, True)
            if combinacao in EXPLICACOES:
                explicacao = EXPLICACOES[combinacao]
            else:
                if segura:
                    explicacao = "Esta mistura é considerada segura. No entanto, recomenda-se sempre testar em uma pequena área antes de usar em grandes superfícies."
                else:
                    explicacao = "Esta mistura é considerada perigosa. Não a utilize sob hipótese nenhuma, sob risco à sua saúde e a de sua família."

        self.criar_janela_resultado(segura, explicacao)

    def criar_janela_resultado(self, segura, explicacao):
        resultado_janela = tk.Toplevel(self.root)
        resultado_janela.title("Resultado")
        resultado_janela.geometry("600x400")
        resultado_janela.resizable(False, False)

        resultado_janela.config(bg='#f0f0f0')

        resultado_label = tk.Label(resultado_janela, text="Resultado da Mistura", font=self.titulo_font, bg='#f0f0f0')
        resultado_label.pack(pady=10)

        if segura:
            mensagem = "A mistura é segura."
            cor = '#66ff66'
        else:
            mensagem = "A mistura NÃO é segura."
            cor = '#ff6666'
        
        resultado_msg = tk.Label(resultado_janela, text=mensagem, font=self.label_font, bg=cor, fg='black', padx=10, pady=10, wraplength=580, relief='flat')
        resultado_msg.pack(pady=10, fill=tk.X, padx=20)

        explicacao_text = scrolledtext.ScrolledText(resultado_janela, wrap=tk.WORD, height=8, width=70, font=self.label_font, bg='#f9f9f9', fg='black', borderwidth=2, relief='sunken')
        explicacao_text.insert(tk.END, explicacao)
        explicacao_text.configure(state='disabled')
        explicacao_text.pack(pady=10, padx=20)

        ok_button = tk.Button(resultado_janela, text="OK", command=resultado_janela.destroy, bg='blue', fg='white', font=self.button_font, relief='raised', borderwidth=3)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = VerificadorDeMisturaApp(root)
    root.mainloop()
