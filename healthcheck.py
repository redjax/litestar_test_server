import requests
import time

http_scheme = "http://"
host = "localhost"
port = 8120
endpoint = "healthy"
healthcheck_url = f"{http_scheme}{host}:{port}/{endpoint}"
print(f"Pinging {healthcheck_url}")

sleep_time = 3


def check_health(url: str = healthcheck_url):
    """
    Ping API's healtcheck endpoint.
    """

    try:
        req = requests.get(healthcheck_url)
        print(f"Request: [{req.status_code}]: {req.text}")

        status_code = req.status_code
        text = req.text

        if status_code == 200:
            success = True
        else:
            success = False

        return_obj = {
            "success": success,
            "res": {"status_code": status_code, "text": text},
        }

    except ConnectionRefusedError as exc:
        return_obj = {"success": False, "res": {"status_code": None, "text": exc}}
    except Exception as exc:
        return_obj = {"success": False, "res": {"status_code": None, "text": exc}}

    return return_obj


last_status = None
last_text = None

while last_status == True or last_status == None:
    _req = check_health()
    print(f"Last Request: {_req}")

    if not _req["success"]:
        last_status = _req["res"]["status_code"]
        last_text = _req["res"]["text"]
        break

    time.sleep(sleep_time)

if type(last_text) == requests.exceptions.ConnectionError:
    print(f"[ERROR] Script failed due to connection error.")

    exit(1)
else:
    print(f"Last request failed: [{last_status}]: {last_text}")
