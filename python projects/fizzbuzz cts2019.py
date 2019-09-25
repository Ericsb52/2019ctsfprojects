def fizz_buzz(maxnum,mutiple1,mutiple2):
    for num in range(1,maxnum +1):
        if num % mutiple1 == 0 and num % mutiple2 == 0:
            print (str.format("{} fiz buzz",num))
            continue
        elif num % mutiple1 == 0:
            print (str.format("{} fizz",num))
        elif num % mutiple2 == 0:
            print (str.format("{} buzz",num))
        else:
            print(num)
        
            

while True:
    maxnum = input("how high would you like to count \n")
    mutiple1 = input("what is the first number you would like to find all mutiples of \n")
    mutiple2 = input("what is the first number you would like to find all mutiples of \n")
    try:
        maxnum = float(maxnum)
        mutiple1 = float(mutiple1)
        mutiple2 = float(mutiple2)
    except:
        print("somthing went wrong try it again")
        continue
    break
fizz_buzz(maxnum,mutiple1,mutiple2)
        

    
