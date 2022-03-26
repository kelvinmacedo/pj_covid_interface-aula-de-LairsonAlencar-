
class funcao:
    def __init__(self):
        pass

# analise de quantas pessoas do genero masculino e feminino se vacinaram.

    def genero_m_f():
        arq = open("entrada.txt","r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)

        dados[0] = dados[0][0].replace("\n","")
        div = int(dados[0])
        fem = int(0)
        for i in dados:
            if "f" in i:
                fem1 = i.count("f")
                fem = fem + fem1
                Porc_fem = (fem*100/div)
                Porc_masc = (100-(fem*100/div))
                resultado = f"Percetual de genero feminino {Porc_fem}%, genero masculino {Porc_masc}%"
        return resultado

# analise de quantas pessoas do genero masculino e feminino se vacinaram, separado por virgula.

    def genero_virgula():
        arq = open("entrada.txt","r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)

        dados[0] = dados[0][0].replace("\n","")
        div = int(dados[0])
        fem = int(0)
        for i in dados:
            if "f" in i:
                fem1 = i.count("f")
                fem = fem + fem1
        res = float(fem*100/div)
        res1 = float(100-res)
        res = str (res).replace(".",",")
        res1 = str (res1).replace(".",",")
        resultado = f" Publico feminino {res}%\n Publico masculino {res1}%."
        return resultado

# Eficacia da vicina em jovem , adultos e idosos.

    def jovem_adulto_idoso():
        arq = open("entrada.txt","r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)
        dados[0] = dados[0][0].replace("\n","")
        div = int(dados[0])
        jovem = 0
        adulto = 0
        idoso = 0
        for i in range(1, div + 1,1):
            idade = dados[i]
            valor = idade [1]
            if 0 < int(valor) <= 19:
                jovem += 1
            elif 20 < int(valor) <= 59:
                adulto += 1
            else:
                idoso += 1
        eficasGenero = []
        jovemA = 0
        adultoA = 0
        idosoA = 0
        for e in range ( 1 , div + 1, 1):
            nao = dados[e]
            efiGen = [nao[1],nao[3]]
            if efiGen[1]== "n\n":
                eficasGenero.append(efiGen[0])
        for a in eficasGenero:
            if 0 < int(a) <= 19:
                jovemA += 1
            elif 20 <= int(a) <= 59:
                adultoA += 1
            else:
                idosoA += 1
        resJovem = (jovemA * 100)/jovem
        resAdulto = (adultoA * 100)/adulto
        resIdoso = (idosoA * 100)/ idoso
        resultado = f" Eficácia da vacine em jovens {resJovem}%\n Eficácia da vacine em adultos {resAdulto:.2f}%\n Eficácia da vacine em idosos {resIdoso:.2f}%."
        return resultado

# Eficacia entre vacina e placebo.

    def vacina_placebo():
        arq = open("entrada.txt", "r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)
        dados[0] = dados[0][0].replace("\n", "")
        div = int(dados[0])
        infVacina = 0
        infPlacebo = 0
        for i in range(1, div+1 , 1):
            cont = dados[i]
            contra = [cont[2],cont[3]]
            if contra[0]== "p" and contra[1] == "s\n":
                infPlacebo += 1
            elif contra[0] == "v" and contra[1] == "s\n":
                infVacina += 1
        resEficacia = 100 * (infPlacebo - infVacina)/infPlacebo
        resultado = f"A eficácia da vacina e de {resEficacia}%"
        return resultado

    def eficacia_m_f():
        arq = open("entrada.txt", "r")
        linhas = arq.readlines()
        dados = []
        for l in linhas:
            lista = l.split(",")
            dados.append(lista)
        dados[0] = dados[0][0].replace("\n", "")
        div = int(dados[0])
        mascNeg = int(0)
        femNeg = int(0)
        for i in range (1,div + 1,1):
            contraiu = dados[i]
            sim = contraiu[0]+contraiu[3]
            if sim == "m"+"n\n":
                mascNeg = mascNeg + 1
            elif sim == "f"+"n\n":
                femNeg = femNeg + 1
        resFem =(femNeg*100/div)
        resMasc =(mascNeg*100/div)
        resultado = f"Eficacia no publico feminino {resFem}%\nEficacia no publico masculino {resMasc}%."
        return resultado
