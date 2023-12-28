import random
import subprocess
import threading
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import string
from colorama import Fore, Back, Style, init
# from pynput.keyboard import Key, Listener
import keyboard

from functions import gerar_numero_de_telefone, gerar_letras_aleatorias

import json

init()

SENHA = "matuezin000"

screen_width, screen_height = pyautogui.size()
window_width = screen_width // 2
window_height = screen_height // 2

ddd = [71, 73, 74, 75, 77, 98, 99, 41, 42, 43, 44, 45, 46, 51, 53, 54, 55]

vpn_status = False

def abrir_navegador_e_interagir(url, x, y, browser_index, flow):

    pause = False
    step = -1

    options = Options()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(window_width, window_height)
    browser.set_window_position(x, y)
    browser.get(url)
    time.sleep(1)
    wait = WebDriverWait(browser, 6)
    ddd_escolhido = random.choice(ddd)

    numero_telefone = f"{ddd_escolhido}{gerar_numero_de_telefone()}"
    # print(Fore.GREEN + numero_telefone)

    while pause_list[browser_index]:
        for index in range(len(flow)):
            point = flow[index]

            xpath = point['xpath']
            action = point['action']

            print(point)
            time.sleep(1)

            if step > index:
                # print('passo')
                continue

            if action == 'click':
                if step > index:
                    # print('passo')
                    continue
                else:
                    try:
                        el = wait.until(
                            EC.visibility_of_element_located(
                                (By.XPATH, xpath))
                        )
                        el.click()
                        browser.execute_script("arguments[0].click();", el)
                        step = index

                    except Exception as e:
                        pause_list[browser_index] = False
                        # print(pause_list)
                        # print(pause_list[browser_index])

            if action == 'change_to_iframe':
                try:
                    if step > index:
                        # print('passo')
                        continue
                    else:
                        el = wait.until(
                            EC.visibility_of_element_located(
                                (By.XPATH, xpath))
                        )
                        browser.switch_to.frame(el)
                        step = index
                except Exception as e:
                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])

            if action == 'sleep':
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:
                        timer = point['delay']
                        time.sleep(int(timer))
                        step = index
                except Exception as e:
                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])

            if action == 'generate_nickname':
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:
                        def gerar_letras_aleatorias():
                            letras_aleatorias = ''.join(random.choice(string.ascii_letters) for _ in range(7))
                            return letras_aleatorias

                        el = wait.until(
                            EC.visibility_of_element_located(
                                (By.XPATH, xpath))
                        )
                        el.send_keys(gerar_letras_aleatorias())
                        step = index
                except Exception as e:
                    pause_list[browser_index] = False
                    print(pause_list)
                    # print(pause_list[browser_index])

            if action == 'scroll':
                sc = point['scroll']
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:
                        x = sc['scrollX']
                        y = sc['scrollY']
                        browser.execute_script(f"window.scrollBy({x}, {y});")
                        step = index
                except Exception as e:
                    pass
                    # pause_list[browser_index] = False
                    # print(pause_list)

            if action == 'awaitForValue':
                awaitForValue = point['awaitForValue']
                value = awaitForValue['valueToAwaitFor']
                timeout = awaitForValue['timeout']

                def esperar_valor_do_saldo(browser, valor_esperado, tempo_limite=timeout):
                    wait = WebDriverWait(browser, tempo_limite)

                    def obter_valor_elemento(driver):
                        elemento_saldo = driver.find_element(By.XPATH, xpath)

                        if elemento_saldo.tag_name == "input":
                            saldo_atual = elemento_saldo.get_attribute("value")
                        else:
                            saldo_atual = elemento_saldo.text

                        print(f'valor: {saldo_atual}')
                        return saldo_atual == valor_esperado


                    try:
                        wait.until(obter_valor_elemento)

                    except Exception as e:
                        print(
                            f"O valor do saldo não atingiu {valor_esperado} após {tempo_limite} segundos.")
                        pause_list[browser_index] = False

                        print(pause_list)
                        # print(pause_list[browser_index])
                if step > index:
                    print('passo')
                    continue
                else:
                    try:
                        esperar_valor_do_saldo(browser, value)
                    except Exception as e:
                        pause_list[browser_index] = False
                        # print(pause_list)

            if action == 'write':
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:


                        textGenerate = point['textGenerate']
                        if  textGenerate == 'numero':

                            text = gerar_numero_de_telefone()

                            el = wait.until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, xpath))
                            )

                            el.click()
                            el.send_keys(text)
                            step = index

                        elif textGenerate == 'manual':

                            text = point['sendKeys']

                            el = wait.until(
                                EC.visibility_of_element_located(
                                    (By.XPATH, xpath))
                            )

                            el.click()
                            el.send_keys(text)
                            step = index

                except Exception as e:

                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])

            if action == 'generate_number':
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:
                        el = wait.until(
                            EC.visibility_of_element_located(
                                (By.XPATH, xpath))
                        )
                        el.click()
                        el.send_keys(numero_telefone)
                        step = index
                except Exception as e:
                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])

            if action == 'vpnOn':
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:
                        if vpn_status == True:
                            pass
                        else:
                            vpn = 'C:/Users/RAYAN/Downloads/VPN.exe'
                            subprocess.run(vpn)
                            vpn_status = True

                            step = index
                except Exception as e:
                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])
            if action == 'vpnOff':
                try:
                    if step > index:
                        print('passo')
                        continue
                    else:

                        vpn = 'VPN.exe'
                        subprocess.run(['taskkill', '/F', '/IM', vpn])

                        step = index
                except Exception as e:
                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])

            if action == 'externalClick':
                try:
                    if step >= index:
                        print('passo')
                        continue
                    else:
                        x = point['externalClickX']
                        y = point['externalClickY']

                        pyautogui.click(x, y)

                        step = index
                        pass
                except Exception as e:
                    pause_list[browser_index] = False
                    # print(pause_list)
                    # print(pause_list[browser_index])

pause_list = [True, True, True, True]

def resume():
    global pause_list  # Adicione esta linha
    for i in range(len(pause_list)):
        pause_list[i] = True

def on_press(e):
    print(f"Key pressed: {e.name}")



threads = []

with open('C:/Users/RAYAN/Downloads/arquivo.txt', 'r') as arquivo:

    flow = json.loads(arquivo.read())
    initial_urls = flow['initialUrls']
    points = flow['elements']

    for i, url in enumerate(initial_urls):

        row = i // 2
        col = i % 2
        x_position = col * window_width
        y_position = row * window_height
        thread = threading.Thread(
            target=abrir_navegador_e_interagir, args=(initial_urls[i], x_position, y_position, i, points[i], ))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()




