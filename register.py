from requests import get
from threading import Thread

url = "https://videas-fr.vercel.app/create-account/"

with open("flag.txt") as f:
    flags = f.read()

flags = flags.split("\n")

n = len(flags)

def create_account(index: int):
    for i in range((index-1)*50, min(index*50, n-1)):
        response = get(url + str(flags[i]))
        with open("output.txt", "a") as f:
            if "message" in response.text:
                print(response.text+'\n')
                f.write(response.text+'\n')
            else:
                print("flag"+str(i)+'\n')
                f.write("flag"+str(i)+'\n')

threads = [Thread(target=create_account, args=(i,)) for i in range(1, 21)]
[open("output/output" + str(i) + ".txt", "w").close() for i in range(1, 21)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()