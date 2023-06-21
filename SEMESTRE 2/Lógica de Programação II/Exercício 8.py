class TipoDocumento:
    numero_documento = 0
    codigo_cliente = 0
    dia_vencimento = 0
    dia_pagamento = 0
    valor = 0
    juros = 0


class TipoCliente:
    codigo = 0
    nome = ''
    telelfone = ''


def main():

    vetor_clientes = []
    vetor_documentos = []

    opcao = menu()
    while opcao < 1 or opcao > 11:
        print("Opção incorreta")
    while opcao != 11:
        if opcao == 1:
            cadastrar_cliente(vetor_clientes)
        elif opcao == 2:
            relatorio_clientes(vetor_clientes)
        elif opcao == 3:
            cadastrar_documento(vetor_clientes, vetor_documentos)
        elif opcao == 4:
            relatorio_documentos(vetor_documentos)
        elif opcao == 5:
            excluir_clientes_sem_documentos(vetor_clientes, vetor_documentos)
        elif opcao == 6:
            excluir_documento(vetor_documentos)
        elif opcao == 7:
            excluir_documentos_cliente(vetor_clientes, vetor_documentos)
        elif opcao == 8:
            excluir_documentos_periodo(vetor_documentos)
        elif opcao == 9:
            alterar_cliente(vetor_clientes)
        elif opcao == 10:
            total_documentos_cliente(vetor_clientes, vetor_documentos)

        opcao = menu()
        while (opcao < 1 or opcao > 11):
            print("Opção incorreta")


def menu():
    print('\nMenu do Sistema:')
    print('1. Cadastrar cliente')
    print('2. Relatório de clientes')
    print('3. Cadastrar documentos')
    print('4. Relatório de documentos')
    print('5. Excluir clientes sem documentos')
    print('6. Excluir documentos individuais pelo número')
    print('7. Excluir documentos por cliente')
    print('8. Excluir documentos por período')
    print('9. Alterar informações do cliente')
    print('10. Mostrar total de documentos do cliente')
    print('11. Sair')

    opcao = int(input('Digite sua opção: '))
    return opcao


def encontrar_cliente(vetor_clientes, codigo_cliente):
    for i in range(len(vetor_clientes)):
        if vetor_clientes[i].codigo == codigo_cliente:
            # aqui retorna o index do cliente encontrado dentro do vetor_clientes
            return i
    # retorna -1 se não encontrar o cliente
    return -1


def cadastrar_cliente(vetor_clientes):
    # verifica se já chegou no limite de clientes
    if len(vetor_clientes) < 15:
        codigo = int(input('Digite o código do cliente: '))
        # pesquisa o código do cliente no vetor usando a função encontrar_cliente para garantir que esse código não exista
        if encontrar_cliente(vetor_clientes, codigo) == -1:
            # inicializa a estrutura
            cliente_cadastro = TipoCliente()
            cliente_cadastro.codigo = codigo
            cliente_cadastro.nome = input('Digite o nome do cliente: ')
            cliente_cadastro.telefone = input('Digite o telefone do cliente: ')
            # anexa a estrutura TipoCliente criada e com os dados alocados ao fim do vetor_clientes
            vetor_clientes.append(cliente_cadastro)
            print('Cliente cadastrado com sucesso')
        else:
            # caso o código do cliente já exista
            print('Código de cliente já cadastrado')
    else:
        print("O sistema já possui 15 clientes cadastrados")


def relatorio_clientes(vetor_clientes):
    # verifica se há clientes cadastrados
    if len(vetor_clientes) > 0:
        # exibe um cabeçalho de dados
        print("Código  |  Nome  |  Telefone")
        # percorre todos os clientes do vetor
        for cliente in vetor_clientes:
            print(f"{cliente.codigo}  |  {cliente.nome}  |  {cliente.telefone}")
    else:
        print("Não há clientes cadastrados")


def cadastrar_documento(vetor_clientes, vetor_documentos):
    if len(vetor_documentos) < 30:
        codigo_cliente = int(input("Digite o código do cliente: "))
        # procura se existe um cliente cadastrado com o código informado
        index_cliente = encontrar_cliente(vetor_clientes, codigo_cliente)
        # se existir, ou seja, se não retornar -1
        if index_cliente >= 0:
            # inicializa a estrutura do tipo TipoDocumento
            documento_cadastro = TipoDocumento()
            # adiciona os dados
            documento_cadastro.codigo_cliente = codigo_cliente
            documento_cadastro.numero_documento = int(
                input("Digite o número do documento: "))
            documento_cadastro.valor = int(
                input("Digite o valor do documento: "))
            documento_cadastro.dia_vencimento = int(
                input("Digite o dia do vencimento: "))
            documento_cadastro.dia_pagamento = int(
                input("Digite o dia do pagamento: "))
            # confere se a data de vencimento é edpois da data de pagamento
            if documento_cadastro.dia_vencimento < documento_cadastro.dia_pagamento:
                # caso o dia do vencimento seja depois, calcula o juros e exibe ao usuário
                documento_cadastro.juros = documento_cadastro.valor * 0.05
                valor = documento_cadastro.valor + documento_cadastro.juros
                print(
                    f"Pagamento feito após o vencimento, haverá juros de R${documento_cadastro.juros:.2f} totalizando R${valor:.2f}")
            # caso não haja juros
            else:
                print(
                    f"Pagamento feito até o vencimento, não haverá juros e totalizará R${documento_cadastro.valor:.2f}")
                documento_cadastro.juros = 0
            # adiciona a estrutura montada ao vetor de documentos
            vetor_documentos.append(documento_cadastro)
        # caso não exista cliente com o código informado, ou seja, a função encontrar_cliente retorna None
        else:
            print("Código de cliente não encontrado")
    else:
        print("O sistema já passui 30 documentos cadastrados")


def relatorio_documentos(vetor_documentos):
    # verifica se há documentos cadastrados
    if len(vetor_documentos) > 0:
        # exibe um cabeçalho de dados
        print("Código Cliente  |  Número Documento  |  Vencimento  |  Pagamento  |  Valor  |  Juros  |  Valor Total")
        # percorre todos os documentos do vetor
        for documento in vetor_documentos:
            valor = documento.valor + documento.juros

            print(f"{documento.codigo_cliente}  |  {documento.numero_documento}  |  {documento.dia_vencimento}  |  {documento.dia_pagamento}  |  {documento.valor}  |  {documento.juros}  |  {valor}")
    else:
        print("Não há documentos cadastrados")


def encontra_documentos_cliente(vetor_documentos, codigo_cliente):
    # devolve uma lista (vetor) com todos os documentos de determinado cliente através do codigo
    documentos_cliente = []
    # percorre todo o vetor de documentos
    for documento in vetor_documentos:
        if documento.codigo_cliente == codigo_cliente:
            # caso o codigo do cliente seja igual, adicionan o documento na nova lista
            documentos_cliente.append(documento)
    return documentos_cliente


def excluir_clientes_sem_documentos(vetor_clientes, vetor_documentos):
    # faz um for inverso, começando do último cliente cadastrado para o primeiro, diminuindo o índice de 1 em 1\
    ultimo_index = len(vetor_clientes)-1
    for i in range(ultimo_index, -1, -1):
        if len(encontra_documentos_cliente(vetor_documentos, vetor_clientes[i].codigo)) == 0:
            vetor_clientes.pop(i)
    print("Clientes removidos")


def encontrar_documento_numero(vetor_documentos, numero):
    # percorre todos os documentos
    for i in range(len(vetor_documentos)):
        if (vetor_documentos[i].numero_documento == numero):
            # se encontrar o documento com esse numero, retorna o índice desse documento no vetor
            return i
    # se não encontrar retorna -1
    return -1


def excluir_documento(vetor_documentos):
    numero = int(input("Digite o numero do documento à ser excluido: "))
    # usa a função encontrar_documento_numero pra procurar o indice do documento
    indice = encontrar_documento_numero(vetor_documentos, numero)
    # verifica se o documento foi encontrado (quando a função encontrar_documento_numero um indice)
    if indice > -1:
        # se encontrado, exclui o documento
        vetor_documentos.pop(indice)
        print("Documento removido")
    else:
        print("Documento não encontrado")


def excluir_documentos_cliente(vetor_clientes, vetor_documentos):
    codigo_cliente = int(input("Digite o código do cliente: "))
    # usa a função encontrar_documentos_cliente pra procurar os documentos de um cliente
    documentos_cliente = encontra_documentos_cliente(
        vetor_documentos, codigo_cliente)
    # verifica se foi encontrado algum documento cadastrado no código desse cliente
    if len(documentos_cliente) > 0:
        # percorre todos os elementos do vetor que contém os documentos do cliente, e remove cada um desses elementos do vetor principal de documentos
        for documento in documentos_cliente:
            vetor_documentos.remove(documento)
        print("Documentos removidos")
    else:
        print("Nenhum documento encontrado")


def excluir_documentos_periodo(vetor_documentos):
    dia_inicial = int(input("Digite o dia inicial: "))
    dia_final = int(input("Digite o dia final: "))
    # faz um for inverso, começando do último documento cadastrado para o primeiro, diminuindo o índice de 1 em 1\
    ultimo_indice = len(vetor_documentos) - 1
    for i in range(ultimo_indice, -1, -1):
        # caso o vencimento se encontre entre o dia inicial e o dia final
        if vetor_documentos[i].dia_vencimento >= dia_inicial and vetor_documentos[i].dia_vencimento <= dia_final:
            vetor_documentos.pop(i)
    print("Documentos removidos")


def alterar_cliente(vetor_clientes):
    # confere se existem clientes cadastrados
    if len(vetor_clientes) > 0:
        codigo = int(input("Digite o código do cliente: "))
        # busca o cliente usando a função encontrar_cliente
        index_cliente = encontrar_cliente(vetor_clientes, codigo)
        # confere se foi encontrado algum cliente, a função retorna um índice ou -1 caso não seja encontrado
        if index_cliente >= 0:
            # altera os dados do cliente diretamente no vetor através do index
            vetor_clientes[index_cliente].nome = input(
                "Digite o novo nome do cliente: ")
            vetor_clientes[index_cliente].telefone = input(
                "Digite o novo telefone do cliente: ")
            print("Cliente alterado")
        else:
            print("Cliente não encontrado")
    else:
        print("Não há clientes cadastrados")


def total_documentos_cliente(vetor_clientes, vetor_documentos):
    # confere se existem clientes cadastrados
    if len(vetor_clientes) > 0:
        codigo = int(input("Digite o código do cliente: "))
        # verifica se o cliente existe
        if (encontrar_cliente(vetor_clientes, codigo) >= 0):
            # busca a lista de documentos cadastrados desse cliente
            documentos_cliente = encontra_documentos_cliente(
                vetor_documentos, codigo)
            # exibe o tamanho dessa lista, ou seja, quantos documentos foram encontrados desse cliente
            print(
                f"O cliente tem {len(documentos_cliente)} documentos cadastrados")
        else:
            print("Código de cliente não encontrado")
    else:
        print("Não há clientes cadastrados")


main()
