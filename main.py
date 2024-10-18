from dummy.corpus_counter import token_count

def print_count(corpus, token):
    count = token_count(corpus, token)
    print(f'The term {token} shows up in the corpus {count} times.')