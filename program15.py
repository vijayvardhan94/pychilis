def Convert(string): 
    li = list(string.split(" ")) 
    return li 
  
    
str1 = "Geeks for Geeks"
print(Convert(str1)) 

##method 2
def reverseWord(w):
  return ' '.join(w.split()[::-1])