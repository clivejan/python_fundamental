def make_car(brand, model, **car_info):
	"""build the information avout a car"""
	car_info['brand'] = brand
	car_info['model'] = model

	return car_info

car = make_car('Audi', 'Q5', color='black', all_packages=True)
print(car)
