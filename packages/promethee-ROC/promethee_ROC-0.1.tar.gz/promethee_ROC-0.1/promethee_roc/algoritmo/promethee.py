def roc(criterios):
    criterios_com_pesos = []
    somatorio = 0
    for i in range(len(criterios) - 1, -1, -1):
        criterios_com_pesos.append((f"{criterios[i]}", 1 / len(criterios) * (somatorio + 1 / (i + 1))))
        somatorio += 1 / (i + 1)
    criterios_com_pesos.reverse()

    return criterios_com_pesos

def calcular_indices_preferencia(alternativa1, alternativa2, criterios, alternativas, dados):
    indice_preferencia = 0
    for j in range(len(criterios)):
        indice = 0

        valor_alternativa1 = float(dados[alternativas.index(alternativa1)][j])
        valor_alternativa2 = float(dados[alternativas.index(alternativa2)][j])

        if valor_alternativa1 > valor_alternativa2 > 0:
            indice = 1 - (valor_alternativa2 / valor_alternativa1)
        elif valor_alternativa1 <= valor_alternativa2:
            indice = 0
        elif valor_alternativa2 == 0:
            indice = 1
        indice_preferencia += indice * criterios[j][1]

    return indice_preferencia

def calcular_fluxos(alternativas, criterios, dados):
    pares = [(a, b) for a in alternativas for b in alternativas if a != b]
    todos_indices = {}
    todos_fluxos_positivos = {}
    todos_fluxos_negativos = {}

    for par in pares:
        indice_par = calcular_indices_preferencia(par[0], par[1], criterios, alternativas, dados)
        todos_indices[f"Indice({par[0]}, {par[1]})"] = indice_par

    for alternativa in alternativas:
        soma_indice_positivo = 0
        for par, indice in todos_indices.items():
            if par.startswith(f"Indice({alternativa}"):
                soma_indice_positivo += indice
        fluxo_positivo = 1 / (len(alternativas) - 1) * soma_indice_positivo
        todos_fluxos_positivos[alternativa] = fluxo_positivo

        soma_indice_negativo = 0
        for par, indice in todos_indices.items():
            if par.endswith(f"{alternativa})"):
                soma_indice_negativo += indice
        fluxo_negativo = 1 / (len(alternativas) - 1) * soma_indice_negativo
        todos_fluxos_negativos[alternativa] = fluxo_negativo

    todos_fluxos_totais = {}
    for alternativa in alternativas:
        todos_fluxos_totais[alternativa] = todos_fluxos_positivos[alternativa] - todos_fluxos_negativos[alternativa]

    return todos_fluxos_totais, todos_fluxos_positivos, todos_fluxos_negativos, todos_indices

def classificacao_parcial(todos_fluxos_positivos, todos_fluxos_negativos, alternativas):
    pares = [(a, b) for a in alternativas for b in alternativas if a != b]
    classificacoes = []
    for par in pares:
        if (todos_fluxos_positivos[par[0]] > todos_fluxos_positivos[par[1]] and todos_fluxos_negativos[par[0]] < todos_fluxos_negativos[par[1]]) or \
                (todos_fluxos_positivos[par[0]] == todos_fluxos_positivos[par[1]] and todos_fluxos_negativos[par[0]] < todos_fluxos_negativos[par[1]]) or \
                (todos_fluxos_positivos[par[0]] > todos_fluxos_positivos[par[1]] and todos_fluxos_negativos[par[0]] == todos_fluxos_negativos[par[1]]):
            classificacoes.append(f"{par[0]} é preferível a {par[1]}")
        elif todos_fluxos_positivos[par[0]] == todos_fluxos_positivos[par[1]] and todos_fluxos_negativos[par[0]] == todos_fluxos_negativos[par[1]]:
            classificacoes.append(f"{par[0]} e {par[1]} são indiferentes")
            pares.remove((par[1], par[0]))
        elif (todos_fluxos_positivos[par[0]] > todos_fluxos_positivos[par[1]] and todos_fluxos_negativos[par[0]] > todos_fluxos_negativos[par[1]]) or \
                (todos_fluxos_positivos[par[0]] < todos_fluxos_positivos[par[1]] and todos_fluxos_negativos[par[0]] < todos_fluxos_negativos[par[1]]):
            classificacoes.append(f"{par[0]} e {par[1]} são incomparáveis")
            pares.remove((par[1], par[0]))

    return classificacoes

def classificacao_total(fluxos_totais):
    alternativas_ordenadas = sorted(fluxos_totais.items(), key=lambda x: x[1], reverse=True)

    return alternativas_ordenadas