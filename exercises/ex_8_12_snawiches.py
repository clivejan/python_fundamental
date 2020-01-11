def make_sandwich(*metarials):
	"""summarize an ordered sandwich"""
	print("\nThe sandwich will be made with:")
	for metarial in metarials:
		print(f"- {metarial}")

make_sandwich('booger')
make_sandwich('booger', 'sock')
make_sandwich('booger', 'sock', 'rock')
