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
matches = pattern.search(text_to_search)

# print(matches)  # <re.Match object; span=(1, 4), match='abc'>
# print(text_to_search[1:4])  # abc


