import requests
import sys

'''if len(sys.argv) > 1:
    argExist = True
else:
    argExist = False
    print('Insert host')

if argExist == True:
    url = sys.argv[1]
'''
host = 'https://google.com/'
filesFounds = []
bkpOldFiles = ['.bkp', '.bak', '.src', '.dev', '.txt', '.old', '.inc', '.orig', '.copy', '.tmp']

with open("/var/www/html/common.txt.bkp") as file:
    archive = file.readlines()
    for i in archive:

        page = i.replace(" ","")
        page = page.replace("\n", "")

        url = host+page
        r = requests.get(url)
        r = r.status_code

        if r == 200:
            print("File found:", url)

            for i in bkpOldFiles:
                url2 = url + i
                r = requests.get(url2)
                r = r.status_code

                if r == 200:
                    print("File found:", url2)

