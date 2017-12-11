def rotate_word(string, integer):
	r = ''
	for letter in string:
		a = ord(letter)
		if ord('a') <= a <= ord('z'):
			b = ord('a')
		else:
			b = ord('A')
		a = a + integer - b
		while a < 0:
			a = a + 26
		r += chr(a % 26 + b)
	return r

