import streamlit as st
def main():
    st.title('Adding two numbers')
    st.warning('Only Enter Numeric Values in the Following Fields')
    a = st.text_input("Enter first number")
    b = st.text_input("Enter second number")
    submit = st.button('Add numbers')
    if submit: 
        if a and b:
            with st.spinner('Calculating...'):
                time.sleep(2)
                addition = a+b
                st.info(f"Your **sum** of {a} and {b} is {addition}")
        else:
            st.error('Please Enter All the Details')

if __name__ == '__main__':
    main()
