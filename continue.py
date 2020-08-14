#! /usr/bin/python3

oddNum = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

print ("These are all the even numbers from 1-18")

for n in range(0, 20):
	if n in oddNum:
		continue
	print(n)
