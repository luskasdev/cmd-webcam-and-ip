# 📸 IP Webcam Logger

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🔒 Ferramenta de segurança para logging de acessos com captura de IP e imagem da webcam

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2091/2091665.png" width="120" alt="Logo">
</p>

---

## ⚡ Funcionalidades

- 🌐 **Captura de IP** - Obtém IP público, local e geolocalização aproximada
- 📸 **Captura de Webcam** - Tira foto da câmera do dispositivo
- 🗺️ **Geolocalização** - Identifica cidade, região e provedor de internet
- 💬 **Integração Discord** - Envia dados e imagem via webhook em tempo real
- 💻 **Info do Sistema** - Coleta hostname, usuário, SO e arquitetura
- 📁 **Logs Locais** - Salva cópia dos dados e imagens capturadas

---

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Webcam funcionando
- Conexão com internet

---

## 🚀 Instalação

### 1. Clone o repositório

git clone https://github.com/seu-usuario/ip-webcam-logger.git
cd ip-webcam-logger


2. Instale as dependências
pip install -r requirements.txt

Ou manualmente:
pip install opencv-python requests


3. Configure o webhook
Edite o arquivo main.py e substitua a URL do webhook do Discord:

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/SEU_WEBHOOK_AQUI"



🎯 Como Usar
Execução básica

python main.py

O script irá:

Coletar informações de IP e sistema
Aguardar 3 segundos (tempo para a webcam inicializar)
Capturar uma imagem da webcam
Enviar tudo para o Discord configurado
Salvar cópia local da imagem

---

**Estrutura e Preview:**

```bash
## 📁 Estrutura do Projeto
```bash
ip-webcam-logger/
├── 📄 main.py              # Script principal
├── 📄 requirements.txt     # Dependências
├── 📄 README.md           # Este arquivo
├── 📄 LICENSE             # Licença MIT
└── 📁 captures/           # Logs e imagens salvos

🖼️ Preview
Mensagem no Discord:
🚨 Nova Captura - 10/08/2026 15:30:45

┌─────────────────────────────────────┐
│  📸 Captura de Webcam + IP          │
├─────────────────────────────────────┤
│  🌐 IP Público:  201.xxx.xxx.xxx    │
│  📍 IP Local:    192.168.1.100      │
│  📍 Localização: São Paulo, Brasil  │
│  🌐 Provedor:    Vivo Fibra         │
│  💻 Sistema:     Windows 10 x64     │
│  👤 Usuário:     admin / DESKTOP-PC │
│  🗺️ Mapa:        [Ver no Google]    │
└─────────────────────────────────────┘

[webcam_capture.jpg]` ` `




*🛡️ Aviso Legal
Este software é destinado apenas para fins educacionais e de segurança em seus próprios sistemas.

✅ Uso Permitido:
Monitoramento de acesso aos seus próprios dispositivos
Sistemas de autenticação e segurança pessoal
Logging de acessos em servidores próprios
Provas de conceito em ambientes controlados
❌ Uso Proibido:
Espionagem sem consentimento
Acesso não autorizado a dispositivos de terceiros
Coleta de dados de pessoas sem permissão explícita
Qualquer atividade ilegal ou antiética
O autor não se responsabiliza pelo uso indevido desta ferramenta.

🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:

Fork o projeto
Crie uma branch (git checkout -b feature/nova-feature)
Commit suas alterações (git commit -m 'Adiciona nova feature')
Push para a branch (git push origin feature/nova-feature)
Abra um Pull Request
📜 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

📞 Suporte
📧 Email: joaoluskas128@gmail.com
💬 Discord: madebycriminalviolenc
🐛 Issues: Mandar do Discord ou no E-Mail


<p align="center"> Feito com ❤️ e Python </p>*
