# Print the names which contain the character 'a' from the dictionary containing 2 lists of male and female students given below.

d = {"male": ["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"] }



for values in d.values():
    for i in values:
        if 'a' in i:
            print(i)
