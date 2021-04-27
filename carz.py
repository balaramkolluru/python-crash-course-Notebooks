class Car:

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.make} {self.model} {self.year}"
		return long_name

	def update_odometer(self, miles):
		self.odometer_reading = miles

	def increment_odometer(self, miles):
		self.odometer_reading += miles


	def read_odemeter(self):
		print(f"This car has {self.odometer_reading} miles on it!")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odemeter()

my_used_car.increment_odometer(100)
my_used_car.read_odemeter()