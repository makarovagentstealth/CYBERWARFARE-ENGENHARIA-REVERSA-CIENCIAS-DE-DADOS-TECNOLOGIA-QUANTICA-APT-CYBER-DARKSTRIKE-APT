import random

class NDQ_Lite:
    def __init__(self, fator_seguranca):
        self.fator_seguranca = fator_seguranca

    def criptografar(self, dados):
        dados_criptografados = ""
        for caractere in dados:
            valor_ascii = ord(caractere)
            valor_criptografado = valor_ascii + random.randint(1, self.fator_seguranca)
            dados_criptografados += chr(valor_criptografado)
        return dados_criptografados

    def descriptografar(self, dados_criptografados):
        dados_descriptografados = ""
        for caractere in dados_criptografados:
            valor_criptografado = ord(caractere)
            valor_descriptografado = valor_criptografado - random.randint(1, self.fator_seguranca)
            dados_descriptografados += chr(valor_descriptografado)
        return dados_descriptografados

    def analisar_dados(self, dados):
        # Simulação de análise de dados simplificada
        return len(dados) / self.fator_seguranca

# Exemplo de uso
ndq_lite = NDQ_Lite(fator_seguranca=10)
dados = "mensagem secreta"
dados_criptografados = ndq_lite.criptografar(dados)
dados_descriptografados = ndq_lite.descriptografar(dados_criptografados)
analise = ndq_lite.analisar_dados(dados)

print("Dados originais:", dados)
print("Dados criptografados:", dados_criptografados)
print("Dados descriptografados:", dados_descriptografados)
print("Análise:", analise)

