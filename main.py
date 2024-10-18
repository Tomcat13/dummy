from dummy.corpus_counter import token_count

def report_count(token):
    
    count = token_count(token)
    #print(f'The term {token} shows up in the corpus {count} times.')
    print(count)