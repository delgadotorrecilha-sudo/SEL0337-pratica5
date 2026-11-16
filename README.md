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
