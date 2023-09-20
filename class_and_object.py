class Phone:
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
    
    def add(self,number1,number2):
        return number1 + number2


phone1 = Phone("ios",123,True)
print("Phone OS: "+phone1.os)
print("Phone Model Number: "+str(phone1.number))
print("Is the phone water-proof? "+str(phone1.is_waterproof))
print("Is the phone's OS is IOS? "+str(phone1.is_ios()))

phone2 = Phone("android", 456, False)
print("Phone OS: "+phone2.os)
print("Phone Model Number: "+str(phone2.number))
print("Is the phone water-proof? "+str(phone2.is_waterproof))
print("Is the phone's OS is IOS? "+str(phone2.is_ios()))

