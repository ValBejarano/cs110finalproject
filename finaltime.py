import time

def main():

	seconds = 0
	runtime = True
	while runtime == True:
		print(seconds)
		# Sleep for a second
		time.sleep(1)
		# Increment the seconds total
		seconds += 1

		
main()
