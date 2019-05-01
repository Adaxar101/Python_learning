import unittest
import cap

class TestCap(unittest.TestCase):   #tworzenie klasy, która ma być wywoałana po zakończeniu dziedzicenia z jednostki testowej

	def test_one_word(self):       #a następnie funkcja, która ma być wywołana
		text = 'python'
		result = cap.cap_text(text)   #wywołanie funkcji do testu
		self.assertEqual(result,'Python')

	def test_multiple_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
	unittest.main()

	#testowanie w cmd:   python test_cap.py