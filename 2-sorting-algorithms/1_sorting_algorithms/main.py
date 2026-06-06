class Influencer:
    def __init__(self, num_selfies, num_bio_links) -> None:
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self) -> str:
        return f"({self.num_selfies}, {self.num_bio_links})"

def vanity(influencer: Influencer) -> int:
    return influencer.num_bio_links * 5 + influencer.num_selfies

def vanity_sort(influencers: list[Influencer]) -> list[Influencer]:
    return sorted(influencers, key=vanity)


# Test cases
if __name__ == "__main__":
    influencers = [
        Influencer(10, 2),
        Influencer(5, 3),
        Influencer(8, 1),
        Influencer(12, 4),
    ]
    sorted_influencers = vanity_sort(influencers)
    print(sorted_influencers)

    inf1 = Influencer(2, 8)
    print(vanity(inf1))