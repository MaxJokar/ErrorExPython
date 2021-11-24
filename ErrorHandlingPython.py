print("==============================START================================================================")
while True:
    def Result(x,y):
        if not isinstance(x ,int):   
                raise ValueError() #The x is determined to show what is in process 
        
        if not isinstance(y ,int):   
                raise ValueError()  #The x is determined to show what is in process 
      
        if y=='0':
               raise ZeroDivisionError()    # Also possible :raise ZeroDivisionError("\tError Zero Division Error 1")
            
            # return x,y
    
    try:  
                print("\tIn order  to divide Two Numbers,Please Enter Two Integer numbers one after the Other to divide ")
                x=int(input("\t\t\t\tEnter a number : "))
                y=int(input("\t\t\t\tEnter a number ,Except for  '0': "))
                Result(x,y)
                Result=x/y
                print(f"\t\t\t\tthe Result of Your Division is : {Result}\n")

                list1=[56,59,78,100,21,36,78]
                print(list1)
                n=int(input("\t\twhat index number from this list is needed  : "))
                n-=1
                print(f"\t\t\t\tThe index number you Asked  from the  list is : {list1[n]}")

    except ValueError  : #as error
                
                  print(f"\t\t\t\t'VALUE ERROR' . Not CORRECT :  You MAY   have studied 'Maths Badly '   In School :)   ") #number 2  to  destinguish which error  is working 
                
    except ZeroDivisionError : #as error:
               print("\t\t\t\t Do Not Enter ZERO  X/0==>ZERO DIVISION ERROR")   
    
    except IndexError as error:
               print(error)   
    
    
            
    finally:
        continuish="c" # Determine to  Determine the Logic of  True or False to Continue over again OR Not 
        proceedish= str(input("\t\t\t\tTo Contine ,  Please Type  'c' :"))
        if proceedish==continuish:
            continue
        else:
            print("\t\t\t\tHAVE A GOOD  TIME &  GOODBYE")
                 
            print("===================================THE  END ========================================================")    
            break
