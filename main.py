import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

# Sidebar ----------------------------------------------
## st.sidebar.title("Navigation") if  i wanna have a title in there
page = st.sidebar.radio("Go to:", ["Expenses", "Income"])

# Session State ----------------------------------------
if "expenses" not in st.session_state:
  st.session_state.expenses = []
if "income" not in st.session_state:
  st.session_state.income = []

# Layout Columns----------------------------------------
col1, col2 = st.columns(2)

# Expenses Page ----------------------------------------

if page =="Expenses":
  st.title ("Expense Tracker")
  st.write ("Track your daily expenses below:")

  desc = st.text_input("Description")
  amount = st.number_input("Amount", min_value = 0.0, format = "%.2f", key = "expense_amount")

  if st.button("Add Expense"):
    if desc.strip() and amount > 0:
      st.session_state.expenses.append({"desc" : desc, "amount" : amount})
      st.success(f"Added: {desc} - ${amount:.2f}")
    else:
      st.warning("Please enter both a description and an amount.")

  if st.session_state.expenses:
    st.subheader("All Expenses")
    df = pd.DataFrame(st.session_state.expenses)
    df['amount'] = df['amount'].apply(lambda x: f"${x:.2f}")
    st.dataframe(df)
    total = sum(float(item['amount'].replace('$','')) for item in df.to_dict('records'))
    st.markdown(f"### Total Spent: ${total:.2f}")

# Income Page ------------------------------------------

elif page == "Income":
  st.title ("Income Tracker")
  st.write ("Track your income below:")

  income_desc = st.text_input("Income Source")
  income_amount = st.number_input("Amount", min_value = 0.0, format = "%.2f", key = "income_amount")

  if st.button("Add Income"):
    if income_desc.strip() and income_amount > 0:
      st.session_state.income.append({"desc" : income_desc, "amount" : income_amount})
      st.success(f"Added: {income_desc} - ${income_amount:.2f}")
    else:
      st.warning("Please enter both a source and an amount.")

  if st.session_state.income:
    st.subheader("All Income")
    df = pd.DataFrame(st.session_state.income)
    df['amount'] = df['amount'].apply(lambda x: f"${x:.2f}")
    st.dataframe(df)
    total = sum(float(item['amount'].replace('$','')) for item in df.to_dict('records'))
    st.markdown(f"### Total Income: ${total:.2f}")
