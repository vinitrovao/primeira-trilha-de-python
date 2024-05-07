print("Primeiro Exercício")
print("\n")


def troca_de_palavra():
    palavra_antiga = "Python"
    palavra_nova = "Fython"
    texto = (
        "Python é uma linguagem de programação de alto nível, "
        "[5] interpretada de script, imperativa, orientada a objetos, "
        "funcional, de tipagem dinâmica e forte. Foi lançada por Guido van "
        "Rossum em 1991. [1] Atualmente, possui um modelo de desenvolvimento "
        "comunitário, aberto e gerenciado pela organização sem "
        "fins lucrativos Python Software Foundation. "
        "Apesar de várias partes da linguagem possuírem "
        "padrões e especificações formais, a linguagem, "
        "como um todo, não é formalmente especificada. "
        "O padrão na pratica é a implementação CPython. "
        "A linguagem foi projetada com a filosofia de "
        "enfatizar a importância do esforço do programador "
        "sobre o esforço computacional. "
        "Prioriza a legibilidade do código sobre a velocidade "
        "ou expressividade. Combina uma sintaxe "
        "concisa e clara com os recursos poderosos de "
        "sua biblioteca padrão e por módulos e "
        "frameworks desenvolvidos por terceiros."
    )
    texto_modificado = texto.replace(palavra_antiga, palavra_nova)
    return texto_modificado


def main():
    texto_modificado = troca_de_palavra()
    print(texto_modificado)


if __name__ == "__main__":
    main()

print("\n Segundo Exercício")
print("\n")


def ordenar_figurinhas(figurinhas):

    figurinhas_lista = figurinhas.split(", ")
    figurinhas_ordenadas = sorted(figurinhas_lista)
    figurinhas_ordenadas_str = ", ".join(figurinhas_ordenadas)

    return figurinhas_ordenadas_str


figurinhas_desordenadas = (
    "URU2, CRC5, SEN3, ESP10, WAL6, SRB5, BEL6, SEN7, ECU20, "
    "GER5, USA20, SEN16, URU7, AUS6, GER11, CMR12, ENG1, ECU8, "
    "WAL18, SEN12, URU19, ENG14, KSA18, FRA15, FWC2, CRC6, BRA8, "
    "BRA6, AUS3, IRN5, KSA4, CMR8, WAL4, CMR4, KOR9, POR11, "
    "URU13, CMR16, ARG15, TUN15, KOR13, DEN15, CRO13, USA4, "
    "GER4, ECU7, CRC20, POL20, QAT18, FWC3, DEN10, CMR1, "
    "NED6, BEL15, CAN12, FWC12, BEL9, KSA15, NED4, ESP20, "
    "ENG2, CRC2, TUN6, IRN12, ENG8, TUN7, MAR11, URU12, "
    "DEN20, BRA11, MEX10, MEX20, SUI16, ECU17, ESP15, "
    "MAR9, DEN12, MEX11, ARG18, KOR4, SUI3, FRA12, CAN10, "
    "POL15, MAR8, WAL10, ECU10, FRA16, FWC6, POL12, ECU13, "
    "MEX17, MAR20, FWC21, POR14, TUN3, BRA13, CRO15, "
    "GER1, AUS13, GHA18, URU6, MEX4, POR19, POR4"
)

print(ordenar_figurinhas(figurinhas_desordenadas))
