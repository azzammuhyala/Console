#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AngelSecurityTeam/Cam-Hackers

def func_main():
  try:
    import requests, re , colorama ,random
    from requests.structures import CaseInsensitiveDict
    colorama.init()
      
    url = "http://www.insecam.org/en/jsoncountries/"
      
    headers = CaseInsensitiveDict()
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    headers["Cache-Control"] = "max-age=0"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "www.insecam.org"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
      
      
    resp = requests.get(url, headers=headers)
    
    data = resp.json()
    countries = data['countries']
    
    print("""
\033[1;31m\033[1;37m ██████╗ █████╗ ███╗   ███╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██╔════╝██╔══██╗████╗ ████║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║     ███████║██╔████╔██║█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
██║     ██╔══██║██║╚██╔╝██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
╚██████╗██║  ██║██║ ╚═╝ ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
\033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
\033[1;31m                                                                        ANGELSECURITYTEAM \033[1;31m\033[1;37m""")
    
    for key, value in countries.items():
      print(f'Code : (\033[36m{key}\033[0m) - \033[32m{value["country"]}\033[0m / (\033[35m{value["count"]}\033[0m)')
      #print("")

    country = input("\nCode(##) : ")
    num = 0
    res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]
    for page in range(int(last_page)):
      res = requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}", headers=headers)
      find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
      #with open(f'{country}.txt', 'w') as f:
      for ip in find_ip:
        #print("")
        num += 1
        print(f"\033[33m[\033[31m{num}\033[0m. '\033[32m{country}\033[0m' \033[37mlink\033[33m] \033[36m>>\033[1;32m", ip)
        #f.write(f'{ip}\n')
  except KeyboardInterrupt:
    print("\033[33mYou just terminated the program.\033[0m")
  except EOFError:
    print("\033[33mYou just terminated the program.\033[0m")
  except:
    print("Something error. Please check your connection...")
  finally:
    print("\033[1;37m\033[0m")
    #print('\033[37mSave File :'+country+'.txt')