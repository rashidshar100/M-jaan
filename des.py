#--> Tool -> LMNx9 FBX Gift
#--> Codded By -> DARK_LMNx9
 
#---------[ LMNx9 MODULE ]---------#
 
import os,sys,string,json,hashlib,random
from os import system as lmnxsys;import time
try:
    import requests
    import rich
    import faker
except ImportError:
    lmnxsys("pip install rich")
    lmnxsys("pip install requests")
    lmnxsys("pip install faker")
import rich,requests,faker
from faker import Faker
from rich import print
 
og='\x1b[38;5;208m';rd='\033[1;31m';gr='\033[1;32m';sk='\033[1;36m'
 #------------------[geet-pass]-------------#

    #====SCRIPT PASSWORD SYSTEM===
import getpass
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': lmnx9_string(32),
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = lmnx9_requests_call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    
#---------[ LMNx9 RESULT ]---------#
    
    print(f'''
[bold red]<[bold cyan]/[bold red]>[bold green] NAME      : [bold purple]{first_name} {last_name}
[bold red]<[bold cyan]/[bold red]>[bold green] EMAIL     : [bold violet]{email}
[bold red]<[bold cyan]/[bold red]>[bold green] UID       :[bold purple] {id}
[bold red]<[bold cyan]/[bold red]>[bold green] PASSWORD  : [bold violet]{password}
[bold red]<[bold cyan]/[bold red]>[bold green] BIRTHDAY  : [bold purple]{birthday} 
[bold red]<[bold cyan]/[bold red]> [bold green]GENDER    : [bold purple]{gender}
[bold red]<[bold cyan]/[bold red]> [bold green]TOOL      : [bold cyan]RASHID-SINDHI Gift
[bold red]<[bold cyan]/[bold red]>[bold green] TOKEN     : [bold violet]{token}
    ''');lnx()
    lmn_x=open('/sdcard/RASHID-SINDHI-Gift.txt','a')
    lmn_x.write(f"{email} | {password}\n")
    lmn_x.close()
 
#---------[ LMNx9 REQUEST CALL ]---------#
 
def lmnx9_requests_call(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()
 
#---------[ LMNx9 MAIN ]---------#
 
def LMNx9():
    logo();lnx()
    for i in range(int(input(f'{og}<{gr}+{og}> {gr}HOW MANY ACCOUNT NEED {sk}:{og} '))):
        lnx()
        email, password, first_name, last_name, birthday = lmnx9_account()
        if email and password and first_name and last_name and birthday:
            lmnx9_register(email, password, first_name, last_name, birthday)
 
#---------[ LMNx9 CONTROL ]---------#
 
if __name__ in "__main__":
    LMNx9();lnx()
    print(f"\n[bold red]<[bold cyan]✔[bold red]> [bold violet]ID's Saved - [bold green]/sdcard/RASHID-SINDHI-Gift.txt")
    input(f"{sk}<{gr}➤{sk}> {og}PRESS ENTER TO BACK MAIN")
    LMNx9()
    
#--------[-> Coded By - Limon_Hossain <-]--------
#----[-> Join - t.me/DARK_TEAM_LMNx9 <-]----
