from sys import argv # imports the argv from sys module.

script, filename = argv #defining no. of arguments.(script is default and filename is userdefine input.)

txt = open(filename)

print("Here's your file %r:" % filename)
file_content = txt.read()
print(file_content)

#-----------------------------------------

print("I'll also ask you to type it again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
