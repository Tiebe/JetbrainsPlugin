import requests

def jetbrains_request(endpoint, method, host, password = None, port = None):
    if port is not None:
        requests.request(method, f"http://{host}:{port}{endpoint}", headers = { "Authorization": password })
    else:
        for i in range(63342, 63353):
            try:
                requests.request(method, f"http://{host}:{i}{endpoint}", headers = { "Authorization": password })
                break
            except Exception:
                pass


