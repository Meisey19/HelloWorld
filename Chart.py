import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def app():

# Function to read data from the file
    def read_data(file_path):
        data = []

        try:
            with open(file_path, "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    if len(parts) == 2:
                        number = int(parts[0].split(": ")[1])
                        date = datetime.strptime(parts[1].split(": ")[1], '%d-%m-%Y')
                        data.append({"date": date, "number": number})
        except FileNotFoundError:
            st.error("The data file was not found.")
        return data

    progress_bar = st.sidebar.progress(0)
    #status_text = st.sidebar.empty()
    
    # Read data from the file
    data = read_data("data.txt")

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Plot the data using matplotlib
    if not df.empty:
        fig, ax = plt.subplots()
        ax.plot(df['date'], df['number'], marker='o', linestyle='-')
        ax.set_xlabel("Date")
        ax.set_ylabel("Value")
        ax.set_title("Values over Time")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.write("No data available to plot.")

    # Display the DataFrame
    st.write("Data from file:", df)
    progress_bar.empty()

    # st.title("Chart")

    # progress_bar = st.sidebar.progress(0)
    # status_text = st.sidebar.empty()
    # last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    # for i in range(1, 101):
    #     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    #     status_text.text("%i%% Complete" % i)
    #     chart.add_rows(new_rows)
    #     progress_bar.progress(i)
    #     last_rows = new_rows
    #     time.sleep(0.05)

    # progress_bar.empty()

    # # Streamlit widgets automatically run the script from top to bottom. Since
    # # this button is not connected to any other logic, it just causes a plain
    # # rerun.
    # st.button("Re-run")

