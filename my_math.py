def calculate():
	operand = input("What should we do?")
	firstnum = int(input("okay, Give the firt number : "))
	second_num = int(input("that's good! provide the second number: "))

	if operand == "add":
		return firstnum + second_num
	elif operand == "subtract":
		return firstnum - second_num
	elif operand == "multiply":
		return firstnum * second_num
	elif operand == "divide":
		return firstnum / second_num
	else:
		return "invalid input"

print (calculate())
