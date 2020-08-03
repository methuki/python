#! /usr/bin/python3

import webbrowser
### https://finance.yahoo.com/quote/RTX/

webbrowser.register("w3m", None, 1)

ticker = input("Stock ticher ? ")
url = "https://finance.yahoo.com/quote/" + ticker + "/"
 
print (url)
webbrowser.open(url, new=2) 
