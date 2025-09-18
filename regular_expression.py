
import re

my_string = 'Esta es la leccion numero 7 de python: Leccion llamada expresiones regulares'
other_string = 'Esta no es la leccion numero 6, manejo de ficheros'

match = re.match('Esta es la leccion', my_string, re.I)
match_span = match.span()
start, end = match_span

# print(my_string[start:end])

match = re.match('Esta no es la leccion', other_string)
if match is not None:
    # print(match)
    start, end = match.span()
    print(other_string[start:end])
else:
    print('No hubo match')

# print(re.match('expresiones regulares', my_string))

# search

match = re.search('leccion', my_string, re.I)
start, end = match.span()
print(my_string[start:end])

match = re.findall('leccion', my_string, re.I)
print(match)

#  split

print(re.split(':', my_string))

#  sub

print(re.sub('[l|L]eccion', 'LECCION', my_string))
print(re.sub('expresiones regulares', 'RegEx', my_string))

#  Patterns

pattern = r"[lL]eccion|expresiones"
print(re.findall(pattern, my_string))

pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))