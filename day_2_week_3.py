# Question 1
   

itin_tup = [('Alice', 'New York', 'London'), ('Bob', 'Tokyo', 'San Fran')]

def itinerary(atuple):
    count = 1
   
    for count, (name, from_city, to_city) in enumerate(atuple, start = 1):
        print(f"Itinerary {count}: {name} - From {from_city} to {to_city}")
        count += 1
   


itinerary(itin_tup)


#---------------------------------------------------------------------------------#
# Question 2


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

new_tup = []


book = input("What book would you like to add? ")
new_tup.append(book)
author = input("What is the Author's name? ")
new_tup.append(author)

new_tup = tuple(new_tup)
library.append(new_tup)


print(library)