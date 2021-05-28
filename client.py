import requests

base_link = "http://127.0.0.1:5000/"

result = requests.get(base_link + "/vaccineregistration/amritha", {"date": "27-05-2021"})
print(result.json())
