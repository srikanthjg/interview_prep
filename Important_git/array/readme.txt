Strings:

Raw Strings
You can place an r before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string.
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.

Escape characters:
spam = 'Say hi to Bob\'s mother.'

Triple Quote:
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

Slicing:
the starting index is included and the ending index is not.

In operator:
'Hello' in 'Hello World' ==> True
'cats' not in 'cats and dogs' ==> False


spam = spam.lower()
'hello'.isalpha() ==> True

Join:
', '.join(['cats', 'rats', 'bats'])
  'cats, rats, bats'
' '.join(['My', 'name', 'is', 'Simon'])
  'My name is Simon'

Split:
'My name is Simon'.split()
  ['My', 'name', 'is', 'Simon']
'MyABCnameABCisABCSimon'.split('ABC')
  ['My', 'name', 'is', 'Simon']
