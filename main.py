def main():
    file_path = 'books/frankenstein.txt'
    file_contents = read_file(file_path)
    #print(file_contents)
    
    #print(f"Number of words in file: {count_words(file_contents)}")
    
    #print(f"Dictionary of character occurances: {count_chars(file_contents)}")
    
    word_count = count_words(file_contents)
    characters = count_chars(file_contents)
    
    pretty_print_report(file_path, word_count, characters)
    
def read_file(file_path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    return file_contents
        
def count_words(text):
    return(len(text.split()))

def count_chars(text):
    dictionary = {}
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            char = chr(ord(char)+32)
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def pretty_print_report(file_path, num_words, char_dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the file")
    
    sorted_chars = dict(sorted(char_dict.items(), reverse=True, key=lambda item: item[1]))
    
    for key in sorted_chars:
        if key.isalpha():
            print(f"Character '{key}' was found {sorted_chars[key]} times")

if __name__=="__main__":
    main()