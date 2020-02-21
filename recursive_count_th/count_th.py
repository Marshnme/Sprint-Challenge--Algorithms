'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    #.find returns index of first accurance
    th = word.find("th")
    # .find returns -1 if nothing found 
    if th == -1:
        return 0
        # adds one, then adds 2 to the index of TH and reruns till out of indexs. 
    else: 
        count +=1 + count_th(word[th+2:])
        return count
       

    
 
count_th("togetherth")