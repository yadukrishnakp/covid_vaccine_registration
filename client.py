import requests

base_link = "http://127.0.0.1:5000/"
name_of_hospital = input('name of hospital  :')
name_of_patient = input('name of patient  :')
phone_number = input('mobile number of patient  :')
age_of_patient = input('age of patient  :')
date = input('date format like dd-mm-yyyy (eg:01-01-2021)  :')
result = requests.put(base_link + "/vaccineregistration/" + name_of_hospital,
                      {"name_of_patient": name_of_patient, "phone_number": phone_number, "age": age_of_patient,
                       "date": date})
print(result.json())
# input()


# result = requests.get(base_link + "/vaccineregistration/amritha", {"date": "27-05-2021"})
# print(result.json())

# result = requests.get(base_link + "/vaccineregistration/amritha", {"date": "27-05-2021"})
# print(result.json())
