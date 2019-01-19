def largestPalindromeProduct(min1,min2,max1,max2):
    palindromes = []
    for x in range(min1,max1):
        for i in range(min2,max2):
            product = i*x
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
    return(max(palindromes))
