#import
import subprocess




# function get-password-wi-fi

def get_password(wifi_name : str, text : bool = True):

    command = f'netsh wlan show profile name="{wifi_name}" key=clear'

    result = subprocess.check_output(command, shell=True, text=True, errors="ignore")

    for line in result.split('\n'):

        if "Key Content" in line or "محتوى المفتاح" in line:

            password = line.split(":")[1].strip()

            break
    if text == True :
        print(f"password : {password}")
    elif text == False :
        return password



#function get-available-wi-fi

def get_available(text : bool = True):

    command = 'netsh wlan show networks'

    output = subprocess.check_output(command, shell=True, text=True, errors='ignore')



    if text == True :
        print('[+] available wi-fi :')
        print(output)
    elif text == False :
        return output


def get_ip_website(website : str, text : bool = True):

    command = f'ping -n 1 {website}'

    output = subprocess.check_output(command, shell=True, text=True, errors="ignore")

    ip = output.split("[")[1].split("]")[0]

    if text == True :
        print(f'ip : {ip}')
    elif text == False :
        return ip
    

def get_ip_humans(text : bool = True):
    command = 'arp -a'

    output = subprocess.check_output(command, shell=True, text=True, errors='ignore')

    if text == True :
        print('[+] ip humans :')
        print(output)
    elif text == False :
        return output