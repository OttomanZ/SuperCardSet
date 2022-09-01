import requests
import cv2
import numpy as np
import names
import random
import string
import uuid
import traceback
import progressbar
import time
import os
class GenerateDataset:
    '''
    This Classes Generates 10,000 Images 50% Visa / 50% MasterCard. This API uses a third party service, which I found on the internet.
    Use at your own Risk, I am not responsible for any malicious payloads from the original maintainer of the API.

    # Usage Examples

    img = GenerateDataset.generate_img('Visa','John Doe')
    '''

    def __init__(self):
        # generating 10,000 images of size 28x28
        print('[+] Sucessfully Loaded SuperCardSet ...')
        print('[DOCS] https://supercardset.muneeb.co/')
    def generate_dataset(self,ammount=10000):
        card_type = ['Visa','Mastercard']
        print('[INFO] Generating images...')
        # progress bar
        this_time = True
        for i in progressbar.progressbar(range(int(ammount))):
            # generate a random name
            name = names.get_full_name()
            name = name.replace(' ','+')
            if this_time:
                img = self.generate_img('Visa',name)
                card_type = 'Visa'
            if this_time == False:
                img = self.generate_img('MasterCard',name)
                card_type = 'MasterCard'
            
            this_time = not this_time
            # saving image to disk
            cv2.imwrite(f'{card_type}/{str(uuid.uuid4())}.png',img)

    def generate_img(self,type,username):
        try:
            standard_master = ['Gold','Platinum','Standard']
            standard = random.choice(standard_master)
            session = requests.session()
            burp0_url = f"https://herramientas-online.com:443/tarjvsmc.php?nombreth={username}&tj=4440542763922359&cl={standard}&mc={type}&co=IbboRH5F6VtNsccVpRwORcdzqc&code=6295"
            burp0_cookies = {"_tccl_visitor": "a0b69523-47ec-5daa-91c7-cd78fdb6b5b3", "_tccl_visit": "a0b69523-47ec-5daa-91c7-cd78fdb6b5b3", "_ga": "GA1.2.522911686.1662045066", "_gid": "GA1.2.1654263577.1662045066", "__gads": "ID=72c33a6f0724e5f9-226a070618d50021:T=1662045069:RT=1662045069:S=ALNI_MYaFyxsv1Pn1UYTs6SWJVV_4x4yCg", "__gpi": "UID=00000aad82fafef7:T=1662045069:RT=1662045069:S=ALNI_MaSSgV9uOfE-qhOy_UA0RdsokGFnA", "FCNEC": "[[\"AKsRol_hvBnEvJ_r8lqRCbh6kmLnr7kRAUCCAekpw889dyJs0TSkRL0yueRYckihtpL485C9q9SLTTNRHwMukki0p_EUjIqFpDGGxCowuQ3lCgVDlZWxYcwAXxdqliu3mNL7RU4974-C514i8NicDTw-yZ0Za7PfnA==\"],null,[]]"}
            burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
            output = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
            img = cv2.imdecode(np.frombuffer(output.content, np.uint8), cv2.IMREAD_UNCHANGED)
            return img
        except:
            print('[+] Request Failed, Please Check your Internet Connection ...')
            print('[See Full Traceback Below] - Ignoring Exiting...')
            traceback.print_exc()

if __name__ == '__main__':
    GenerateDataset().generate_dataset(2)
    print('[+] Download Successful ...')
