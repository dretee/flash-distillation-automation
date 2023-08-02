
import sys
import numpy as np
from tabulate import tabulate


# FLASH DISTILLATION CALCULATION AUTOMATION

k = [1.62, 1.81, 1.13, 0.91, 0.46]
z = [0.15, 0.20, 0.20, 0.25, 0.20]

#define the formular 1
def f_cal_1(k,z,v_f):
    f= (z * (k-1)) / (1 + v_f * (k-1))
    return f

def f(k,z,v_f):
    output_1 = 0
    for i in range(len(k)):
        output_1 += f_cal_1(k[i], z[i], v_f)
    return output_1

#define the formular 2
def f_cal_2(k,z,v_f):
    f_2 = (z * (k-1)**2) / ((1 + v_f * (k-1))**2)
    return f_2

def f_2(k,z,v_f):
    output_2 = 0
    for i in range(len(k)):
        output_2 += f_cal_2(k[i], z[i], v_f)
    return output_2

# this is meant to calculate the mole fraction of all the components of the mixture to be distilled by the flash distillation
# it involves the relationship between the values of z,k and the attained value of the vapour-liquid ratio
def x_calc(z, v_f, k):
    values = []
    for i in range(len(k)):
        x = z[i]/(1+ (v_f * (k[i]-1)))
        values.append(x)
    return values



def y_calc(x,k):
    values = []
    for i in range(len(k)):
        y = k[i] * x[i]
        values.append(y)
    return values
 
# define the liquid and gas component solution
def flow_frac(Flow,z,x,y):
   value = []
   for i in range (len(z)):
        f1 = Flow * z[0]
        f2 = Flow * z[3]
        
        print(f1,f2)

        A = np.array([[x[0],y[0]],[x[3],y[3]]])
        B = np.array([f1,f2])
        C = np.linalg.solve(A,B)
        return C  


#
# 
#The main funtion uses all the defined formulars above. It has the looping process that is activated if the conditions are true
#
#
def main():
    
    # Take the initial vapour fraction to be 0 to verify if the system number of phases
   
    
    print("\n Note:The initial Value of v_f is taken to be 0")
    v_f = float(input('Pick a value between 0 and 1: '))
    

    initial_f = f(k, z, v_f)
    initial_f_prime = -1 * f_2(k, z, v_f)

# for the solution to be f=effective we need to test if there are two phases in the still. 
# If there is only one phase the code will automatical inform you and will stop
# In the case where there are two phases the program informs you and continues to calculate 
#
#
    if (initial_f > 0 and initial_f_prime < 0) or (initial_f < 0 and initial_f_prime > 0):
        print("\nTwo Phases are present in the mixture")

    else:
        print("Only one phase is present ")
        sys.exit()
# if the case is ture there exist 2 phases you will be prompted to input a value between 0 and 1.
#if the vaule isn't met again you will be prompted to inpute the right value
# the code has been made to be iterated 100 times with a tolerance of error value of 1e-3
    
 
    while True:
        v_f = float(input("Input a new value of V/F: "))
        if 0 <= v_f <= 1: 
            tolerance = 1e-3
            fin_it = 100
            table = []
            break                                                                              # exit the loop
        else:
            print("Number must be between 0 and 1")

    
    for i in range(fin_it):
        f_val = f(k, z, v_f)
        f_prime_val = f_2(k, z, v_f)
        

#introducing the table into the program for easy display

        table.append([i, v_f, f_val, f_prime_val])
        v_f_new = v_f - (f_val / (-1 * f_prime_val))
    
        v_f = v_f_new
        if abs(f_val) < tolerance:
            break
    
    print("\nIteration results:")
    headers = ["Iteration", "V/F", "F Value", "F Prime Value"]
    print(tabulate(table, headers=headers))
    
    
    print("\nThe value of the vapour to liquid ratio is = " + str(v_f))
    

    #print the component of each phase 

    x = x_calc(z, v_f, k)
    y = y_calc(x,k)

    print("\nComponent\tLiquid Phase (x)\tVapor Phase (y)")
    for i in range(len(k)):
        print(f"Component-{i+1}\t{x[i]:.4f}\t\t\t{y[i]:.4f}")
        
        
    print("\nWrite the value of the flow rate from the question below")
    Flow = int(input("input the value of the flow rate: "))   


    C = flow_frac(Flow, z, y, x)
    print(f"\n liquid flow rate: {C[0]}")
    print(f"\n gas flow rate:    {C[1]}")

    
if __name__ == "__main__":
    main()
    



