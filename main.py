from modelos import Produto, Carrinho, Pedido
from repositorio import ProdutoRepository, DB_FILE

# -------------------------------------------
# LÓGICA PRINCIPAL (INTERFACE COM O USUÁRIO)
# -------------------------------------------

def gerenciar_produtos(repo: ProdutoRepository):
    """Sub-menu para operações CRUD de produtos."""
    while True:
        print("\n--- Gerenciar Produtos ---")
        print("1. Inserir novo produto")
        print("2. Listar todos os produtos")
        print("3. Pesquisar produto por tipo")
        print("4. Alterar descrição do produto")
        print("5. Excluir produto por ID")
        print("6. Voltar ao menu principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do produto: ")
            tipo = input("Digite o tipo (ex: Eletrônico, Roupa, Alimento): ")
            try:
                preco = float(input("Digite o preço: "))
                repo.salvar_produto(Produto(nome=nome, tipo=tipo, preco=preco))
            except ValueError:
                print("\n[ERRO] Preço inválido. Use ponto como separador decimal (ex: 49.99).")
        
        elif escolha == '2':
            produtos = repo.listar_todos()
            print("\n--- Lista de Produtos Cadastrados ---")
            if not produtos: print("Nenhum produto cadastrado.")
            for p in produtos: print(p)

        elif escolha == '3':
            tipo = input("Digite o tipo a ser pesquisado: ")
            produtos = repo.buscar_por_tipo(tipo)
            print(f"\n--- Produtos do tipo '{tipo}' ---")
            if not produtos: print("Nenhum produto encontrado com este tipo.")
            for p in produtos: print(p)

        elif escolha == '4':
            try:
                produto_id = int(input("Digite o ID do produto para alterar: "))
                novo_nome = input("Digite a nova descrição (nome): ")
                if repo.atualizar_descricao(produto_id, novo_nome):
                    print("\n[SUCESSO] Produto atualizado.")
                else:
                    print(f"\n[ERRO] Produto com ID {produto_id} não encontrado.")
            except ValueError:
                print("\n[ERRO] ID inválido. Digite um número.")

        elif escolha == '5':
            try:
                produto_id = int(input("Digite o ID do produto para excluir: "))
                if repo.deletar_por_id(produto_id):
                    print("\n[SUCESSO] Produto excluído.")
                else:
                    print(f"\n[ERRO] Produto com ID {produto_id} não encontrado.")
            except ValueError:
                print("\n[ERRO] ID inválido. Digite um número.")
        
        elif escolha == '6':
            break
        else:
            print("\n[ERRO] Opção inválida.")


def main():
    # Instancia o repositório, que cuidará da lógica de banco de dados
    repo = ProdutoRepository(DB_FILE)
    # Instancia o carrinho de compras, que viverá durante a execução do programa
    carrinho = Carrinho()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Ver carrinho")
        print("4. Finalizar Pedido")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            gerenciar_produtos(repo)
        
        elif escolha == '2':
            try:
                produto_id = int(input("Digite o ID do produto para adicionar ao carrinho: "))
                produto_encontrado = repo.buscar_por_id(produto_id)
                if produto_encontrado:
                    carrinho.adicionar_item(produto_encontrado)
                else:
                    print(f"\n[ERRO] Produto com ID {produto_id} não encontrado.")
            except ValueError:
                print("\n[ERRO] ID inválido. Digite um número.")

        elif escolha == '3':
            carrinho.mostrar_itens()

        elif escolha == '4':
            if not carrinho.itens:
                print("\n[ERRO] O carrinho está vazio. Adicione itens antes de finalizar.")
            else:
                # Cria o objeto Pedido a partir do carrinho atual
                novo_pedido = Pedido(carrinho)
                novo_pedido.mostrar_resumo()
                # Limpa o carrinho para uma nova compra
                carrinho = Carrinho()
                print("\nCarrinho esvaziado, pronto para uma nova compra!")
        
        elif escolha == '5':
            break
        
        else:
            print("\n[ERRO] Opção inválida.")
            
    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()