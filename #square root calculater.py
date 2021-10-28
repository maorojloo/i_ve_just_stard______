#square root calculater
#babylonian algoritem

num = float(input ('enter a fukin number :'))
guess=num/2
while (abs(num-(guess**2)))>0.01 :
    divide = num/guess
    guess=(guess+divide)/2
    print ('cheking',guess)
