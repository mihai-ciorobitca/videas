from requests import get
from threading import Thread

url = "https://videas-fr.vercel.app/create-account/"

def create_account(index: int):
    for i in range(500*(index-1)+1, 500*(index-1)+501):
        response = get(url + str(i))
        print(i, response.text)
        with open("output/output" + str(index) + ".txt", "a") as f:
            f.write(response.text)

threads = [Thread(target=create_account, args=(i,)) for i in range(1, 21)]
[open("output/output" + str(i) + ".txt", "w").close() for i in range(1, 21)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()