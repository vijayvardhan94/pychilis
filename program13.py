def remove(duplicate_list): 
    final_list = [] 
    for i in duplicate_list: 
        if i not in final_list: 
            final_list.append(i) 
    return final_list 
      

duplicate_list = [2, 4, 10, 20, 5, 2, 20, 4] 
print(remove(duplicate_list)) 