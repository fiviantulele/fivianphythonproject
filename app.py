import streamlit as st

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    st.title("Celsius to Fahrenheit Converter")
    
    celsius_temp = st.number_input("Enter temperature in Celsius", value=0.0)
    
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    
    st.write(f"{celsius_temp} Celsius is equal to {fahrenheit_temp} Fahrenheit.")

if __name__ == "__main__":
    main()

