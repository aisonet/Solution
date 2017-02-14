DEFAULT_TEXT = "aabaa"

def palindrome(s):

    results = set()
    text_length = len(s)
    #print text_length
    for idx, char in enumerate(s):

        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and s[start] == s[end]:
            results.add(s[start:end + 1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and s[start] == s[end]:
            results.add(s[start:end + 1])
            start -= 1
            end += 1

    return list(results)


print palindrome(DEFAULT_TEXT)