Projeto de automação, na qual foi utilizado script em Python para envio no Discord de informações de containers que veem a parar, informações estas sendo Nome, ID e data de quando parou.

Foi criado um bot no discord para webhook da variavel gerada com as informações do container. No script foi usado a biblioteca requests para enviar, usando a função post, a mensagem no webhook do discord.
Além de da biblioteca Requests, usei a lib docker para realizar todas essas operações de events, definindo somente para containers que pararam e por ultimo, usei a lib datetime para formatar a data, ja que a mesma vem no formato epoch time, do unix.
