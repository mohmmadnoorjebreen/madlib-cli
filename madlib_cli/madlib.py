import re
print('welcome to your future game\n Fill in the following information in brackets')

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
    data = input('plz enter all missing word') 
    data_list=data.split(' ')
    with open('assets/madlib.txt ' ,'r') as file:
        new_file = file.read()
        with open('assets/completed .txt' , 'w') as file:
            new_string=re.sub("\{.*?\}","{}",new_file)
            new_file = merge(new_string,tuple(data_list))
            file.write(new_file)
    with open('assets/completed .txt' ,'r') as file:
        new_file = file.read()
        print(new_file)   
    
# it work but i put it in this way because of pytest: reading from stdin while output is captured!
#user_game()   



        

 


 
 
 