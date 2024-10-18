

def report_count(token):
    #test = "subscriber"
    from dummy.corpus_counter import token_count

    count = token_count(token)
    #print(f'The term {token} shows up in the corpus {count} times.')
    print(count)