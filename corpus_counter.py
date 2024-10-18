def token_count(token):
    print(token)
    print("this works")
    return

    # reads corpus.txt
    with open('corpus.txt', 'r') as file:
        corpus = file.read()

    # makes token case-insensitive, returns count
    #return corpus.lower().split().count(token.lower())
    return corpus[0]