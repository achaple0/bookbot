def get_word_count(book_text):
    num_words = book_text.split()
    return len(num_words)

def per_letter_count(book_text):
    book_text = book_text.lower() 
    dictionary = {} 
    
    for i in book_text: 
        if i in dictionary: 
            dictionary[i] += 1
        elif i not in dictionary:
            dictionary[i] = 1
        else: 
            pass
    return dictionary
def sort_on(some_dict):
    return some_dict["num"]

def sorting_dictionaries(dictionary): 
    dict_of_dicts = []
    for key, values in dictionary.items(): 
        dict_of_dicts.append({"char": key, "num": values})
    dict_of_dicts.sort(key=sort_on, reverse=True)
    return dict_of_dicts
