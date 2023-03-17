response = requests.get("https://api.chucknorris.io/jokes/random")
response_text = response.text
dict = json.loads(response_text)
joke = dict['value']



