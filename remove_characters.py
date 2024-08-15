#solve
def remove_characters(arr1, arr2):
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            f = arr1.find(arr2[i])
            arr1 = arr1.replace(arr2[i], '')
    return arr1

str1 = "computer"
str2 = "cat"
print(remove_characters(str1, str2))