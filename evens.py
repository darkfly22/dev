def even():
	first_num  = int(input("Give a first number"))
	second_num = int(input("Give a second number to print the even numbers in between"))
	
	i =first_num + 1
	while i < second_num - 1:
		if i %2 == 0:
			print (i)
		i = i + 1


even()

def rev_even():
        first_num  = int(input("Give a first number"))
        second_num = int(input("Give a second number to print the numbers between in a reverse order"))

        i = second_num - 1
        while i > first_num + 1:
                if i %2 == 0:
                        print (i)
                i = i - 1


rev_even()
