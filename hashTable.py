# Hash table

"""
Hash table is a hash function with an array

Hash function maps strings to numbers:
1. Maps same strings to same indexes.
2. Maps different strings to different indexes.
3. A valid range of indexes, an array with fixed slots.

Scenarios of hash table:
1. Creating a mapping from one item to another.
2. Looking something up.

DNS(domain name server) resolution is mapping web address to IP address.

Collision occurs when mapping different items into same slot,
usually the latter one can be linked with former one.

Load factor = number of items in hash table / total number of slots.
The good rule of thumb is resizing the hash table when the load factor is greater than 0.7.

"""

# Two ways to make hash table(dictionaries)
hash_table_1 = dict()
hash_table_2 = {}

# Prevent duplicate entries

voted = {}


def check_voter(name):
    if voted.get(name):
        print("You have voted, " + name + "!")
    else:
        voted[name] = True
        print("You have chance to vote, " + name + "!!!")


# Cache,memorize data (e.g. mapping url to page data)
cache = {}


def get_page(url):
    if cache[url]:
        return cache[url]
    else:
        # assume there is a function get_data_from_server
        cache[url] = get_data_from_server()
        return cache[url]


