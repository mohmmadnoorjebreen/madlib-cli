import re
print('welcome to your future game')

def read_template(paths):
    try:
        with open(paths,'r') as file:
            read_file=file.read()
            return read_file
    except ValueError:
        return "Oops!  That was no valid path"
    
   
   
def parse_template(string):
    new_string=re.sub("\{.*?\}","{}",string)
    Pattern = r'\{.*?\}'
    parts = re.findall(Pattern, string)
    return_parts = []
    for value in parts:
       parts_new=re.sub("}","",value)
       parts_new=re.sub("{","",parts_new)
       return_parts.append(parts_new)
    return new_string , tuple(return_parts)
             
def merge(stripped:str,parts):
    merge = stripped.format(*parts)
    return merge
  

def user_game():
    input_msg = 'Please enter a series of words so that they fit between the brackets above.Please follow these instructions: \n  Adjective: you must enter an adjective that fits the context. Be careful, you must enter six adjectives (without a sequence)\nA First Name:\n you must enter a A First Name (Choose a name you like) that fits the context. Be careful, you must enter tow First Name (without a sequence)\n Plural Noun :  \n you must enter a Plural Noun (Choose what you see fit the context). Be careful, you must enter five Plural Noun (without a sequence)\n Large Animal and Small Animal \n You must enter a large animal and a small animal, in turn \n number: \n you must enter number , Pay attention, one of the numbers must be between 1-50'
    
    with open('assets/madlib.txt ' ,'r') as file:
        new_file = file.read()
        print(new_file)
        data = input(input_msg) 
        data_list=data.split(' ')
        with open('assets/completed .txt' , 'w') as file:
            new_string=re.sub("\{.*?\}","{}",new_file)
            new_file = merge(new_string,tuple(data_list))
            file.write(new_file)
    with open('assets/completed .txt' ,'r') as file:
        new_file = file.read()
        print(new_file)   
    
# it work but i put it in this way because of pytest: reading from stdin while output is captured!
user_game()   



        

 


 
 
 