def print_this(this):
    print(this)
    
def add_these(num_1 = 1, num_2 = 2):
    return num_1 + num_2
    
def do_nothing():
    pass
    
def print_add_these(a = 3, b = 5):
    out = str(add_these(a, b))
    print(out)
    
def meow(in_call = 'meow'):
    print(in_call)

# we can declare this even though make_data() is undefined
def inherit_data(some_int = 5):
    out = make_data(some_int)
    print(out)
    it_wouldve_been = make_data()
    print("It would've been: " + str(it_wouldve_been))
    
def make_data(some_int = 0):
    some_int += 1
    return some_int
    
import double_import as d

def double_inherit_data(some_int = 15):
    out = d.make_data(some_int)
    print(out)
    it_wouldve_been = d.make_data()
    print("It would've been doubled inherited: " + str(it_wouldve_been))
    
# polymorphism
def polymorphic_comp(whatever):
    if type(whatever) == int:
        print("It's an int.")
        print(str(whatever * 4) + ' = input times 4.')        
    if type(whatever) == bool:
        print("It's a bool.")
        print("The kind is: " + str(whatever))
    if type(whatever) == str:
        print("It's a string.")
        print("The string is: " + whatever)
    if type(whatever) == float:
        print("It's a float.")
        print(str(whatever * 4) + ' = input times 4.')
        
# encapsulation
def encapsuled_data():
    secret_info = ['secret_3', 'secret_1', 'secret_2']
    secret_info.sort()
    not_secret_info = ['unsecret_1', 'unsecret_2', 'unsecret_3']
    print(not_secret_info)
    return not_secret_info
    
