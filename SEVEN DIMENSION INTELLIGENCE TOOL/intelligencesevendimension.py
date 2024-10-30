# Início do código da ferramenta de Análise Quântica de Localização

def calcular_numero_de_atomicos(densidade, altura_andar, largura, profundidade, num_andares):
    """
    Calcula o número de átomos usando a densidade e o volume do espaço.
    """
    volume_total = num_andares * (altura_andar * largura * profundidade)  # Volume total do prédio
    numero_atomico = (densidade * volume_total) ** 2  # Elevação ao quadrado como pedido
    return numero_atomico

def calcular_configuracao_extra(numero_atomico, num_pessoas, num_materiais):
    """
    Ajusta o resultado com base no número de pessoas e matérias-primas.
    """
    fator_pessoas = 1 + (num_pessoas * 0.1)  # Aumento de 10% por pessoa
    fator_materiais = 1 + (num_materiais * 0.05)  # Aumento de 5% por material

    # Ajuste do número atômico com base nas pessoas e materiais
    numero_atomico_ajustado = numero_atomico * fator_pessoas * fator_materiais
    return numero_atomico_ajustado

def main():
    print("=== Ferramenta de Análise Quântica de Localização ===")
    
    # Entrada de coordenadas geográficas
    latitude = float(input("Insira a latitude do local: "))
    longitude = float(input("Insira a longitude do local: "))
    
    # Entrada de características do objeto
    densidade_atomica = float(input("Insira a densidade atômica média do material (átomos por m³): "))
    
    # Configurações de espaço
    altura_andar = float(input("Insira a altura de cada andar (em metros): "))
    largura = float(input("Insira a largura do espaço (em metros): "))
    profundidade = float(input("Insira a profundidade do espaço (em metros): "))
    num_andares = int(input("Insira o número de andares (entre 0 e 20): "))
    
    # Validação do número de andares
    if num_andares < 0 or num_andares > 20:
        print("O número de andares deve estar entre 0 e 20.")
        return
    
    # Entrada de número de pessoas e materiais
    num_pessoas = int(input("Insira o número de pessoas (entre 0 e 15): "))
    num_materiais = int(input("Insira o número de matérias-primas periódicas (entre 0 e 50): "))

    # Validação dos números de pessoas e materiais
    if num_pessoas < 0 or num_pessoas > 15:
        print("O número de pessoas deve estar entre 0 e 15.")
        return
    if num_materiais < 0 or num_materiais > 50:
        print("O número de matérias-primas deve estar entre 0 e 50.")
        return

    # Cálculo do número de átomos
    numero_atomico = calcular_numero_de_atomicos(densidade_atomica, altura_andar, largura, profundidade, num_andares)
    
    # Ajuste do resultado com base no número de pessoas e materiais
    numero_atomico_ajustado = calcular_configuracao_extra(numero_atomico, num_pessoas, num_materiais)
    
    # Exibição do resultado
    print("\n=== Resultado da Análise ===")
    print(f"Coordenadas do local: Latitude {latitude}, Longitude {longitude}")
    print(f"Dimensões do edifício: {num_andares} andares, cada andar com {altura_andar}m de altura, largura {largura}m, profundidade {profundidade}m")
    print(f"Número de pessoas: {num_pessoas}")
    print(f"Número de matérias-primas periódicas: {num_materiais}")
    print(f"Estimativa de número de átomos no local (quântico elevado ao quadrado): {numero_atomico}")
    print(f"Resultado ajustado considerando pessoas e materiais: {numero_atomico_ajustado}")

# Executar o programa
if __name__ == "__main__":
    main()
