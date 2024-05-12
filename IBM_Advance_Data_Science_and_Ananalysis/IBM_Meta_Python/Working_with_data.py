''''' with open('example.txt', 'r') as readfile:
    with open('example2.txt','w') as writefile:
        for line in readfile:
            writefile.write(line) '''''

#with open ('file.txt', 'w') as file :
#    file.write('this is a \n')
#    file.write('this is b')

#    print(file)
    
with open ('file.txt', 'r' ) as file:
    read_file=file.read()
    
    print(read_file )

