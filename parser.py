def char(character):
    def fn(bytes):
        if bytes[0] == character:
            return (character, bytes[1:])
        else:
            return (None, bytes)
    return fn

def repeat(parser):
    def fn(bytes):
        buffer = ""
        while True:
            consumed, bytes = parser(bytes)
            if consumed == None:
                return buffer, bytes
            else:
                buffer += consumed
                if len(bytes) == 0:
                    return buffer, ""
    return fn

def either(first, second):
    def fn(bytes):
        consumed, bytes = first(bytes)
        if consumed == None:
            return second(bytes)
        else:
            return consumed, bytes
    return fn


def a():
    return repeat(either(char("a"), char("b")))

if __name__ == "__main__":

    print(a()("aaabbbab"))
