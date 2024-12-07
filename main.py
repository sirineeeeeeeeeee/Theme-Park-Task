# Theme Park Task
class Attraction:
    def __init__(self,name,capacity):
        self._name=name
        self._capacity=capacity
        
    def get_details(self):
        return(f"Attraction:{self._name},Capacity:{self._capacity}")
        
    def start(self):
        return("The attraction is starting!")
        
class ThrillRide(Attraction):
    def __init__(self,name,capacity,min_height):
        super().__init__(name,capacity)
        self.min_height=min_height
        
    def start(self):
        print(f"Thrill Ride {self._name} is now starting. Hold on tight! ")
        
    def is_eligible(self,height):
        if height >= self.min_height:
            return True
        else:
            return False
            
            
class FamilyRide(Attraction):
    def __init__(self,name,capacity,min_age):
        super().__init__(name,capacity)
        self.min_age=min_age
        
    def start(self):
        print(f"Family Ride {self._name} is now starting. Enjoy the fun!")
        
    def is_eligible(self,age):
        if age >= self.min_age:
            return True
        else:
            return False
            
            
class Staff:
    def __init__(self,name,role):
        self._name=name
        self._role=role
    def work(self):
        print(f"Staff {self.name} is performing their role: {self.role}")
        
        
class Visitor:
    def __init__(self,name,age,height):
        self._name=name
        self._age=age
        self._height=height
        
    def ride(self,attraction):
        if attraction.is_eligible(self._age)==True or attraction.is_eligible(self._height)==True :
            attraction.start()
        else:
            print("Sorry, you arent eligible for this ride either because of your age or because of your height :(")

thrillrideobject=ThrillRide("Rage",16,160)
Famrideobject=FamilyRide("Merry Go Round",20,4)
Visitorobject=Visitor("Sirine",16,160)
Visitorobject.ride(thrillrideobject)
Visitorobject.ride(Famrideobject)

thrillrideobject2=ThrillRide("Vampire",16,150)
Famrideobject2=FamilyRide("Ferris Wheel",100,4)

thrillrideobject.start()
thrillrideobject2.start()
Famrideobject.start()
Famrideobject2.start()