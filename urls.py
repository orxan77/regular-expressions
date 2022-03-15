import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# <re.Match object; span=(1, 23), match='https://www.google.com'>
# group(0) = match field of re.Match object
# group(1) = (www\.)?
# group(2) = (\w+)
# group(3) = (\.\w+)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0))

subbed_urls = pattern.sub(r'\2\3', urls)
# replaces the whole url with the 2nd and 3rd groups.
# e.g. https://www.google.com -> google.com 
print(subbed_urls)

matches = pattern.findall(urls)
for match in matches:
    print(match)