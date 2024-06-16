#  Install the Python Requests library:
# `pip install requests`
import requests

def send_request():
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': '8KGX7HWF6F7K7V74S99RYJW22Z8EIE8GU68SNBTIGMD9P51PSGAWWYI79VTMHZZNGVW8Q9LS6BKXB6N6',
            'url': 'https://www.mobile.de/ro/Automobil/BMW-Gran-Coup%C3%A9-420d-M-Paket-Facelift/vhc:car,ms1:3500__/pg:vipcar/394150676.html',
        },
        
    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
send_request()