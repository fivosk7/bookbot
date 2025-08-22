def word_count(text: str):
    word_list = text.split()
    return len(word_list)

def character_count(text: str):
    lowercased_text = text.lower()
    frequency_dict = {}
    spaces = 0
    for char in lowercased_text:
        if char not in set(frequency_dict.keys()):
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1
    
    return frequency_dict


def sort_the_dict_list(dictionary: dict):
    dict_list = []

    for key in list(dictionary.keys()):    
        dict_list.append({"char": key, "num": dictionary[key]})
    
    def sort_on(items):
        return items["num"]

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
   