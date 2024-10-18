def token_count(corpus, token):
    # makes token case-insensitive
    return corpus.lower().split().count(token.lower())