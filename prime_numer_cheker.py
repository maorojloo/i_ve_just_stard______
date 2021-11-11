
def prime_checker(input):
    counter = 0;
    for i in range (2,input):
        if input%i == 0:
            counter=counter+1;
    if counter <1:
        print(input);

for i in range (2,10000):
    prime_checker(i)
