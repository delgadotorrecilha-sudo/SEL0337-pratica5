# SEL0337-pratica5
**Instituição:** Escola de Engenharia de São Carlos (EESC-USP)  
**Alunos:** 

Luís Carlos Delgado Torrecilha - 15472530

Beatriz Fonseca Silva - 15653959
## Estrutura de Arquivos
Checkpoint 1 : -`blink.py` `blinkoff.py` `blink_py.service`
Checkpoint 2 : -`historico_git.txt`

## Funcionamento dos programas
blink.py

Usa a biblioteca gpiozero para controlar o GPIO 18 como saída. Em um laço infinito, liga o LED por 0,2 s e desliga por 0,2 s. O programa também trata o sinal SIGTERM (enviado pelo systemd no systemctl stop): ao recebê-lo, apaga o LED, libera o pino e encerra de forma limpa.

blinkoff.py

Executado pelo systemd quando o serviço é parado. Grava uma linha com data e hora em /home/sel/blink_stop.log.

blink_py.service
ini
[Unit]
Description=Blink LED em Python (Pratica 5)
After=multi-user.target

[Service]
Type=simple
User=sel
ExecStart=/usr/bin/python3 -u /home/sel/blink.py
ExecStop=/usr/bin/python3 /home/sel/blinkoff.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
After=multi-user.target: o serviço inicia depois que o sistema chega ao modo multiusuário.
ExecStart: o interpretador python3 é chamado explicitamente, pois o script depende dele e de suas bibliotecas.
ExecStop: programa executado ao parar o serviço com systemctl stop.
Restart=on-failure: reinicia o serviço automaticamente se ele falhar.
WantedBy=multi-user.target: define o alvo em que o serviço é habilitado no boot.
