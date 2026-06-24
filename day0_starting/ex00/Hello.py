ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# pretty straightforward
ft_list[1] = "World!"

# 'tuple' object does not support item assignment, are unchangeable
# ft_tuple[1] = "test"
# so we move to direct re-assignation, if we need changing items, better make a list.
ft_tuple = ("Hello", "France!")

# kinda compare to classes in C++ like vect
ft_set.add("Paris!")
ft_set.discard("tutu!")
# note that a set is NOT ordered, so the output seems random between {'Hello', 'Paris!'} and {'Paris!', 'Hello'}
# print(sorted(ft_set))
# DO NOT use a set if order matter.

# dictionnaries are not ordered before 3.7, but are changeable
# ft_dict["Hello"] = "42Paris!"
ft_dict.update({"Hello": "42Paris!"}) # works aswell

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)