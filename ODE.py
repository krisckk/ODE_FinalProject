import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def sugar_dynamics(Q, t, R, X, Q0):
    """
    Differential equation for sugar concentration dynamics
    
    Parameters:
    Q: Current sugar quantity (g)
    t: Time
    R: Inflow/outflow rate (liters/minute)
    X: Inflow concentration (g/liter)
    Q0: Initial sugar quantity (g)
    
    Returns:
    dQ/dt: Rate of change of sugar quantity
    """
    return R * X - (R / 100) * Q

def plot_sugar_dynamics(parameter_values, parameter_name, fixed_params):
    """
    Plot sugar concentration dynamics for different parameter values
    
    Parameters:
    parameter_values: List of values to test
    parameter_name: Name of the varying parameter
    fixed_params: Dictionary of fixed parameters
    """
    plt.figure(figsize=(10, 6))
    
    # Time array
    t = np.linspace(0, 60, 200)
    
    for value in parameter_values:
        # Create a copy of fixed parameters and update with current value
        params = fixed_params.copy()
        params[parameter_name] = value
        
        # Initial conditions
        Q0 = params['Q0']
        R = params['R']
        X = params['X']
        
        # Solve ODE
        solution = odeint(sugar_dynamics, Q0, t, args=(R, X, Q0))
        
        # Plot results
        plt.plot(t, solution, label=f'{parameter_name} = {value}')
    
    plt.title(f'Sugar Quantity Dynamics - Varying {parameter_name}')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Sugar Quantity (g)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Goal A: Varying Inflow/Outflow Rate (R)
def goal_a():
    fixed_params_a = {
        'Q0': 1000,  # Initial sugar quantity (g)
        'X': 10,     # Inflow concentration (g/liter)
        'R': 5       # Reference flow rate
    }
    
    # Different flow rates to test
    R_values = [2, 5, 10, 15]
    
    plot_sugar_dynamics(R_values, 'R', fixed_params_a)

# Goal B: Varying Initial Sugar Amount (Q0)
def goal_b():
    fixed_params_b = {
        'Q0': 500,   # Reference initial quantity
        'X': 10,     # Inflow concentration (g/liter)
        'R': 5       # Inflow/outflow rate (liters/minute)
    }
    
    # Different initial sugar quantities to test
    Q0_values = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    
    plot_sugar_dynamics(Q0_values, 'Q0', fixed_params_b)

# Goal C: Varying Inflow Concentration (X)
def goal_c():
    fixed_params_c = {
        'Q0': 1000,  # Initial sugar quantity (g)
        'X': 5,      # Reference inflow concentration
        'R': 5       # Inflow/outflow rate (liters/minute)
    }
    
    # Different inflow concentrations to test
    X_values = [2, 5, 10, 15]
    
    plot_sugar_dynamics(X_values, 'X', fixed_params_c)

# Run all goals
goal_a()
goal_b()
goal_c()