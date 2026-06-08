import numpy as np
import streamlit as st
from statsmodels.stats.proportion import proportions_ztest

st.set_page_config(page_title="Two-Proportion Z-Test", layout="centered")

st.title("Two-Proportion Z-Test")
st.caption("Test whether two observed proportions differ significantly")
st.divider()

with st.form("proportion_test_form"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Group 1")
        num_1   = st.number_input("Successes", min_value=0, step=1, key="num1")
        denom_1 = st.number_input("Total",     min_value=1, step=1, key="denom1")
    with col2:
        st.subheader("Group 2")
        num_2   = st.number_input("Successes", min_value=0, step=1, key="num2")
        denom_2 = st.number_input("Total",     min_value=1, step=1, key="denom2")
    submitted = st.form_submit_button("Run", use_container_width=True, type="primary")

if submitted:
    prop_1 = num_1 / denom_1
    prop_2 = num_2 / denom_2
    stat, pval = proportions_ztest(np.array([num_1, num_2]), np.array([denom_1, denom_2]))

    st.subheader("Observed Proportions")
    c1, c2, c3 = st.columns(3)
    c1.metric("Group 1", f"{prop_1:.4f}", f"{int(num_1)} / {int(denom_1)}", delta_color="off")
    c2.metric("Group 2", f"{prop_2:.4f}", f"{int(num_2)} / {int(denom_2)}", delta_color="off")
    c3.metric("Difference", f"{prop_1 - prop_2:+.4f}")

    st.divider()
    st.subheader("Test Results")

    if pval < 0.05:
        alert_fn, label = st.success, "Significant at the 5% level"
    elif pval < 0.10:
        alert_fn, label = st.warning, "Significant at the 10% level only"
    else:
        alert_fn, label = st.error, "Not significant at the 10% level"

    with alert_fn(label):
        r1, r2 = st.columns(2)
        r1.metric("Test Statistic", f"{stat:.3f}")
        r2.metric("P-Value", f"{pval:.3f}")
