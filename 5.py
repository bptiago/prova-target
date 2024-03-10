def inverter_string(str):
    tamanho_str = len(str) * -1
    chars_invertidas = []
    for i in range(-1, tamanho_str - 1, -1):
        chars_invertidas.append(str[i])
    print("".join(chars_invertidas))

inverter_string("eu fiz bastante coisa hoje") # ejoh asioc etnatsab zif ue