#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
# def reverse_lookup_old(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise ValueError

def reverse_lookup_new(d, v):
    list1 = []
    for k in d:
        if str(d[k]) == v:
            list1.append(k)
   
    return list1
    


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
def histogram_old(s):
    d = dict()
    
    for c in s:
 
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_new(s):
    d = dict()
    
    for c in s:

        d[c] = 1 + d.get(c,0)
    return d
    

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    pledge_list=[]
    with open("pledge.txt","r") as fo:

        #list1 = (list1.append(line.split()) for line in fo)
        string1 = fo.read()
        pledge_list = string1.replace(';',' ').replace(':',' ').replace('.',' ').replace('\n',' ').split()
        

    return pledge_list



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram=histogram_new(get_pledge_list())
    print reverse_lookup_new(pledge_histogram, "1")
    print reverse_lookup_new(pledge_histogram, "9")
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
