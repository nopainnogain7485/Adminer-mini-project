import database_link

product_menu =  ["0 - Main menu", "1 - Print Products List", "2 - Create New Product", "3 - Update Existing Product", "4 - Delete Product"] # CREATE Product Menu
main_menu = ["0 - Exit app", "1 - Product Menu", "2 - Order Menu", "3 - Couriers menu"] #CREATE Main Menu
order_menu = ["0 - Main menu", "1 - Print orders","2 - Enter order details", "3 - Update order status", "4 - Update exitsting order", "5 - Find specific orders", "6 - Delete order"]
courier_menu =  ["0 - Main menu", "1 - Print Couiers List", "2 - Create New Courier", "3 - Update Existing Courier", "4 - Delete Courier"]
order_details = {}
orders_list = {}
order_key_num = 0
order_number = 0



# This function is used to send the products the customer would like
def get_order(customer_first_name, customer_last_name, customer_tele):
    courier = database_link.random_courier()
    while True:
        database_link.show_all_data('products')
        add_item = input("Please select an item to order: ")
        database_link.product_availability(add_item.lower(), customer_first_name, customer_last_name, customer_tele, courier)
        add_more_items = input("Would you like to add more items to your order? Type Y or N: ")
        if add_more_items.lower() == "y":
            continue
        elif add_more_items.lower() == "n":
            print("Your order has been sent ;)")
            break
        else:
            print("That is not an option, your order has been sent")
            break






while True:
    print(main_menu)
    menu_input = int(input("Select the number of your option: "))

    # EXIT APP
    if menu_input == 0:
        print("Goodbye")
        exit()

    #PRODUCTS MENU
    elif menu_input == 1:
        print(product_menu)
        product_input = int(input("Select the number of your option: "))

        #RETURN to main menu 

        if product_input == 0:
            continue

        #PRINT products list 
        
        elif product_input == 1:
            database_link.show_all_data('products')

        # # CREATE new product

        elif product_input == 2:
            new_product = input("Enter the name for your product: ")
            new_product_price = float(input("Enter a price for your product in £: "))
            database_link.new_record_couriers_products('products', new_product.lower(), new_product_price)

        # STRETCH GOAL - UPDATE existing product

        elif product_input == 3:
            database_link.show_all_data('products')
            product_id = int(input("Enter the product ID number you want to update: "))
            database_link.update_record('products', product_id)
            

        ## STRETCH GOAL - DELETE product 

        elif product_input == 4:
            database_link.show_all_data('products')
            product_id = int(input("Enter the product ID number you want to remove: "))
            database_link.delete_record('products', product_id)
        
        else:
            print("Sorry that is not a valid option. Try again")

    #ORDERS MENU
    elif menu_input == 2:
        while True:
            print(order_menu)
            order_input = int(input("Enter an option number from the order menu: "))

            # RETURN TO MAIN MENU
            if order_input == 0:
                break

            # SHOWS ALL THE CUSTOMER ORDERS
            elif order_input == 1:
                database_link.show_all_data('orders')
            
            # USED TO CREATE A NEW CUSTOMER RECORD INCLUDING THEIR ORDER
            elif order_input == 2:
                customer_first_name = input("Enter your first name: ")
                customer_last_name = input("Enter your last name: ")
                customer_tele = input("Enter your phone number: ")
                customer_order = get_order(customer_first_name, customer_last_name, customer_tele)


            #USED TO UPDATE A CUSTOMER'S ORDER STATUS
            elif order_input == 3:
                database_link.show_all_data('orders') 
                get_order_id = input("Enter the order ID number for the order you want to update: ")
                while True:
                    choice = int(input("Enter '1' to change the status to 'preparing' or Enter '2 to change the status to 'ready to collect': "))
                    if choice == 1 or choice == 2:
                        database_link.update_order_status(get_order_id, choice)
                        break
                    else:
                        print("This option is not valid, try again.")
                        
            

            # USED TO UPDATE A CUSTOMERS INFORMATION
            elif order_input == 4:
                database_link.show_all_data('orders')
                order_id = int(input("Enter the Order ID number for the record you'd like to alter: "))
                while True:
                    key = int(input("""Which part of the order would you like to ammend? 
                                Please select one of the following options: 
                                1 - Customer order 
                                2 - Customer Name 
                                3 - Customer Phone number 
                                Enter the number of your option: """))
                    if key ==  1 or key == 2 or key == 3:
                        database_link.update_customer_info(order_id, key)
                    else:
                        print("Sorry that it not an option")
                    tryagain = input(f"would you like to ammend more fields for 'Order ID {order_id}'?. Y or N: ")
                    if tryagain.lower() == 'y':
                        continue
                    elif tryagain.lower() == 'n':
                        print('All orders updated accordingly')
                        break
                    
                        
                    
            #USED TO RETRIVE CUSTOMER INFORMATION SPECIFICALLY BY ORDER STATUS OR COURIER
            elif order_input == 5:
                get_info = int(input("""How would you like to search for orders?
                                     1 - By 'Status'
                                     2 - By 'Courier
                                     Please select the option number: """))
                if get_info == 1:
                    get_status = int(input("""Select an order status to retrive the orders for
                                           1 - 'Preparing' orders
                                           2 - 'Ready to collect' orders
                                           Please select the option number: """))
                    
                    database_link.show_specific_data('status', get_status)
                if get_info == 2:
                    database_link.show_all_data('couriers')
                    get_status = int(input("""Select a Courier ID number to retrive orders for: """))
                    
                    database_link.show_specific_data('couriers', get_status)


            #USED TO DELETE ORDERS
            elif order_input == 6:
                database_link.show_all_data('orders')
                index = int(input("Select the Order ID of the record to delete: "))
                database_link.delete_record('orders', index)

            else: 
                print("Sorry that option is not valid, try again")


    #COURIERS MENU       
    elif menu_input == 3:
        print(courier_menu)
        courier_input = int(input("Select the number of your option: "))

        #RETURN to main menu 

        if courier_input == 0:
            continue

        #PRINT couriers list 
        
        elif courier_input == 1:
            database_link.show_all_data('couriers')

        # # CREATE new courier

        elif courier_input == 2:
            courier_name = input("Enter the name for your courier: ")
            courier_tele = float(input("Enter the telephone number for your courier: "))
            database_link.new_record_couriers_products('couriers', courier_name.lower(), courier_tele)

        # STRETCH GOAL - UPDATE existing courier

        elif courier_input == 3:
            database_link.show_all_data('couriers')
            courier_id = int(input("Enter the courier ID number you want to update: "))
            database_link.update_record('couriers', courier_id)
            

        ## STRETCH GOAL - DELETE courier 

        elif courier_input == 4:
            database_link.show_all_data('couriers')
            courier_id = int(input("Enter the courier ID number you want to remove: "))
            database_link.delete_record('couriers', courier_id)
        
        else:
            print("Sorry that is not a valid option. Try again")


                    
    else: 
        print("Sorry that option is not valid, try again")

