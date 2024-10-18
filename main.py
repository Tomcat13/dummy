def report_count(token):
    # gets function from corpus_counter
    from dummy.corpus_counter import token_count

    # gets count of token
    count = token_count(token)

    print(f'The term {token} shows up in the corpus {count} times.')