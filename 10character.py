f = open("input.txt", 'r')

contents = f.readlines()

f.close()

x = open("output.txt", 'w')


number = 1


for line in contents:
    for char in line:
        if number == 11:
            break
        x.write(char) 
        number = number + 1
    number = 1



