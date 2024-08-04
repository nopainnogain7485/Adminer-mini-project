
try:
    import pymysql
    import os
    from dotenv import load_dotenv
    import random 

    # Load environment variables from .env file
    load_dotenv()
    host_name = os.environ.get("mysql_host")
    database_name = os.environ.get("mysql_db")
    user_name = os.environ.get("mysql_user")
    user_password = os.environ.get("mysql_pass")


    #USED TO ASSIGN A COURIER TO A CUSTOMERS ORDER
    def random_courier():
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()
                
                    sql = f"""
                        SELECT courier_id FROM couriers"""
                    cursor.execute(sql)
                    all = cursor.fetchall()
                    randomselect = random.randrange(1, len(all))
                    assign_courier = all[randomselect][0]
                    return assign_courier
                
    #USED TO CREATE A NEW RECORD FOR A COURIER OR PRODUCT
    def new_record_couriers_products(table_name, a, b):

                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()
                
                    if table_name == 'couriers':
                        print('Inserting info for new courier ...')
                        # Insert a new record
                        sql = f"""
                            INSERT INTO {table_name} (courier_name, phone_number)
                            VALUES (%s, %s)
                        """
                        data_values = (a, b)
                        cursor.execute(sql, data_values)
                        # Commit the record
                        connection.commit()
                        print("Record successfully creted!")
                    
                    elif table_name == 'products':
                        print('Inserting info for new product ...')
                        # Insert a new record
                        sql = f"""
                            INSERT INTO {table_name} (product_name, product_price)
                            VALUES (%s, %s)
                        """
                        data_values = (a, b)
                        cursor.execute(sql, data_values)
                        # Commit the record
                        connection.commit()
                        print("Record successfully creted!")
                
                
    #USED TO CREATE A NEW RECORD FOR A CUSTOMER ORDER
    def new_record_orders(product, customer_first_name, customer_last_name, customer_tele, courier):
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()

                    print('Inserting new order...')
                    

                    sql = f"""
                        INSERT INTO orders (first_name, last_name, phone_number, courier_id, product_id, order_status)
                        VALUES ('{customer_first_name}', '{customer_last_name}', '{customer_tele}', '{courier}', '{product}', 1)
                    """
                    print('New order added!')
                    cursor.execute(sql)
                    connection.commit()
                    
    # USED TO UPDATE A RECORD
    def update_record(table_name, id):
                  
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()

                               
                    if table_name == 'couriers':
                        new_name = input('Enter the updated name for this courier: ')
                        new_tele = input('Enter the update phone number for this courier: ')
                        print('updating record record...')
                        # Insert a new record
                        sql = f"""
                            UPDATE {table_name} SET courier_name = '{new_name}', phone_number = '{new_tele}' WHERE courier_id = '{id}'
                        """
                        print('record successfully updated!')
                        cursor.execute(sql)
                        connection.commit()

                    elif table_name == 'products':
                        new_name = input('Enter the updated name for this product: ')
                        new_tele = input('Enter the update price for this product in £s: ')
                        print('updating record...')
                        # Insert a new record
                        sql = f"""
                            UPDATE {table_name} SET product_name = '{new_name}', product_price = '{new_tele}' WHERE product_id = '{id}'
                        """
                        print('record successfully updated!')
                        cursor.execute(sql)
                        connection.commit()
                    

  
    #USED TO UPDATE THE STATUS OF A CUSTOMER ORDER
    def update_order_status(order_id, choice):
                  
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()

                               
                    print('updating order status...')
                    # Insert a new record
                    sql = f"""
                        UPDATE orders SET order_status = '{choice}' WHERE order_id = '{order_id}'
                    """
                    print('Order status successfully updated!')
                    cursor.execute(sql)
                    connection.commit()

    #USED TO DELETE A RECORD
    def delete_record(table_name, id):

                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()

                    if table_name == 'couriers':
                        print('Deleting record...')
                        # Insert a new record
                        sql = f"""
                            DELETE FROM {table_name}  WHERE courier_id = '{id}'
                        """
                        cursor.execute(sql)
                        connection.commit()
                        print("Record deleted successfully!")
                
                    elif table_name == 'products':
                        print('Deleting record...')
                        # Insert a new record
                        sql = f"""
                            DELETE FROM {table_name}  WHERE product_id = '{id}'
                        """
                        cursor.execute(sql)
                        connection.commit()
                        print("Record deleted successfully!")
                    
                    elif table_name == 'orders':
                        print('Deleting record...')
                        # Insert a new record
                        sql = f"""
                            DELETE FROM {table_name}  WHERE order_id = '{id}'
                        """
                        cursor.execute(sql)
                        connection.commit()
                        print("Record deleted successfully!")
                          


    #USED TO SHOW ALL THE DATA FOR A SPECIFIC TABLE
    def show_all_data(table_name):
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()


                    print('ALL RECORDS: ')

                    cursor.execute(f'SELECT * FROM {table_name}')
                    rows = cursor.fetchall()

                    if table_name == 'orders':
                        for cell in rows:
                            print(f'Order ID: {cell[0]}, First Name: {cell[1]}, Last Name: {cell[2]}, Phone Number: {cell[3]}, Courier: {cell[4]}, Products: {cell[5]}, Order Status: {cell[6]}')
                        
                    elif table_name == 'couriers':
                        for cell in rows:
                            print(f'Courier ID: {cell[0]}, Courier Name: {cell[1]}, Phone Number: {cell[2]}')    
                    
                    elif table_name == 'products':
                        for cell in rows:
                            print(f'Product ID: {cell[0]}, Product Name: {cell[1]}, Product Price: £{cell[2]}')
                            
    #USED TO CHECK THE AVAILABILITY OF A PRODUCT
    def product_availability(product, customer_first_name, customer_last_name, customer_tele, courier):
                print(product)
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()

                    try:
    
                        print('Chekcing if product is available .... ')
                        sql = f"""
                        SELECT product_id FROM products WHERE product_name = '{product}'
                    """
                        cursor.execute(sql)
                        retrive_id = cursor.fetchone()
                        product_id = retrive_id[0]
                        new_record_orders(product_id, customer_first_name, customer_last_name, customer_tele, courier)
                    except:
                        print('Sorry the product you have selected is not on the menu :(')
        
    #USED TO UPDATE A CUSTOMERS INFORMATION
    def update_customer_info(order_id, key):
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()

                    if key == 1:
                        show_all_data('products')
                        try:
                            new_product = input("Enter the name of the updated product: ")
                            print('Chekcing if product is available .... ')
                            sql = f"""
                            SELECT product_id FROM products WHERE product_name = '{new_product}'
                        """
                            cursor.execute(sql)
                            retrive_id = cursor.fetchone()
                            product_id = retrive_id[0]
                            print('updating product in record ...')
                            sql = f"""
                                UPDATE orders SET product_id = '{product_id}' WHERE order_id = '{order_id}'
                            """
                            print('record successfully updated!')
                            cursor.execute(sql)
                            connection.commit()
                            
                        except:
                            print('Sorry the product you have selected is not on the menu :(')
                    
                    elif key == 2:
                        first_name = input("Enter the updated first name: ")
                        last_name = input("Enter the updated last name: ")
                        print('updating name in record ...')
                        sql = f"""
                            UPDATE orders SET first_name = '{first_name}', last_name = '{last_name}' WHERE order_id = '{order_id}'
                        """
                        print('record successfully updated!')
                        cursor.execute(sql)
                        connection.commit()
                    
                    elif key == 3:
                          phone_number = input("Enter the updated phone number: ")
                          print('updating name in record ...')
                          sql = f"""
                            UPDATE orders SET phone_number = '{phone_number}' WHERE order_id = '{order_id}'
                        """
                          print('record succefully updated!')
                          cursor.execute(sql)
                          connection.commit()


                       

    #USED TO RETRIVE A SPECIFIC SET OF ORDER DATA
    def show_specific_data(searchmethod, id):
                
                with pymysql.connect(
                    host = host_name,
                    database = database_name,
                    user = user_name,
                    password = user_password
                ) as connection:
                    cursor = connection.cursor()


                    if searchmethod == 'status':
                        sql = f"""
                        SELECT * FROM orders WHERE order_status = {id}
                    """
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        for cell in rows:
                            print(print(f'Order ID: {cell[0]}, First Name: {cell[1]}, Last Name: {cell[2]}, Phone Number: {cell[3]}, Courier: {cell[4]}, Products: {cell[5]}, Order Status: {cell[6]}'))
                          
                    elif searchmethod == 'couriers':
                        sql = f"""
                        SELECT * FROM orders WHERE courier_id = '{id}'
                    """
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        print(rows)
                        for cell in rows:
                            print(print(f'Order ID: {cell[0]}, First Name: {cell[1]}, Last Name: {cell[2]}, Phone Number: {cell[3]}, Courier: {cell[4]}, Products: {cell[5]}, Order Status: {cell[6]}'))
  
                        





except Exception as ex:
    print('Failed to:', ex)

