def letter(title):
    words = title.split()
    result = ""
    for word in words:
        result += word[0]
    print(result.upper())
letter("Game Of Thrones")