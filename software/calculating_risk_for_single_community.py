def calculating_risk_for_single_community(vec_I,population,sigma,ave_k):
""" This function computes the daily risk score for a single community given the number of daily infected cases, population of the community, 
inverse of average recovery dates, and number of times actual infected cases is higher than reported ones."""

# Inputs:
# - vec_I       :   Represents the vector of number of daily infected cases reported for the community
# - population  :   Indicates the population of the community
# - sigma       :   Is equal to 1/D where D represents the average recovery days (usually D is around 7.5)
# - ave_k       :   Average value for the ration of actual active daily infected cases to reported ones (should be >=1)

# Outputs:
# - risk        :    Vector of the risk score of the community over time

    c = len(vec_I)
    matrix_I = vec_I[np.newaxis,:]
    beta_SIR,R,risk = np.zeros((c-1,)),np.zeros((c-1,)),np.zeros((c-1,))
    for time in range(c-1):
        clear_output(wait=True)
        next_I,curr_I,N = ave_k*vec_I[time+1],ave_k*vec_I[time],population
        print("curr", curr_I, "next", next_I)
        if next_I>curr_I:
            if next_I != 0 and curr_I != 0 and next_I != curr_I:
                m = GEKKO()             # create GEKKO model
                beta = m.Var(value=.2)      # define new variable, initial value=0
                m.Equations([((1/(beta-sigma))*m.log(next_I/((beta-sigma)-beta*next_I/N))) -  ((1/(beta-sigma))*m.log(curr_I/((beta-sigma)-beta*curr_I/N))) == 1.0]) # equations
                m.solve(disp=False)     # solve
                output = beta.value[0]
            else:
                if curr_I != 0:
                    output = (next_I - curr_I+sigma*curr_I)/(curr_I-(1/N)*curr_I**2)
                else:
                    output = 0
        else:
            if curr_I != 0:
                output = (next_I - curr_I+sigma*curr_I)/(curr_I-(1/N)*curr_I**2)
            else:
                output = 0

        beta_SIR[time] = max(0,output)
        #beta_SIR[time] = max(0,solve_beta_for_single_time_exponential(matrix_I[0,time+1],matrix_I[0,time],sigma,population,0) )
        R[time] = beta_SIR[time] / sigma
        risk[time] = (10000)*R[time]*vec_I[time]*ave_k/(1.0*population)
    clear_output(wait=True) 

    return risk