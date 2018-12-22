def N min_elements(list1, N): 
    final_list =[]; 
 for i in range(0, N):     
        min3 = 9999; 
  for j in range(len(list1)):       
       if list1[j]<min3: 
           min3 = list1[j]; 
  list1.remove(min3); 
  final_list.append(min3) 
        print(final_list) 
list1 = [4, 78, 34, 10,]; 
N = 2; 
N min_elements(list1, N) 
