# calculator using height

h=(int(input("Please Enter the height : ")))
h=h*1000
# print(f"The value for acceleration due to gravity at {h*1000}m is {9.8/(1+(h*1000/6400000)*(1+(h*1000/640000)))}")

g0 = 9.8  # m/s^2, acceleration due to gravity at Earth's surface
R = 6400 * 10**3  # meters, Earth's radius

if h>0:
# Correct formula
    g_h = g0 * (R / (R + h)) ** 2
    print(f"The value for acceleration due to gravity at {h/1000} km is {g_h:.2f} m/s^2")

elif h<0:
    g_h= (g0*(1-(h/R)))/R
    print(f"The value for acceleration due to gravity at {h/1000} km is {g_h:.2f} m/s^2")

