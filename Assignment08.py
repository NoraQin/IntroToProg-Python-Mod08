# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# qinlaura,2020-12-08,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ''
strProductName = ''
strProductPrice = ''

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        qinlaura,2020-12-08,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self):
        # -- Attributes --
        self.__product_name = None
        self.__product_price = None

    # -- Properties --
    @property
    def product_name(self):
        return self.__product_name
    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception('ERROR: Product name cannot be a number')

    @property
    def product_price(self):
        return self.__product_price
    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except:
            raise Exception('ERROR: Product price must be a number')

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        qinlaura,2020-12-08,Modified code to complete assignment 8
    """
    # -- methods --
    @staticmethod
    def read_data_from_file(file_name):
        infile = open(file_name, 'r')
        product_list = []
        for line in infile:
            lst = line.split(',')
            p = Product()
            try:
                p.product_name = lst[0]
                p.product_price = lst[1]
                print(str(p.product_name), str(p.product_price), sep = ', ')
                product_list.append(p)
            except Exception as e:
                print('Failed to read this entry due to invalid value')
                print(line.strip())
                print(e.__str__())
        infile.close()
        return product_list

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        outfile = open(file_name, 'w')
        for p in list_of_product_objects:
            outstr = str(p.product_name) + ',' + str(p.product_price) + '\n'
            outfile.write(outstr)
        outfile.close()


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Display data and get input from user:

    methods:
        display_menu():
        get_selection(): -> (a string)
        display_current_data(list_of_product_objects):
        get_product_data(): -> (two strings)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        qinlaura,2020-12-08,Modified code to complete assignment 8
    """

    @staticmethod
    def display_menu():
        print('''
        Options:
        (1) Display current data
        (2) Add new data
        (3) Save data to file and exit program
        
        ''')

    @staticmethod
    def get_selection():
        while True:
            selection = input('Your selection (1-3): ')
            if (selection.isnumeric() != False) and (int(selection) <= 3) and (int(selection) >= 1):
                return selection
                break
            print('Invalid choice, please select again')

    @staticmethod
    def display_current_data(list_of_product_objects):
        for p in list_of_product_objects:
            print(str(p.product_name), str(p.product_price), sep = ', ')

    @staticmethod
    def get_product_data():
        input_product_name = input('Enter a product name: ')
        input_product_price = input('Enter a product price: ')
        return input_product_name, input_product_price




# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

# Show user a menu of options
while True:
    IO.display_menu()
    # Get user's menu option choice
    strChoice = IO.get_selection()
    if strChoice == '1':
        # Show user current data in the list of product objects
        IO.display_current_data(lstOfProductObjects)
    elif strChoice == '2':
        # Let user add data to the list of product objects
        try:
            strProductName, strProductPrice = IO.get_product_data()
            new_product = Product()
            new_product.product_name = strProductName
            new_product.product_price = strProductPrice
            lstOfProductObjects.append(new_product)
        except Exception as e:
            print(e.__str__())
            print('Invalid entry')
    elif strChoice == '3':
        # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        break
    else:
        continue

# Main Body of Script  ---------------------------------------------------- #

