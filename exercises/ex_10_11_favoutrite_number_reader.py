import json

filename = 'ex_10_11_favoutrite_number.json'

try:
	with open(filename) as f:
		number = json.load(f)
except:
	print(f"There are somthinng wrong. Contact somebody...")
else:
	print(f"I knnow your favourite number. It's {number}".)
