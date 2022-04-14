import string

ch_ascii_values = dict(zip(list(string.ascii_letters), [ord(w) for w in list(string.ascii_letters)]))
words = [input() for w in range(int(input()))]

for word in words:
    flag = True
    for i, ch in enumerate(word[1:],1): 
        diff, reverse_diff = abs(ch_ascii_values[ch] - ch_ascii_values[word[i - 1]]), \
        abs(ch_ascii_values[word[-i]] - ch_ascii_values[word[-i - 1]])
        
        if diff != reverse_diff:
            flag = False
            break         
    print('Funny') if flag else print('Not Funny')

        
       
        
        
        

