def main():
    def get_book():
        #change to open(location)
        with open("books/frankenstein.txt") as f:
            book = f.read()
        return book
        

    def words_in_book(book):
        words = book.split()
        words_n = len(words)
        return words_n
    
    def count_chars(book):
        cased = book.lower()
        char_count = {}
        for char in cased:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] +=1
        return char_count
    
    def create_report(char_dictionary):
        for char in char_dictionary:
            if char.isalpha():
                print(f"The letter '{char}' appears {char_dictionary[char]} times in frankenstein")
                
        return 
    
    current_book = get_book()
    word_count = words_in_book(current_book) 
    chars = count_chars(current_book)
    create_report(chars)
    print(word_count)
main()
