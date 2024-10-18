def token_count(token):
    # reads corpus.txt
    with open('corpus.txt', 'r') as file:
        corpus = file.read()

    # makes token case-insensitive, returns count
    return corpus.lower().split().count(token.lower())