
class funcao:
    def __init__(self):
        pass

# analise de quantas pessoas do genero masculino e feminino se vacinaram.

    def genero_masclino_feminino():
        arquivo = open ( "entrada.txt" , "r" )
        linhas = arquivo.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)

        dados[0] = dados[0][0].replace("\n","")
        quantidade_pessoas = int (dados[0])
        feminino = int (0)
        for i in dados:
            if "f" in i:
                feminino1 = i.count("f")
                feminino = feminino + feminino1
                Porcentagem_feminino = ( feminino * 100 / quantidade_pessoas )
                Porcentagem_mascasculino = ( 100 - ( feminino * 100 / quantidade_pessoas ))
                resultado = f"Percetual de genero feminino {Porcentagem_feminino}%, genero masculino {Porcentagem_mascasculino}%"
        return resultado

# analise de quantas pessoas do genero masculino e feminino se vacinaram, separado por virgula.

    def genero_virgula():
        arq = open ( "entrada.txt" , "r" )
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)

        dados[0] = dados[0][0].replace("\n","")
        quantidade_pessoas = int (dados[0])
        feminino = int (0)
        for i in dados:
            if "f" in i:
                feminino1 = i.count("f")
                feminino = feminino + feminino1
        porcentagem_feminino = float ( feminino * 100 / quantidade_pessoas )
        porcentagem_masculino = float ( 100 - porcentagem_feminino )
        porcentagem_feminino = str (porcentagem_feminino).replace(".",",")
        porcentagem_masculino = str (porcentagem_masculino).replace(".",",")
        resultado = f" Publico feminino {porcentagem_feminino}%\n Publico masculino {porcentagem_masculino}%."
        return resultado

# Eficacia da vicina em jovem , adultos e idosos.

    def jovem_adulto_idoso():
        arq = open ( "entrada.txt" , "r" )
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)
        dados[0] = dados[0][0].replace("\n","")
        quatidade_pessoas = int (dados[0])
        jovem = 0
        adulto = 0
        idoso = 0
        for i in range( 1, quatidade_pessoas + 1, 1 ):
            idade = dados[i]
            valor = idade [1]
            if 0 < int ( valor ) <= 19:
                jovem += 1
            elif 20 < int ( valor ) <= 59:
                adulto += 1
            else:
                idoso += 1
        eficasGenero = []
        jovemA = 0
        adultoA = 0
        idosoA = 0
        for e in range ( 1 , quatidade_pessoas + 1, 1 ):
            nao = dados[e]
            eficasGenero1 = [nao[1], nao[3]]
            if eficasGenero1[1] == "n\n":
                eficasGenero.append(eficasGenero1[0])
        for a in eficasGenero:
            if 0 < int (a) <= 19:
                jovemA += 1
            elif 20 <= int (a) <= 59:
                adultoA += 1
            else:
                idosoA += 1
        resultado_Jovem = ( jovemA * 100 ) / jovem
        resultado_Adulto = ( adultoA * 100 ) / adulto
        resultado_Idoso = ( idosoA * 100 ) / idoso
        resultado = f" Eficácia da vacine em jovens {resultado_Jovem}%\n Eficácia da vacine em adultos {resultado_Adulto:.2f}%\n Eficácia da vacine em idosos {resultado_Idoso:.2f}%."
        return resultado

# Eficacia entre vacina e placebo.

    def eficacia_vacina():
        arq = open("entrada.txt", "r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)
        dados[0] = dados[0][0].replace("\n", "")
        quantidade_pessoas = int(dados[0])
        eficacia_vacina = 0
        eficacia_placebo = 0
        for i in range (1, quantidade_pessoas + 1 , 1):
            interador = dados[i]
            contraiu = [interador[2],interador[3]]
            if contraiu[0]== "p" and contraiu[1] == "s\n":
                eficacia_placebo += 1
            elif contraiu[0] == "v" and contraiu[1] == "s\n":
                eficacia_vacina += 1
        resultado_eficacia = 100 * ( eficacia_placebo - eficacia_vacina ) / eficacia_placebo
        resultado = f"A eficácia da vacina e de {resultado_eficacia}%"
        return resultado

    def eficacia_masculino_feminino():
        arq = open("entrada.txt", "r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)
        dados[0] = dados[0][0].replace("\n", "")
        quantidade_pessoas = int (dados[0])
        masculino_negativo = int (0)
        feminino_Negativo = int (0)
        for i in range (1, quantidade_pessoas + 1, 1):
            contraiu = dados[i]
            sim = contraiu[0] + contraiu[3]
            if sim == "m" + "n\n":
                masculino_negativo += 1
            elif sim == "f" + "n\n":
                feminino_Negativo += 1
        resultado_Feminino = ( feminino_Negativo * 100 / quantidade_pessoas )
        resultado_Masculino = (masculino_negativo * 100 / quantidade_pessoas )
        resultado = f"Eficacia no publico feminino { resultado_Feminino }%\nEficacia no publico masculino { resultado_Masculino }%."
        return resultado
