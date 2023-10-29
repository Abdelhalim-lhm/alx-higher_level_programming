#!/usr/bin/python3
def text_indentation(text):
    ''' function that prints a text with 2 new lines"
    "after each of these characters: ., ? and : '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    if text[0].isspace():
        while i < len(text) and text[i].isspace():
            i += 1
    while i < len(text):
        if text[i] in ('.', '?', ':'):
            print("{}".format(text[i]), end="\n\n")
            i = i + 1
            while i < len(text) and text[i].isspace():
                i += 1
        else:
            print("{}".format(text[i]), end="")
            i = i + 1


if __name__ == "__main__":
    import doctest
    doctest.filetest('5-text_indentation.txt')
