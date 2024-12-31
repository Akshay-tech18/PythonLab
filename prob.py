import pandas as pd
import numpy as np
from scipy.stats import pearsonr

data = {'variable_A' : [1,2,3,4,5,6],
        'variable_B' : [2,3,4,5,6,7]}

df = pd.DataFrame(data)

def calculate_correlation(df, col1, col2):
    correlation, _ =pearsonr(df[col1], df[col2])
    return correlation

def joint_probability(df,event_A,event_B):
    joint_df =df[(df['variable_A']==event_A)&(df['variable_B']==event_B)]
    joint_prob=len(joint_df/len(df))
    return joint_prob

def marginal_probability(df,event,variable):
    marginal_df=df[(df[variable]==event)]
    marginal_prob=len(marginal_df/len(df))
    return marginal_prob

def conditional_probability(df,event_A,event_B):
    joint_prob=joint_probability(df,event_A,event_B)
    marginal_prob=marginal_probability(df,event_B,'variable_B')
    if marginal_prob == 0:
        return 0
    return joint_prob/marginal_prob

correlation=calculate_correlation(df,'variable_A','variable_B')
print("Correlation between variable_A and variable_B",correlation)

joint_prob=joint_probability(df,3,4)
print("Joint probability p(A=3 and B=4)", joint_prob)

marg_prob_A=marginal_probability(df,3,'variable_A')
print("Marginal probability p(A=3)",marg_prob_A)

marg_prob_B=marginal_probability(df,4,'variable_B')
print("Marginal probability p(B=4) ",marg_prob_B)

cond_prob=conditional_probability(df,3,4)
print("Conditional probability p(A=3|B=4):",cond_prob)