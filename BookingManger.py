from booking import Booking
from passangerManager import PassagerManager
from FlightManger import FlightManager  
class BookingManager():
    Bookings = []
    flightmg= FlightManager()
    passangermg = PassagerManager()
    def list(self):
        for info in self.Bookings:
            self.show(info)
    def show(self,info):
        print(info.name,"  ",info.SitNumber," ",info.Price," ",info.TypeOfFlight," ",info.TimeOfFlight," ",info.destination)
    def create(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name,flightno):
        avalFlight = self.flightmg.find(flightno)
        
        if avalFlight == None:
            print("Flight no available")
            return False
        
        else:
            info = Booking(destination,TimeOfFlight,TypeOfFlight,SitNumber,name,avalFlight)
            self.Bookings.append(info)
            return True
    def find(self,SitNumber):
        for info in self.Bookings:
            if info.SitNumber == SitNumber:
                return info
    def delete(self,SitNumber):
        info = self.find(SitNumber)
        self.Bookings.remove(info)
    def update(self,destination,TimeOfFlight,TypeOfFlight,Price,SitNumber,name):
        info = self.find(SitNumber)
        info.name = name
        info.destination = destination
        info.TimeOfFlight = TimeOfFlight
        info.TypeOfFlight = TypeOfFlight
        info.Price = Price




