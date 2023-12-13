#https://rinatz.github.io/python-book/ch04-05-pipenv/
#今まではvenvで仮想環境を作って、中に入ってからpipでinstallする必要があった
#特に考えずにpipenvで仮想環境の作成とinstallの両方が実現可能

#!/usr/bin/env python

import requests

def main():
    response = requests.get('http://example.com')
    print(response.text)

if __name__ == '__main__':
    main()