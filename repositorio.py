# repositorio.py

import sqlite3
from typing import List, Optional
from modelos import Produto  # Importa a classe do outro arquivo

DB_FILE = "loja.db"

class ProdutoRepository:
    """Classe responsável por todas as interações com a tabela de produtos."""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._criar_tabela()

    def _get_conexao(self):
        """Retorna uma conexão com o banco de dados."""
        return sqlite3.connect(self.db_path)

    def _criar_tabela(self):
        """Cria a tabela de produtos se não existir."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    preco REAL NOT NULL
                );
            """)
            conexao.commit()

    def salvar_produto(self, produto: Produto) -> Produto:
        """Salva um novo produto no banco."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO produtos (nome, tipo, preco) VALUES (?, ?, ?);",
                (produto.nome, produto.tipo, produto.preco)
            )
            produto.id = cursor.lastrowid
            conexao.commit()
            print(f"\n[SUCESSO] Produto '{produto.nome}' salvo com ID: {produto.id}")
            return produto

    def listar_todos(self) -> List[Produto]:
        """Busca todos os produtos e retorna uma lista de objetos."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, tipo, preco FROM produtos ORDER BY nome;")
            rows = cursor.fetchall()
            # Converte cada linha do resultado em um objeto Produto
            return [Produto(id=row[0], nome=row[1], tipo=row[2], preco=row[3]) for row in rows]

    def buscar_por_tipo(self, tipo: str) -> List[Produto]:
        """Busca produtos por tipo e retorna uma lista de objetos."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, tipo, preco FROM produtos WHERE tipo LIKE ?;", (f"%{tipo}%",))
            rows = cursor.fetchall()
            return [Produto(id=row[0], nome=row[1], tipo=row[2], preco=row[3]) for row in rows]

    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        """Busca um único produto pelo seu ID."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, tipo, preco FROM produtos WHERE id = ?;", (produto_id,))
            row = cursor.fetchone()
            if row:
                return Produto(id=row[0], nome=row[1], tipo=row[2], preco=row[3])
            return None

    def atualizar_descricao(self, produto_id: int, novo_nome: str) -> bool:
        """Altera o nome (descrição) de um produto pelo ID."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE produtos SET nome = ? WHERE id = ?;", (novo_nome, produto_id))
            conexao.commit()
            return cursor.rowcount > 0

    def deletar_por_id(self, produto_id: int) -> bool:
        """Exclui um produto pelo ID."""
        with self._get_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?;", (produto_id,))
            conexao.commit()
            return cursor.rowcount > 0