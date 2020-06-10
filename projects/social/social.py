from faker import Faker
import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        fake = Faker()
        # Add users
        for _ in range(num_users):
            # generate a random name
            name = fake.name()
            self.add_user(name)

        # Create friendships
        for user in self.users.keys():
            user1 = user
            # if it's not the first user
            if user > 1:
                # only create a friendships with a user ID less than themselves to prevent warnings
                user2 = random.randint(1, user1-1)
            else:
                continue

            self.add_friendship(user1, user2)            

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        queue = [[user_id]]

        # as long as there are extended friends this loop will run
        while queue:
            path = queue.pop(0)
            # get the first user
            cur_user = path[-1]

            if cur_user not in visited:
                visited.update({cur_user: path})
                
                # getting user's friends
                extended_friends = self.friendships[cur_user]

                for friend in extended_friends:
                    new_path = list(path)
                    new_path.append(friend)
                    queue.append(new_path)        

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
