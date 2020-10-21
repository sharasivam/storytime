from random import choice
print("Weclome to our little story...")

dict = {}
dict['animal'] = input("What animal is the main character? ")
dict['name'] = input("What's " + dict['animal'] + "\'s name? ")
dict['size'] = input("How big is " + dict['name'] + "? ")
dict['toy'] = input("What toy does " + dict['name'] + " like the most? ")
dict['home'] = input("Where does " + dict['name'] + " live? ")
dict['relationship'] = input("Is " + dict['name'] + " in a relationship? In which kind? ")


einleitung = ["Our little {animal} {name} is small and likes {toy}. It lives by {home} and is {relationship}.",
              "Being the {size} {animal} {name} is, having fun with {toy} seems almos natural. Living by {home}, {relationship}, all fits into that picture."]

haupt1 = ["In the morning {name} leaves for the {toy} store and does some shopping.",
          "The first thing to do on {name}\’s list is cleaning the area near {home}",
          "In the morning our {animal} likes to relax at the usual favorite spot, by {home}",
          "The first thing to do is brushing the teeth.",
          "At lunchtime collecting {toy} is important."]

haupt2 = ["Next the {animal} plays at {home}",
          "{name} is having a lot of fun during the day, being {relationship}.",
          "As the day goes on, {name} decided to meet some friends and play with their {toy}.",
          "Later in the day, being {relationship}, {name} likes to pick up the {toy} and go on a walk alone to relax."]

schluss = ["Late at night, {name} goes to bed." ,
           "Having drunk waaaay to much coke, {name} couldn’t sleep the whole night.",
           "In the evening the {animal} {name} goes back to {home}. Having an exhausting day, going to sleep under a wonderful sky of stars was easy."]

print(choice(einleitung).format(**dict))
print(choice(haupt1).format(**dict))
print(choice(haupt2).format(**dict))
print(choice(schluss).format(**dict))
