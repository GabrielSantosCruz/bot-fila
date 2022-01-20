# Bot de filas - League of Legends

Um bot criado ultilizando a biblioteca `pyautogui`, reponsável por automatizar movimentos do mouse e do teclado além de analisar a tela do computador. Além disso, também foi utilizada a `API` do Telegram para a criação de um bot para notificar sempre que uma partida fosse encontrada e aceita.

## Notas de uso:

O arquivo `ids.txt` que o código solicita deve ser preenchido da seguinte forma: a primeira linha deve conter a `Key` gerada pelo BotFather do Telegram e a segunda o `Id` do chat onde ele deve enviar a mensagem alertando que uma partida foi encontrada. Caso não queira criar um bot, basta digitar "N" quando o script perguntar se deseja ser alertado.

Na `linha 13` do código, na função "locateOnScreen", o primeiro parâmetro recebido é um print do bota aceitar a partida encontrada, este print deve ser substituido por um de sua tela, devido as diferenças de resolução