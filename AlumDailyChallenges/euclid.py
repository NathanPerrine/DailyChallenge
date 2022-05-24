# Where E(a, b) = b if remainder is 0, else E(b, r) = n if r=0, --> etc
# recursive design, can be iterative

def euclid(a, b, k=0):
    # handle edge case
    if a < b:
        a, b = b, a
    #####
    r = a % b
    print(b)
    if r !=0:
        euclid(b, r)
    else:
        return b

print(euclid(2166, 6099))

## Iterative