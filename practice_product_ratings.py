# Write your code here.
# On the real test, you'll have access to everything in the reference_notes

rating_dict = {
    "tshirts": [],
    "mugs": [],  
    "stickers": [],
}

# returns average rating
def average_rating(rating_dict, product): 
    product_ratings = rating_dict.get(product, [])

    if len(product_ratings) == 0:
        return 0.0
    
    total = 0
    for r in product_ratings:
        total += r

    return total / len(product_ratings)


def latest_rating(rating_dict, product):
    product_ratings = rating_dict.get(product)
    if len(product_ratings) == 0:
        return None
    return product_ratings[-1]

        
           
#THE ANALYZER    
print("Welcome to the Vendor Product Ratings Analyzer!")

#this is what prints on repeat
while True:
    print("\n1. Add a rating")
    print("2. Show average rating for each product")
    print("3. Show latest rating for each product")
    print("4. Show all raw ratings")
    print("5. Exit")
    pick = input("\nEnter an option (1-5): ")

#this is option 1, adding a rating
    if pick == "1":
        print("Products:")
        for p in rating_dict:
            print(f"{p}") 

        product = input("Enter a product name: ")
        rate = int(input("Enter a rating (1-5): "))

        if product in rating_dict and 1 <= rate <= 5:
                rating_dict[product].append(rate)
                print(f"Added rating {rate} to {product}.")
        else:
            print("Invalid product or rating out of range.")

 #this is option 2, average rating  
    elif pick == "2":
        print()
        for product in rating_dict:
            avg = average_rating(rating_dict, product)
            print(f"{product}: average = {avg:.2f}")  

#this is option 3, latest rating
    elif pick == "3":
        print()
        for product in rating_dict:
            latest = latest_rating(rating_dict, product)
            if latest is not None:
                print(f"{product}: latest = {latest}")
            else:
                print(f"{product}: No ratings yet.")

#this is option 4, show all raw ratings
    elif pick == "4":
        print()
        for product, ratings in rating_dict.items():
            print(f"{product}: {ratings}")

#this is option 5, exit
    elif pick == "5":
        print("Exiting the analyzer. Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 5.")




