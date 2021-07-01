# nest lists

outside_list = []
inside_list = []

for i in range(10):
    #print(f"i = {i}")
    for j in range(9,-1,-1):
        #print(f"----------BEFORE APPENDING J:----------\ni: {i}\nj: {j}\noutside_list: {outside_list}\ninside_list: {inside_list}\n---------------------------------------")
        inside_list.append(j)
        #print(f"----------AFTER APPENDING J:----------\ni: {i}\nj: {j}\noutside_list: {outside_list}\ninside_list: {inside_list}\n--------------------------------------")
        if j == 0:
            #print(f"j is equal to 0")
            outside_list.append(list(inside_list))
            inside_list.clear()

#print(f"------------------------------\nfinal lists:\noutisde_list:\n{outside_list}\ninside_list: {inside_list}------------------------------")