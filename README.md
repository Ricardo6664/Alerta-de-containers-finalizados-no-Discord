Projeto de automação, na qual foi utilizado script em Python para envio no Discord de informações de containers que veem a parar, informações estas sendo Nome, ID e data de quando parou.

Foi criado um bot no discord para webhook da variavel gerada com as informações do container. No script foi usado a biblioteca requests para enviar, usando a função post, a mensagem no webhook do discord.
Além de da biblioteca Requests, usei a lib docker para realizar todas essas operações de events, definindo somente para containers que pararam e por ultimo, usei a lib datetime para formatar a data, ja que a mesma vem no formato epoch time, do unix.

Todo este projeto foi realizado em ambiente virtual, venv do python, na qual segue o arquivo requeritments com as libs usadas.

![Captura de tela de 2024-02-14 17-57-52](https://github.com/Ricardo6664/Alerta-de-containers-finalizados-no-Discord/assets/124509531/7d1823b5-476f-4d96-9fd3-038249dd2c2d)
