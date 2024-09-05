import random

# Função para gerar o quarto código experimental de Kryptos
def gerar_codigo_kryptos_experimental(metadados):
    # Simulação de uma sequência quântica gerada
    random.seed(sum(ord(char) for char in metadados))  # Baseado nos metadados
    codigo = [random.randint(0, 9) for _ in range(16)]  # Gera uma sequência de 16 números
    return codigo

# Função de interpretação da numeração
def interpretar_codigo_kryptos(codigo):
    # Interpretação teórica simples
    soma = sum(codigo)
    media = soma / len(codigo)
    return f"Interpretação: A soma dos números é {soma}, e a média é {media}."

# Console de Digitação
def console_digitacao():
    print("Digite os metadados para gerar o quarto código experimental:")
    metadados = input("Metadados: ")
    codigo = gerar_codigo_kryptos_experimental(metadados)
    print(f"Código Kryptos gerado: {codigo}")
    return codigo

# Console de Interpretação
def console_interpretacao(codigo):
    interpretacao = interpretar_codigo_kryptos(codigo)
    print(interpretacao)

# Main
if __name__ == "__main__":
    codigo_gerado = console_digitacao()
    console_interpretacao(codigo_gerado)
