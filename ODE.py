import numpy as np
import matplotlib.pyplot as plt
# The ODE Functiom to calculate sugar Quantity is dQ/dt = R * (X - Q/100)
# Solve the ODE function using Euler's method will get Q(t) = 100 * X + C * e ^ (-Rt/100)
# The initial condition is Q(0) = Q0, so C = Q0 - 100 * X
# The solution is Q(t) = 100 * X + (Q0 - 100 * X) * e ^ (-Rt/100)

# Function to compute sugar quantity over time
def OriginalODEFunction(Q0, X, R, T, C):
    Q = 100 * X + C * np.exp(-R * T / 100)
    return Q
def ODESolvingFunction(Q0, X, R, T):
    C = Q0 - 100 * X
    return 100 * X + C * np.exp(-R * T / 100)
def SugarCalcFunction(Q0, X, R, time):
    t = np.linspace(0, time, 10000) # create 10000 evenly spaced points for smooth lines
    Q = ODESolvingFunction(Q0, X, R, t)
    return t, Q

# Goal A: Vary R and plot the dynamics
def GoalA(Q0, X, R_values, time):
    plt.figure()
    for R in R_values:
        t, Q = SugarCalcFunction(Q0, X, R, time)
        plt.plot(t, Q, label=f"R={R}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Sugar Quantity (gram)")
    plt.title("Impact of Inflow/Outflow Rate (R)")
    plt.legend()
    plt.grid()
    plt.show()

# Goal B: Vary Q0 and plot the dynamics
def GoalB(Q0_values, X, R, time):
    plt.figure()
    for Q0 in Q0_values:
        t, Q = SugarCalcFunction(Q0, X, R, time)
        plt.plot(t, Q, label=f"Q0={Q0}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Sugar Quantity (g)")
    plt.title("Impact of Initial Sugar Quantity (Q0)")
    plt.legend()
    plt.grid()
    plt.show()

# Goal C: Vary X and plot the dynamics
def GoalC(Q0, X_values, R, time):
    plt.figure()
    for X in X_values:
        t, Q = SugarCalcFunction(Q0, X, R, time)
        plt.plot(t, Q, label=f"X={X}")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Sugar Quantity (g)")
    plt.title("Impact of Inflow Concentration (X)")
    plt.legend()
    plt.grid()
    plt.show()

# Parameters
time = 100  # Total simulation time in minutes

GoalType = input("Enter the goal type (A, B, C): ")
if(GoalType == "A"):
    Q0_values = input("Enter the initial sugar quantity values (Only enter one value): ")
    X_values = input("Enter the inflow concentration values (Only enter one value): ")
    R_values = input("Enter the rate values (separate by space): ")
elif(GoalType == "B"):
    Q0_values = input("Enter the initial sugar quantity values (seprate by space): ")
    X_values = input("Enter the inflow concentration values (Only enter one value): ")
    R_values = input("Enter the rate values (Only enter one value): ")
elif(GoalType == "C"):
    Q0_values = input("Enter the initial sugar quantity values (Only enter one value): ")
    X_values = input("Enter the inflow concentration values (seprate by space): ")
    R_values = input("Enter the rate values(Only enter one value): ")
# Convert input strings to lists of floats
Q0_values = [float(val) for val in Q0_values.split()]
X_values = [float(val) for val in X_values.split()]
R_values = [float(val) for val in R_values.split()]
# Call the corresponding function based on the goal type
if GoalType == "A":
    GoalA(Q0_values[0], X_values[0], R_values, time)
elif GoalType == "B":
    GoalB(Q0_values, X_values[0], R_values[0], time)
elif GoalType == "C":
    GoalC(Q0_values[0], X_values[0], R_values, time)

