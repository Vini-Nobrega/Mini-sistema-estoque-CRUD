from functions import adicionar_produto, listar_prod, remover_produto, valida_codigo_exiteste, listar_codigos, estoque_baixo, buscar_produto_por_codigo

opcoes = [
    'Cadastrar produto',
    'Listar produtos',
    'Buscar produto por código',
    'Atualizar produto',
    'Remover produto',
    'Relatório de estoque baixo',
    'Sair'
]

lista_produtos = [
    {'Código': 1, 'Nome': 'Iphone 11', 'Preço': 2500.23, 'Quantidade em estoque': 10},
    {'Código': 2, 'Nome': 'Mouse Logitech g300s', 'Preço': 380, 'Quantidade em estoque': 21},
    {'Código': 3, 'Nome': 'Luminária Branca', 'Preço': 143, 'Quantidade em estoque': 3},
    {'Código': 4, 'Nome': 'Caneca personalizada', 'Preço': 54, 'Quantidade em estoque': 15},
    {'Código': 5, 'Nome': 'Mouse Pad', 'Preço': 120, 'Quantidade em estoque': 1},
    {'Código': 6, 'Nome': 'Air Force - Nike', 'Preço': 222.90, 'Quantidade em estoque': 2},
    {'Código': 7, 'Nome': 'Teclado Monsgeek', 'Preço': 139.90, 'Quantidade em estoque': 1},
    {'Código': 8, 'Nome': 'Monitor Samsung', 'Preço': 549.50, 'Quantidade em estoque': 8},
    {'Código': 9, 'Nome': 'Gabinete Gamer com Led', 'Preço': 142.85, 'Quantidade em estoque': 0},
    {'Código': 10, 'Nome': 'Placa de Vídeo GTX 1660 Super', 'Preço': 2457.33, 'Quantidade em estoque': 17}
]

selecionado = ''

while True:
    
    print('\nOpções:\n')

    for o in opcoes:
        print(f'{o}')
    
    selecionado = input('\nDigite uma opção: ').lower()

    if selecionado == 'cadastrar produto':
        print('Você escolheu Cadastrar Produto\n')

        codigo = int(input('Digite o código do produto: '))

        while valida_codigo_exiteste(lista_produtos, codigo):
            print('Esse código já existe. Digite outro.')
            codigo = int(input('Digite o código do produto: '))

        nome_criar_prod = input('Nome do produto: ')
        preco_criar_prod = float(input('Preço do produto: '))
        quantidade_criar_prod = int(input('Quantidade disponível: '))

        adicionar_produto(
            lista_produtos,
            codigo=codigo,
            nome=nome_criar_prod,
            preco=preco_criar_prod,
            quantidade=quantidade_criar_prod
        )

        print('Produto cadastrado com sucesso!')

    elif selecionado == 'listar produtos':
        print(f'Você escolheu Listar produtos\nExibindo a lista atual:\n')

        listar_prod(lista_produtos)

        print('\nVoltando para o menu de opções')

    elif selecionado == 'buscar produto por código':
        print('Você escolheu Buscar produto por código. Exibindo os códigos existentes:\n')

        listar_codigos(lista_produtos)
            
        v_codigo_desejado = int(input('\nDigite o código do produto que está procurando:\n'))
        
        produto_encontrado = buscar_produto_por_codigo(lista_produtos, v_codigo_desejado)

        if produto_encontrado is not None:
            print(f'\nProduto encontrado: {produto_encontrado}\nVoltando ao menu inicial...')
        else:
            print('\nProduto não encontrado. Voltando ao menu inicial...')

    elif selecionado == 'atualizar produto':
       
        print('Você escolheu Atualizar produto.\n')

        print('\nAbaixo a lista dos itens:\n')
        
        listar_prod(lista_produtos)

        v_codigo_desejado = int(input('\nDigite o código do produto que deseja atualizar: '))

        produto_select = buscar_produto_por_codigo(lista_produtos, v_codigo_desejado)

        if produto_select is None:
            print('\nProduto não encontrado. Voltando ao menu inicial...')
            continue

        print(f'\nProduto encontrado: {produto_select}\n.')

        opcoes_para_atualiar = [
            '1 - Código', 
            '2 - Nome',
            '3 - Preço',
            '4 - Quantidade',
            '5 - Tudo',
            '6 - Sair'
        ]
        
        print(f'Essas são as opções:\n')
        
        for opcoes_de_atualizacao in opcoes_para_atualiar:
            print(f'{opcoes_de_atualizacao}\n')

        deseja_atualizar_o_que = int(input('Digite o número do que deseja atualizar: '))

        while deseja_atualizar_o_que < 1 or deseja_atualizar_o_que > 6:
            deseja_atualizar_o_que = int(input('Por favor, digite apenas os números mostrados anteriormente: '))

        if deseja_atualizar_o_que == 1:
            novo_codigo = int(input('Digite o novo código: '))

            while novo_codigo != produto_select['Código'] and valida_codigo_exiteste(lista_produtos, novo_codigo):
                print('Esse código já existe. Digite outro.')
                novo_codigo = int(input('Digite o novo código: '))

            produto_select['Código'] = novo_codigo

        elif deseja_atualizar_o_que == 2:
            novo_nome = input('Digite o novo nome: ')
            produto_select['Nome'] = novo_nome

        elif deseja_atualizar_o_que == 3:
            novo_preco = float(input('Digite o novo preço: '))
            produto_select['Preço'] = novo_preco

        elif deseja_atualizar_o_que == 4:
            nova_quantidade = int(input('Digite a nova quantidade: '))
            produto_select['Quantidade em estoque'] = nova_quantidade

        elif deseja_atualizar_o_que == 5:
            novo_codigo = int(input('Digite o novo código: '))

            while novo_codigo != produto_select['Código'] and valida_codigo_exiteste(lista_produtos, novo_codigo):
                print('Esse código já existe. Digite outro.')
                novo_codigo = int(input('Digite o novo código: '))

            novo_nome = input('Digite o novo nome: ')
            novo_preco = float(input('Digite o novo preço: '))
            nova_quantidade = int(input('Digite a nova quantidade: '))

            produto_select['Código'] = novo_codigo
            produto_select['Nome'] = novo_nome
            produto_select['Preço'] = novo_preco
            produto_select['Quantidade em estoque'] = nova_quantidade

        elif deseja_atualizar_o_que == 6:
            print('Saindo...')
            continue

        print('Produto atualizado com sucesso:\n')
        listar_prod(lista_produtos)
        print('\nVoltando para o menu.')

    elif selecionado == 'remover produto':
        print('Você escolheu Remover produto\n')

        codigo = int(input('Digite o código do produto que deseja remover: '))

        removido = remover_produto(lista_produtos, codigo)

        if removido:
            print('Produto removido!')
        else:
            print('Produto não encontrado.')

    elif selecionado == 'relatório de estoque baixo':
        
        print('Você escolheu Relatório de estoque baixo\n')
        
        estoque = estoque_baixo(lista_produtos)

        if not estoque:
            print('Nenhum produto com o estoque baixo!')

    elif selecionado == 'sair':
        print('Saindo...')
        break
    
    else:
        print('Digite uma opção válida, por favor.')