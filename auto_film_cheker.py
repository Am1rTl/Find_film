#
import webbrowser
a = input()
b = []
g = 0
s = ''
a+=' '
for i in range (0,len(a)):
	if a[i] == ' ' :
		b.append(s)
		s = ''
		g+=1
	else:
		s = s+a[i]
s = ''
for i in b:
	s = s+i+'+'
s = s[:-1]
try:
	webbrowser.get('chrome').open('https://www.youtube.com')	
except:
	try:
		webbrowser.get('yandex').open('https://www.youtube.com')
	except:
		webbrowser.open_new('https://www.kinopoisk.ru/index.php?kp_query='+s)
