import requests
import time
import os,sys,random
class Api_ig:
    def __init__(self,cookie):
        self.cookie = cookie
        self.headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': self.cookie,
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/p/DBHIlVQyw8s/?utm_source=ig_web_copy_link',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="129.0.6668.60", "Not=A?Brand";v="8.0.0.0", "Chromium";v="129.0.6668.60"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-bloks-version-id': '1fbbc4a302825e0a86a865a39546a4fa9f0b70d85f967657fb4bb32422a40f5c',
    'x-csrftoken': self.cookie.split('csrftoken=')[1].split(';')[0],
}
        
    def like(self,id):
        data = {
        'av': '17841463976553652',
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': 'p',
        '__hs': '20011.HYP:instagram_web_pkg.2.1..0.1',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1017345987',
        '__s': 'b499oe:jq6ibt:qj8c7j',
        '__hsi': '7425956412009585319',
        '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o1DU2_CwjE1xoswaq0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9O1TwQzXwae4UaEW2G0AEco5G0zK5o4q3y1Sx-0lKq2-azqwt8d-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2O4UrAwHxW1oCz8rwHwrE5SEy9w',
        '__csr': 'gD7gqhIavkaN9y48HlhBZbqHAkBrWFqJ5FllaKCAGDV9Wh9FFr-Ftat2J6z7zFJaTBy5ACqyVpf8m8y8yUlBAoSbz8yu8ze8DKaxp2pByV8G-EG4UG4Kh29kpuit4BCzUV3XwJyUG8Gi4U01euU2Nwik0hi2O0kaqt2FE1pde3tw5pw1CK0u0zwdl2E1iU0AxqwQxAEkwm8zB5wko7i0ii1fqgK2h2A6RfeV27wbxsUHg5u0myq0OE5q0Q8co3Owgk02xC01m-w2C8',
        '__comet_req': '7',
        'fb_dtsg': 'NAcO5YZaiI4yIUckXZzN94rV_ZbkIHbtHkYSPzAOMJzLS7iuDXTgt0g:17865068956001195:1728736147',
        'jazoest': '26352',
        'lsd': 'X75RNmje5WVfzVL-Ea0r-t',
        '__spin_r': '1017345987',
        '__spin_b': 'trunk',
        '__spin_t': '1728990211',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'usePolarisLikeMediaLikeMutation',
        'variables': '''

            {
            "media_id": "'''+id+'''",
            "container_module": null,
            "inventory_source": null,
            "ranking_info_token": null,
            "nav_chain": null
            }

            ''',
        'server_timestamps': 'true',
        'doc_id': '8552604541488484',
            }
        a = requests.post('https://www.instagram.com/graphql/query',headers=self.headers,data=data)
    def unlike(self,id):
        data = {
                'av': '17841463976553652',
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': 'w',
                '__hs': '20067.HYP:instagram_web_pkg.2.1.0.0.1',
                'dpr': '1',
                '__ccg': 'GOOD',
                '__rev': '1018751871',
                '__s': 'z8aele:imtjcp:fq6vw9',
                '__hsi': '7446692498273804459',
                '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o1DU2_CwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2swtUd8-U2zxe2GewGw9a361qw8Xxm16wUwtE1uVEbUGdG1QwTU9UaQ0Lo6-3u2WE5B08-269wr86C1mwPwUQp1yUb8jK5V8aUuwm9EO6UaUaE4e1tG8BK4o',
                '__csr': 'gnglNk5DsSIAoRilGIysgAZajirS_t5jmVlBQmH-iq8hsxbyFUhGmAHQAmdXX-jVu5aDtrKdpuiUCnyoHy48gycyV8ObhWh5xJ5yqKSHDLVEhyHQehQq9x2FHyWUgyoTAeBiCo8Aq8yo01g-U4te08hzqwrU6K0Lk0CU3IwdS2Svo1Lo6JyE0ye0eFwbyVnw129rDBig9okyEGO0l16tVWiw28EZ4cClr6zQ12A8mdQ1OwTF9ixCl0iE5W1jCkM7C5Hxt7xy0SUaoe83uwZ2wCYwk5o2dwBy8Ghw0zXhFQ01luw1fy0fZw1US',
                '__comet_req': '7',
                'fb_dtsg': 'NAcPHxu8O_93_Ttyz1kZ5SRg9HvsJF-PX4sgqY5I3BfQ_eWCzarK8xA:17843708194158284:1732955500',
                'jazoest': '26219',
                'lsd': 'Ftl-_viq8yWO_q6ijJJZzp',
                '__spin_r': '1018751871',
                '__spin_b': 'trunk',
                '__spin_t': '1733818207',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'usePolarisLikeMediaUnlikeMutation',
                'variables': '''
{
  "media_id": '''+id+''',
  "container_module": "single_post",
  "inventory_source": null,
  "ranking_info_token": null,
  "nav_chain": "null"
}
            ''',
                'server_timestamps': 'true',
                'doc_id': '8525474704176507',
            }
        un = requests.post('https://www.instagram.com/graphql/query',headers=self.headers,data=data).text
        return un
    def follow(self,target_user_id):
        data = {
                
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': '27',
                '__hs': '20018.HYP:instagram_web_pkg.2.1..0.1',
                'dpr': '1',
                '__ccg': 'UNKNOWN',
                '__rev': '1017538317',
                '__s': 'cyi8q2:kpt43i:qi9c9v',
                '__hsi': '7428485612332142635',
                '__dyn': '7xeUjG1mxu1syaxG4Vp41twpUnwgU7SbzEdF8aUco2qwJyEiw9-1DwUx60p-0LVE4W0om78c87m0yE462mcw5Mx62G5UswoEcE7O2l0Fwqo31w9a9waOfK0zEkxe2GewGw9a3614xm0zK5o4q3y261kx-0lKq2-azqwt8d-2u2J08O321LwTwKG1pg2fwxyo6O1FwlEcUed6goK3ibxKi2qiUqwm9EO6UaU3cG8BK4o',
                '__csr': '8Yr22SJZsSYZcZPECy9sOEJFv8x9e_WpdF22JvRKAQV9vAaiFAJkl4Bh9dGn8iWp8ymhpp5mmSit7AjmETByQaKUjy9pUBqVEOiu8AxuaZaKh394teGBDGvAAG8GXzooK5ESvmvxbzopyoSfyFEzUox6U06yV00diGOUe96EhBzZw2_QGG0gu2cODgSHw968gjwE80Aagx163qkm1gwpUdp7g0I6yG4k4U1bU4ne0Fo2-xC8w72gcLjDz2AzA0xqxq5-cCy8W1QQ481L0C4k4YUcU2Cw9l0Rw8N0z28-m1cg4W4K9o5lhUNw92OyE7y4EhBhE2EG363mm13w7QaFR2awAg9QgAUnyQ1-wtE0zmrBwbeUlwLo0Yqu1mxaQm0gC1fBx-axe2aZo2wyFE7y9o0aNU09r-it2aTwrU0JWK2pxK0BVQaw7Cz80y1zqwai2O0kLw-wRw',
                '__comet_req': '7',
                'fb_dtsg': 'NAcPUaEwOII6I1Hb3gj1Q_ZlKUJD_wfiS35jvm5pmyIVG5MguCFRMwA:17865068956001195:1728736147',
                'jazoest': '26179',
                'lsd': 'tP8SLtrdcEQZFS6mkwuP-9',
                '__spin_r': '1017538317',
                '__spin_b': 'trunk',
                '__spin_t': '1729579086',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'usePolarisFollowMutation',
                'variables': '''{
                            "target_user_id": "'''+target_user_id+'''",
                            "container_module": "profile",
                            "nav_chain": "PolarisFeedRoot:feedPage:2:topnav-link,PolarisProfilePostsTabRoot:profilePage:3:unexpected,PolarisProfilePostsTabRoot:profilePage:4:unexpected"
                            }''',
                'server_timestamps': 'true',
                'doc_id': '7275591572570580',
            }
        
        follow = requests.post('https://www.instagram.com/graphql/query',headers=self.headers,data=data).json()
        
          
        return follow['data']['xdt_create_friendship']['friendship_status']['following']
        
    def ten(self):
        response = requests.get('https://www.instagram.com/', headers=self.headers).text
        ten = response.split('"username":"')[1].split('"')[0]
        return ten
class get_job_hustMedia:
    def __init__(self,apikey):
        self.apikey = apikey
        self.headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        
        'origin': 'https://hust.media',
        'priority': 'u=1, i',
        'referer': 'https://hust.media/reactapp/sunflower/insta/timcheo?webappmode=showadview',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        }
    def getJob(self,theloai,social):
        json_data = {

        'key': self.apikey,
        'chedo': 'getjop',
        'theloai': theloai,
        'social': social,

            }
        response = requests.post('https://hust.media/insta/profile.php', headers=self.headers, json=json_data).json() 
        return response
    def receive_money(self,idpost,theloai,social):
        data = {
            'key':  self.apikey,
            'idpost':idpost,
            'theloai': theloai,
            'social':social, }   
        a = requests.post('https://hust.media/insta/nhantien.php', headers=self.headers,json = data).text
        return a
    def danngnhap(self):
        json_data = {
            'key': self.apikey,
            'chedo': 'kiemtradangnhap',}
        login = requests.post('https://hust.media/insta/profile.php',headers=self.headers,json=json_data).json()
        if 'message' in login:
            print('đăng nhập thành công')
            sodiem = login['sodiem']
            return sodiem
        else:
            print(login)
    def listnickchay(self,ten):
        # list cấu hình 
        data = {
            "chedo": "listcauhinh",
            "key":self.apikey}
        listnick = requests.post('https://hust.media/insta/profile.php',headers=self.headers,json=data).json()['listcauhinh']
        def datnickchay():
            for k in range(len(listnick)):
                nick = listnick[k]['tenfb']
                if  nick == ten:
                    return listnick[k]['idfacebook']  
                else:
                    continue
        # đặt nick chạy 
        json_data = {
                'key': self.apikey,
                'idfacebook': datnickchay(),
                'chedo': 'choncauhinh',
                'chedokiemxu': 1,
                'username_ig': '',
            }
        response = requests.post('https://hust.media/insta/profile.php', headers=self.headers, json=json_data).text
        for m in range(3):
            print('đặt nick thành công',end='\r')
            time.sleep(1)
if 'nt' in os.name:
    os.system('cls')
else:
    os.system('clear')
# màu 
do = '\033[31m'
xanhla ='\033[32m' 
xanhduong ='\033[34m'
vang ='\033[33m'
tim ='\033[35m'
xanhCyan ='\033[36m'
trang ='\033[37m'
chonmau = random.randint(3,8)

if chonmau == 3:
    mau = xanhla
elif chonmau == 4:
    mau = xanhduong
elif chonmau == 5:
    mau = xanhCyan
elif chonmau == 6:
    mau = tim
elif chonmau == 7:
    mau = trang
elif chonmau == 8:
    mau = vang
banner = f'''{mau}

 .-._        ,--.-,,-,--,                          _,.----.   
/==/ \  .-._/==/  /|=|  | _,..---._  .--.-. .-.-..' .' -   \  
|==|, \/ /, /==|_ ||=|, /==/,   -  \/==/ -|/=/  /==/  ,  ,-'  
|==|-  \|  ||==| ,|/=| _|==|   _   _\==| ,||=| -|==|-   |  .  
|==| ,  | -||==|- `-' _ |==|  .=.   |==|- | =/  |==|_   `-' \ 
|==| -   _ ||==|  _     |==|,|   | -|==|,  \/ - |==|   _  , | 
|==|  /\ , ||==|   .-. ,\==|  '='   /==|-   ,   |==\.       / 
/==/, | |- |/==/, //=/  |==|-,   _`//==/ , _  .' `-.`.___.-'  
`--`./  `--``--`-' `-`--`-.`.____.' `--`..---'                
                                                      {do} dev Nguyễn Huỳnh Đức  
'''
for m in banner:
    sys.stdout.write(m)
    sys.stdout.flush()
    time.sleep(0.0012)
print(f'{trang}-------------------------------------------------------------------------------------')
listfile = os.listdir()
if 'apikey.txt' in listfile and 'cookie.txt' in listfile:
    luachon = input(f'{xanhla}bạn có muốn đổi apikey hoặc cookie ko (n/y) : ')
    if luachon == 'n':
        apikey = open('apikey.txt','r').read()
        cookie = open('cookie.txt','r').read()
    elif luachon == 'y':
        luachon2 = input(f'{xanhCyan}bạn muốn đổi cookie(c) hay apikey(a) muốn đổi cả 2 nhấn (ca) : ')
        if luachon2 == 'a':
            nhapApikey1 = input(f'{xanhCyan}nhập apikey của bạn : ')
            writeApikey = open('apikey.txt','w').write(nhapApikey1)
            cookie = open('cookie.txt','r').read()
            apikey = open('apikey.txt','r').read()
        elif luachon2 == 'c':
            nhapCookie1 = input(f'{tim}nhập cookie nick bạn chạy : ')
            writeCookie = open('cookie.txt','w').write(nhapCookie1)
            apikey = open('apikey.txt','r').read()
            cookie = open('cookie.txt','r').read()
        elif luachon2 == 'ca':
            nhapApikey2 = input(f'{xanhCyan}nhập apikey của bạn : ')
            nhapCookie2 = input(f'{xanhduong}nhập cookie của ban : ')
            writeApikey2 = open('apikey.txt','w').write(nhapApikey2)
            writeCookie2 = open('cookie.txt','w').write(nhapCookie2)
            apikey = open('apikey.txt','r').read()
            cookie = open('cookie.txt','r').read()
        else:
            print(f'{do}nhập sai vui lòng vào lại tool')
            exit()
    else:
        print(f"{do}nhập sai vui lòng vào lại tool")
        exit()
elif 'apikey.txt' not in listfile and 'cookie.txt' not in listfile:
            nhapApikey2 = input(f'{tim}nhập apikey của bạn : ')
            nhapCookie2 = input(f'{xanhduong}nhập cookie của bạn : ')
            writeApikey2 = open('apikey.txt','w').write(nhapApikey2)
            writeCookie2 = open('cookie.txt','w').write(nhapCookie2)
            apikey = open('apikey.txt','r').read()
            cookie = open('cookie.txt','r').read()
 
hustmedia = get_job_hustMedia(apikey)
instagam = Api_ig(cookie)
def RunTim():
    loi = 0
    while True:
        get = hustmedia.getJob("timcheo","insta")
        mes = get['message']
        if "Hết Jop hoặc ấn hơi nhanh vui lòng tải lại danh sách" in mes:
            for i in range(30):
                print('hết job vui lòng chờ : '+str(i),'giây',end='\r')
                time.sleep(1)
        elif 'đăng nhập' in mes:
            print('đăng nhập thất bại')
            break
        else:
            for j in range(len(mes)-1):
                c = mes[j]
                mediaid = c['mediaid']
                work = instagam.like(mediaid)
                time.sleep(4)
                idpost = c['idpost']
                nhan = hustmedia.receive_money(idpost,"timcheo","insta")
                if 'error' in nhan:
                    for solannhan in range(1,4):
                        unlike = instagam.unlike(mediaid)
                        time.sleep(2)
                        instagam.like(mediaid)
                        print('bấm nhận lần : ',solannhan,end='\r')
                        nhan = hustmedia.receive_money(idpost,"timcheo","insta")
                        if 'mess' in nhan:
                            print(xanhCyan,nhan)
                            break
                        elif 'error' in nhan:
                            time.sleep(2)
                            continue
                        elif 'error' in nhan and solannhan == 4:
                            print(do+str(loi),idpost,nhan)
                            loi += 1
                        time.sleep(3)
                for k in range(6):
                    print('đang làm việc : '+str(k),end='\r')
                    time.sleep(0.7)
                print(xanhCyan,nhan)
def RunFollow():
    thanhcong = 1
    thatbai = 1
    nhanArr = []
    while True:
        get = hustmedia.getJob("subcheo","insta")
        mes = get['message']
        jopArr = []
        for jop in mes:
            jopArr.append(jop['idpost'])
        if "Hết Jop hoặc ấn hơi nhanh vui lòng tải lại danh sách" in mes:
            for i in range(30):
                print('hết job vui lòng chờ : '+str(i),'giây',end='\r')
                time.sleep(1)
        elif 'đăng nhập' in mes:
            print('đăng nhập thất bại')
            break
        for idpost in jopArr:
                if len(nhanArr) == 6:
                    for time1 in range(5):
                        print(f'{xanhCyan}==> đang nhận tiền',end ='\r')
                        time.sleep(0.4)
                    nhan = hustmedia.receive_money(','.join(nhanArr),"subcheo","insta")
                    if 'message' in nhan:
                        kq = nhan['message']
                        print(f'[{xanhla}success{trang}]',kq)
                        nhanArr = []
                    elif 'error' in nhan:
                        print(do+nhan)
                else:
                    for k in range(5):
                        print('đang làm việc : ',str(k),end='\r')
                        time.sleep(1)
                    work = instagam.follow(idpost)
                    if  work:
                        print(xanhCyan,str(thanhcong),f'{vang}follow thành công :))')
                        nhanArr.append(idpost)
                        time.sleep(0.4)
                        thanhcong += 1
                    else:
                        print(tim,str(thatbai),f'{do}follow flail :((')
                        time.sleep(0.4)
                        thatbai += 1
chon = input('chạy tim hay follow(t/f) : ')
for tg in range(5):
    print('8==> đang đăng nhập ',end='\r')
    time.sleep(0.5)
sodu = hustmedia.danngnhap()
print('so du instagam của bạn là : ',sodu)
for k in range(6):
    print('đang vào tools',end='\r')
    time.sleep(0.4)
ten = instagam.ten()
hustmedia.listnickchay(ten)
if 'nt' in os.name:
    os.system('cls')
else:
    os.system('clear')


hay = f''''    {do}
                                             
 ════════════════════════code by{xanhCyan} ᥫᩣđức{do}═══════════════════════
                      
                                               '''
print(hay)
if chon == 't':
    RunTim()
elif chon == 'f':
    RunFollow()

