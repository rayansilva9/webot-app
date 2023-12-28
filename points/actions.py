import subprocess
import datetime
import time
import pyautogui
from pynput import keyboard
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from functions import gerar_numero_de_telefone


def click_point(wait, xpath, browser, index):
    el = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, xpath))
    )
    el.click()
    browser.execute_script("arguments[0].click();", el)


def change_to_iframe(wait, xpath, browser, index):
    el = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, xpath))
    )
    browser.switch_to.frame(el)


def change_default_iframe(browser):
    browser.switch_to.default_content()

def sleep(point):
    # Converte o tempo para um objeto datetime
    timer = datetime.datetime.strptime(point['delay'], '%H:%M:%S')

    # Extrai a quantidade total de segundos
    seconds = timer.second + timer.minute * 60 + timer.hour * 3600

    # Usa time.sleep com o número de segundos calculado
    time.sleep(seconds)


def scroll(sc, browser):
    x = sc['scrollX']
    y = sc['scrollY']
    browser.execute_script(f"window.scrollBy({x}, {y});")


def await_for_value(point, xpath, wait, browser):
    await_for_value = point['awaitForValue']
    value = await_for_value['valueToAwaitFor']
    timeout = await_for_value['timeout']
    condition = await_for_value['condition']

    wait = WebDriverWait(browser, timeout)

    def obter_valor_elemento(driver):
        elemento_saldo = driver.find_element(By.XPATH, xpath)

        if elemento_saldo.tag_name == "input":
            saldo_atual = elemento_saldo.get_attribute("value")
        else:
            saldo_atual = elemento_saldo.text

        if condition == '==':
            return saldo_atual == value
        elif condition == '>':
            return float(saldo_atual) > float(value)
        elif condition == '<':
            return float(saldo_atual) < float(value)
        elif condition == '>=':
            return float(saldo_atual) >= float(value)
        elif condition == '<=':
            return float(saldo_atual) <= float(value)
        else:
            raise ValueError(f"Condição não suportada: {condition}")

    try:
        wait.until(obter_valor_elemento)

    except Exception as e:
        print(f"O valor do saldo não atingiu {value} após {timeout} segundos.")


def write(point, wait, xpath, index, step):
    textGenerate = point['textGenerate']
    if textGenerate == 'numero':

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


def vpn_on(vpn_status):
    if vpn_status:
        pass
    else:
        vpn = 'C:/Users/RAYAN/Downloads/VPN.exe'
        subprocess.run(vpn)
        vpn_status = True


def vpn_off():
    vpn = 'VPN.exe'
    subprocess.run(['taskkill', '/F', '/IM', vpn])


def external_click(point):
    x = point['externalClickX']
    y = point['externalClickY']

    pyautogui.click(x, y)


def await_for_command(point):
    key_code = point['keyboardCommand']
    # Variável de controle para pausa
    paused = True

    def on_press(key):
        nonlocal paused  # Utiliza a variável de controle da função externa

        try:

            if hasattr(key, 'char') and key.char == key_code:
                print('Esc pressionado. Saindo do pause.')
                paused = False  # Altera a variável de controle para encerrar a pausa
                return False  # Encerra o listener
        #
        except AttributeError:
            print('Tecla especial {0} pressionada'.format(key))

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Loop de espera enquanto estiver pausado
    while paused:
        # print(paused)
        time.sleep(0.1)  # Adiciona um pequeno atraso para evitar consumo excessivo de CPU

    print('Continuando após o pause.')
    listener.stop()


def refresh_page(browser):
    browser.refresh()

