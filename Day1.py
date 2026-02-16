


dic={}



max=0
person=''
while True:
    name=input("please enter your name")
    price=float(input( "please enter a price"))
    dic[name]=price

    if price >max :
        max=price
        person=name

        x =input("Do  you have any other player ")
        print('\n'*100 )
        
        if x=='no':
         break
print(f'the player{name} is winner by price{max}')

    