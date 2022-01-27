import pyautogui as pg
from time import sleep
from datetime import datetime

def validation(string):
    while string not in 'SN':
        string = input('Digite apenas S ou N: ')
    return string

# clicar para aceitar a partida
def click(x, y):
    pg.moveTo(x, y)
    pg.click()

# verficar se apareceu partida
def verificar_fila():
    # a função 'locateOnScreen' deve receber como primeiro parâmetro um print do nome 'aceitar' que é mostrado quando uma partida é encontrada
    position = pg.locateOnScreen('aceitar2.png', confidence=0.7)
    if position != None:
        click(position.left, position.top)
        return True

def main():
    alert = validation(input('Deseja ser alertado pelo Bot no Telegram? [S/N]: ').upper())
    
    if alert == 'S':
        import telebot as tb # importa a API do Telegram

        # abre um arquivo com os dados da KEY do bot e o Id onde ele deve enviar a mensagem
        with open('ids.txt', 'r') as file:
            dados = file.readlines()
            #print(dados[0][:46])

        KEY = dados[0][:46] # key gerada pelo BotFather quando seu bot é criado
        MY_ID = dados[1] # id do chat onde a mensagem deve ser enviada

        bot = tb.TeleBot(KEY)

        # função para o bot enviar a mensagem 
        def avisar_fila():
            bot.send_message(MY_ID, 'Fila aceita meu jovem')

    print('Buscando fila!')
    while True:
        time = str(datetime.now())
        if verificar_fila():
            # fica avisando várias vezes
            if alert == 'S':
                avisar_fila()
            print(f'Fila encontrada às {time[11:19]}')
            sleep(6)

if __name__ == '__main__':
    main()