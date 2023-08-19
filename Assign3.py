import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate a normal distribution
def generate_normal_distribution(mean, std, n):
    data = np.random.normal(mean, std, n)
    return data

# Main function
def main():
    # Set the title of the app
    st.title('Normal Distribution App')

    # Inputs
    mean = st.slider('Mean', 0, 100, 50)
    std = st.slider('Standard deviation', 0, 10, 2)
    n = st.slider('Number of samples', 10, 1000, 100)

    # Generate the normal distribution
    data = generate_normal_distribution(mean, std, n)

    # Plot the histogram using Matplotlib and Streamlit
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto', color='blue', alpha=0.7)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of normal distribution")
    st.pyplot(fig)

    # Download the generated data as a .csv file
    if st.button('Download data'):
        df = pd.DataFrame(data)
        df.to_csv('normal_distribution.csv', index=False)

if __name__ == '__main__':
    main()
