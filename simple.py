import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# r'abc' is a raw string. ignores escape characters and takes them as raw strings.
# print('normal string:', '\tTab')
# print('raw string:', r'\tTab')
# normal string:  Tab
# raw string: \tTab

pattern = re.compile(r'abc')  # case-sensitive
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)  # <re.Match object; span=(1, 4), match='abc'>
# print(text_to_search[1:4])  # abc

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # matches the phone numbers
matches = pattern.finditer(text_to_search)

for match in matches:
    # print(match)
    ...


## data.txt file.

# no need to escape the characters inside of the brackets.
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# r'[89]00\d[-.]\d\d\d[-.]\d\d\d\d' match numbers beginning with 800 or 900
# r'[0-9]00\d[-.]\d\d\d[-.]\d\d\d\d' when - is inserted bw two values, it acts like range
# r'[^a-zA-Z]' when inside brackets acts like negate. all characters except lower and capital letters
# r'^[a-zA-Z]' when outside brackets matches the beginning of string e.g. all strings beginning with
# lower and capital letters.


### Quantifiers
# r'\d{3}[-.]\d{3}[-.]\d{4}' \d{n} the digit character repeated n times
# r'Mr\.?' 0 or 1 (optional) dot (.)
# r'Mr\.?\s[A-Z]\w*' 0 or more word characters after capital letter after space
# r'M(r|s|rs)\.?\s[A-Z]\w*' or r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*'

with open('data.txt', mode='r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
