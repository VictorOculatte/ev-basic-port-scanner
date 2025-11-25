# EV Charger Basic Port Scanner 🔌🔐

Projeto simples de segurança ofensiva voltado para identificar portas críticas expostas em carregadores veiculares elétricos (EV Chargers).

## 🔍 O que o scanner faz?

- Analisa portas comuns em dispositivos EV Charging  
- Verifica riscos como:
  - Telnet ativo (crítico)
  - Modbus exposto
  - Configuração remota TR-069 acessível
  - Painéis web abertos sem proteção
- Exibe resultados direto no terminal

## 🧠 Objetivo
Aprender fundamentos de scanners, footprinting e identificação de exposição em dispositivos IoT/Industrial, essenciais para Red Team.

## ▶ Como executar

No terminal execute:

```bash
python scanner_basico.py

📂 Estrutura do projeto
ev-basic-port-scanner/
│
├── scanner_basico.py
└── README.md

📌 Observação

Este projeto é apenas para fins educacionais, simulando cenários comuns em EV Chargers.
Não execute em dispositivos reais ou redes sem autorização.
