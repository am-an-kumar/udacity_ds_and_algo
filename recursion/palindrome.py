def is_palindrome(input):
    """
    Checks if a string is palindrome
        :params: -
            input - string to check for palindrome
        :output: -
            is_palindrome - True/False based on whether the string is palindrome or not
    Time complexity - O(n*k), k is the size of substring at any time
    """
    length = len(input)
    if (length == 0) or (length == 1):
        return True
    elif input[0] != input[length - 1]:
        return False
    return input[1:length-1]
