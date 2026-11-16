#!/usr/bin/python3
"""
Pratica 5 - Checkpoint 1 - SEL0337
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
