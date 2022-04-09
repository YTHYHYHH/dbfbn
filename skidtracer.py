from json import loads
import requests
import sys

'''
Programmed by Z3NTL3
'''

header  = {
    'cache-control': 'no-cache',
    'connection': 'keep-alive'
}

# Z3NTL3
class IP_API():
    def __init__(self):
        try:
            self.scraperinfo = requests.get(f"http://ip-api.com/json/{sys.argv[1]}", headers=header, timeout=20)
            self.contentscraper = self.scraperinfo.content.decode('utf-8')
            self.dump = loads(self.contentscraper)
        except:
            sys.exit("\033[31mNot a correct IP format: \033[0m", sys.argv[1])
    
    def DUMP(self):
        return self.dump

    def READJSON(self,valuename):
        value = self.dump
        vl = value[valuename]

        return str(vl)
# Constant GLOBAL VARS
print('ss')
)
def Run():
    print(LOGO)
    obj = IP_API()

    if obj.READJSON('status') == 'success':
        print(f"""
\033[38;5;205mCountry: \033[38;5;207m{obj.READJSON('country')}
\033[38;5;205mRegion: \033[38;5;207m{obj.READJSON('regionName')}
\033[38;5;205mCity: \033[38;5;207m{obj.READJSON('city')}
\033[38;5;205mZip: \033[38;5;207m{obj.READJSON('zip')}
\033[38;5;205mLat: \033[38;5;207m{obj.READJSON('lat')}
\033[38;5;205mLon: \033[38;5;207m{obj.READJSON('lon')}
\033[38;5;205mTimezone: \033[38;5;207m{obj.READJSON('timezone')}
\033[38;5;205mISP: \033[38;5;207m{obj.READJSON('isp')}
\033[38;5;205mORG: \033[38;5;207m{obj.READJSON('org')}
\033[38;5;205mAS: \033[38;5;207m{obj.READJSON('as')}\033[0m
""")
    else:
        sys.exit(f"\033[31mCannot lookup this ip into the database\033[0m.\n\033[38;5;205mCheck\033[38;5;206m your\033[38;5;207m I\033[38;5;219mP for\033[38;5;207mmat: \033[38;5;219m{sys.argv[1]}\033[0m\n")

if __name__ == '__main__':
    Run()
    
