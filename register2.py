from requests import get
from multiprocessing import Process, Queue

url = "https://videas-fr.vercel.app/create-account/"

def create_account(index: int, queue: Queue):
    results = []
    for i in range(500 * (index - 1) + 1, 500 * (index - 1) + 501):
        response = get(url + str(i))
        results.append(str(i) + response.text)
    queue.put(results)

if __name__ == '__main__':
    queue = Queue()
    processes = [Process(target=create_account, args=(i, queue)) for i in range(1, 21)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    # Collect results from all processes
    all_results = []
    while not queue.empty():
        all_results.extend(queue.get())

    # Print all results
    for result in all_results:
        print(result)
