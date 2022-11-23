# Joseph Kirchhoff

# ----------GOAL------------
# Input temperature
# Output modulus, CTE

# --------------------------

def modulus(temperature):
    #data is from datasheet Pratik provided
    #AS4, PEEK
    #calculated value is linear interp between nearest. if larger than max temp, just taken to be modulus at max temp
    T_measured = [23, 65, 121, 168, 182, 232, 288, 315]
    E1_measured = [1.30, 1.30, 1.30, 1.27, 1.26, 1.25, 1.26, 1.24]*10^5
    E2_measured = [103, 95.8, 82.7, 42.5, 42.7, 36.1, 16.7,6.29]*10^2

    float val = 0


    return val 

def cte(temperature):
    #data is from datasheet Pratik provided
    #AS4, PEEK
     #calculated value is linear interp between nearest. if larger than max temp, just taken to be CTE at max temp
    float val = 0
    T_measured = [0, 50, 100, 150, 200, 250, 300, 350, 400]
    alpha1_measured = [1.5, 3.0, 5.0, 2.0, 0,0,0,0,0]*10^-7
    alpha2_measured = [2.82, 2.96, 3.16, 3.69, 7.3,7.7,8.4,8.8,8.2]*10^-5

    return val 