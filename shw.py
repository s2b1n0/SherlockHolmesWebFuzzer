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
host = 'http://localhost/'
filesFounds = []
bkpOldFiles = ['.bkp', '.bak', '.src', '.dev', '.txt', '.old', '.inc', '.orig', '.copy', '.tmp']

# initial server recognition
def recon(host):
    r = requests.get(host)
    r = r.headers

    for key, value in r.items():
        if key == 'Server':
            print('\nServer identified:',value,'\n')

# backup, old or copy files analysis
def bocf(url):
    for extension in bkpOldFiles:
        url2 = url + extension
        r = requests.get(url2)
        r = r.status_code
        if r == 200:
            return print("BOC  found:", url2,'Must be interessanting')

def windowsCopyFile():
    print('TODO')

def main():
    recon(host)

    with open("/var/www/html/common.txt.bkp") as file:
        archive = file.readlines()
        for word in archive:

            page = word.replace(" ","")
            page = page.replace("\n", "")

            url = host+page
            r = requests.get(url)

            codeHttp = r.status_code

            # searching files
            if codeHttp == 200:
                print("File found:", url)
                bocf(url)

            # searching directories
            history = r.history
            if len(history) > 0:
                history = str(r.history[0])
                historyHttp = history[11:14]
                print('Directory Found', url)

main()


'''r = requests.get('http://localhost/js')
s = r.history
print(s,'\n\n')
'''


