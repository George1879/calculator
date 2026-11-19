from calculator import split_input

def test_add():
	assert split_input("5 + 2") == 7.0

def test_divide():
	assert split_input("6 / 2") == 3

def test_subtract():
	assert split_input("7 - 3") == 4

def test_multiply():
	assert split_input("5 * 3") == 15

def test_negative_addition():
	#arrange
	a= 7
	b= -2

	#act
	result = split_input(str(a)+" + "+str(b))

	#assert
	assert result == 5
