def analyze_sentence(sentence):
    
    length = 0
    word_count = 0
    vowel_count = 0
    
    vowels = "aeiou"
    inside_word = False
    
    
    for char in sentence:
        if char == '.':
            break
        length += 1
        
        if char in vowels:
            vowel_count += 1
        
        if char == ' ' and inside_word:
            word_count += 1
            inside_word = False
        
        if char != ' ':
            inside_word = True
    
    if inside_word:
        word_count += 1
    
    return length, word_count, vowel_count

sentence = input("Enter a sentence ending with a point: ")
length, word_count, vowel_count = analyze_sentence(sentence)

print(f"Length of the sentence (excluding the point): {length}")
print(f"Number of words in the sentence: {word_count}")
print(f"Number of vowels in the sentence: {vowel_count}")
