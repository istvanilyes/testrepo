import streamlit as st
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


st.header('Difference between 2 proportions')
  
with st.form("proportion_test_form"):
    prop_count_1 = st.number_input(label="Numerator 1", min_value=0, step=1)
    prop_total_1 = st.number_input(label="Denominator 1", min_value=1, step=1)
    prop_count_2 = st.number_input(label="Numerator 2", min_value=0, step=1)
    prop_total_2 = st.number_input(label="Denominator 2", min_value=1, step=1)
    
    submitted_proportion_test = st.form_submit_button("Run")
    if submitted_proportion_test:
        if prop_count_1 > prop_total_1:
            st.error('Numerator 1 cannot be greater than Denominator 1')
        elif prop_count_2 > prop_total_2:
            st.error('Numerator 2 cannot be greater than Denominator 2')
        else:
            nums = np.array([prop_count_1, prop_count_2])
            denoms = np.array([prop_total_1, prop_total_2])
            stat, pval = proportions_ztest(nums, denoms)
            
            st.write('Prop 1: ',round(100*prop_count_1/prop_total_1,1),'%')
            st.write('Prop 2: ',round(100*prop_count_2/prop_total_2,1),'%')
            st.write('Test Stat: ', round(stat, 3))
            st.write('P-Val: ',round(pval, 3))