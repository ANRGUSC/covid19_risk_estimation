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
        
        if curr_I != 0:
            a1,a2 = curr_I-(curr_I**2)/N, next_I-(next_I**2)/N
            b1,b2 = -sigma*curr_I, -sigma*next_I
            if next_I>curr_I:
                delta_t =1
            else:
                delta_t =-1
            A = a1*a2*delta_t
            B = (a1*b2+a2*b1)*delta_t-(a1-a2)
            C = b1*b2*delta_t-(b1-b2)
            if B**2-4*A*C > 0:
                output = (-B+np.sqrt(B**2-4*A*C))/(2*A)
            else:
                output = 0
            #output = (next_I - curr_I+sigma*curr_I)/(curr_I-(1/N)*curr_I**2)
        else:
            output = 0
        print("curr", curr_I, "next", next_I)
        beta_SIR[time] = max(0,output)
        #beta_SIR[time] = max(0,solve_beta_for_single_time_exponential(matrix_I[0,time+1],matrix_I[0,time],sigma,population,0) )
        R[time] = beta_SIR[time] / sigma
        risk[time] = max((10000)*R[time]*vec_I[time]*ave_k/(1.0*population),0)
    clear_output(wait=True) 

    return risk