def make_album(artist, title, numbers=None):
	
	if numbers:
		album = {'artist': artist, 'title': title, 'numbers': numbers}
	else:
		album = {'artist': artist, 'title': title}

	return album

while True:
	print("Please enter the information of an album: ('q' to quit)")
	artist = input("The artist: ")
	if artist == 'q':
		break
	title = input("The title: ")
	if title == 'q':
		break

	album = make_album(artist, title)
	print(album)
