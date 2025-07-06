# 📡 Sniffer e Visualizador de Tráfego de Rede

Projeto em Python para capturar e visualizar em tempo real o tráfego de rede, monitorando pacotes **TCP**, **UDP** e **ICMP**.

Utiliza:
- [Scapy](https://scapy.net/) para captura de pacotes.
- [Matplotlib](https://matplotlib.org/) para visualização animada dos dados.

---

## 🎯 Objetivo

Permitir o monitoramento simples e em tempo real do tráfego de rede local, mostrando gráficos atualizados com o número de pacotes por protocolo ao longo do tempo.

---

## 🖼️ Visão Geral

O sistema possui dois módulos:

- **sniffer.py**: captura pacotes usando Scapy e contabiliza TCP, UDP e ICMP.
- **visualizer.py**: exibe um gráfico animado em tempo real com as contagens, atualizando a cada intervalo definido.

O gráfico mostra:
- Contagem acumulada de pacotes por protocolo.
- Evolução temporal dos pacotes em uma janela deslizante (por padrão, os últimos 100 segundos).

---

## ⚙️ Como Usar

### 1️⃣ Instalação

```bash
pip install -r requirements.txt
````
Alternativa (caso o comando acima não funcione):

Instale os pacotes manualmente:
```bash
pip install scapy matplotlib
````

### 2️⃣ Execução
```bash
python visualizer.py
````
