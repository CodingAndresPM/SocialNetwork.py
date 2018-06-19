## Made by Andres Pinon
## My Social Network

class User:
    def __init__(self, username):
        self.firstname = ""
        self.Lastname = ""
        self.username = username
        self.bios = ""
        self.friends = []
        self.posts = []

    def addFriend (self,door):
        self.friends.append(door)

    def addUsernames (self,username):
        self.usernames.append(username)

    def addPost (self, post):
        self.posts.append(post)

    def addBio (self,bio):
        self.bios.append(bio)

    def addFirstname (self,firstname):
        self.firstname.append(firstname)

    def addLastname (self,lastname):
        self.Lastname (self, lastname)
    
    def viewFeed(self):
        for friend in self.friends:
            print(friend.posts)

    def unFriend (self,obj):
        for friend in self.friends:
            if friend.username == obj.username:
                self.friends.remove(obj)
    
    def profileName(self):
        for friend in self.friends:
            print(friend.username)
        
    
        
if __name__ == "__main__":
    
    Pinon = User("Pinon")
    Jaqualin = User("Jakie100")
    Andres = User("Andres")
    lucy = User("lucy123")
    
    
    Andres.addFriend (Jaqualin)
    Andres.addFriend(lucy)

    Jaqualin.addPost("HI")
    lucy.addPost("HELLO FRIEND")
    Jaqualin.addPost("HI BUD")


    Andres.profileName()
    Andres.unFriend(lucy)
    Andres.viewFeed()
    

    
