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

target = input("Digite o IP do carregador: ")

print(f"\n[+] Escaneando {target}...\n")

found_any = False  # Flag para saber se encontrou algo

for port, desc in ports.items():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.7)
        result = sock.connect_ex((target, port))

        if result == 0:
            found_any = True
            print(f"PORTA {port} ABERTA → {desc}")

            if port == 23:
                print("   ⚠ Vulnerabilidade crítica (Telnet ativo)")
            if port == 502:
                print("   ⚠ Modbus aberto pode permitir controle remoto")

        sock.close()

    except Exception as e:
        print(f"Erro ao testar porta {port}: {str(e)}")

if not found_any:
    print("[!] Nenhuma das portas comuns de carregadores EV está aberta.")

print("\n[+] Scan concluído.")
input("\nPressione ENTER para sair...")
