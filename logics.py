# Find the Avg of three numbers
n1=int(input("Enter First number : "))
n2=int(input("Enter Second number : "))
n3=int(input("Enter Third number : "))
sum=n1+n2+n3
avg=sum/3
print("Avg of 3 numbers : ",avg)

#Output
# Enter First number : 12
# Enter Second number : 12
# Enter Third number : 12
# Avg of 3 numbers : 12.0



# finding profit percentage

cp=int(input("Enter Cost price: "))
sp=int(input("Enter Selling price: "))
profit=sp-cp
profitpercent=(profit/cp)*100
print("profit percentsge : ",profitpercent,"%")

#Output
# Enter Cost price: 200
# Enter Selling price: 300
# profit percentsge :  50.0 %



# finding missing angle 
angel_1=int(input("Enter angel 1 : "))
angel_2=int(input("Enter angel 2 : "))
missing_angel=180-(angel_1+angel_2)
print("Missing Angel : ",missing_angel)

#output
# Enter angel 1 : 40
# Enter angel 2 : 60
# Missing Angel : 80



# display last element in number 
n=int(input("Enter a number : "))
lasi_digit=n%10
print("Last digit of given number : ",lasi_digit)

#Output
# Enter a number : 123
# Last digit of given number :  3



# remove last digit from given number 
n=int(input("Enter a number : "))
lasi_digit=n//10
print("Without Last Digit : ",lasi_digit)

#Output
# Enter a number : 123                           
# Without Last Digit :  12



# Find the first digit of 4 digit number
n=int(input("Enter a number : "))
First_digit=n//1000
print("First digit of 4 digit number : ",First_digit)

#Output
# Enter a number : 2345
# First digit of 4 digit number :  2



# Find the Sum of First n Natural Numbers
n=int(input("Enter a Number : "))
sum=n*(n+1)/2
print("Sum of First n Natural Numbers : ",sum)

#output
# Enter a Number : 10
# Sum of First n Natural Numbers :  55.0



# Find the Avg of First n Natural Numbers 
n=int(input("Enter a Number : "))
sum=n*(n+1)
Avg=sum/n 
print("Avg of First n Natural Numbers : ",Avg)

# Output
# Enter a Number : 10
# Avg of First n Natural Numbers :  11.0
