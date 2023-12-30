import streamlit as st
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


st.header('Difference between 2 proportions')
  
with st.form("proportion_test_form"):
    num_1 = st.number_input(label="Numerator 1", min_value=0, step=1)
    denom_1 = st.number_input(label="Denominator 1", min_value=1, step=1)
    num_2 = st.number_input(label="Numerator 2", min_value=0, step=1)
    denom_2 = st.number_input(label="Denominator 2", min_value=1, step=1)

    submitted_proportion_test = st.form_submit_button("Run")
    
    nums = np.array([num_1, num_2])
    denoms = np.array([denom_1, denom_2])
    stat, pval = proportions_ztest(nums, denoms)
    
    st.write('Test Stat: ', round(stat, 3))
    st.write('P-Val: ',round(pval, 3))