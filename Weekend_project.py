class ParkingGarage:
    
    
    
    def __init__(self,parking_spaces = 25,ticket = 25,current_ticket = {}):
        self.parking_spaces = parking_spaces
        self.ticket = ticket 
        self.current_ticket = current_ticket

    
    
    
    def take_ticket(self, item):
        print(f"number of available parking spaces {self.parking_spaces} and tickets {self.ticket}")
        self.item = item
        self.parking_spaces = self.parking_spaces - 1
        self.ticket = self.ticket - 1
        key = input("type in your License plate number ? ")
        value = input ("how many hours are you staying ? ")
        self.current_ticket[key] = value
    
    
    
    def pay_for_parking(self):
        key = input("type in your License plate number ? ")
        value = input ("how long have you stayed [1] less than one hour, [2] between 1 to 5 hours [3] more than 5 hours [4] less than 15 minitus? ")
        if int(value) == 4:
            print("you are good to go with no charge!")
            if key in self.current_ticket:
                del self.current_ticket[key] 
        elif int(value) == 1:
            paid_amount  = input(" your charge is 10 dollar enter the amount you wish to pay ? ")
            if int(paid_amount) >= 10:
                if key in self.current_ticket:
                    del self.current_ticket[key] 
                print("you have 15 minitues to leave the garage! ")
            elif int(paid_amount) < 10:
                print("you need to pay the full amount")
        elif int(value) == 2:
            paid_amount  = input(" your charge is 20 dollar enter the amount you wish to pay ? ")
            if int(paid_amount) >= 20:
                if key in self.current_ticket:
                    del self.current_ticket[key] 
                print("you have 15 minitues to leave the garage! ")
            elif int(paid_amount) < 20:
                print("you need to pay the full amount")
        elif int(value) == 3:
            paid_amount  = input(" your charge is 30 dollar enter the amount you wish to pay ? ")
            if int(paid_amount) >= 30:
                if key in self.current_ticket:
                    del self.current_ticket[key] 
                print("you have 15 minitues to leave the garage! ")
            elif int(paid_amount) < 30:
                print("you need to pay the full amount")       
        else:
            print("please type in digitsb 1,2,3,4")
        
    
    
    def leave_garage(self):
        key = input("type in your License plate number ? ")
          
        if key not in self.current_ticket:
            print('Thank You have a nice day')
            self.parking_spaces = self.parking_spaces + 1
            self.ticket = self.ticket + 1
        elif  key in self.current_ticket:
            print("you forgot to pay")
        else:
            print("type correct license plate")
        
     
# carone = ParkingGarage()
# cartwo = ParkingGarage()
# carone.take_ticket(1)
# cartwo.take_ticket(1)
# carone.pay_for_parking()
# cartwo.pay_for_parking()
# carone.leave_garage()
# cartwo.leave_garage()
# print(carone.ticket)
# print(carone.parking_spaces)
# print(carone.current_ticket)
