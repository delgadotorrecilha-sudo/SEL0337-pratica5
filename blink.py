#!/usr/bin/python3
"""
Pratica 5 - Checkpoint 1 - SEL0337
Aplicacao: pisca um LED ligado ao GPIO 18 da Raspberry Pi (0,2 s ligado / 0,2 s desligado).
O programa e iniciado automaticamente no boot pelo systemd (unit file: blink_py.service).

Funcionamento:
- Usa a biblioteca gpiozero (ja instalada no Raspberry Pi OS) para controlar o pino.
- Trata o sinal SIGTERM, que o systemd envia ao executar 'systemctl stop':
  o LED e apagado e o programa encerra de forma limpa.
"""
import signal
import sys
from time import sleep
from gpiozero import LED

PINO_LED = 18          # GPIO 18 (pino fisico 12)
led = LED(PINO_LED)    # configura o pino como saida


def encerrar(signum, frame):
    """Chamada quando o systemd manda parar o servico."""
    led.off()          # garante LED apagado
    led.close()        # libera o pino
    sys.exit(0)


signal.signal(signal.SIGTERM, encerrar)   # systemctl stop
signal.signal(signal.SIGINT, encerrar)    # Ctrl+C no teste manual

while True:
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
