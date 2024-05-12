#if else statement
#age=17
#if(age>18):
    #print('you can enter')
#else:
    #print('go see meat loaf')

#print('move on ')

#loops#
squares=['orange', 'orange', 'purple', 'blue']
new_squares=[]
i=0
while (squares[i]=='orange'):
    new_squares.append(squares[i])
    
    i=i+1
print(new_squares)

#Functions
def type_of_album(artist,album, year_released):
    print(artist,album,year_released)
    if year_released>1980:
        return 'modern'
    else:
        return 'Oldie'
x=type_of_album('michael Jackson', 'Thriller', 1980)
print(x)

#try, except, else, finally, statement
a=1
try:
    b=int(input('please enter a number'))
    a=a/b
except ZeroDivisionError:
    print('zero division error')
except ValueError:
    print('value error')
except:
    print('error')
else:
    print(a)

finally:
    print('everthing is okey')


#local and global veriable
def get_total(a,b):
    total=a+b
    print(special)

    def double_it():
        double=total*2
        print(special)
    double_it()

    return total

#dictionary
employee= {
1234:{ 'id':'12345', 'name':'memet','department':'programmer' }, 
12458: {
        "id": "12458",
        "name": "Rosandro", 
        "department": "House Floor"   }
 
 }
def get_employee_from_dic(id):
    return employee[id]
print(get_employee_from_dic(12458))

