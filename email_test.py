#### First Bitbucket email code ####
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth in wardrobe:
    #print(wardrobe[cloth])
    for colour in wardrobe[cloth]:
        print("{} {}".format(colour, cloth))


def email_list(domains):
        emails = []
        for users in domains:
                for user in domains[users]:
                        emails.append(user+"@"+users)
        return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
