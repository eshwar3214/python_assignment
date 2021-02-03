# name    : sai eshwar reddy kottapally
# rollno  : 100519733022
# program to combine two lists into a dictionary



test_keys = ["Rash", "Kil", "Varsha"] 
test_values = [1, 4, 5] 
  
print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  

res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break  
  

print ("Resultant dictionary is : " +  str(res)) 