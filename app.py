import streamlit as st

st.title("🌏 Unit Convertor App")
st.markdown("### Converts Length, Weight and Time instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    try:
        value = float(value)
        if category == "Length":
            if unit == "Kilometers to miles":
                return value * 0.621371
            elif unit == "Miles to kilometers":
                return value * 1.60934  
            
        elif category == "Weight":
            if unit == "Kilograms to pounds":
                return value * 2.20462
            elif unit == "Pounds to kilograms":
                return value / 2.20462
                
        elif category == "Time":
            if unit == "Seconds to minutes":
                return value / 60  
            elif unit == "Minutes to seconds":
                return value * 60
            elif unit == "Minutes to hours":
                return value / 60
            elif unit == "Hours to minutes":
                return value * 60
            elif unit == "Hours to days":
                return value / 24
            elif unit == "Days to hours":
                return value * 24
    except ValueError:
        return None

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to kilometers"])

elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])

elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Seconds to minutes", "Minutes to seconds", 
                                               "Minutes to hours", "Hours to minutes", 
                                               "Hours to days", "Days to hours"])

value = st.number_input("Enter the value to convert", min_value=0.0, format="%.6f")

if st.button("Convert"):
    if value == "":
        st.error("Please enter a value to convert")
    else:
        result = convert_units(category, value, unit)
        if result is not None:
            st.success(f"Converted Result: {value} {unit.split(' to ')[0]} = {result:.6f} {unit.split(' to ')[1]}")
        else:
            st.error("Invalid input. Please enter a numeric value")