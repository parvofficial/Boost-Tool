import os, random, tls_client, time, ctypes, base64, requests, json
from threading import Lock, Thread
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import init, Fore
from datetime import datetime
import sys
from keyauth import *
from pystyle import Colors, Write
import yaml
from os import listdir
from faker import Faker
lock = Lock()
init(autoreset=True)

# Value
chrome_version = random.randint(110, 118)
locale = random.choice(["af", "af-NA", "af-ZA", "agq", "agq-CM", "ak", "ak-GH", "am", "am-ET", "ar", "ar-001", "ar-AE", "ar-BH", "ar-DJ", "ar-DZ", "ar-EG", "ar-EH", "ar-ER", "ar-IL", "ar-IQ", "ar-JO", "ar-KM", "ar-KW", "ar-LB", "ar-LY", "ar-MA", "ar-MR", "ar-OM", "ar-PS", "ar-QA", "ar-SA", "ar-SD", "ar-SO", "ar-SS", "ar-SY", "ar-TD", "ar-TN", "ar-YE", "as", "as-IN", "asa", "asa-TZ", "ast", "ast-ES", "az", "az-Cyrl", "az-Cyrl-AZ", "az-Latn", "az-Latn-AZ", "bas", "bas-CM", "be", "be-BY", "bem", "bem-ZM", "bez", "bez-TZ", "bg", "bg-BG", "bm", "bm-ML", "bn", "bn-BD", "bn-IN", "bo", "bo-CN", "bo-IN", "br", "br-FR", "brx", "brx-IN", "bs", "bs-Cyrl", "bs-Cyrl-BA", "bs-Latn", "bs-Latn-BA", "ca", "ca-AD", "ca-ES", "ca-FR", "ca-IT", "ccp", "ccp-BD", "ccp-IN", "ce", "ce-RU", "cgg", "cgg-UG", "chr", "chr-US", "ckb", "ckb-IQ", "ckb-IR", "cs", "cs-CZ", "cy", "cy-GB", "da", "da-DK", "da-GL", "dav", "dav-KE", "de", "de-AT", "de-BE", "de-CH", "de-DE", "de-IT", "de-LI", "de-LU", "dje", "dje-NE", "dsb", "dsb-DE", "dua", "dua-CM", "dyo", "dyo-SN", "dz", "dz-BT", "ebu", "ebu-KE", "ee", "ee-GH", "ee-TG", "el", "el-CY", "el-GR", "en", "en-001", "en-150", "en-AG", "en-AI", "en-AS", "en-AT", "en-AU", "en-BB", "en-BE", "en-BI", "en-BM", "en-BS", "en-BW", "en-BZ", "en-CA", "en-CC", "en-CH", "en-CK", "en-CM", "en-CX", "en-CY", "en-DE", "en-DG", "en-DK", "en-DM", "en-ER", "en-FI", "en-FJ", "en-FK", "en-FM", "en-GB", "en-GD", "en-GG", "en-GH", "en-GI", "en-GM", "en-GU", "en-GY", "en-HK", "en-IE", "en-IL", "en-IM", "en-IN", "en-IO", "en-JE", "en-JM", "en-KE", "en-KI", "en-KN", "en-KY", "en-LC", "en-LR", "en-LS", "en-MG", "en-MH", "en-MO", "en-MP", "en-MS", "en-MT", "en-MU", "en-MW", "en-MY", "en-NA", "en-NF", "en-NG", "en-NL", "en-NR", "en-NU", "en-NZ", "en-PG", "en-PH", "en-PK", "en-PN", "en-PR", "en-PW", "en-RW", "en-SB", "en-SC", "en-SD", "en-SE", "en-SG", "en-SH", "en-SI", "en-SL", "en-SS", "en-SX", "en-SZ", "en-TC", "en-TK", "en-TO", "en-TT", "en-TV", "en-TZ", "en-UG", "en-UM", "en-US", "en-US-POSIX", "en-VC", "en-VG", "en-VI", "en-VU", "en-WS", "en-ZA", "en-ZM", "en-ZW", "eo", "es", "es-419", "es-AR", "es-BO", "es-BR", "es-BZ", "es-CL", "es-CO", "es-CR", "es-CU", "es-DO", "es-EA", "es-EC", "es-ES", "es-GQ", "es-GT", "es-HN", "es-IC", "es-MX", "es-NI", "es-PA", "es-PE", "es-PH", "es-PR", "es-PY", "es-SV", "es-US", "es-UY", "es-VE", "et", "et-EE", "eu", "eu-ES", "ewo", "ewo-CM", "fa", "fa-AF", "fa-IR", "ff", "ff-CM", "ff-GN", "ff-MR", "ff-SN", "fi", "fi-FI", "fil", "fil-PH", "fo", "fo-DK", "fo-FO", "fr", "fr-BE", "fr-BF", "fr-BI", "fr-BJ", "fr-BL", "fr-CA", "fr-CD", "fr-CF", "fr-CG", "fr-CH", "fr-CI", "fr-CM", "fr-DJ", "fr-DZ", "fr-FR", "fr-GA", "fr-GF", "fr-GN", "fr-GP", "fr-GQ", "fr-HT", "fr-KM", "fr-LU", "fr-MA", "fr-MC", "fr-MF", "fr-MG", "fr-ML", "fr-MQ", "fr-MR", "fr-MU", "fr-NC", "fr-NE", "fr-PF", "fr-PM", "fr-RE", "fr-RW", "fr-SC", "fr-SN", "fr-SY", "fr-TD", "fr-TG", "fr-TN", "fr-VU", "fr-WF", "fr-YT", "fur", "fur-IT", "fy", "fy-NL", "ga", "ga-IE", "gd", "gd-GB", "gl", "gl-ES", "gsw", "gsw-CH", "gsw-FR", "gsw-LI", "gu", "gu-IN", "guz", "guz-KE", "gv", "gv-IM", "ha", "ha-GH", "ha-NE", "ha-NG", "haw", "haw-US", "he", "he-IL", "hi", "hi-IN", "hr", "hr-BA", "hr-HR", "hsb", "hsb-DE", "hu", "hu-HU", "hy", "hy-AM", "id", "id-ID", "ig", "ig-NG", "ii", "ii-CN", "is", "is-IS", "it", "it-CH", "it-IT", "it-SM", "it-VA", "ja", "ja-JP", "jgo", "jgo-CM", "jmc", "jmc-TZ", "ka", "ka-GE", "kab", "kab-DZ", "kam", "kam-KE", "kde", "kde-TZ", "kea", "kea-CV", "khq", "khq-ML", "ki", "ki-KE", "kk", "kk-KZ", "kkj", "kkj-CM", "kl", "kl-GL", "kln", "kln-KE", "km", "km-KH", "kn", "kn-IN", "ko", "ko-KP", "ko-KR", "kok", "kok-IN", "ks", "ks-IN", "ksb", "ksb-TZ", "ksf", "ksf-CM", "ksh", "ksh-DE", "kw", "kw-GB", "ky", "ky-KG", "lag", "lag-TZ", "lb", "lb-LU", "lg", "lg-UG", "lkt", "lkt-US", "ln", "ln-AO", "ln-CD", "ln-CF", "ln-CG", "lo", "lo-LA", "lrc", "lrc-IQ", "lrc-IR", "lt", "lt-LT", "lu", "lu-CD", "luo", "luo-KE", "luy", "luy-KE", "lv", "lv-LV", "mas", "mas-KE", "mas-TZ", "mer", "mer-KE", "mfe", "mfe-MU", "mg", "mg-MG", "mgh", "mgh-MZ", "mgo", "mgo-CM", "mk", "mk-MK", "ml", "ml-IN", "mn", "mn-MN", "mr", "mr-IN", "ms", "ms-BN", "ms-MY", "ms-SG", "mt", "mt-MT", "mua", "mua-CM", "my", "my-MM", "mzn", "mzn-IR", "naq", "naq-NA", "nb", "nb-NO", "nb-SJ", "nd", "nd-ZW", "nds", "nds-DE", "nds-NL", "ne", "ne-IN", "ne-NP", "nl", "nl-AW", "nl-BE", "nl-BQ", "nl-CW", "nl-NL", "nl-SR", "nl-SX", "nmg", "nmg-CM", "nn", "nn-NO", "nnh", "nnh-CM", "nus", "nus-SS", "nyn", "nyn-UG", "om", "om-ET", "om-KE", "or", "or-IN", "os", "os-GE", "os-RU", "pa", "pa-Arab", "pa-Arab-PK", "pa-Guru", "pa-Guru-IN", "pl", "pl-PL", "ps", "ps-AF", "pt", "pt-AO", "pt-BR", "pt-CH", "pt-CV", "pt-GQ", "pt-GW", "pt-LU", "pt-MO", "pt-MZ", "pt-PT", "pt-ST", "pt-TL", "qu", "qu-BO", "qu-EC", "qu-PE", "rm", "rm-CH", "rn", "rn-BI", "ro", "ro-MD", "ro-RO", "rof", "rof-TZ", "ru", "ru-BY", "ru-KG", "ru-KZ", "ru-MD", "ru-RU", "ru-UA", "rw", "rw-RW", "rwk", "rwk-TZ", "sah", "sah-RU", "saq", "saq-KE", "sbp", "sbp-TZ", "se", "se-FI", "se-NO", "se-SE", "seh", "seh-MZ", "ses", "ses-ML", "sg", "sg-CF", "shi", "shi-Latn", "shi-Latn-MA", "shi-Tfng", "shi-Tfng-MA", "si", "si-LK", "sk", "sk-SK", "sl", "sl-SI", "smn", "smn-FI", "sn", "sn-ZW", "so", "so-DJ", "so-ET", "so-KE", "so-SO", "sq", "sq-AL", "sq-MK", "sq-XK", "sr", "sr-Cyrl", "sr-Cyrl-BA", "sr-Cyrl-ME", "sr-Cyrl-RS", "sr-Cyrl-XK", "sr-Latn", "sr-Latn-BA", "sr-Latn-ME", "sr-Latn-RS", "sr-Latn-XK", "sv", "sv-AX", "sv-FI", "sv-SE", "sw", "sw-CD", "sw-KE", "sw-TZ", "sw-UG", "ta", "ta-IN", "ta-LK", "ta-MY", "ta-SG", "te", "te-IN", "teo", "teo-KE", "teo-UG", "tg", "tg-TJ", "th", "th-TH", "ti", "ti-ER", "ti-ET", "to", "to-TO", "tr", "tr-CY", "tr-TR", "tt", "tt-RU", "twq", "twq-NE", "tzm", "tzm-MA", "ug", "ug-CN", "uk", "uk-UA", "ur", "ur-IN", "ur-PK", "uz", "uz-Arab", "uz-Arab-AF", "uz-Cyrl", "uz-Cyrl-UZ", "uz-Latn", "uz-Latn-UZ", "vai", "vai-Latn", "vai-Latn-LR", "vai-Vaii", "vai-Vaii-LR", "vi", "vi-VN", "vun", "vun-TZ", "wae", "wae-CH", "wo", "wo-SN", "xog", "xog-UG", "yav", "yav-CM", "yi", "yi-001", "yo", "yo-BJ", "yo-NG", "yue", "yue-Hans", "yue-Hans-CN", "yue-Hant", "yue-Hant-HK", "zgh", "zgh-MA", "zh", "zh-Hans", "zh-Hans-CN", "zh-Hans-HK", "zh-Hans-MO", "zh-Hans-SG", "zh-Hant", "zh-Hant-HK", "zh-Hant-MO", "zh-Hant-TW", "zu", "zu-ZA"])

# Getting Data From Json
settings = yaml.safe_load(open("config.yaml", encoding="utf-8"))

# Variables
Boosted = 0; Errors = 0; count = 0; msg_append = []; Captcha = 0; Solved = 0

# Logger
class Logger:
    def success(token):
        current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        if settings['Hide']:
            print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "SUCCESS" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Boosted Server. " + "-> Token: " + Fore.RESET + Fore.LIGHTGREEN_EX + f"{token[:27]}...." + Fore.RESET)
        else:
            print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "SUCCESS" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Boosted Server. " + "-> Token: " + Fore.RESET + Fore.LIGHTGREEN_EX + token + Fore.RESET)

    def Failed(token, error):
        current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        if settings['Hide']:
            print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "FAILED" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + f"- {error} " + "-> Token: " + Fore.RESET + Fore.LIGHTRED_EX + f"{token[:27]}...." + Fore.RESET)
        else:
            print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "FAILED" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + f"- {error} " + "-> Token: " + Fore.RESET + Fore.LIGHTRED_EX + token + Fore.RESET)
        
    def debug(info: str, args: str):
        current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        print(Fore.MAGENTA + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + f"- {info} -> " + Fore.RESET + Fore.LIGHTGREEN_EX + args + Fore.RESET)
        
    def error(error: str):
        current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "ERROR" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + f"- {error} " + Fore.RESET)

def checkconfig():
    try:
        if settings['proxyless'] == False and len(open("input/proxies.txt", "r").readlines()) in (0, 1, 2, 3):
            Logger.error(f'Config Error: Enter Proxies in input/proxies.txt !')
            return
        
        if settings['Webhook']['Webhook_Logging'] == True and settings['Webhook']['webhook_url'] == '':
            Logger.error(f'Config Error: Look like you enable Webhook_Logging but you didnt Enter Webhook Url in config.yaml')
            return
        
        if settings['Captcha']['Solvercaptcha'] == True and settings['Captcha']['key'] == '':
            Logger.error(f'Config Error: Look like you enable Captcha Solver but you didnt Enter Captcha key')
            return
        
    except:
        return
    
def send_webhook():
    try:
        if settings['Webhook']['Webhook_Logging'] == True:
            Utils.send_webhook_embed()
    except Exception as e:
        print(e)
        return

class Utils:
    @staticmethod
    def remove(token: str, filename: str) -> None:
        lock.acquire()
        try:
            with open(filename, "r+") as io:
                content = io.readlines()
                io.seek(0)
                for line in content:
                    if token not in line:
                        io.write(line)
                io.truncate()
        except Exception as e:
            print(f"Error removing token: {e}")
        finally:
            lock.release()
    
    @staticmethod
    def getchecksum():
        md5_hash = hashlib.md5()
        file = open(''.join(sys.argv), "rb")
        md5_hash.update(file.read())
        digest = md5_hash.hexdigest()
        return digest

    @staticmethod
    def write(args: str, filename: str):
        try:
            lock.acquire()
            with open(filename, 'a') as f:
                f.write(f'{args}\n')
            lock.release()
        except:
            return
    
    @staticmethod
    def encoded(path: str):
        try:
            with open(path + random.choice(listdir(path)), "rb") as f:
                img = f.read()
            return f'data:image/png;base64,{base64.b64encode(img).decode("ascii")}'
        except Exception as e:
            print(e)
    
    @staticmethod
    def send_webhook_embed(arrow = settings['Webhook']['Arrow_Emojis_ID']):
        global Boosted, Errors, count , Solved, Captcha
        try:
            if settings['Captcha']['Solvercaptcha']:
                msg = f'{arrow} **Boosted:** ```{Boosted}```\n{arrow} **Failed:** ```{Errors}```\n{arrow} **Captcha Detected:** ```{Captcha}```'
            else:
                msg = f'{arrow} **Boosted:** ```{Boosted}```\n{arrow} **Failed:** ```{Errors}```\n{arrow} **Captcha Detected:** ```{Captcha}/{Solved}```'

            if msg_append:
                 embed = DiscordEmbed(title="live session",description=msg,color=int("0x2f3136", 0), type="rich")
                 embed.set_author(name="@Rexamine | Rexamine Boost Tool V2.0.0", icon_url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 embed.set_footer(text="Rexamine Boosts", icon_url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 msg = msg_append[-1]
                 webhook = DiscordWebhook(url=settings['Webhook']['webhook_url'], id=msg)
                 webhook.add_embed(embed=embed)
                 webhook.edit()
            
            else:
                 embed = DiscordEmbed(title="live session",description=msg,color=int("0x2f3136", 0), type="rich")
                 embed.set_author(name="@Rexamine | Rexamine Boost Tool V2.0.0", icon_url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 embed.set_footer(text="Rexamine Boosts", icon_url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 webhook = DiscordWebhook(url=settings['Webhook']['webhook_url'])
                 webhook.add_embed(embed=embed)
                 xd = webhook.execute()
                 msg_append.append(xd.json()['id'])

        except Exception as e:
            raise Exception(f'Error while sending Webhook')
        
    @staticmethod
    def edit_send_txt(arrow = settings['Webhook']['Arrow_Emojis_ID']):
        global Boosted, Errors, count , Solved, Captcha
        try:
            if settings['Captcha']['Solvercaptcha']:
                msg = f'{arrow} **Boosted:** ```{Boosted}```\n{arrow} **Failed:** ```{Errors}```\n{arrow} **Captcha Detected:** ```{Captcha}```'
            else:
                msg = f'{arrow} **Boosted:** ```{Boosted}```\n{arrow} **Failed:** ```{Errors}```\n{arrow} **Captcha Detected:** ```{Captcha}/{Solved}```'

            if msg_append:
                 embed = DiscordEmbed(title="Session Completed",description=msg,color=int("0x2f3136", 0), type="rich")
                 embed.set_author(name="@Rexamine | Rexamine Boost Tool V2.0.0", icon_url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 embed.set_footer(text="Rexamine Boosts", icon_url="https://cdn.discordapp.com/icons/1201757515541663815/b1921d34d32fef4541089250cce9cb24.webp?size=240")
                 msg = msg_append[-1]
                 webhook = DiscordWebhook(url=settings['Webhook']['webhook_url'], id=msg)
                 webhook.add_embed(embed=embed)
                 sucess = open("output/Success/success.txt", "rb")
                 faileds = open("output/Failed/FailedToken.txt", "rb")
                 webhook.add_file(file=sucess, filename='success.txt')
                 webhook.add_file(file=faileds, filename='FailedToken.txt')
                 webhook.edit()
                 
        except Exception as e:
            raise Exception(f'Error while editing Webhook')
    
    @staticmethod
    def updateHeaders():
        try:
            while True:
                titles = f'Rexamine Boost Tool V2.0.0 | Boosted: {Boosted}, Failed: {Errors}, Captcha: {Captcha}, Solved: {Solved}'
                ctypes.windll.kernel32.SetConsoleTitleW(titles)
        except Exception as e:
            Logger.error(f'Function: updateHeaders, Error: {e}')
            return
        
    @staticmethod
    def getcontextheader(invite):
        try:
            response = requests.get(f'https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true')
            
            if response.status_code in (200, 201, 202, 203, 204):
                return base64.b64encode(json.dumps({"Location": "Join Guild","LocationGuildID": response.json()['guild']['id'],"LocationChannelID": response.json()['channel']['id'],"LocationChannelType": response.json()['channel']['type']}).encode()).decode()
            
            else:
                return None
        
        except Exception as e:
            Logger.error(f'Function: getContextheaders, Error: {e}')
            return
    
    @staticmethod
    def build_super_properties():
        try:
            properties = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": locale,
            "browser_user_agent": f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36',
            "browser_version": f'{chrome_version}.0.0.0',
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": "154186",
            "client_event_source": "null"
            }
            return base64.b64encode(json.dumps(properties, separators=(',', ':')).encode("utf-8")).decode()
        except Exception as e:
            Logger.error(f'Function: build_super_properties, Exception type: Error, Exception: {e}')
            return
    
    @staticmethod
    def __generatepass__() -> str:
      fake = Faker()
      random_first_name = str(fake.first_name()).lower()
      return ''.join(str(random_first_name) + str(random.randint(0, 9999999)))

class Solver:
    def __init__(self, sitekey, useagent, rqdata, token) -> None:
        self.sitekey = sitekey
        self.useragent = useagent
        self.rqdata = rqdata
        self.token = token
        self.siteurl = 'https://discord.com/'

        self.session = tls_client.Session(
       client_identifier="chrome_112",
       random_tls_extension_order=True
    )
    
    def Hcoptcha(self):
        if settings['Captcha']['use_proxies']:
            proxy = random.choice(open("input/proxies.txt", "r").read().splitlines())
            payload = {
                "task_type": "hcaptchaEnterprise",
                "api_key": settings['Captcha']['key'],
                "data": {
                    "sitekey": self.sitekey,
                    "url": self.siteurl,
                    "proxy": proxy,
                    "rqdata": self.rqdata
	}
}
        else:
            Logger.error(f'Proxies mandatory to use Hcoptcha Captcha Services!')
            return

        headers={'content-type': 'application/json'}
        try:
            response = self.session.post(f'https://api.hcoptcha.online/api/createTask', json=payload, headers=headers)

            if response.status_code != 200:
                Logger.Failed(token=self.token, error=f"Failed to Solve Captcha [Create Task] Error: {response.json()}")
                return
            
            else:
                taskid = response.json()['task_id']

            payloads = {
                "api_key": settings['Captcha']['key'],
                "task_id": taskid
                }

            while True:
                try:
                    responsee = self.session.post(f'https://api.hcoptcha.online/api/getTaskData', json=payloads)
                    if responsee.json()['task']['state'] == "completed":
                        key = responsee.json()["task"]["captcha_key"]
                        return key
                
                except Exception as e:
                    Logger.Failed(token=self.token, error=f"Failed to Solve Captcha. Error: {e}")
                    return
        except Exception as e:
            Logger.Failed(token=self.token, error=f"Failed to Solve Captcha. Error: {e}")
            return

    def Capsolver(self):
        if settings['Captcha']['use_proxies']:
            proxy = random.choice(open("input/proxies.txt", "r").read().splitlines())
            payload = {
            "clientKey": settings['Captcha']['key'],
            "task": {
                "type": "HCaptchaTask",
                "websiteURL": self.siteurl,
                "websiteKey": self.sitekey,
                "isInvisible": True,
                "proxyType": "http",
                "proxyAddress": proxy.split("@")[1].split(":")[0],
                "proxyPort": proxy.split("@")[1].split(":")[1],
                "proxyLogin": proxy.split("@")[0].split(":")[0],
                "proxyPassword": proxy.split("@")[0].split(":")[1],
                "enterprisePayload": {
                    "rqdata": self.rqdata
                    },
                "userAgent": self.useragent
  }
}
        else:
            payload = {
            "clientKey": settings['Captcha']['key'],
            "task": {
                "type": "HCaptchaTaskProxyLess",
                "websiteURL": 'https://discord.com',
                "websiteKey": self.sitekey,
                "isInvisible": True,
                "enterprisePayload": {
                    "rqdata": self.rqdata
                    },
                "userAgent": self.useragent
  }
}
        headers={'content-type': 'application/json'}
        try:
            response = self.session.post(f'https://api.capsolver.com/createTask', json=payload, headers=headers)

            if response.status_code != 200:
                Logger.Failed(token=self.token, error=f"Failed to Solve Captcha [Create Task] Error: {response.json()['errorDescription']}")
                return
            
            else:
                taskid = response.json()['taskid']

            payloads = {
                "clientKey": settings['Captcha']['key'],
                "taskId": taskid
                }

            while True:
                try:
                    responsee = self.session.post(f'https://api.capsolver.com/getTaskResult', json=payloads)
                    if responsee.json()['status'] == "ready":
                        key = responsee.json()["solution"]["gRecaptchaResponse"]
                        return key
                    elif responsee.json()['status'] == "failed":
                        Logger.Failed(token=self.token, error=f"Failed to Solve Captcha [GET TASK RESULT] Error: {response.json()['errorDescription']}")
                        return
                
                except Exception as e:
                    Logger.Failed(token=self.token, error=f"Failed to Solve Captcha. Error: {e}")
                    return
        except Exception as e:
            Logger.Failed(token=self.token, error=f"Failed to Solve Captcha. Error: {e}")
            return

class Customization:
    def __init__(self, token, fingerprint, cookies, useragent, x):
        global Errors
        self.token = token
        self.fingerprint = fingerprint
        self.cookies = cookies
        self.useragent = useragent
        self.x = x

        self.session = tls_client.Session(
       client_identifier="chrome_112",
       random_tls_extension_order=True
    )

    def Bio(self):
        global Errors
        try:
            headers = {
            'authority': 'discord.com',
            'method': 'PATCH',
            'path': f'/api/v9/users/%40me/profile',
            'scheme': 'https',
            'Accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Authorization': self.token,
            'Content-Type': 'application/json',
            'Cookie': self.cookies,
            'Origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'User-Agent': self.useragent,
            'X-Debug-Options': 'bugReporterEnabled',
            'x-discord-locale': 'en',
            'x-discord-timezone': 'Europe/Paris',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ii9jaGFubmVscy9AbWUifQ==',
            'X-Super-Properties': self.x,
            'fingerprint': self.fingerprint
        }
            
            json = {
                'bio': settings['Customization']['Bio'],
                'pronouns': settings['Customization']['Pronouns'],
                'accent_color': settings['Customization']['Accent_color']
            }
            response = self.session.patch(f'https://discord.com/api/v9/users/%40me/profile', headers=headers, json=json)
            print(response.json())

            if response.status_code in (200, 201):
                 return 'Success'
            else:
                 return 'Failed'
        
        except Exception as e:
            Errors += 1
            Logger.error(f'Function: Customization, Error: {e}')
            return

    def Banner(self):
        global Errors
        try:
            headers = {
            'authority': 'discord.com',
            'method': 'PATCH',
            'path': f'/api/v9/users/@me',
            'scheme': 'https',
            'Accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Authorization': self.token,
            'Content-Type': 'application/json',
            'Cookie': self.cookies,
            'Origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'User-Agent': self.useragent,
            'X-Debug-Options': 'bugReporterEnabled',
            'x-discord-locale': 'en',
            'x-discord-timezone': 'Europe/Paris',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ii9jaGFubmVscy9AbWUifQ==',
            'X-Super-Properties': self.x,
            'fingerprint': self.fingerprint
        }
            ava = Utils.encoded(path='input/avatar/')
            baner = Utils.encoded(path='input/banners/')
            
            json2 = {
                'avatar': ava
            }
            json = {
                "banner": baner,
                "global_name": settings['Customization']['Global_name']
            }
            response = self.session.patch(f'https://discord.com/api/v9/users/@me', headers=headers, json=json)
            responsee = self.session.patch(f'https://discord.com/api/v9/users/@me', headers=headers, json=json2)

            if response.status_code in (200, 201):
                 return 'Success'
            else:
                 return 'Failed'
        
        except Exception as e:
            Errors += 1
            Logger.error(f'Function: Customization, Error: {e}')
            return
        

    def changepass(self, fulltk):
        global Errors
        headers = {
            'authority': 'discord.com',
            'method': 'PATCH',
            'path': f'/api/v9/users/@me',
            'scheme': 'https',
            'Accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Authorization': self.token,
            'Content-Type': 'application/json',
            'Cookie': self.cookies,
            'Origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'User-Agent': self.useragent,
            'X-Debug-Options': 'bugReporterEnabled',
            'x-discord-locale': 'en',
            'x-discord-timezone': 'Europe/Paris',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ii9jaGFubmVscy9AbWUifQ==',
            'X-Super-Properties': self.x,
            'fingerprint': self.fingerprint
        }
        try:
            if ":" in fulltk:
                split = fulltk.split(":")
            
            self.oldpass = split[1]
            self.token = split[2]
            self.email = split[0]
            if settings['Password_Changer']['random_Password'] == True:
                self.newpass = Utils.__generatepass__()
            
            else:
                self.newpass = settings['Password_Changer']['Password']

                
            json = {
                "password": self.oldpass,
                "new_password": self.newpass
            }
            response = self.session.patch(f'https://discord.com/api/v9/users/@me', headers=headers, json=json)
            
            if response.status_code in (200, 201):
                 return f'{self.email}:{self.newpass}:{response.json()["token"]}'
            else:
                 return False
        
        except Exception as e:
            Errors += 1
            Logger.error(f'Function: Customization, Error: {e}')
            return
        
class Booster:
    def __init__(self, token: str, invite: str, filename: str) -> None:
        self.fulltoken = token
        try:
            if ":" in token:
                self.token = token.split(":")[2]
            else:
                self.token = token
        
        except:
            Logger.error(f'Invalid token format!')
            return
        
        self.invite = invite
        self.filename = filename
        send_webhook()

    def boostes(self):
        global Boosted, Errors, count , Solved, Captcha
        try:
            self.x = Utils.build_super_properties()
            self.contextheaders = Utils.getcontextheader(self.invite)
            self.useragent = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36"
            self.ja3 = "771,4866-4867-4865-49196-49200-49195-49199-52393-52392-159-158-52394-49327-49325-49326-49324-49188-49192-49187-49191-49162-49172-49161-49171-49315-49311-49314-49310-107-103-57-51-157-156-49313-49309-49312-49308-61-60-53-47-255,0-11-10-35-16-22-23-49-13-43-45-51-21,29-23-30-25-24,0-1-2"

        except:
            Logger.error(f'Failed to Get Useragent, Ja3, X-Super-properties')
            return
        
        fingheaders = {
            'authority': 'discord.com',
            'method': 'GET',
            'path': f'/api/v9/experiments?with_guild_experiments=true',
            'scheme': 'https',
            'Accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Content-Type': 'application/json',
            'Origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'User-Agent': self.useragent,
            'X-Debug-Options': 'bugReporterEnabled',
            'x-discord-locale': 'fr',
            'x-discord-timezone': 'Europe/Paris',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ii9jaGFubmVscy9AbWUifQ==',
            'X-Super-Properties': self.x
        }

        try:
            while True:
                response = requests.get('https://discord.com/api/v9/experiments', headers=fingheaders)
                
                if not (response.status_code in [200, 201, 204]):
                    Logger.error('Failed to Extract Fingerprints and Cookies')
                    return
                
                else:
                    self.fingerprint = response.json()['fingerprint']
                    self.cookie = f"locale=en; __dcfduid={response.cookies.get('__dcfduid')}; __sdcfduid={response.cookies.get('__sdcfduid')}; __cfruid={response.cookies.get('__cfruid')}"
                    break
        except:
            Logger.error(f'Error Getting Fingerprints')
            return
        
        try:
            self.session = tls_client.Session(ja3_string=self.ja3, client_identifier = "firefox_102")

            if settings['proxyless'] == False:
                proxy = random.choice(open("input/proxies.txt", "r").read().splitlines())

                self.session.proxies = {
          'http': f'http://{proxy}',
          'https': f'https://{proxy}',
       }

        except Exception as e:
            Errors += 1
            Logger.error(f'Function: CreateSession, Error: {e}')
            return
        
        send_webhook()

        headers = {
            'authority': 'discord.com',
            'method': 'GET',
            'path': f'/api/v9/users/@me/guilds/premium/subscription-slots',
            'scheme': 'https',
            'Accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Authorization': self.token,
            'Content-Type': 'application/json',
            'Cookie': self.cookie,
            'Origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'User-Agent': self.useragent,
            'X-Debug-Options': 'bugReporterEnabled',
            'x-discord-locale': 'en',
            'x-discord-timezone': 'Europe/Paris',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ii9jaGFubmVscy9AbWUifQ==',
            'X-Super-Properties': self.x,
            'fingerprint': self.fingerprint
        }
        try:
            response = self.session.get('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots', headers=headers)

            if response.status_code == 401:
                Logger.Failed(self.token, f'The provided token is Invalid')
                Utils.remove(self.fulltoken, self.filename)
                Utils.write(self.fulltoken, 'output/Failed/FailedToken.txt')
                Errors += 1
                return

            elif len(response.json()) == 0:
                Logger.Failed(self.token, f'The token does not have Nitro')
                Utils.remove(self.fulltoken, self.filename)
                Utils.write(self.fulltoken, 'output/Failed/FailedToken.txt')
                Errors += 1
                return
            
            elif response.status_code == 403:
                Logger.Failed(self.token, f'The provided token is locked')
                Utils.remove(self.fulltoken, self.filename)
                Utils.write(self.fulltoken, 'output/Failed/FailedToken.txt')
                Errors += 1
                return
            
            elif response.status_code != 200:
                Logger.Failed(self.token, f'Failed to fetch Error. Response: {response.text}')
                Utils.remove(self.fulltoken, self.filename)
                Utils.write(self.fulltoken, 'output/Failed/FailedToken.txt')
                Errors += 1
                return

        except Exception as e:
            Errors += 1
            Logger.error(f'Function: Checktoken, Error: {e}')
            return
        
        self.response_ = response.json()

        send_webhook()

        headers = {
                'authority': 'discord.com',
                'method': 'POST',
                'path': f'/api/v9/invites/{self.invite}',
                'scheme': 'https',
                'Accept': '*/*',
                'Authorization': self.token,
                'accept-language': 'fr-FR,fr;q=0.9',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Content-Type': 'application/json',
                'Origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
                'Sec-Ch-Ua-Mobile': '?1',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'User-Agent': self.useragent,
                'X-Debug-Options': 'bugReporterEnabled',
                'x-discord-locale': 'en',
                'x-discord-timezone': 'Europe/Paris',
                'x-context-properties': self.contextheaders,
                'X-Super-Properties': self.x,
                'Cookie': self.cookie,
                'fingerprint': self.fingerprint
                }
        self.joined = False
        
        try:
            for x in range(10):
                response = self.session.post(f'https://discord.com/api/v9/invites/{self.invite}', json={}, headers=headers)
                print(response.json())

                if response.status_code in [200, 204]:
                    self.guild_id = response.json()["guild"]["id"]
                    self.guild_name = response.json()["guild"]["name"]
                    self.joined = True
                    break

                elif "captcha_rqdata" in response.text:
                    Captcha += 1
                    if settings['Captcha']['Solvercaptcha']:
                        solver = Solver(sitekey=response.json()['captcha_sitekey'], useagent=self.useragent, rqdata=response.json()['captcha_rqdata'], token=self.token)
                        if settings['Captcha']['Captcha_Services'] == 'hcoptcha':
                            key = solver.Hcoptcha()
                        else:
                            key = solver.Capsolver()

                        hheaders = {
                'authority': 'discord.com',
                'method': 'POST',
                'path': f'/api/v9/invites/{self.invite}',
                'scheme': 'https',
                'Accept': '*/*',
                'Authorization': self.token,
                'accept-language': 'fr-FR,fr;q=0.9',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Content-Type': 'application/json',
                'Origin': 'https://discord.com',
                'referer': 'https://discord.com/channels/@me',
                'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
                'Sec-Ch-Ua-Mobile': '?1',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'User-Agent': self.useragent,
                'X-Debug-Options': 'bugReporterEnabled',
                'x-discord-locale': 'en',
                'x-discord-timezone': 'Europe/Paris',
                'x-context-properties': self.contextheaders,
                'X-Super-Properties': self.x,
                'Cookie': self.cookie,
                "X-Captcha-Key": key,
                'X-Captcha-Rqtoken': response.json()['captcha_rqtoken'],
                'fingerprint': self.fingerprint
                }
                        response = self.session.post(f'https://discord.com/api/v9/invites/{self.invite}', json={}, headers=hheaders)
                        print(response.json())
                        if response.status_code in [200, 204]:
                            self.guild_id = response.json()["guild"]["id"]
                            self.guild_name = response.json()["guild"]["name"]
                            Solved +=1
                            self.joined = True
                            break

                        else:
                            Logger.Failed(self.token, f'Failed to join Server!')
                            Utils.remove(self.fulltoken, self.filename)
                            Utils.write(self.fulltoken, 'output/Failed/FailedToken.txt')
                            Errors += 1
                            return

        except Exception as e:
            Errors += 1
            Logger.error(f'Function: JoinServer, Error: {e}')
            return
        
        if self.joined != True:
            Logger.Failed(self.token, f'Failed to join Server!')
            Utils.remove(self.fulltoken, self.filename)
            Utils.write(self.fulltoken, 'output/Failed/FailedToken.txt')
            Errors += 1
            return
        send_webhook()
        
        headers = {
            'authority': 'discord.com',
            'method': 'PUT',
            'path': f'/api/v9/guilds/{self.guild_id}/premium/subscriptions',
            'scheme': 'https',
            'Accept': '*/*',
            'accept-language': 'fr-FR,fr;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Authorization': self.token,
            'Content-Type': 'application/json',
            'Cookie': self.cookie,
            'Origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
            'Sec-Ch-Ua-Mobile': '?1',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'User-Agent': self.useragent,
            'X-Debug-Options': 'bugReporterEnabled',
            'x-discord-locale': 'en',
            'x-discord-timezone': 'Europe/Paris',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ii9jaGFubmVscy9AbWUifQ==',
            'X-Super-Properties': self.x,
            'fingerprint': self.fingerprint
        }

        self.boosted = False
        try:
            for x in self.response_:
                sub_id = x["id"]
                payload = {
                    "user_premium_guild_subscription_slot_ids": [sub_id]
                    }
                response = self.session.put(f'https://discord.com/api/v9/guilds/{self.guild_id}/premium/subscriptions', json=payload,headers=headers)

                if response.status_code in [201, 200]:
                    Logger.success(self.token)
                    self.boosted = True
                    Boosted += 1

            if self.boosted:
                if settings['Customization']['Customization']:
                    custom = Customization(token=self.token, fingerprint=self.fingerprint, cookies=self.cookie, useragent=self.useragent, x=self.x)
                    xdsa = custom.Bio()
                    if xdsa == 'Success':
                        sss = custom.Banner()
                        if sss == 'Success':
                            current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
                            print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "SUCCESS" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Successfully Customized. " + "-> Token: " + Fore.RESET + Fore.LIGHTGREEN_EX + f"{self.token[:27]}...." + Fore.RESET)
                            send_webhook()
                        else:
                            Logger.Failed(self.token, f'Failed to Customized')
                            pass
                    else:
                        Logger.Failed(self.token, f'Failed to Customized')
                        pass
                send_webhook()
                if settings['Password_Changer']['Password_Changer'] == True:
                    custom = Customization(token=self.token, fingerprint=self.fingerprint, cookies=self.cookie, useragent=self.useragent, x=self.x)
                    xds = custom.changepass(fulltk=self.fulltoken)
                    if xds != False:
                        Utils.write(xds, f'output/Success/success.txt')
                        pass
                else:
                    Utils.write(self.fulltoken, f'output/Success/success.txt')
                    send_webhook()
                Utils.remove(self.fulltoken, self.filename)
                return
            else:
                Utils.write(self.fulltoken, f'output/Failed/FailedToken.txt')
                Utils.remove(self.fulltoken, self.filename)
                Logger.Failed(self.token, f'Failed to Boost Server. Error: {response.text}')
                Errors += 1
                return
            
        except Exception as e:
            Errors += 1
            Logger.error(f'Function: BoostServer, Error: {e}')
            return

def __thread__(invite, months, amount):
    global Boosted, Errors, count
    try:
        if months == 3:
            filename = "input/3months.txt"
        elif months == 1:
            filename = "input/1months.txt"

        while Boosted != amount:
            tokens = open(filename, "r").read().splitlines()

            if Boosted % 2 != 0:
                Boosted -= 1

            thr = int((amount - Boosted)/2)
            threads = []
            for i in range(thr):
                token = tokens[i]
                t = Thread(target=Booster(token=token, invite=invite, filename=filename).boostes, args=())
                t.daemon = True
                threads.append(t)
                
            for i in range(thr):
                threads[i].start()

            for i in range(thr):
                threads[i].join()
        
    except IndexError:
        pass
    except Exception as e:
        Logger.error(f'Error while starting: {e}')
        return

def update():
    try:
            Thread(target=Utils.updateHeaders, daemon=True).start()
    except:
        return

for i in range(1):
    Thread(target=update, daemon=True).start()

logo = '''

\t\t\t ▄▄▄▄    ▒█████   ▒█████    ██████ ▄▄▄█████▓ █    ██   ██████ 
\t\t\t▓█████▄ ▒██▒  ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ██  ▓██▒▒██    ▒ 
\t\t\t▒██▒ ▄██▒██░  ██▒▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▓██  ▒██░░ ▓██▄   
\t\t\t▒██░█▀  ▒██   ██░▒██   ██░  ▒   ██▒░ ▓██▓ ░ ▓▓█  ░██░  ▒   ██▒
\t\t\t░▓█  ▀█▓░ ████▓▒░░ ████▓▒░▒██████▒▒  ▒██▒ ░ ▒▒█████▓ ▒██████▒▒
\t\t\t░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
\t\t\t▒░▒   ░   ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░░▒░ ░ ░ ░ ░▒  ░ ░
\t\t\t ░    ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░  ░  ░    ░       ░░░ ░ ░ ░  ░  ░  
\t\t\t ░          ░ ░      ░ ░        ░              ░           ░  
\t\t\t      ░                                                       
'''

def main():
    global Boosted, Errors, count
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print(logo, Colors.blue_to_purple, interval=0.000) 
        print()
        try:
            checkconfig()
        except:
            return
        current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Welcome to NotClubA Boosts. I am delighted to see you again." + Fore.RESET)
        print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Please Enter " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "Invite." + Fore.RESET)
        invite = input(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "USER" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + Fore.RESET + Fore.LIGHTYELLOW_EX + ">> " + Fore.RESET)
        print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Please Enter " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "Amount." + Fore.RESET)
        amount = int(input(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "USER" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + Fore.RESET + Fore.LIGHTYELLOW_EX + ">> " + Fore.RESET))
        print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + "- Please Enter " + Fore.RESET + Fore.LIGHTMAGENTA_EX + "Months." + Fore.RESET)
        months = int(input(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "USER" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + Fore.RESET + Fore.LIGHTYELLOW_EX + ">> " + Fore.RESET))
        go = time.time()
        __thread__(invite=invite, months=months, amount=amount)
        print()
        Logger.error(f'Ran out of material. Threads May stopped')
        current_date = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
        if settings['Webhook']['Webhook_Logging']:
            Utils.edit_send_txt()
        end = time.time()
        timewent = round(end - go, 5)
        print(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + f"- Session Completed in {timewent}, Success: {Boosted}, Failed: {Errors}." + Fore.RESET)
        input(Fore.LIGHTBLUE_EX + current_date + Fore.RESET + Fore.LIGHTWHITE_EX + " [" + Fore.RESET + Fore.LIGHTMAGENTA_EX + "INFO" + Fore.RESET + Fore.LIGHTWHITE_EX + "] " + f"- Press Enter to Exit -> " + Fore.RESET)
    except Exception as e:
        Logger.error(f'Enter Threads in Interger.')
        return

main()
