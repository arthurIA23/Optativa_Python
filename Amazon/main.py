
class Produto:
    def __init__(self, nome, preco, quantidade, codigo_produto, categoria):
        self.nome = nome
        self.preco =  preco
        self.quantidade = quantidade
        self.codigo_produto = codigo_produto
        self.categoria = categoria

    
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def get_quantidade(self):
        return self.quantidade

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

    def get_codigo_produto(self):
        return self.codigo_produto

    def set_codigo_produto(self, codigo_produto):
        self.codigo_produto = codigo_produto

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

class SistemaCadastro:
    def __init__(self):
        self.produtos = []

    def criarProduto(self, nome, preco, quantidade, codigo_produto, categoria):
        livro = Livro(titulo, autor, isbn, ano_publicacao, status)
        self.livros.append(livro)
    
    
