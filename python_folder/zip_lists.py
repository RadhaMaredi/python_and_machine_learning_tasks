#Q.create four list and containing string and combine every element from each list in a single tuple?

def combine(list_a, list_b, list_c, list_d):
    """it takes the lists as input and retunrs zipped list"""

    #store the length of each list into variables for convient
    a = len(list_a)
    b = len(list_b)
    c = len(list_c)
    d = len(list_d)

    #creating empty list to store the final outputt
    new_list=[]

    #this loop iterate over the maximum length of the list
    for i in range(max(a,b,c,d)):        

        #this while loop is iterates over the items of the list
        while True:  

            #if the all lists have same lenght then this try block is executed       
            try:
                tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

            #if the lenghts of the each list is have different lengths 
            # then this is executed.    
            except IndexError:

                #if the list_a is max. then this block executed
                if a > (b >= c >=d):
                    list_b.append('')
                    list_c.append('')
                    list_d.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                #if the list_b is max. then this block executed    
                elif b > (a >= c >=d):
                    list_a.append('')
                    list_c.append('')
                    list_d.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                #if the list_a is max. then this block executed    
                elif c > (b >= a >=d):
                    list_b.append('')
                    list_a.append('')
                    list_d.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                #if the list_a is max. then this block executed
                elif d > (b >= a >=c):
                    list_b.append('')
                    list_c.append('')
                    list_a.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                continue #this exception block continuous upto list elements are combined

            new_list.append(tuple_a)  #appends combined list elements
            break
    #returns the final result    
    return new_list

#decalring the inputs
list_a= ["r", "a", "h", "d", "e"]
list_b= ["1", "2", "3", "4"]
list_c= ["a", "e", "i", "o","454"]
list_d= ["@", "*", "ra", "z"]

#calling the function
list_to_tuple = combine(list_a, list_b, list_c, list_d)
print(list_to_tuple)