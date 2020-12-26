import sys

class Error():

	def __init__(self):
		self.write_location = sys.stderr

	def write(self, message):
		self.write_location.write(message)

	def setErrorLocation(self, location):
		self.write_location = location



if __name__ == '__main__':
	print("Don't run this file from the command line.")
else:
	ERROR = Error()