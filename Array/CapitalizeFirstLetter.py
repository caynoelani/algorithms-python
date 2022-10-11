# Given a list of words, capitalize the first letter of each word

def capitalize(names):
    return [ name.capitalize() for name in names]

names = ["alice", "bob", "charlie", "danielle"]
print(capitalize(names))