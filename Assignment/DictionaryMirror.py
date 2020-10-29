def mirrorChars(input,k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original, reverse))

    # separate out string after length k to change
    # characters in mirror
    prefix = input[0:k - 1]
    suffix = input[k - 1:]
    mirror = ''

    # change into mirror
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]

    # concat prefix and mirrored part
    print(prefix + mirror)


# Driver program

if __name__ == "__main__":
    input = 'asmagulzar'
    k = 5
    mirrorChars(input, k)