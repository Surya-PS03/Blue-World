import requests
base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
word = input("Enter the word: ")
def meaning(w,b):
  URL = b + w 
  response = requests.get(URL)
  if response.status_code == 200:
    data = response.json()
    print(data)
    a_definition = data[0]['meanings'][0]['definitions'][0]['definition']
    print(f"The first meaning of word is: {a_definition}")
    b_definition = data[0]['meanings'][1]['definitions'][0]['definition']
    print(f"The second meaning of word is: {b_definition}")
  else:
    print(f"Error {response.status_code}")
meaning(word,base_url)
