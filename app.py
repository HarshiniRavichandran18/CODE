import streamlit as st

# Page config
st.set_page_config(page_title="SMART FARMER", page_icon="🌟")

# Sidebar
st.sidebar.title("NAVIGATION")
menu = st.sidebar.radio("Go to", ["Home", "About", "Current Price", "Order", "Your Activities"])

# Home
if menu == "Home":
    st.title("SMART FARMER🌟")
    st.subheader("United as one team, we’ve crafted an unparalleled experience of innovation.")
    name = st.text_input("Enter your name: ")
    if st.button("Login"):
        st.success(f"Welcome {name} 🌟")

# About
elif menu == "About":
    st.header("📌 About Me")
    st.write("""
    - Direct farmer to customer supply  
    - Smart way to buy fresh items   
    - Friendly and your easiest way to buy!!  
    """)

# Current Price
elif menu == "Current Price":
    st.header("🛠 CURRENT PRICE")
    st.write("🔹 Tomato : 30/KG")
    st.write("🔹 Potato : 30/KG")
    st.write("🔹 Onion : 40/KG")

# Order
elif menu == "Order":

    # Price dictionary
    amt = {
        "Tomato": 30,
        "Potato": 30,
        "Onion": 40
    }

    orderitem = st.selectbox("Select item:", list(amt.keys()))
    kg = st.number_input("Enter Required KG:", min_value=1)

    if st.button("Place now"):
        st.success("Order accepted successfully ✅")

    if st.button("View Amount"):
        total = kg * amt[orderitem]
        st.success(f"Your Total Amount: ₹{total}")
    st.write("📞 Contact Me : 999 9999 999")
# Your Activities
elif menu == "Your Activities":
    st.header("You are a member now!! 🎉")
    st.write("Thank you shop again!!")