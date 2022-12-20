import datetime


class BookLibrary():
    def __init__(self,Booklist,Handler):
        self.BookList = Booklist
        self.Handler = Handler

if __name__ == '__main__':
    BL = BookLibrary(["Python", "Java", "DataScience", "SQL", "Web"], "Ramesh")
    #print(BL.BookList)
    Blist = BL.BookList.copy()
    #TakenHistory = {"Takenname": "TakenBookName"}
    #ReturnHistory =  {"ReturnName":"ReturnBookName"}
    #print(len(TakenHistory))

    while True:
        print("Enter 1 to Display books")
        print("Enter 2 to TAKE Books")
        print("Enter 3 to RETURN BOOKS")
        print("Enter 4 to view History")
        

        userinput = int(input("Enter the number b/w 1 and 4 :: "))
        if userinput not in [1,2,3,4]:
            print("***********************Enter the valid number***************************************")
        else:

            if(userinput == 1):
                print("*******************************************")
                print(f"The Following Books Are under control of {BL.Handler}")
                for i in Blist:
                    print(i)
                print("*******************************************")

            elif(userinput==2):

                TakenBookName = str(input("Enter the Book Name you want :: "))


                if(TakenBookName in Blist):
                    TakenCustomer_Name = str(input("Enter your name :: "))
                    print(f"The Book was given to {TakenCustomer_Name}")
                    Blist.remove(TakenBookName)
                    # print(Blist)
                    #TakenHistory.update({TakenCustomer_Name:TakenBookName})
                    file = open("BookLib.txt", "a")
                    file.write(f"The Book {TakenBookName} is Taken by {TakenCustomer_Name} @ {datetime.datetime.now()}\n")
                    file.close()

                else:
                    print("The book isn't in the library")

            elif(userinput==3):
                ReturnBookName = str(input("Enter the Book Name you Return :: "))
                if((ReturnBookName in BL.BookList) and (ReturnBookName not in Blist)):
                    ReturnCustomer_Name = str(input("Enter your name :: "))
                    print(f"The Book was submitted by {ReturnCustomer_Name}")
                    Blist.append(ReturnBookName)
                    #ReturnHistory.update({ReturnCustomer_Name:ReturnBookName})
                    file = open("BookLib.txt", "a")
                    file.write(f"The Book {ReturnBookName} is Taken by {ReturnCustomer_Name} @ {datetime.datetime.now()}\n")
                    file.close()

                else:
                    print("The Book doesnt match ")

            else:
                f = open("BookLib.txt")
                content = f.read()
                print(content)
                # HistoryInput = int(input("Enter 1 to view TakenHistory 2 to view ReturnHistory"))
                # #i = 1
                # if HistoryInput==1:
                #     # for x,y in TakenHistory.items():
                #     #     print(x,"==>",y)
                # elif(HistoryInput==2):
                #    # for x,y in ReturnHistory.items():
                #    #     print(x,"==>",y)
                #
                # else:
                #     print("Enter the valid Number")


