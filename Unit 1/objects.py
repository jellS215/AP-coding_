


class instaProfile:
    def __init__(self, username, followers, following, posts):
        self.username = username
        self.followers = followers
        self.following = following
        self.posts = posts

    def display_profile(self):
        print(f"Username: {self.username}")
        print(f"Followers: {self.followers}")
        print(f"Following: {self.following}")
        print(f"Posts: {self.posts}")




class CarMaker:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        
    def windshieldwipers(self, On, Off):
        if On:
            print("Windshield wipers activated")
        if Off:
            print("Windshield wipers deactivated")
        
    def headlights(self, Low_beam, High_beam, Off):
        if Low_beam:
            print("Low beam headlights turned on")
        if High_beam:
            print("High beam headlights turned on")
        if Off:
            print("Headlights turned off")
        
    def airbag(self, On, Off):
        if On:
            print("Airbag deployed")
        if Off:
            print("Airbag deactivated")
        
    def turnsignal(self, left, right):
        if left:
            print("turn left")
        if right:
            print("turn right")
        if not left and not right:
            print("no turn signal")
            
            
    # Creating an instance of CarMaker outside the class definition
ToyotaCarolla = CarMaker("Toyota", "Corolla", 2020, "Blue")
def display_car_info(ToyotaCarolla):
    print(f"Car Brand: {ToyotaCarolla.brand}")
    print(f"Car Model: {ToyotaCarolla.model}")
    print(f"Car Year: {ToyotaCarolla.year}")
    print(f"Car Color: {ToyotaCarolla.color}")

# Call the function and some methods to produce output
display_car_info(ToyotaCarolla)
ToyotaCarolla.headlights(Low_beam=True, High_beam=False, Off=False)
ToyotaCarolla.turnsignal(left=False, right=False)
ToyotaCarolla.windshieldwipers(On=True, Off=False)
ToyotaCarolla.airbag(On=False, Off=True)


class IPhone:
    def __init__(self, model, storage, color, os_version):
        self.model = model
        self.storage = storage
        self.color = color
        self.os_version = os_version
    
    
    def make_call(self, number):
        print(f"Calling {number}...")
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")
    def take_photo(self):
            print("Photo taken!")
    def install_app(self, app_name):
            print(f"Installing {app_name}...")
    def update_os(self, new_version):
            print(f"Updating iOS to version {new_version}...")
            self.os_version = new_version
            print("Update complete.")

   
        
phoneA = IPhone("iPhone 13", "128GB", "Midnight", "iOS 15")

phoneB = IPhone("iPhone 14 Pro", "256GB", "Deep Purple", "iOS 16")

phoneA.make_call("123-456-7890")
phoneA.send_message("123-456-7890", "Hello, Phone B!")


phoneB.make_call("987-654-3210")
phoneB.send_message("987-654-3210", "Hi there, Phone A!")


        




    