import datetime


class datesp:
    now=datetime.date.today()
    
    def __init__(self,std=1,endd=1):
        if std==1 and endd==1:
            
            self.std="1989-01-01"
            self.endd=str(datesp.now)
            
        else:
            self.std=std
            self.endd=endd           
        
    def spl(self,std=0,endd=0):
        
        day=[]
        std2=[]
        endd2=[]
        
        std=self.std.split("-",2)
        endd=self.endd.split("-",2)
        
        for j in std:
            std2.append(int(j))
        for j in endd:
            endd2.append(int(j))
            
        day.append(std2)
        day.append(endd2)
        
        return day

    def zeroof(self,num):
        if num < 10:
            num= "0"+str(num)

        return str(num)
    
    def dayaddof(self,year,mon,sday=1,eday=31,addof=1):
        listof=[]
        c=True
        date=str(year)+"-"+self.zeroof(int(mon))+"-"+self.zeroof(int(sday))
        listof.append(date)
        while c:
            sday+=addof
            
            if sday >= eday:
                sday=eday
                c=False
            mon=self.zeroof(int(mon))
            sday2=self.zeroof(int(sday))

            date=str(year)+"-"+str(mon)+"-"+str(sday2)
            listof.append(date)
        return listof

    def sday(self):
        
        days=[]
        
        adday=1
        seday=self.spl()
        
        sday=seday[0]
        eday=seday[1]
        day =int(sday[2])
        
        n=True
        
        while n:
            
            if int(sday[0]) == int(eday[0]):

                while int(sday[1]) <= int(eday[1]):
                    if int(sday[1]) == int(eday[1]):
                        
                        days.extend(self.dayaddof(sday[0],sday[1],sday[2],eday[2]))
                    else:
                        days.extend(self.dayaddof(sday[0],sday[1],sday[2]))
                        
                    sday[2]=1
                    sday[1]+=1
                n=False
            
            else:
                
                while int(sday[1]) <= 12:
                    days.extend(self.dayaddof(sday[0],sday[1],int(sday[2])))
                    sday[2]=1
                    sday[1]+=1
                sday[1]=1
                sday[0]+=1
                
        return(days)

    def main(self):
        a=0
        b2=[]
        
        listof=self.sday()
        listof2=[]
        
        if len(listof)<=2:
            listof2=listof
        else:
            
            for i in listof:

                b=i
                day=[]
                if  a==0:
                    a=b
                else:
                    day.append(a)
                    day.append(b)
                    listof2.append(day)
                    b2=b.split("-",2)
                    
                    b=""
                    if b2[2] == "31":
                        b=0
                    else:
                        b2[2]=self.zeroof(int(b2[2])+1)
                        b=b2[0]+"-"+b2[1]+"-"+b2[2]
                    a=b
  
        return listof2
        

def oned(a):
    listt=[]
    list2=a
    
    if type(list2[0]) != list:
        
        listt.extend(list2)
    else:   
        listt.append(list2[0][1])
        for i in list2:
            listt.append(i[0])
        lisv=listt[0]
        lisvv=listt[1]
        listt[0]=lisvv
        listt[1]=lisv
    
    return listt


