import requests
import time
from concurrent.futures import ThreadPoolExecutor

FUNCTION_URL = "http://127.0.0.1:8080/function/chatbot"

def send_request(data):
    start_time = time.time()
    response = requests.post(FUNCTION_URL, data=data)
    end_time = time.time()
    return end_time - start_time

def send_parallel_requests(data, num_requests):
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request, data) for _ in range(num_requests)]
        return [future.result() for future in futures]

parallel_times = send_parallel_requests("What is your name?", 50)
print(f"Sent 50 parallel requests. Times: {parallel_times}")

