import random
import threading
import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import time
from colorama import Fore, Back, Style, init
from functions import gerar_numero_de_telefone
import json
from fake_useragent import UserAgent
from points.actions import click_point, sleep, scroll, await_for_value, change_to_iframe, write, vpn_on, vpn_off, \
    external_click, await_for_command, refresh_page, change_default_iframe

init()


proxies = [
    '8.219.74.58:443',
    "47.74.152.29:8888",
    "128.199.202.122:8080",
    "20.210.113.32:80",
    "138.68.60.8:8080",
    "13.81.217.201:80",
    "103.152.112.145:80",
    "139.162.78.109:3128",
    "195.181.172.223:8082",
    "162.223.94.163:80",
    "47.56.110.204:8989",
    "51.15.242.202:8888",
    "20.111.54.16:8123",
    "20.206.106.192:80",
    "20.24.43.214:80",
    "139.59.1.14:8080",
    "46.47.197.210:3128",
    "188.166.56.246:80",
    "162.223.94.164:80",
    "195.181.172.231:8082",
    "47.88.62.42:80",
    "118.69.134.2:80",
    "89.208.122.98:59414",
    "189.240.60.164:9090",
    "75.89.101.62:80",
    "159.65.77.168:8585",
    "20.6.0.172:80",
    "49.0.199.132:9091",
    "189.240.60.163:9090",
    "47.89.240.232:56682",
    "43.250.107.223:80",
    "78.46.210.112:80",
    "195.114.209.50:80",
    "162.223.89.84:80",
    "89.116.229.56:80",
    "209.97.150.167:3128",
    "200.164.28.168:8111",
    "133.18.234.13:80",
    "218.255.187.60:80",
    "187.204.9.203:53281",
    "189.240.60.169:9090",
    "20.163.133.5:80",
    "198.11.175.180:8080",
    "8.219.97.248:80",
    "193.41.155.11:3128",
    "165.227.120.250:10006",
    "195.14.123.50:8443",
    "115.96.208.124:8080",
    "4.247.16.242:80",
    "195.158.18.236:3128",
    "202.144.157.1:9009",
    "138.91.159.185:80",
    "50.168.163.177:80",
    "107.1.93.211:80",
    "50.171.68.130:80",
    "50.204.219.226:80",
    "89.185.29.2:80",
    "107.1.93.219:80",
    "50.168.163.178:80",
    "50.170.90.24:80",
    "85.26.146.169:80",
    "50.169.23.170:80",
    "50.168.210.226:80",
    "50.207.199.86:80",
    "50.172.75.122:80",
    "50.122.86.118:80",
    "50.222.245.40:80",
    "50.222.245.45:80",
    "50.222.245.46:80",
    "50.231.104.58:80",
    "50.168.72.119:80",
    "50.170.90.28:80",
    "50.174.7.152:80",
    "50.206.111.90:80",
    "50.239.72.16:80",
    "50.171.152.30:80",
    "107.1.93.217:80",
    "50.230.222.202:80",
    "50.168.72.114:80",
    "50.207.199.80:80",
    "68.188.59.198:80",
    "41.230.216.70:80",
    "50.171.32.229:80",
    "211.128.96.206:80",
    "50.222.245.41:80",
    "50.217.226.47:80",
    "50.168.163.182:80",
    "50.171.32.224:80",
    "107.1.93.222:80",
    "50.228.141.99:80",
    "50.170.90.30:80",
    "50.172.75.126:80",
    "50.200.12.87:80",
    "213.33.126.130:80",
    "127.0.0.7:80",
    "189.240.60.168:9090",
    "50.171.32.228:80",
    "50.168.163.181:80",
    "50.173.140.151:80",
    "41.207.187.178:80",
    "50.218.57.69:80",
    "103.178.13.51:3030",
    "191.7.216.31:8080",
    "103.87.169.194:32650",
    "181.205.241.227:999",
    "202.162.213.178:8080",
    "66.210.33.34:8080",
    "103.164.229.108:8080",
    "183.100.14.134:8000",
    "50.204.219.230:80",
    "50.207.199.82:80",
    "50.207.199.81:80",
    "50.174.7.157:80",
    "50.174.145.15:80",
    "190.58.248.86:80",
    "50.207.199.87:80",
    "50.222.245.50:80",
    "189.202.188.149:80",
    "50.220.168.134:80",
    "0.0.0.0:80",
    "32.223.6.94:80",
    "50.168.72.116:80",
    "50.168.210.232:80",
    "50.207.199.83:80",
    "50.171.32.222:80",
    "50.228.141.100:80",
    "50.174.41.66:80",
    "50.228.141.96:80",
    "50.228.141.101:80",
    "66.225.254.16:80",
    "50.170.90.25:80",
    "50.204.219.224:80",
    "50.200.12.84:80",
    "80.228.235.6:80",
    "50.221.74.130:80",
    "50.168.163.183:80",
    "50.168.163.179:80",
    "50.168.210.235:80",
    "195.23.57.78:80",
    "50.217.29.198:80",
    "50.222.245.43:80",
    "50.174.7.162:80",
    "107.1.93.212:80",
    "50.239.72.17:80",
    "82.119.96.254:80",
    "50.228.141.97:80",
    "50.168.72.115:80",
    "50.217.226.41:80",
    "50.174.7.154:80",
    "50.168.210.236:80",
    "50.222.245.44:80",
    "50.171.32.230:80",
    "50.200.12.80:80",
    "50.174.7.156:80",
    "50.173.140.150:80",
    "50.221.166.2:80",
    "50.173.140.146:80",
    "50.174.7.153:80",
    "50.168.72.112:80",
    "50.168.210.238:80",
    "50.206.111.91:80",
    "50.218.57.65:80",
    "50.200.12.85:80",
    "50.207.199.84:80",
    "50.218.57.68:80",
    "50.217.226.40:80",
    "107.1.93.209:80",
    "62.99.138.162:80",
    "154.65.39.8:80",
    "50.228.141.98:80",
    "50.173.140.138:80",
    "50.173.140.145:80",
    "107.1.93.215:80",
    "50.206.111.88:80",
    "107.1.93.218:80",
    "50.173.140.149:80",
    "85.192.40.171:3128",
    "62.33.136.222:8080",
    "190.187.163.2:999",
    "45.71.202.148:1993",
    "178.134.31.226:8080",
    "176.241.143.197:8080",
    "213.5.188.210:3128",
    "113.23.183.154:1122",
    "202.5.46.245:5020",
    "177.190.189.26:44443",
    "41.77.188.131:80",
    "71.235.183.92:80",
    "202.131.65.110:80",
    "177.200.91.109:12312",
    "124.123.108.15:80",
    "35.199.93.247:8083",
    "162.248.224.103:80",
    "58.234.116.197:80",
    "195.181.172.211:8081",
    "162.223.91.11:80",
    "159.138.122.91:18081",
    "195.181.172.220:8080",
    "47.88.3.19:8080",
    "162.248.225.230:80",
    "160.19.94.188:5671",
    "12.186.205.121:80",
    "123.30.154.171:7777",
    "114.156.77.107:8080",
    "167.71.212.154:80",
    "165.154.186.232:80",
    "195.181.172.230:8082",
    "51.159.0.236:2020",
    "202.61.204.51:80",
    "49.228.131.169:5000",
    "133.242.229.79:33333",
    "43.156.0.125:8888",
    "189.240.60.166:9090",
    "5.161.103.41:88",
    "114.129.2.82:8081",
    "216.137.184.253:80",
    "36.88.51.210:80",
    "190.103.177.131:80",
    "116.203.28.43:80",
    "51.210.28.182:80",
    "103.133.221.251:80",
    "20.1.56.27:80",
    "82.223.102.92:9443",
    "200.19.177.120:80",
    "35.209.198.222:80",
    "107.1.93.223:80",
    "68.185.57.66:80",
    "50.175.212.74:80",
    "50.173.140.148:80",
    "50.168.72.122:80",
    "107.1.93.220:80",
    "50.228.83.226:80",
    "50.174.7.159:80",
    "50.170.90.31:80",
    "103.169.130.42:8080",
    "183.89.188.9:8080",
    "177.229.210.66:8080",
    "185.255.46.121:8080",
    "184.107.90.26:3128",
    "187.102.208.203:999",
    "171.245.96.9:5004",
    "77.235.31.24:8080",
    "162.214.165.203:80",
    "45.76.196.51:80",
    "46.149.77.234:80",
    "194.182.163.117:3128",
    "197.243.20.186:"
    ]


screen_width, screen_height = pyautogui.size()
window_width = screen_width // 2
window_height = screen_height // 2

ddd = [71, 73, 74, 75, 77, 98, 99, 41, 42, 43, 44, 45, 46, 51, 53, 54, 55]

vpn_status = False

folder_path = "C:\\Users\\RAYAN\\Downloads"
chromedriver_path = download_undetected_chromedriver(
    folder_path, undetected=True, arm=False, force_update=True
)

class MyUDC(uc.Chrome):
    def __del__(self):
        try:
            self.service.process.kill()
        except:  # noqa
            pass
        # self.quit()

def abrir_navegador_e_interagir(url, x, y, browser_index, flow, botSettings):
    pause = False
    step = -1

    options = Options()
    # ua = UserAgent()
    if 'user_agent' in botSettings:
        options.add_argument(f'user-agent={botSettings['user_agent']}')


    if 'proxy' in botSettings:
        if len(botSettings['proxy']) > 0:
            options.add_argument(f'--proxy-server={random.choice(botSettings['proxy'])}')



    # options.add_experimental_option("detach", True)
    browser = MyUDC(options=options, driver_executable_path=chromedriver_path, headless=False, use_subprocess=True)

    # SET WINDOW DISMENSION

    proporcaoWidth = botSettings['width'] / 840
    proporcaoHeight = botSettings['height'] / 500

    window_width = proporcaoWidth * screen_width
    window_height = proporcaoHeight * screen_height
    browser.set_window_size(window_width, window_height)

    # SET WINDOW POSITION

    percentHeight = (botSettings['positionY'] / 500) * 100
    percentWidth = (botSettings['positionX'] / 850) * 100
    py = (percentHeight / 100) * screen_height
    px = (percentWidth / 100) * screen_width

    browser.set_window_position(px, py)



    # browser.get('http://ip.jsontest.com/')
    browser.get(url)
    wait = WebDriverWait(browser, 60 * 2)
    time.sleep(0.2)

    # ddd_escolhido = random.choice(ddd)

    # numero_telefone = f"{ddd_escolhido}{gerar_numero_de_telefone()}"
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
