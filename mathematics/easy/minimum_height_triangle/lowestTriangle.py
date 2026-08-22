import  math
def lowestTriangle(trianglebase, area):
    # Write your code here
    h = (2 * area) / trianglebase
    return math.ceil(h)

# test solution
print(lowestTriangle(17, 100)) # It will return 12