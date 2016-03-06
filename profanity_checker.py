import urllib
def read_text():
    quotes = open("C:\Users\Siddharth\Desktop\Python projects\movie_quotes.txt")
    contents_of_file = quotes.read();
    #print(contents_of_file);
    quotes.close();
    check_profanity(contents_of_file);

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read();
    #print(output)
    connection.close();
    if "true" in output:
        print "Profanity laert!!! Curse word found please edit text"
    elif "false" in output:
        print "This document doesnot have any curse words"
    else:
        print "Couldnot scan the document"
read_text()    
