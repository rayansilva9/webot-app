import random
import threading
import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from colorama import Fore, Back, Style, init
from functions import gerar_numero_de_telefone
import json

from points.actions import click_point, sleep, scroll, await_for_value, change_to_iframe, write, vpn_on, vpn_off, \
    external_click, await_for_command, refresh_page, change_default_iframe

init()

screen_width, screen_height = pyautogui.size()
window_width = screen_width // 2
window_height = screen_height // 2

ddd = [71, 73, 74, 75, 77, 98, 99, 41, 42, 43, 44, 45, 46, 51, 53, 54, 55]

vpn_status = False


def abrir_navegador_e_interagir(url, x, y, browser_index, flow, botSettings):
    pause = False
    step = -1

    options = Options()

    if 'user_agent' in botSettings:
        options.add_argument(f'user-agent={botSettings['user_agent']}')

    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)

    proporcaoWidth = botSettings['width'] / 840
    proporcaoHeight = botSettings['height'] / 500

    window_width = proporcaoWidth * screen_width
    window_height = proporcaoHeight * screen_height
    browser.set_window_size(window_width, window_height)

    percentHeight = (botSettings['positionY'] / 500) * 100
    percentWidth = (botSettings['positionX'] / 850) * 100
    py = (percentHeight / 100) * window_height
    px = (percentWidth / 100) * window_width
    browser.set_window_position(px, py)



    browser.get(url)
    wait = WebDriverWait(browser, 60 * 2)
    time.sleep(0.2)

    ddd_escolhido = random.choice(ddd)

    numero_telefone = f"{ddd_escolhido}{gerar_numero_de_telefone()}"
    # print(Fore.GREEN + numero_telefone)

    while pause_list[browser_index]:
        for index in range(len(flow)):
            point = flow[index]

            xpath = point['xpath']
            action = point['action']

            time.sleep(0.1)

            if step > index:
                continue

            try:

                # CASE INTERNAL CLICK
                if action == 'Clique':
                    click_point(wait, xpath, browser, index)
                    step = index

                # CASE CHANGE IFRAME
                elif action == 'Mudar para iframe':
                    change_to_iframe(wait, xpath, browser, index)
                    step = index

                # CASE CHANGE DEFAULT IFRAME
                elif action == 'Mudar para iframe padrâo':
                    change_default_iframe(browser)
                    step = index

                # CASE DELAY
                elif action == 'Delay':
                    sleep(point)
                    step = index

                # CASE SCROLL
                elif action == 'Scroll':
                    sc = point['scroll']
                    scroll(sc, browser)
                    step = index

                # CASE AWAIT FOR CONDITION
                elif action == 'Aguardar valor':
                    await_for_value(point, xpath, wait, browser)

                # CASE SEND KEYS TO INPUT
                elif action == 'Digitar':
                    write(point, wait, xpath, index, step)

                # CASE TURN ON VPN
                elif action == 'Ligar VPN':
                    vpn_on(vpn_status)
                    step = index

                # CASE TURN OFF VPN
                elif action == 'Desligar VPN':
                    vpn_off()
                    step = index

                # CASE EXTERNAL CLICK
                elif action == 'Clique Externo':
                    external_click(point)
                    step = index
                    pass

                # CASE AWAIT FOR COMMAND
                elif action == 'Aguardar comando':
                    await_for_command(point)
                    step = index

                elif action == 'Atualizar página':
                    refresh_page(browser)
                    step = index

            except Exception as e:
                pause_list[browser_index] = False


pause_list = [True, True, True, True]


def resume():
    global pause_list
    for i in range(len(pause_list)):
        pause_list[i] = True


def on_press(e):
    print(f"Key pressed: {e.name}")


threads = []

with open('C:/Users/RAYAN/Downloads/arquivo.txt', 'r') as arquivo:
    flow = json.loads(arquivo.read())
    initial_urls = flow['initialUrls']
    points = flow['elements']
    botSettings = flow['botSettings']

    for i, url in enumerate(initial_urls):
        row = i // 2
        col = i % 2
        x_position = col * window_width
        y_position = row * window_height
        thread = threading.Thread(
            target=abrir_navegador_e_interagir, args=(url, x_position, y_position, i, points[i], botSettings[i]))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
