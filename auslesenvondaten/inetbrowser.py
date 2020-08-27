import webbrowser as wb

url = "www.google.de/search?q="
suchbegriff = input("Bitte Suchbegriff eingeben: ")
wb.open(url+suchbegriff)
