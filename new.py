class base:
    def __init__(self):
        self.d = {}
        print("HELLO USER")
        # file = open(r'C:\tech practice\read and write.txt', 'r')
        # content = file.read()
        # lines = file.readlines()
        # print(content)
        # print(lines)
        
                

                # print(line.strip())


        
    def inputtt(self):
        self.i=True
        self.i1=False
        while self.i==True:
            
            ii=input("do u want to add car model:")

            
            if ii=="y": 
                a=input("enter car brand name:")
                b=input("enter car model name:")
                
                self.file1 = open(r'C:\tech practice\read and write.txt', 'r+')
                z=self.file1
                z.write(a)
                z.write(' ')
                z.write(b+'\n')
                # z.flush()
                # os.fsync(z.fileno())
                # self.file1.seek(0)
                # line=self.file1.readlines()
                # ent=int(input("enter the line :"))
                # line1=line[ent]
                # x,y=line1.split()
                # print(x,y)

                # with open(r'C:\tech practice\read and write.txt', 'r') as file:
            
                    
                #     for line in file:
                #         print(line)
                print("<--- SUCCESSFULLY ADDED --->")
                self.i1=True
               
            else:
                print("HAVE A NICE DAY")
                self.i=False
                

                

    def second(self):

        if self.i1:
            d=self.d
            count=1
            ind=list(d)
            # for k,v in d.items():
            
            #     print(count,k,v)
            #     count+=1

            # st11,stt1=input("enter name of car brand and model:").split()
            # print(st11,stt1)
            # key= [key for key, val in self.d.items() if val == stt1]
            # if self.d[st11]==stt1:
            a=self.file1
            line=a.readlines()
            print(line)

            ent=int(input("enter the line :"))
            line1=line[ent-1]
            x,y=line1.split()
            print(x,y)

            print(f"SELECTED CAR BRAND {x} NAME ")
            
    
            q=False
            a=True
            while a:
                print(f"enter start to start the {x} car")
                print(f"enter stop to stop  car")
                print("terminate to terminate:")
                a=input("enter your chooes:")
                if a=="start":
                    if q:
                        print(f"ur  car already started\n")
        
                    else:
                        q=True
                        print(f"ur  car started\n")
    
                elif a=="stop":
                    if q:
                        print(f"ur  car stoped \n")
                        q=False
                    else:
                        print(f"ur  car already stoped\n")
                elif a=="terminate":
    
                    print("terminated")
                    print("HAVE A NICE DAY")
                    break
        
            else:
                print("!! SOMETHING WENT WRONG !!\n  PLEASE CHECK THE INPUT U ENTERD")
        else:
            pass
        





        
o=base()
o.inputtt()
o.second()
            

            
        
        
