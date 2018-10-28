import urllib.request
url = "http://dfedorov.spb.ru/python/files/tutchev.txt"
url2 = "http://dfedorov.spb.ru/python/files/tutchev.jpg"
with open("tutchev.html", 'w', encoding = 'utf-8') as file:
    file.write('''
<!DOCTYPE html>
<html>
    <head>
       <meta charset="utf-8">
       <title>Стихи</title>
    </head>
    <body>''')
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        with open("tutchev.html", 'a', encoding = 'utf-8') as file:
            line = line.decode('utf-8')
            file.write(line + '<br>')

with urllib.request.urlopen(url2) as webpage:
    with open("tutchev.html", 'a', encoding = 'utf-8') as file:
        file.write('<p><img src=' + url2 + ' alt="Портрет Тютчева">'+'<p>')
        
with open("tutchev.html", 'a', encoding = 'utf-8') as file:
        file.write( '''</body>
</html>''' )
