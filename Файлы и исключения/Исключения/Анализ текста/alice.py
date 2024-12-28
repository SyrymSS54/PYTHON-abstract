filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file {0} does not exist".format(filename))        
else:
    words = contents.split()
    num_words = len(words)    
    print("The file {0} has about {1} words.".format(filename, str(num_words)))