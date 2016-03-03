f = open("input.txt", 'r')

contents = f.read()

f.close()

x = open("output.txt", 'w')


number = 1

for char in contents:
    if number == 11:
        exit()
    x.write(char) 
    number = number + 1



