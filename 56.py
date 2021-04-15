try:
    import requests
    from colorama import *
    import os
    import sys
    from time import sleep
    import json
    from pywebcopy import save_webpage
    import socket
    import threading
    import concurrent.futures
    from pprint import pprint
    import platform
    from bs4 import BeautifulSoup as bs
    import random
except Exception as e:
    print('\033[1;31m[-] Missing Modules')
    exit()
r = requests.session()
lock = threading.Lock()
red = "\033[1;31m" 
blue = "\033[1;34m"
cyan = "\033[1;36m"
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
sratar = [f'{red}[{blue}!{red}]',f'{red}[{blue}?{red}]',f'{red}[{blue}*{red}]',f'{red}[{blue}#{red}]',f'{red}[{blue}${red}]']
hcise = random.choice(sratar)
allcolorise = [red, blue, cyan]
raall = random.choice(allcolorise)

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def Banner():
    clear()
    print(f'''
  {red}███████╗{blue} █████╗
  {red}██╔════╝{blue}██╔═══╝
  {red}██████╗ {blue}██████╗
  {red}╚════██╗{blue}██╔══██╗
  {red}██████╔╝{blue}╚█████╔╝
  {red}╚═════╝ {blue} ╚════╝  ''')
    print(f' {raall}_'*21)
    print(' ')
    print( f' {red}[{blue}**{red}] {blue}By Wardencraz || @i0.wf')
    print(f''' {red}[{blue}01{red}] {cyan}Port Scanner           {red}[{blue}10{red}] {cyan}Reverse IP
 {red}[{blue}02{red}] {cyan}DDOS {red}[ {blue}SOON {red}]          {red}[{blue}11{red}] {cyan}Domian Info
 {red}[{blue}03{red}] {blue}[ {red}CLOSED {blue}]             {red}[{blue}12{red}] {cyan}GEOIP Lookup 2
 {red}[{blue}04{red}] {cyan}Webpage Cloner         {red}[{blue}13{red}] {cyan}Evil Net {OKGREEN}[@Matrix0700 | Twitter]
 {red}[{blue}05{red}] {cyan}BIN DATA               {red}[{blue}14{red}] {cyan}Hosting Finder
 {red}[{blue}06{red}] {cyan}Packet Sniffer {red}[ {blue}SOON {red}]          
 {red}[{blue}07{red}] {cyan}Availability Email    
 {red}[{blue}08{red}] {cyan}SubDoamin           
 {red}[{blue}09{red}] {blue}[ {red}CLOSED {blue}]''')
    option = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option == '1':
        PortScanner()
    elif option == '2':
        ddos()
    elif option == '3':
        Lagger()
    elif option == '4':
        Sitecloneing()
    elif option == '5':
        CMS()
    elif option == '6':
        PacketSniffer()
    elif option == '7':
        BruteNET()
    elif option == '8':
        ssltlsscan()
    elif option == '9':
        closed2()
    elif option == '10':
        reverseip()
    elif option == '11':
        Domaininfo()
    elif option == '12':
        geoip2()
    elif option == '13':
        Evilnet()
    elif option == '14':
        smsb0mber()
def PortScanner():
    clear()
    print(f'''

 {red}██████╗░░█████╗░██████╗░████████╗  {blue}░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
 {red}██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  {blue}██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
 {red}██████╔╝██║░░██║██████╔╝░░░██║░░░  {blue}╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
 {red}██╔═══╝░██║░░██║██╔══██╗░░░██║░░░  {blue}░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
 {red}██║░░░░░╚█████╔╝██║░░██║░░░██║░░░  {blue}██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
 {red}╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  {blue}╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝    
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Port Scanner
 {red}[{blue}99{red}] {cyan}Return To Main Menu    
''')
    option1 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option1 == '1':
        port0 = input(f' {blue}[{red}??{blue}] {red}Enter IP/Domain {cyan}: ')
        port = 'https://api.hackertarget.com/nmap/?q='+port0
        info = requests.get(port)
        print(OKGREEN,info.text)
    elif option1 == '99':
        clear()
        Banner()
def ddos():
    clear()
    print(f'''
 {red}██████╗ ██████╗{blue}  █████╗  ██████╗
 {red}██╔══██╗██╔══██╗{blue}██╔══██╗██╔════╝
 {red}██║  ██║██║  ██║{blue}██║  ██║╚█████╗
 {red}██║  ██║██║  ██║{blue}██║  ██║ ╚═══██╗
 {red}██████╔╝██████╔╝{blue}╚█████╔╝██████╔╝
 {red}╚═════╝ ╚═════╝  {blue}╚════╝╚═════╝
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}DDOS {cyan}[ {red}SOON {cyan}]
 {red}[{blue}99{red}] {cyan}Return To Main Menu    
''')
    option2 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option2 == '1':
        print(f' {blue}SOON{red}...')    
    elif option2 == '99':
        clear()
        Banner()
def Lagger():
    clear()
    Banner()
def Sitecloneing():
    clear()
    print(f'''

 {red}░██╗░░░░░░░██╗███████╗██████╗░██████╗░░█████╗░░██████╗░███████╗  {blue}░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
 {red}░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔════╝  {blue}██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
 {red}░╚██╗████╗██╔╝█████╗░░██████╦╝██████╔╝███████║██║░░██╗░█████╗░░  {blue}██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
 {red}░░████╔═████║░██╔══╝░░██╔══██╗██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░  {blue}██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
 {red}░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░░░░██║░░██║╚██████╔╝███████╗  {blue}╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
 {red}░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝  {blue}░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝    
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Webpage Cloner
 {red}[{blue}99{red}] {cyan}Return To Main Menu    
''')
    option4 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option4 == '1':
        webpageurl = input(f' {red}[{blue}**{red}] {blue}Enter URL {red}: ')
        kwargs = {'project_name': 'site folder'}
        save_webpage(
        url=webpageurl,
        project_folder='C:/',
        **kwargs
)
    elif option4 == '99':
        clear()
        Banner()
def CMS():
    clear()
    print(f'''
 {red}██████╗░██╗███╗░░██╗   {blue}██████╗░░█████╗░████████╗░█████╗░
 {red}██╔══██╗██║████╗░██║   {blue}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
 {red}██████╦╝██║██╔██╗██║   {blue}██║░░██║███████║░░░██║░░░███████║
 {red}██╔══██╗██║██║╚████║   {blue}██║░░██║██╔══██║░░░██║░░░██╔══██║
 {red}██████╦╝██║██║░╚███║   {blue}██████╔╝██║░░██║░░░██║░░░██║░░██║   
 {red}╚═════╝░╚═╝╚═╝░░╚══╝   {blue}╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}BIN Data
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option5 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option5 == '1':
        binby = input(f' {red}[{blue}**{red}] {blue}Enter BIN : ')
        binurl = f'https://input.payapi.io/v1/api/fraud/bindata/{binby}'
        binreq = r.get(binurl)
        if ('{"error":"Request failed; Bin data not found."}') in binreq.text:
            print(f' {red} Error')
            exit()
        print(binreq.text)
        #mainbin = binreq.json()["bin"]
        #binbrand = binreq.json()["brand"]
        #bincountrycode = binreq.json()["countryCode"]
        #bincountry = binreq.json()["countryName"]
        #binbank = binreq.json()["bankName"]
        #binxradty = binreq.json()["cardType"]
        #bincardcat = binreq.json()["cardCategory"]
        #print(f' {red}[{blue}**{red}] {blue}BIN : ' + red + str(mainbin))
        #print(f' {red}[{blue}**{red}] {blue}Brand : ' + red + binbrand)
        #print(f' {red}[{blue}**{red}] {blue}Country Code : ' + red + bincountrycode)
        #print(f' {red}[{blue}**{red}] {blue}Country : ' + red + bincountry)
        #print(f' {red}[{blue}**{red}] {blue}Bank : ' + red + binbank)
       # print(f' {red}[{blue}**{red}] {blue}Card Type : ' + red + binxradty)
       # print(f' {red}[{blue}**{red}] {blue}bincardcat : ' + red + bincardcat)
    elif option5 == '99':
        clear()
        Banner()
def PacketSniffer():
    clear()
    print(f'''    
 {red}██████╗░░█████╗░░█████╗░██╗░░██╗███████╗████████╗  {blue}░██████╗███╗░░██╗██╗███████╗███████╗███████╗██████╗░
 {red}██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝  {blue}██╔════╝████╗░██║██║██╔════╝██╔════╝██╔════╝██╔══██╗
 {red}██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░  {blue}╚█████╗░██╔██╗██║██║█████╗░░█████╗░░█████╗░░██████╔╝
 {red}██╔═══╝░██╔══██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░  {blue}░╚═══██╗██║╚████║██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══██╗
 {red}██║░░░░░██║░░██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░  {blue}██████╔╝██║░╚███║██║██║░░░░░██║░░░░░███████╗██║░░██║
 {red}╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  {blue}╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝    
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Packet Sniffer {red}[ {blue}SOON {red}]
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option7 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option7 == '1':
        print(f' {red}[ {blue}SOON {red} ]')
    elif option7 == '99':
        clear()
        Banner()
def BruteNET():
    clear()
    print(f'''
 {red}░█████╗░██╗░░░██╗░█████╗░██╗██╗░░░░░░█████╗░██████╗░██╗░░░░░███████╗  {blue}███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░
 {red}██╔══██╗██║░░░██║██╔══██╗██║██║░░░░░██╔══██╗██╔══██╗██║░░░░░██╔════╝  {blue}██╔════╝████╗░████║██╔══██╗██║██║░░░░░
 {red}███████║╚██╗░██╔╝███████║██║██║░░░░░███████║██████╦╝██║░░░░░█████╗░░  {blue}█████╗░░██╔████╔██║███████║██║██║░░░░░
 {red}██╔══██║░╚████╔╝░██╔══██║██║██║░░░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░  {blue}██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░
 {red}██║░░██║░░╚██╔╝░░██║░░██║██║███████╗██║░░██║██████╦╝███████╗███████╗  {blue}███████╗██║░╚═╝░██║██║░░██║██║███████╗
 {red}╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝  {blue}╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Availability Email
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option7 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option7 == '1':
        doemail = input(f' {red}[{blue}**{red}] {blue}Enter Email {red}: ')
        dourl = f'https://api.2ip.me/email.txt?email={doemail}'
        doreq = r.get(dourl)
        doresponse = doreq.text
        if ("true") in doresponse:
            print(f' {OKGREEN}[**] Available Email')
        elif ("false") in doresponse:
            print(f' {red}[**] Falied To Find Email')
    elif option7 == '99':
        clear()
        Banner()
def ssltlsscan():
    clear()
    print(f'''  
{red} ░██████╗██╗░░░██╗██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░██╗███╗░░██╗
{red} ██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║
{red} ╚█████╗░██║░░░██║██████╦╝██║░░██║██║░░██║██╔████╔██║███████║██║██╔██╗██║
{red} ░╚═══██╗██║░░░██║██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██╔══██║██║██║╚████║
{red} ██████╔╝╚██████╔╝██████╦╝██████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║██║░╚███║
{red} ╚═════╝░░╚═════╝░╚═════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝ 
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}SubDomain
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option8 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option8 == '1':
        dimainandip = input(f' {red}[{blue}**{red}] {blue}Enter IP/Domain {red}: ')
        os.system('cd Extensions/Sublister && python sublist3r.py -d '+ dimainandip)
    elif option8 == '99':
        clear()
        Banner()
def closed2():
    clear()
    Banner()
def reverseip():
    clear()
    print(f'''
 {red}██████╗░███████╗██╗░░░██╗███████╗██████╗░░██████╗███████╗  {blue}██╗██████╗░
 {red}██╔══██╗██╔════╝██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝  {blue}██║██╔══██╗
 {red}██████╔╝█████╗░░╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░  {blue}██║██████╔╝
 {red}██╔══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░  {blue}██║██╔═══╝░
 {red}██║░░██║███████╗░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗  {blue}██║██║░░░░░
 {red}╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝  {blue}╚═╝╚═╝░░░░░
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Reverse IP
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option10 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option10 == '1':
        doip = input(f' {red}[{blue}**{red}] {blue}Enter IP/Domain {red}: ')
        reserve = 'https://api.hackertarget.com/reverseiplookup/?q='+doip
        info = requests.get(reserve)
        print(OKGREEN,info.text)
    elif option10 == '99':
        clear()
        Banner()
def Domaininfo():
    clear()
    print(f'''
{red}██████╗░░█████╗░███╗░░░███╗░█████╗░██╗███╗░░██╗  {blue}██╗███╗░░██╗███████╗░█████╗░
{red}██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║  {blue}██║████╗░██║██╔════╝██╔══██╗
{red}██║░░██║██║░░██║██╔████╔██║███████║██║██╔██╗██║  {blue}██║██╔██╗██║█████╗░░██║░░██║
{red}██║░░██║██║░░██║██║╚██╔╝██║██╔══██║██║██║╚████║  {blue}██║██║╚████║██╔══╝░░██║░░██║
{red}██████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║██║░╚███║  {blue}██║██║░╚███║██║░░░░░╚█████╔╝
{red}╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  {blue}╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░    
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Domain Info
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option11 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option11 == '1':
        domain = input(f' {red}[{blue}**{red}] {blue}Enter Domain {red}: ')
        domainurl = f'https://input.payapi.io/v1/api/fraud/domain/age/{domain}'
        domainurl2 = f'https://input.payapi.io/v1/api/fraud/domain/{domain}'
        domainreq = r.get(domainurl)
        domainreq2 = r.get(domainurl2)
        domainip = domainreq2.json()["ip"]
        domainus = domainreq.json()["domain"]
        domaindays = domainreq.json()["message"]
        domainproxy = domainreq2.json()["isIpProxy"]
        domaincountryname = domainreq2.json()["countryName"]
        domainregion = domainreq2.json()["regionName"]
        domaincity = domainreq2.json()["city"]
        print(f' {red}[{blue}**{red}] {blue}Domain : ' + red + domainus)
        print(f' {red}[{blue}**{red}] {blue}Domain Age : ' + red + domaindays)
        print(f' {red}[{blue}**{red}] {blue}Domain IP : ' + red + domainip)
        print(f' {red}[{blue}**{red}] {blue}Is Domain IP Proxy ? : ' + red + str(domainproxy))
        print(f' {red}[{blue}**{red}] {blue}Domain Country : ' + red + domaincountryname)
        print(f' {red}[{blue}**{red}] {blue}Domain Region : ' + red + domainregion)
        print(f' {red}[{blue}**{red}] {blue}Domain City : ' + red + domaincity)
    elif option11 == '99':
        clear()
        Banner()
def geoip2():
    clear()
    print(f'''
{red}░██████╗░███████╗░█████╗░ {blue}██╗██████╗░
{red}██╔════╝░██╔════╝██╔══██╗ {blue}██║██╔══██╗
{red}██║░░██╗░█████╗░░██║░░██║ {blue}██║██████╔╝
{red}██║░░╚██╗██╔══╝░░██║░░██║ {blue}██║██╔═══╝░
{red}╚██████╔╝███████╗╚█████╔╝ {blue}██║██║░░░░░
{red}░╚═════╝░╚══════╝░╚════╝░ {blue}╚═╝╚═╝░░░░░
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}GEO2IP Lookup 2
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option12 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option12 == '1':
        geoip = input(f' {red}[{blue}**{red}] {blue}Enter IP {red}: ')
        geoipurl = f'https://ipapi.co/{geoip}/json/'
        georeq = r.get(geoipurl)
        geoip = georeq.json()["ip"]
        geover = georeq.json()["version"]
        geocity = georeq.json()["city"]
        georegion = georeq.json()["region"]
        georgcode = georeq.json()["region_code"]
        geocountry = georeq.json()["country"]
        geocountrycode = georeq.json()["country_code"]
        geocountryco3 = georeq.json()["country_code_iso3"]
        geocountrycap = georeq.json()["country_capital"]
        geotld = georeq.json()["country_tld"]
        geopostal = georeq.json()["postal"]
        geolat = georeq.json()["latitude"]
        geolong = georeq.json()["longitude"]
        geotimezone = georeq.json()["timezone"]
        geocalling = georeq.json()["country_calling_code"]
        geocurrency = georeq.json()["currency"]
        geonamecurrency = georeq.json()["currency_name"]
        geolan = georeq.json()["languages"]
        print(f' {red}[{blue}**{red}] {blue}IP : ' + red + geoip)
        print(f' {red}[{blue}**{red}] {blue}IP Version : ' + red + geover)
        print(f' {red}[{blue}**{red}] {blue}City : ' + red + geocity)
        print(f' {red}[{blue}**{red}] {blue}Region : ' + red + georegion)
        print(f' {red}[{blue}**{red}] {blue}Region Code : ' + red + georgcode)
        print(f' {red}[{blue}**{red}] {blue}Country : ' + red + geocountry)
        print(f' {red}[{blue}**{red}] {blue}Country Code  : ' + red + geocountrycode)
        print(f' {red}[{blue}**{red}] {blue}Country Code 2 : ' + red + geocountryco3)
        print(f' {red}[{blue}**{red}] {blue}Country Capital : ' + red + geocountrycap)
        print(f' {red}[{blue}**{red}] {blue}Country TLD : ' + red + geotld)
        print(f' {red}[{blue}**{red}] {blue}Postal  Code : ' + red + geopostal)
        print(f' {red}[{blue}**{red}] {blue}Latitude : ' + red + str(geolat))
        print(f' {red}[{blue}**{red}] {blue}Longitude : ' + red + str(geolong))
        print(f' {red}[{blue}**{red}] {blue}Time Zone : ' + red + geotimezone)
        print(f' {red}[{blue}**{red}] {blue}Country Calling Code : ' + red + geocalling)
        print(f' {red}[{blue}**{red}] {blue}Currency Code : ' + red + geocurrency)
        print(f' {red}[{blue}**{red}] {blue}Currency : ' + red + geonamecurrency)
        print(f' {red}[{blue}**{red}] {blue}Languages : ' + red + geolan)
    elif option12 == '99':
        clear()
        Banner()
def Evilnet():
    clear()
    os.system('cd Extensions/Evilnet && python evilnet.py')
def smsb0mber():
    clear()
    print(f'''
 {red}██╗░░██╗░█████╗░░██████╗████████╗██╗███╗░░██╗░██████╗░  {blue}███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
 {red}██║░░██║██╔══██╗██╔════╝╚══██╔══╝██║████╗░██║██╔════╝░  {blue}██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
 {red}███████║██║░░██║╚█████╗░░░░██║░░░██║██╔██╗██║██║░░██╗░  {blue}█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
 {red}██╔══██║██║░░██║░╚═══██╗░░░██║░░░██║██║╚████║██║░░╚██╗  {blue}██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
 {red}██║░░██║╚█████╔╝██████╔╝░░░██║░░░██║██║░╚███║╚██████╔╝  {blue}██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
 {red}╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  {blue}╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
''')
    print(f'''
 {red}[{blue}01{red}] {cyan}Hosting Finder
 {red}[{blue}99{red}] {cyan}Return To Main Menu   
''')
    option14 = input(f' {red}[{blue}**{red}] {blue}Select {red}: ')
    if option14 == '1':
        hostingdo = input(f' {red}[{blue}**{red}] {blue}Enter Domain {red}: ')
        hostingurl = f'https://api.2ip.me/hosting.json?site={hostingdo}'
        hostingreq = r.get(hostingurl)
        hostingname = hostingreq.json()["name_ripe"]
        print(f' {red}[{blue}**{red}] {blue}Hosting : ' + red + hostingname)
    elif option14 == '99':
        clear()
        Banner()
Banner()