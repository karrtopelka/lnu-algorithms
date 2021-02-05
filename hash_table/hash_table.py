# hash table

word_list = []
hash_table = {}


def hash_function(wrd):
    if len(hash_table) == 0:
        hash_table.update({0: wrd})
    else:
        i = 0
        while i != -1:
            if wrd[0] > list(hash_table.values())[i][0]:
                pass

            # if wrd[0] > list(hash_table.values())[i][0]:
            #     hash_table.update({i+1: wrd})
            # elif wrd[0] == list(hash_table.values())[i][i]:
            #     i += 1
            # else:
            #     break


# Runner
word = 'hello'
word2 = 'beta'
word3 = 'alpha'
word4 = 'bit'
word5 = 'aperol'

hash_function(word)
hash_function(word2)
hash_function(word3)
hash_function(word4)
hash_function(word5)


print(hash_table)