def main():
    counts={}
    words= get_words("address.text")
    
    lowercase_words = [word.lowercase() for word in words]

    for words in lowercase_words:
        if word in counts:
            counts[word]+=1

        else:
            counts[word]=1

    save_counts(counts)

main()
