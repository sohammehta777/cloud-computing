import requests
import time
from statistics import mean

# Function URL
FUNCTION_URL = "http://127.0.0.1:8080/function/chatbot"

# Requests details
NON_FIGLET_REQUEST = "What is your name?"
FIGLET_REQUEST = "figlet for hello world"

def send_request(data):
    """Send a request to the OpenFaaS function and measure response time."""
    start_time = time.time()
    response = requests.post(FUNCTION_URL, data=data)
    end_time = time.time()
    return end_time - start_time

def measure_requests(data, num_requests=1, print_responses=False):
    """Measure response times for a number of requests."""
    times = []
    for _ in range(num_requests):
        response_time = send_request(data)
        times.append(response_time)
        if print_responses:
            print(f"Response time: {response_time}s")
    return times

# Measuring response times
print("a. Time for the first request (non-figlet):", measure_requests(NON_FIGLET_REQUEST)[0], "s")
print("b. Time for the second request (non-figlet):", measure_requests(NON_FIGLET_REQUEST)[0], "s")
non_figlet_times = measure_requests(NON_FIGLET_REQUEST, 10)
print("c. Average over 10 requests (non-figlet):", mean(non_figlet_times), "s")
print("d. Time for the first request (figlet):", measure_requests(FIGLET_REQUEST)[0], "s")
print("e. Time for the second request (figlet):", measure_requests(FIGLET_REQUEST)[0], "s")
print("f. Time for the second request (figlet) following a non-figlet request:", measure_requests(FIGLET_REQUEST)[0], "s")
figlet_times = measure_requests(FIGLET_REQUEST, 10)
print("g. Average over 10 requests (figlet):", mean(figlet_times), "s")

