def adicionar_produto(lista_produtos, codigo, nome, preco, quantidade):
    novo_produto = {
        'Código': codigo,
        'Nome': nome,
        'Preço': preco,
        'Quantidade em estoque': quantidade
    }

    lista_produtos.append(novo_produto)


def valida_codigo_exiteste(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto['Código'] == codigo:
            return True
    
    return False


def buscar_produto_por_codigo(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto['Código'] == codigo:
            return produto
    
    return None


def listar_prod(lista_produtos):
    for lista_percorrida in lista_produtos:
        print(lista_percorrida)


def remover_produto(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto['Código'] == codigo:
            lista_produtos.remove(produto)
            return True
    
    return False


def listar_codigos(lista_produtos):
    for produto in lista_produtos:
        print(produto['Código'])


def estoque_baixo(lista_produtos):
    encontrou = False

    print('Produtos que estão com estoque abaixo de 5 unidades:\n')

    for produto in lista_produtos:
        quantidade = produto['Quantidade em estoque']

        if quantidade < 5:
            print(produto)
            encontrou = True

    return encontrou