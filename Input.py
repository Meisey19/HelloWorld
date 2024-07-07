import streamlit as st
from datetime import datetime

def app():  
    # Function to append data to a file
    def save_to_file(number, date):
        with open("data.txt", "a") as file:
            file.write(f"Number: {number}, Date: {date}\n")

    # Title of the app
    st.title("Number and Date Input")

    # Dropdown menu with numbers 1 to 10
    number = st.selectbox("Select a number", list(range(1, 11)))

    # Textbox with today's date, allowing user to overwrite
    date = st.text_input("Enter a date", value=datetime.today().strftime('%d-%m-%Y'))

    # Save button
    if st.button("Save"):
        save_to_file(number, date)
        st.success(f"Saved: Number {number}, Date {date}")


"""

    file_content = st.text_area("Enter text to save to file")

    # Button to save the content
    if st.button("Save to File"):
        with open("output.txt", "w") as file:
            file.write(file_content)
        st.success("File has been written successfully!")

    # Button to read the content
    if st.button("Read from File"):
        try:
            with open("output.txt", "r") as file:
                st.text(file.read())
        except FileNotFoundError:
            st.error("File not found. Please write to the file first.")
"""