
try:

    f = open("tfc.txt")
    p=1
    b=3

    #p=b/0
    for line in f:
        print(line)


    #f=open("abc.txt")
except FileNotFoundError as e:
    print(e.filename)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
#except FileNotFoundError:
    #print("you should not have done this to me")
#except ZeroDivisionError:
    #print("dont divide by zero you fool")

#i=0/0
#hey there

