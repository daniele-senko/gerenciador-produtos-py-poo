from typing import List, Optional

# -------------------------------------------
# 1. CLASSES DE MODELO (OS OBJETOS)
# -------------------------------------------

class Produto:
    """Representa um produto no sistema."""
    def __init__(self, nome: str, tipo: str, preco: float, id: Optional[int] = None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def __repr__(self):
        """Representação em string do objeto, útil para debug e listagem."""
        return f"ID: {self.id} | Nome: {self.nome} | Tipo: {self.tipo} | Preço: R${self.preco:.2f}"

class Carrinho:
    """Representa o carrinho de compras, que é COMPOSTO por Produtos."""
    def __init__(self):
        # A composição acontece aqui: o Carrinho TEM UMA lista de Produtos.
        self.itens: List[Produto] = []

    def adicionar_item(self, produto: Produto):
        """Adiciona um objeto Produto à lista de itens do carrinho."""
        self.itens.append(produto)
        print(f"\n[CARRINHO] Produto '{produto.nome}' adicionado ao carrinho.")

    def calcular_total(self) -> float:
        """Calcula o valor total dos itens no carrinho."""
        total = sum(produto.preco for produto in self.itens)
        return total
        
    def mostrar_itens(self):
        """Mostra os itens atualmente no carrinho."""
        print("\n--- Itens no Carrinho ---")
        if not self.itens:
            print("O carrinho está vazio.")
        else:
            for item in self.itens:
                print(f"- {item}") # Usa o __repr__ do Produto
        print(f"-------------------------\nTotal: R${self.calcular_total():.2f}")


class Pedido:
    """Representa um pedido finalizado, que também é COMPOSTO por Produtos."""
    def __init__(self, carrinho: Carrinho):
        # A composição acontece aqui também.
        # Copiamos os itens do carrinho para "congelar" o estado do pedido.
        self.itens_comprados: List[Produto] = list(carrinho.itens)
        self.valor_total = carrinho.calcular_total()
        
    def mostrar_resumo(self):
        """Mostra o resumo do pedido que foi finalizado."""
        print("\n" + "="*30)
        print("    PEDIDO FINALIZADO COM SUCESSO!")
        print("="*30)
        print("Itens Comprados:")
        for item in self.itens_comprados:
            print(f"- {item}")
        print("-" * 30)
        print(f"VALOR TOTAL: R${self.valor_total:.2f}")
        print("="*30)