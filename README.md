# 🛍️ Sistema de Gerenciamento de Vendas CLI

Este é um projeto de console (CLI - Command-Line Interface) desenvolvido em Python para simular as operações básicas de um sistema de vendas, incluindo gerenciamento de produtos, um carrinho de compras e a finalização de pedidos.

O principal objetivo deste projeto é demonstrar a aplicação de conceitos fundamentais de **Programação Orientada a Objetos (OOP)**, com ênfase especial no princípio da **Composição**.

## ✨ Conceitos Principais Demonstrados

* **Programação Orientada a Objetos (OOP):** O código é estruturado em classes (`Produto`, `Carrinho`, `Pedido`, `ProdutoRepository`) que representam as entidades e responsabilidades do sistema.
* **Composição (`Tem-um`):** O conceito central do projeto.
    * A classe `Carrinho` **é composta por** uma lista de objetos `Produto`.
    * A classe `Pedido` **é composta por** uma lista de objetos `Produto`, representando os itens comprados.
* **Separação de Responsabilidades:** O projeto é dividido em camadas lógicas para maior organização e manutenibilidade:
    * **Modelos (`modelos.py`):** Define a estrutura dos dados (as classes `Produto`, `Carrinho`, `Pedido`).
    * **Repositório (`repositorio.py`):** Centraliza toda a lógica de acesso e persistência de dados, abstraindo a comunicação com o banco de dados.
    * **Interface/Lógica Principal (`main.py`):** Controla o fluxo da aplicação e a interação com o usuário.
* **Persistência de Dados:** Utiliza o banco de dados `SQLite` para armazenar, consultar e gerenciar os produtos de forma permanente.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Banco de Dados:** SQLite 3 (biblioteca padrão do Python)

## 📁 Estrutura do Projeto

```
gerenciador_itens/
│
├── .gitignore          # Arquivo para ignorar o banco de dados e cache do Python
├── modelos.py          # Contém as classes Produto, Carrinho e Pedido
├── repositorio.py      # Contém a classe ProdutoRepository para interagir com o DB
├── main.py             # Arquivo principal que executa a aplicação e o menu
└── loja.db             # (Será criado na primeira execução) Banco de dados SQLite
```

## 🚀 Como Executar

**Pré-requisitos:**
* Ter o [Python 3](https://www.python.org/downloads/) instalado.

**Passos:**
1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone URL_DO_SEU_REPOSITORIO.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd gerenciador_itens
    ```
3.  Execute o arquivo principal:
    ```bash
    python main.py
    ```
4.  O menu interativo será exibido no terminal e o arquivo `loja.db` será criado automaticamente.

## 📝 Exemplo de Uso (Roteiro)

Siga os passos abaixo para testar todas as funcionalidades do sistema:

1.  **Cadastrar Produtos:**
    * No menu principal, escolha `1. Gerenciar Produtos`.
    * Escolha `1. Inserir novo produto` e cadastre alguns itens (ex: Notebook, Mouse, Teclado).

2.  **Listar e Pesquisar:**
    * Ainda em "Gerenciar Produtos", use as opções `2. Listar todos` e `3. Pesquisar por tipo` para verificar se os produtos foram salvos corretamente.

3.  **Alterar e Excluir:**
    * Use as opções `4. Alterar descrição` e `5. Excluir produto por ID` para testar as operações de atualização e deleção.
    * Volte ao menu principal.

4.  **Montar o Carrinho:**
    * No menu principal, escolha `2. Adicionar produto ao carrinho`.
    * Informe o ID de produtos existentes para adicioná-los.
    * Escolha `3. Ver carrinho` para visualizar os itens e o total.

5.  **Finalizar o Pedido:**
    * Escolha `4. Finalizar Pedido`.
    * Um resumo da sua compra será exibido.
    * Após a finalização, verifique que o carrinho foi esvaziado automaticamente usando a opção `3. Ver carrinho` novamente.