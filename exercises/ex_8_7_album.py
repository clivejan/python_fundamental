def make_album(artist, title, numbers=None):
	
	if numbers:
		album = {'artist': artist, 'title': title, 'numbers': numbers}
	else:
		album = {'artist': artist, 'title': title}

	return album

twice_album = make_album('TWICE', 'Feel Special', 7)
zione_alnum = make_album('IZ*ONE', 'HEART*IZ', 8)
blackpink_album = make_album('BLACKPINK', 'Blackpink in Your Area')

print(twice_album)
print(zione_alnum)
print(blackpink_album)
