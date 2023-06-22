def geosum(k):
    if k==0:
        return 1
    return (1/2**k) + geosum(k-1)

k = 3
print(geosum(k))