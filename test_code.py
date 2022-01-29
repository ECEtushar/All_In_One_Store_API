import requests

url = "http://ecetushar.pythonanywhere.com/post"

payload = '''[{
       "item": "Headache pills",
       "itemCategory": "Medicine",
       "quantity": 50,
       "price": 50
    },

        {
       "item": "Sandwich",
       "itemCategory": "Food",
       "quantity": 2,
       "price": 200
   }

        ]'''
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
