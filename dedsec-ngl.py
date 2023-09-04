import requests
import uuid
import time, os, sys
from tabulate import tabulate
from pystyle import *
import random
import string

def login():
    user = "Razz"
    passwd = "Dedsec"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Salah, Hanya Anggota Dedsec yang bisa memakai tools ini: DEDSEC_COMMUNITY")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ HELLO ANGGOTA DEDSEC <666 😈")
        time.sleep(1)
        
        main()

login()

def generate_random_user_agent():
    operating_systems = [
        "Windows NT 10.0",
        "Windows NT 6.1",
        "Windows NT 6.3",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "Android 4.4.2",
        "Android 5.0",
        "Android 6.0",
        "Android 7.0",
        "Android 8.0",
        "Android 9.0",
        "Android 10.0",
        "Android 11.0",
        "Android 12.0", 
        "CPU iPhone OS 14_7_1 like Mac OS X",
        "CPU iPhone OS 15_0 like Mac OS X",
    ]
    
    web_browsers = [
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0",
        "AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.62",
    ]
    
    os = random.choice(operating_systems)
    browser = random.choice(web_browsers)
    
    user_agent = f"Mozilla/5.0 ({os}) {browser}"
    return user_agent

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_cookie():
    distinct_id = generate_random_string(32)
    device_id = generate_random_string(32)
    initial_referrer = generate_random_string(8)
    initial_referring_domain = generate_random_string(8)
    
    cookie = (
        f"mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22{distinct_id}%22%2C"
        f"%22%24device_id%22%3A%20%22{device_id}%22%2C%22%24initial_referrer%22%3A%20%22{initial_referrer}%22%2C"
        f"%22%24initial_referring_domain%22%3A%20%22{initial_referring_domain}%22%7D;"
    )
    
    for _ in range(4):
        cookie += f" {generate_random_string(8)}={generate_random_string(40)};"
    
    return cookie.strip()


dark = Col.dark_gray
pheart = Colors.StaticMIX((Col.red, Col.purple))


text = r'''
                                                       
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⠶⠶⠶⣦⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⢻⡿⠋⣁⣤⣶⣾⣿⣿⣶⣿⣽⣿⣶⣄⡀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣛⠛⠃⠊⢀⣼⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⡿⣆⠀⠐⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⢷⣶⣤⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⡶⠾⡿⢛⣟⣃⠅⠀⠂⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣳⣿⣿⣿⣿⣦⠿⠛⠉⠋⠉⠁⠀⠉⠙⠛⠛⣿⣿⣷⣦⣣⠐⠢⠑⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢧⣿⣿⣯⡷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⡵⣤⡄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⣾⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢡⣿⣿⡿⠁⠀⢀⣠⡤⠄⠀⠀⠀⠀⠀⠰⠖⠒⠂⠤⡀⠀⢸⣿⣿⢹⣿⠀⠀⠀          DEDSEC SPAMMER TOOL v.1
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⢸⣿⣿⠇⠄⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠁⢸⣿⣿⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⣿⣿⣿⠀⠀⠀⣠⣤⣬⡑⠀⠀⠀⠀⠀⢀⣥⡶⠶⢦⣕⠀⢸⣿⣿⢸⣿⣷⠀⠀⠀⠀⠀One message to your crush is not enough ⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⣿⣿⣿⠀⢠⠾⠁⣀⡈⠋⠁⠀⠀⠀⠀⠀⠀⢠⣤⡀⠈⠇⢨⣿⣿⢸⣿⣿⣇⠀⠀⠀⠀⠀   So, let my tool handle this.⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⣿⡿⣸⣣⠈⠐⠈⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠂⣿⣿⡸⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⡄⣿⠇⣿⠪⢁⠀⢐⠒⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠄⠐⢀⡼⣿⡇⠹⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⢟⣾⣇⣿⢰⣿⣷⡄⠒⠀⠀⠂⠂⠀⠐⠒⠒⠒⠒⠒⠒⠀⠆⠀⠁⣿⡇⣿⣿⢠⡹⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⢏⣾⣿⣿⠛⢸⣿⣿⣷⢄⣀⣀⣀⢤⣤⣤⣤⣤⣤⣤⣤⣤⣤⢦⣤⢲⢻⠇⣿⡿⣼⣷⡝⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⢫⣾⣿⣿⣿⣠⢸⣿⣿⣿⣼⣼⣿⣬⡬⢉⠉⠉⠉⠉⢉⡩⢋⣾⣶⣾⡶⣱⣷⡿⣹⣿⣿⣿⡟⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⢁⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⢟⡽⠋⠇⠀⠉⠒⠖⠊⠁⠀⠀⠊⡻⡟⣼⣿⣿⢳⣿⣿⣿⣿⣧⠀⠹⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣿⣷⢸⣿⣿⡫⠓⠻⠠⣂⠈⠄⠀⠀⠀⠀⢀⠔⠁⣰⣷⣼⣿⣿⣿⣚⠿⣿⣿⣿⣿⡄⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⣾⣿⣿⣿⣿⡿⢯⣿⣿⠏⠀⠀⠂⢁⠋⠄⠀⠱⡄⠀⠐⠁⠀⡰⡋⢯⣿⣿⣿⡏⠉⠙⠚⢝⢿⣿⣿⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⣼⣿⣿⣿⡿⠋⠀⣼⣿⠏⠀⠀⠐⠀⠂⠀⠈⠀⠀⠈⠁⠀⠀⣼⠌⡀⠈⢼⣿⣿⣧⠀⠀⠀⠀⠀⠻⣿⢻⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⡿⣿⣿⣿⡿⠁⠀⣰⣿⣯⠂⠀⠀⢆⠂⠀⡠⡀⠈⢄⠀⠀⡠⢀⠙⠐⡀⠁⠚⣿⣿⣿⡄⠀⢴⠀⠀⠀⢹⣾⣿⣟⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣹⣿⣿⠁⠀⣰⣿⢯⡷⠀⠀⢠⠂⡠⠊⠀⠀⠁⠢⢳⠀⠀⠀⠀⡄⠈⢀⠀⡟⣿⣿⣷⡀⢸⠀⠀⠀⣾⣿⣿⣹⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣹⣿⣿⣇⣿⠁⢆⣼⣿⠏⣸⡄⠀⠀⠀⠊⠀⠀⠀⡀⠀⠄⠁⠀⠀⠀⠀⠀⠀⠀⡀⠃⠘⢿⣿⣷⣸⠀⠀⠀⣿⣿⣷⡻⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⢿⣷⣻⣿⣿⡇⣠⣾⣿⡟⠀⣿⠀⠀⠀⠇⡐⠂⠈⠀⡠⠀⠂⠀⠁⠈⠂⠀⠘⠀⢀⠀⠀⠀⢩⢿⣿⣿⡄⠀⠀⢻⣿⣿⢹⣜⢿⣿⣿⣿⣄⠀⠀⠀
⠀⣴⣿⣿⣿⠃⣾⣿⢣⣿⣿⢱⣿⣿⣿⠃⢰⡏⠀⠀⠀⠂⠀⠁⡠⠪⠈⠀⠠⠀⡀⠀⠀⠡⡀⡀⡀⠀⡀⠀⠀⢯⣻⣿⣿⣆⠀⠈⣿⣿⣇⢿⣯⣿⣿⣿⣿⣷⡄⠀
⢸⣿⣿⣿⠇⠀⢿⣿⣿⣿⢃⣿⣿⣿⣿⠄⢸⠁⠀⠀⢘⣀⣵⡊⠀⠀⠀⢀⡀⠀⠀⠁⠐⠀⠔⣵⣄⣀⣠⠀⠀⠈⣷⡹⣿⣿⡇⠌⠘⣿⣿⡼⣿⡇⠙⢿⣿⣿⣿⡆
⢸⠻⣿⣿⠀⢀⣼⣿⣿⠃⢸⡿⣿⣿⣿⠀⡜⠀⠀⠀⡄⠀⢀⣀⣀⣀⢁⣀⡸⣍⣁⣠⣃⡸⠉⠀⠀⢀⣘⠀⠀⠀⠸⡇⣿⣿⡏⠀⠀⢹⣿⣿⣿⣿⠀⠀⢹⣿⣿⡇
⠀⠀⠈⢻⣴⣿⣿⣿⠃⠀⠸⡇⣿⣿⣿⠀⠂⠀⠀⠀⠛⠛⣶⣶⣿⣿⣮⣿⣵⣾⠿⠿⠿⠷⠾⠿⠿⢷⣶⡄⠀⠀⠀⣿⣿⣿⠃⠀⠀⠈⠹⣿⣧⡻⠀⠀⢸⣿⣿⡇
⠀⣄⣴⣿⣿⡿⠋⠂⠀⠀⠀⣇⣿⣿⣿⡈⠀⠀⠀⢠⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⣟⣿⣿⠀⠀⠀⡇⠀⠹⣿⣿⣄⠀⢸⣿⣿⠀
⠀⠈⠉⠉⠉⠀⠒⠒⠒⠀⠀⠛⠛⠛⠻⠃⠠⠤⠤⠤⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠤⠼⠿⠧⠀⠀⠐⠛⠛⠃⠀⠒⠒⠃⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀

'''

text1 = '''\n\t        ╒═══════════════════════════╕
         \t│ NGL SPAMMER TOOL BY 124Z  │
         \t╘═══════════════════════════╛'''

url = "https://ngl.link/api/submit"


def send_attack(username, message, payload):

    print(tabulate([['PRESS ENTER TO START','CTRL+C TO STOP']], tablefmt='fancy_grid'))
    input()
    while True:
        game = ['','confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
        gameslug = random.choice(game)
        random_cookie: str = generate_cookie()
        user_agent: str = generate_random_user_agent()
       
        try:
            headers = {
                "Accept": "*/*",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": f'{random_cookie}',
                "Host": "ngl.link",
                "Origin": "https://ngl.link",
                "Referer": f"https://ngl.link/{username}",
                "User-Agent": f"{user_agent}",
            }

            data = {
                "username": f"{username}",
                "question": f"{message}",
                "deviceId": str(uuid.uuid4()),
                "gameSlug": f"{gameslug}"
            }

            response = requests.post(url, headers=headers, data=data)
            responde_Code: int = response.status_code
            time.sleep(1)
            if responde_Code == 429:
                print(tabulate([[f'{payload}','message has not been sent to ',f'{username}']], tablefmt='fancy_grid'))
                # time.sleep(10)
            elif responde_Code == 200:
                print(tabulate([[f'{payload}','message has been sent to ',f'{username}']], tablefmt='fancy_grid'))
        except KeyboardInterrupt:
            return menu()

def menu():
    os.system('clear')
    print(Colorate.Diagonal(Colors.DynamicMIX((pheart, dark)), (text)))
    print(((pheart)), (text1))

    text2 = '\n\t\t1. CUSTOM SPAM    0. EXIT \n\t\t2. SPAM HEART \n\t\t3. SPAM FUCK\n\t\t4. INBOX CRASH'
    print(((pheart)), (text2))
    select: str = input('\n\t\t[?] DEDSEC: ')
    if select == '1':
        os.system('clear')
        print(Colorate.Diagonal(Colors.DynamicMIX((pheart, dark)), (text)))
        print(((pheart)), (''))
        print(tabulate([['TYPE YOUR CRUSH USERNAME ','TYPE YOUR MESSAGE']], tablefmt='fancy_grid'))
        username = input(' [?] USERNAME: ')
        message = input(' [?] MESSAGE: ')
        send_attack(username, message, payload=message)
    elif select == '2':
        os.system('clear')
        print(Colorate.Diagonal(Colors.DynamicMIX((pheart, dark)), (text)))
        print(((pheart)), (''))
        print(tabulate([['TYPE YOUR CRUSH USERNAME']], tablefmt='fancy_grid'))
        username = input(' [?] USERNAME: ')
        heart = ''''
        💗💗💗💗💗💗💗💗💗💗
            I LOVE YOUUU
        '''
        send_attack(username, heart, payload='HEART')
    elif select == '3':
        os.system('clear')
        print(Colorate.Diagonal(Colors.DynamicMIX((pheart, dark)), (text)))
        print(((pheart)), (''))
        print(tabulate([['TYPE YOUR CRUSH USERNAME']], tablefmt='fancy_grid'))
        username = input(' [?] USERNAME: ')
        fuck = '''
        ....................../´¯/) 
        ....................,/¯../ 
        .................../..../ 
        ............./´¯/'...'/´¯¯`·¸ 
        ........../'/.../..../......./¨¯\ 
        ........('(...´...´.... ¯~/.'...') 
        .........\.................'...../ 
        ..........''...\.......... _.·´ 
        ............\..............(
        '''
        send_attack(username, fuck, payload='FUCK')
    elif select == '4':
        os.system('clear')
        print(Colorate.Diagonal(Colors.DynamicMIX((pheart, dark)), (text)))
        print(((pheart)), (''))
        print(tabulate([['TYPE YOUR CRUSH USERNAME']], tablefmt='fancy_grid'))
        username = input(' [?] USERNAME: ')
        crash = ''''
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗💗
        '''
        send_attack(username, crash, payload='Inbox crash exploit')
    elif select == '0':
        os.system('clear')
        sys.exit('BYE BYE!')
    else:
        os.system('clear')
        sys.exit('BYE BYE!')

menu()