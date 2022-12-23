class time:
    __hour__=00;
    __minute__=00;
    __second__=00;
    def readtime(self):
        self.hour=int(input("enter the hour: "));
        self.minute=int(input("enter the minute: "));
        self.second=int(input("ether the second: "));
    def __add__(self,t2):
        t_h=self.hour+t2.hour;
        t_m=self.minute+t2.minute;
        t_s=self.second+t2.second;

        if(t_s>59):
            t_s=t_s-60
            t_m=t_m+1
        if(t_m>59):
            t_m=t_m-60
            t_h+=1
        return(t_h, t_m, t_s);

t1=time();
t2=time();
t1.readtime();
t2.readtime();
t3=t1+t2;
print(t3);
