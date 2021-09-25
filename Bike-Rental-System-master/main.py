from bikeRental import BikeRental, Customer

def main():
    shop = BikeRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displaystock()                            # We have currently 100 bikes available to rent.
        
        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())       # You have rented a 1 bike(s) on hourly basis today at 23 hours.
            customer.rentalBasis = 1                                                       # You will be charged $5 for each hour per bike.
                                                                                           # We hope that you enjoy our service.
        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0           # Are you sure you rented a bike with us?
        elif choice == 6:
            break                                                                              # Thank you for using the bike rental system.
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the bike rental system.")


if __name__=="__main__":
    main()