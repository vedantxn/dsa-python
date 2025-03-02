import os

'''
Implement a recursive function with signature find(path, filename) that reports all entries of the file system rooted at the given path having the given file name.
'''
def find(path, filename):
    mathces = []

    if not os.path.exists(path):
        return mathces
    
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        
        if os.path.isdir(full_path):
            mathces.extend(find(full_path, filename))
        elif entry == filename:
            mathces.append(full_path)

    return mathces

#test
result = find('Recursion', '4-23-signature-find.py')
print(result) # ['Recursion/4-23-signature-find.py']