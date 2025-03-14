def get_num_words(text):
    count = len(text.split())
    return count 

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    
    return char_count

def sort_dictionary(dict):
    char_count_items = dict.items()
    sorted_char_counts = sorted(char_count_items, key=lambda item:item[1], reverse = True)
    sorted_char_dict = [{'characters':char, 'count':count} for char, count in sorted_char_counts]
    return sorted_char_dict
