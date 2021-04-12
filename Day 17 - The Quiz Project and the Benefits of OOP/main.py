class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1

    def greet(self):
        print(f"Welcome... \nID: {self.id} - Username: {self.username}")


user1 = User("001","tom")
user2 = User("002","Chris")

user1.follow(user2)
print(user1.followers)
print(user1.following)

user1.greet()

print(user2.followers)
print(user2.following)