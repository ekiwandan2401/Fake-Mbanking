import requests
from anticaptchaofficial.recaptchav2proxyless import *
import re
import rstr
import base64
import time
import colorama
from colorama import Fore, Back, Style


colorama.init(autoreset=True)
BCA = 'BCA'
BNI = 'BNI'
BRI = 'BRI'
BRI2 = 'BRI2'
MANDIRI = 'MANDIRI'

kuning = Fore.YELLOW + Style.BRIGHT
hijau = Fore.GREEN + Style.BRIGHT
merah = Fore.RED + Style.BRIGHT
biru = Fore.BLUE + Style.BRIGHT

print(hijau+"========================================")
print(hijau+"FAKE MOBILE BANKING / E-WALLET GENERATOR")
print(hijau+"Hanya Untuk Flexing")
print(kuning+"By : Eki ID")
print(kuning+"API : jnckmedia")
print(hijau+"========================================")
time.sleep(2)
print("Pilih Bank / E-Wallet")
print("1.BCA")
print("2.BNI")
print("3.BRI")
print("4.BRI (NEW APP)")
print("5.MANDIRI")
print(hijau+"========================================")
pilih_template = int(input("Masukkan Pilihan Lu:"))
try:    
    if pilih_template == 1:
        bank = BCA
        norek = input(kuning+"Masukan Norek :")
        saldo = input(kuning+"Jumlah Saldo :")
    elif pilih_template == 2:
        bank = BNI
        norek = input(kuning+"Masukan Norek :")
        saldo = input(kuning+"Jumlah Saldo :")
    elif pilih_template == 3:
        bank = BRI
        saldo = input(kuning+"Jumlah Saldo :")
        norek = ''
    elif pilih_template == 4:
        bank = BRI2
        saldo = input(kuning+"Jumlah Saldo :")
        norek = ''
    elif pilih_template == 5:
        norek = input(kuning+"Masukan Norek :")
        saldo = input(kuning+"Jumlah Saldo :")
        bank = MANDIRI
    else:
        print(merah+"Ga ada Blokk.....")
except Exception as e:
    raise e

if pilih_template < 6:
    print(hijau+"Proses Bypass Captcha....")
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("ENTER_YOUR_API")
    solver.set_website_url("https://jnckmedia.com/FakeMbank/")
    solver.set_website_key("6LfUEkYUAAAAAJkc9SMZop7EkjrIsE242wkJzTII")
    solver.set_soft_id(0)
    g_response = solver.solve_and_return_solution()
    print(hijau+"Bypass Captcha Selesai..")
    time.sleep(3)
    session = requests.Session()
    session.get('https://jnckmedia.com/FakeMbank/')
    headers = {
        'authority': 'jnckmedia.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryKQktBB7hsciV9EAk',
        'origin': 'https://jnckmedia.com',
        'referer': 'https://jnckmedia.com/FakeMbank/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = '------WebKitFormBoundaryKQktBB7hsciV9EAk\r\nContent-Disposition: form-data; name="template"\r\n\r\n'+bank+'\r\n------WebKitFormBoundaryKQktBB7hsciV9EAk\r\nContent-Disposition: form-data; name="norek"\r\n\r\n'+norek+'\r\n------WebKitFormBoundaryKQktBB7hsciV9EAk\r\nContent-Disposition: form-data; name="saldo"\r\n\r\n'+saldo+'\r\n------WebKitFormBoundaryKQktBB7hsciV9EAk\r\nContent-Disposition: form-data; name="g-recaptcha-response"\r\n\r\n'+g_response+'\r\n------WebKitFormBoundaryKQktBB7hsciV9EAk--\r\n'
    foo = rstr.digits(10)
    response = session.post('https://jnckmedia.com/FakeMbank/create',headers=headers, data=data)
    print(response.text)
    gambar = re.findall(r'<img src="data:image/png;base64,(.*?)"',response.text)[0]
    print(kuning+"Gambar Berhasil Disimpan =>"+'['+foo+'.jpg]')

    imgstring = gambar
    imgdata = base64.b64decode(imgstring)
    filename = ''+foo+'.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
else:
    print("GA ADA BLOKK")
