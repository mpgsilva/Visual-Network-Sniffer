import matplotlib.pyplot as plt  # type: ignore
from matplotlib.animation import FuncAnimation  # type: ignore
from sniffer import protocol_counts, start_sniffing
import threading
import time
from collections import defaultdict, deque
from datetime import datetime

# histórico de pacotes por protocolo
historico = {
    'TCP': deque(maxlen=20),
    'UDP': deque(maxlen=20),
    'ICMP': deque(maxlen=20),
}
timestamps = deque(maxlen=20)

intervalo = 5  # segundos

def snapshot_counts():
    for proto in historico:
        historico[proto].append(protocol_counts.get(proto, 0))
    timestamps.append(datetime.now())
    for key in protocol_counts:
        protocol_counts[key] = 0  # reset para o próximo intervalo

def background_counter():
    while True:
        time.sleep(intervalo)
        snapshot_counts()

def animate(i):
    plt.cla()
    
    # fundo branco
    plt.style.use('seaborn-whitegrid')

    # paleta de cores personalizada
    colors = {
        'TCP': '#1f77b4',    # Azul
        'UDP': '#ff7f0e',    # Laranja
        'ICMP': '#2ca02c',   # Verde
    }

    for proto, data in historico.items():
        plt.plot(timestamps, list(data), label=proto, color=colors.get(proto, 'black'), linewidth=2)

    # totais acumulados
    total_tcp = sum(historico['TCP'])
    total_udp = sum(historico['UDP'])
    total_icmp = sum(historico['ICMP'])
    total_all = total_tcp + total_udp + total_icmp

    # título estilizado
    plt.title(f"Tráfego de Pacotes (últimos {intervalo * len(timestamps)}s)\n"
              f"Total: {total_all} | TCP: {total_tcp} | UDP: {total_udp} | ICMP: {total_icmp}",
              fontsize=12, fontweight='bold')

    plt.xlabel('Tempo', fontsize=10)
    plt.ylabel('Pacotes por intervalo', fontsize=10)
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)

    # grid mais leve
    plt.grid(True, linestyle='--', alpha=0.5)

    # legenda com fundo semi-transparente
    plt.legend(loc='upper left', framealpha=0.7)

    plt.tight_layout()

def main():
    threading.Thread(target=start_sniffing, daemon=True).start()
    threading.Thread(target=background_counter, daemon=True).start()

    fig = plt.figure(figsize=(10, 6))  # Tamanho maior
    ani = FuncAnimation(fig, animate, interval=1000)
    plt.show()

if __name__ == "__main__":
    main()