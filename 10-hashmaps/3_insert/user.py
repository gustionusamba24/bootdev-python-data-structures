import random


class User:
    def __init__(self, id: int, age: int, job_title: str) -> None:
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"
        self.age = age
        self.job_title = job_title

    def __eq__(self, other: "User") -> bool:
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other: "User") -> bool:
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other: "User") -> bool:
        return isinstance(other, User) and self.id > other.id

    def __repr__(self) -> str:
        parts = self.user_name.split("#")
        return f"(Name: {parts[0]}, ID: {self.id}, Age: {self.age}, Job Title: {self.job_title})"


def get_users(num: int) -> list[User]:
    random.seed(1)
    job_titles = ["Engineer", "Designer", "Manager", "Clerk", "Analyst"]
    users = []
    ids = list(range(num * 3))
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        age = random.randint(20, 60)
        job_title = random.choice(job_titles)
        user = User(id, age, job_title)
        users.append(user)
    return users
