import requests
import sys

try:
    if len(sys.argv) > 2:
        argExist = True

        host = sys.argv[1]
        wordlist = sys.argv[2]
        filesFounds = []
        directoriesFounds = []
        bkpOldFiles = ['.bkp', '.bak', '.src', '.dev', '.txt', '.old', '.inc', '.orig', '.copy', '.tmp']


        # initial server recognition
        def recon(host):
            r = requests.get(host)
            r = r.headers

            for key, value in r.items():
                if key == 'Server':
                    print('\nServer identified:', value, '\n')


        # backup, old or copy files analysis
        def bocf(url):
            for extension in bkpOldFiles:
                url2 = url + extension
                r = requests.get(url2)
                r = r.status_code
                if r == 200:
                    return print("BOC  found:", url2, 'Must be interessanting')


        def windowsCopyFile():
            print('TODO')


        def fileSearching(directory):
            try:
                with open(wordlist) as file:
                    archive = file.readlines()

                    countLine = 0
                    # count lines
                    for line in archive:
                        countLine += 1

                    countExecuted = 0
                    # searching files
                    for word in archive:

                        # lines executed

                        countExecuted += 1

                        page = word.replace(" ", "")
                        page = page.replace("\n", "")

                        if directory != 'null':
                            url = directory + page
                        else:
                            url = host + page

                        r = requests.get(url)

                        codeHttp = r.status_code

                        if codeHttp == 200:
                            print("File found:", url)
                            bocf(url)

                        # searching directories
                        history = r.history
                        if len(history) > 0:
                            # history = str(r.history[0])
                            # historyHttp = history[11:14]
                            print('Directory Found', url)

                            # todo se page contiver caracter
                            directoriesFounds.append(url + '/')
                            # print(directoriesFounds)

                        if countLine == countExecuted:
                            directorySearching(directoriesFounds)
            except FileNotFoundError:
                print('Não foi possível abrir o arquivo informado em:', wordlist)


        def directorySearching(directoriesFounds):

            while len(directoriesFounds) >= 1:
                # print(directoriesFounds)

                directory = directoriesFounds[0]
                directoriesFounds.remove(directory)
                print('\nEntring in directory:', directory)
                # print(directoriesFounds)
                fileSearching(directory)


        def main(host, directory):
            recon(host)

            if directory == '':
                fileSearching(directory)
            else:
                fileSearching(directory)


        main(host, 'null')
    else:
        argExist = False
        print('\nExecute: python3 shw.py <http/s://<host>/ <wordlist location>')
except:
    print('\nCancelled')