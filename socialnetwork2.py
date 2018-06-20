## Made by Andres Pinon
## My Social Network

class User:
    def __init__(self, username):
        self.firstname = ""
        self.Lastname = ""
        self.username = username
        self.bios = ""
        self.Friends = []
        self.posts = []

    def crateID (self,nuke):
        self.userID

    def addFriend (self,door):
        self.Friends.append(door)

    def viewUsernames (self,username):
        for friend in self.friends:
            print(friend.username)
        
    def addPost (self, post):
        self.posts.append(post)

    def addBio (self,bio):
         self.bios = bio
            
    def addFirstname (self,Newfirstname):
        self.firstname = Newfirstname
         

    def addLastname (self,Newlastname):
        self.Lastname = Newlastname
    
    def viewFeed(self):
        for friend in self.Friends:
            print(friend.posts)

    def unFriend (self,obj):
        for friend in self.Friends:
            if friend.username == obj.username:
                self.Friends.remove(obj)

    def readbio (self):
         print (self.bios)
    
        
if __name__ == "__main__":
    Pinon = User("Pinon")
    Jaqualin = User("Jakie100")
    Andres = User("Shmecs")
    lucy = User("lucy123")

    Andres.addFirstname("Jaqualin")
    Andres.addFriend(Andres)
    Andres.addFriend(Jaqualin)
    Andres.addFriend(lucy)

    Andres.addPost("SUP DUDES")
    lucy.addPost("HELLO FRIEND")
    Jaqualin.addPost("HI BUD")
    Jaqualin.addBio("HEY, WHAT DOES THIS THING DO?")

    Andres.addLastname("AndresPM")
    Andres.addFirstname("Jaqualin")
    Andres.unFriend(lucy)
    Andres.viewFeed()
    Andres.addBio("MERCH LINK IN BIO WHICH MAKES NO SENSE BECAUSE THIS IS THE BIO")
    Andres.readbio()
    
