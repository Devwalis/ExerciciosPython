from classes.Produto import Produto
from classes.Categoria import Categoria

item = 1
itemAlterar = Produto.consultar(item)



Produto.consultar()
itemAlterar = Produto.consulta(1)
print(itemAlterar['quantidade'])

produto = Produto[itemAlterar['codigo'], itemAlterar['nome'], 60, 4000)
print(produto.detalhar())



categoria = Categoria('Eletrônicos')
categoria.inserir()



#produto = Produto('001', 'Mouse', 2000, 35)
#produto.inserir()
#produto.listarTodos()


