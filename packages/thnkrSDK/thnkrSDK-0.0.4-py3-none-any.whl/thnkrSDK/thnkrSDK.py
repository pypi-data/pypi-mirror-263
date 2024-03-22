import requests

BASE_URL = 'https://api.thnkrai.com/'
#BASE_URL = 'http://localhost:8000/'

def ping():
   response = requests.get(BASE_URL)
   return response.json()


def example(model):
   response = requests.get(BASE_URL + model)
   return response.json()


def predict(model, input, username, password):
   headers = {
      'Content-Type': 'application/json',
   }

   payload = { # change input so it takes raw json (user is informed by example) rather than direct values
      "Title": input,
      "Username": username,
      "Password": password,
   }

   response = requests.post(BASE_URL + model, headers=headers, json=payload) # add error handling if anything other than response 200
   
   if 'Accuracy' in response.json():
      return response.json() # change output so it returns raw json (formatted in api, not sdk)
   else:
      return round(float(response.json()['Prediction']), 2) # make currency/rounding file to control this