#Q.create four list and containing string and combine every element from each list in a single tuple?

def combine(list_a, list_b, list_c, list_d):
    a= len(list_a)
    b= len(list_b)
    c= len(list_c)
    d= len(list_d)

    new_list=[]
    for i in range(max(a,b,c,d)):

        while True:
            try:
                tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

            except IndexError:
                if a > (b >= c >=d):
                    list_b.append('')
                    list_c.append('')
                    list_d.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                elif b > (a >= c >=d):
                    list_a.append('')
                    list_c.append('')
                    list_d.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])
    
                elif c > (b >= a >=d):
                    list_b.append('')
                    list_a.append('')
                    list_d.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                elif d > (b >= a >=c):
                    list_b.append('')
                    list_c.append('')
                    list_a.append('')
                    tuple_a = (list_a[i], list_b[i], list_c[i], list_d[i])

                continue
  
            new_list.append(tuple_a)
            break
    return new_list

list_a= ["r", "a", "h", "d", "e"]
list_b= ["1", "2", "3", "4"]
list_c= ["a", "e", "i", "o","454"]
list_d= ["@", "*", "ra", "z"]

list_to_tuple = combine(list_a, list_b, list_c, list_d)
print(list_to_tuple)