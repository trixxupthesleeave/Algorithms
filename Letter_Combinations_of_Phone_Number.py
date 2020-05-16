"""
Name: Letter combinations of phone number
Q No: 17
Desc: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
	  could represent. A mapping of digit of letter (just like on the telephone buttons) is given below. Note that 
	  1 does not map to any letters. 

Example:
	input: 	"23"
	output:	["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
	
Notes:
	Initial thoughts:
		Create a dictionary for the telephone pad words and map it each digit that will be entered in the string 

		Will have to iterate through the string values and check if the value exists in the dictionary. 
		Create a contigous array of the values from the dictionary. 

		2: abc
		3: def
		4: ghi
		5: jkl
		6: mno
		7: prqs
		8: tuv
		9: wxyz

		"23" = "abcdef"

		ad, ae, af, bd, be, bf
	
		first fucntion will be very similar to the second one. 
		Will have to incorporate the first and second into one recrusive call. The code will be a lot more efficient.

		second function:
			def func2(char, str2):
				if not str2:
					return
				print(char+str2[0])
				func2(char, str2[1:])

"""

class PhoneToCombinations:
	def letterCombinations(self, digits: str) -> List[str]:
