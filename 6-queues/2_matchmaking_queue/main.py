"""
In LockedIn, users that are founding companies can join a matchmaking queue 
to find potential co-founders for their projects. We'll use the Queue 
class we've built to manage the matchmaking process.

Notice the search_and_remove method on the Queue class (in queue.py). 
It breaks the rules of a traditional queue data structure but will be useful in solving this real-world problem.

It's okay to violate academic constraints as software engineers as long as we understand the trade-offs involved.
"""

"""
ASSIGNMENT
Complete the matchmake function that simulates users joining 
and leaving the matchmaking queue. The function should take a queue 
instance and a user tuple containing a name and action (either "join" or "leave"):
example:
user = ('Bob', 'join')
user = ('Alice', 'leave')

For each call to matchmake:
1. If the action is "leave", search the queue for the user and remove them if they are in the queue.
2. If the action is "join", push the user's name onto the queue.
3. Lastly, check if the queue has at least 4 users in it. 
   If so, pop the first 2 users from the queue and return the following string:
   "{user1} matched {user2}!"
   Where user1 is the first user popped and user2 is the second user popped.
4. If there were less than 4 users in the queue, return the following string: "No match found"
"""


from queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    name, action = user

    if action == "leave":
        queue.search_and_remove(name)
    elif action == "join":
        queue.push(name)

    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    else:
        return "No match found"
