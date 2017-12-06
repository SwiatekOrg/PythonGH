dict_ = {'Lemonade': ["1", "45", "87"], 'Coke': ["23", "9", "23"], 'Water': ["98", "2", "127"]}
inp = input("Select key to print value for!" + "/r>>> ")
if inp in dict_:
  print(dict_[inp])