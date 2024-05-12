def my_split(string):
    string_list = []
    word = ""
    
    for char in string:
        if char != " ":
            word = word + char
        else:
            string_list.append(word)
            word = ""
        string_list.append(word)
            
    return string_list