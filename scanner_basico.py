import socket

# Portas comuns em EV Chargers
ports = {
    80:  "Painel Web",
    443: "Painel Web (HTTPS)",
    502: "Modbus (Controle de Energia)",
    7547: "TR-069 (Config Remota)",
    22:  "SSH (Admin)",
    23:  "Telnet (Muito perigoso)"
}

while True:
    target = input("\nDigite o IP do carregador (ou 'sair' para encerrar): ").strip()

    if target.lower() == "sair":
        print("\nEncerrando o programa...")
        break

    print(f"\n[+] Escaneando {target}...\n")

    achou_algo = False

    for port, desc in ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.7)
            result = sock.connect_ex((target, port))

            if result == 0:
                achou_algo = True
                print(f"PORTA {port} ABERTA → {desc}")

                if port == 23:
                    print("   ⚠ Vulnerabilidade crítica (Telnet ativo)")
                if port == 502:
                    print("   ⚠ Modbus aberto pode permitir controle remoto")

            sock.close()

        except:
            pass

    if not achou_algo:
        print("Nenhuma porta comum de EV Charger está aberta.")

    print("\n[+] Scan concluído.")

    # pergunta se quer fazer outro scan
    opc = input("\nDeseja testar outro IP? (S/N): ").strip().lower()
    if opc != "s":
        print("\nEncerrando o programa...")
        break
