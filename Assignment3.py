
# Ask the user for input - how many points?
n = int(input("How many points do you want? "))
print("Please enter the points in counter-clockwise order!!")
# Create empty list - to store coordinates
x = []
y = []

# Ask the user to input coordinates
for i in range(0, n):
    inputx = int(input("Please enter x coordinate: "))
    x.append(inputx)
    inputy = int(input("Please enter y coordinate: "))
    y.append(inputy)


# Print coordinates
print("Coordinate Table")
print("Point", "X", "Y")
print("------------")
for i in range(0, n):
    print(i+1, ":", x[i], y[i])

# AREA
# Create empty list to store individual areas
lax = []
for i in range(0, n):
    ax = (x[i]+x[i-1]) * (y[i]-y[i-1])
    lax.append(ax)
# print((lax))
# Sum all areas from list and divide by two
tax = 0.5*sum(lax)


# STATIC MOMENTS
lsx = []
for i in range(0, n):
    sx = (x[i]-x[i-1]) * (y[i]**2+y[i]*y[i-1]+y[i-1]**2)
    lsx.append(sx)
# print((lsx))
# Sum all areas from list and divide by two
tax = 0.5*sum(lax)
tsx = -1/6*sum(lsx)

lsy = []
for i in range(0, n):
    sy = (y[i]-y[i-1]) * (x[i]**2+x[i]*x[i-1]+x[i-1]**2)
    lsy.append(sy)
# print((lsy))

lix = []
for i in range(0, n):
    ix = (x[i]-x[i-1]) * (y[i]**3+y[i]**2*y[i-1]+y[i]*y[i-1]**2+y[i-1]**3)
    lix.append(ix)
# print((lix))

liy = []
for i in range(0, n):
    iy = (y[i]-y[i-1]) * (x[i]**3+x[i]**2*(x[i-1])+x[i]*x[i-1]**2+x[i-1]**3)
    liy.append(iy)
# print((liy))

lixy = []
for i in range(0, n):
    ixy = (y[i]-y[i-1]) * (y[i]*(3*x[i]**2+2*x[i]*x[i-1]+x[i-1]**2)) + \
        y[i-1]*(3*x[i]**2+2*x[i]*x[i-1]+x[i]**2)
    lixy.append(ixy)
# print((lixy))
# Sum all areas from list and divide by two
tax = 0.5*sum(lax)
tsx = -1/6*sum(lsx)
tsy = 1/6*sum(lsy)
tix = -1/12*sum(lix)
tiy = 1/12*sum(liy)
tixy = -1/24*sum(lixy)
xt = tsy/tax
yt = tsx/tax
ixt = tix - yt**2*tax
iyt = tiy - xt**2*tax
ixyt = tixy + xt*yt*tax
# Print output
print("The calculated properties are as follows:")
print("Ax= ", "%.2f" % (tax))
print("Sx=", "%.2f" % tsx)
print("Sy=", "%.2f" % tsy)
print("Ix=", "%.2f" % tix)
print("Iy=", "%.2f" % tiy)
print("Ixy=", "%.2f" % tixy)
print("xt=", "%.2f" % xt)
print("yt=", "%.2f" % yt)
print("Ixt=", "%.2f" % ixt)
print("Iyt=", "%.2f" % iyt)
print("Ixyt=", "%.2f" % ixyt)
