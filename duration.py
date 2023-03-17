import csv

class Bond:
    def __init__(self,facePrice,couponRate,ytm,m,years = 0) -> None:
        self.facePrice = facePrice
        self.couponRate = couponRate
        self.ytm = ytm
        self.m = m
        self.pvcf = 0 
        self.price = 0
        self.years = years
        self.MD = 0 
        self.D=0
        
        
    def computeBondPrice(self,periodicYtm,years):
        self.price = 0
        self.pvcf = 0
        cash_flow = self.facePrice*self.couponRate/self.m
        for period in range(years*self.m):
            if period == years*self.m - 1:
                self.price = self.price + (cash_flow+self.facePrice)/pow(1+periodicYtm, period+1)
                self.pvcf = self.pvcf + (period+1)*(cash_flow+self.facePrice)/pow(1+periodicYtm, period+1)
            else:
                self.price = self.price + (cash_flow)/pow(1+periodicYtm, period+1)
                self.pvcf = self.pvcf + (period+1)*(cash_flow)/pow(1+periodicYtm, period+1)
        self.MD = self.pvcf/self.price
        self.D = self.MD/(1+periodicYtm)
        
    def bondPrice(self):
        return self.price
    
    def modifiedDuration(self):
        return self.D
    def macaulayDuration(self):
        return self.MD     
    def effectDuration(self,periodicYtm,years,delta):
        self.computeBondPrice(periodicYtm-delta,years)
        ytm_decrease = self.price
        self.computeBondPrice(periodicYtm+delta,years)
        ytm_increase = self.price
        self.computeBondPrice(periodicYtm,years)
        ytm_original = self.price
        return  (ytm_decrease-ytm_increase)/(2*ytm_original*delta)
    def bondPriceChange(self,delta):
        return -self.D*self.price*delta
        


bond = Bond(100,.03,.09,1)






bondPrice=[]
Duration=[]
change_0001=[]
change_0003=[]

for year in [5, 10, 20, 30]:
    bond.computeBondPrice(bond.ytm,year)
    
    bondPrice.append(round(bond.bondPrice(),5))
    Duration.append(round(bond.modifiedDuration(),5))
    change_0001.append(round(bond.bondPriceChange(.001),5))
    change_0003.append(round(bond.bondPriceChange(.003),5))
    


with open('bondPrice.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(bondPrice)
    writer.writerow(Duration)
    writer.writerow(change_0001)
    writer.writerow(change_0003)


    

  





 

