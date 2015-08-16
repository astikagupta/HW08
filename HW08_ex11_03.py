#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

def print_hist_old(h):
	# list1=[]
 #    for c in h:
 #    	list1 = c
 #    print(sorted(list1))
	pass


def print_hist_new(h):
    
    for k,v in sorted(h.items()):
    	print (k,v)
   # print(sorted(h.items())) 


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################


# def histogram_old(s):
#     d = dict()
    
#     for c in s:
 
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

def histogram_new(s):
    d = dict()
    
    for c in s:

        d[c] = 1 + d.get(c,0)

    print_hist_new(d)
    

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
        

    histogram_new(pledge_list)

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    get_pledge_list()

if __name__ == '__main__':
    main()
