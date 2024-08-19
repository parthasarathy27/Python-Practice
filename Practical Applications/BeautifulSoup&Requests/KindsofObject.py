from bs4 import BeautifulSoup

# tag Objects

soup = BeautifulSoup('<b class = "boldest">Hello Python Programmer</b>', 'lxml')
tag = soup.html
tag.name = "Strong"
print(tag)

# Attributes (tag.attrs)

soup = BeautifulSoup('<input type = "text", name = "name", value = "Raju">', 'lxml')
tag = soup.input
print(tag.attrs)
tag['value'] = "Ravi"
print(f'After Update value : {soup}')

tag['id'] = 1011
del tag['name']
print(f'After Delete value and update id : {soup}')
