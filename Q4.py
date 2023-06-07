class Livro:
    def __init__(self, titulo, qtdPaginas, paginasLidas):
        self.titulo = titulo
        self.qtdPaginas = qtdPaginas
        self.paginasLidas = paginasLidas
    
    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo
        
    def getQtdPaginas(self):
        return self.qtdPaginas
    
    def setQtdPaginas(self, qtdPaginas):
        self.qtdPaginas = qtdPaginas
    
    def getPaginasLidas(self):
        return self.paginasLidas
    
    def setPaginasLidas(self, paginasLidas):
        self.paginasLidas = paginasLidas
    
    def verificarProgresso(self):
        print(f'O livro {self.titulo} contém {self.qtdPaginas} páginas e você já leu {self.paginasLidas} páginas')
    

livro1 = Livro('a turma da monica', 30, 10)
livro1.setQtdPaginas(50)
print(livro1.getQtdPaginas())
livro1.verificarProgresso()