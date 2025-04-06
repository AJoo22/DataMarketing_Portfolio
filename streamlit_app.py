import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the title of the app
st.title('Interactive Data Plotting App')

# Sidebar for user input
with st.sidebar:
    st.header("Input Your Data")
    # Allow user to input a CSV file or use example data
    uploaded_file = st.file_uploader("Upload a CSV", type="csv")
    if uploaded_file is not None:
        # Use the uploaded file
        data = pd.read_csv(uploaded_file)
    else:
        # Use example data
        st.info("Using example data.")
        data = pd.DataFrame({
            'x': range(1, 11),
            'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        })

# Display the data
st.write("### Data", data)

# Plotting options
plot_type = st.selectbox("Select plot type:", options=['Line Plot', 'Bar Plot', 'Scatter Plot'])

# Plot the data based on selected plot type
fig, ax = plt.subplots()
if plot_type == 'Line Plot':
    ax.plot(data['x'], data['y'], marker='o')
    st.write("### Line Plot")
elif plot_type == 'Bar Plot':
    ax.bar(data['x'], data['y'])
    st.write("### Bar Plot")
elif plot_type == 'Scatter Plot':
    ax.scatter(data['x'], data['y'], color='r')
    st.write("### Scatter Plot")

# Customizing plot
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title(f'{plot_type}')
plt.grid(True)

# Display the plot
st.pyplot(fig)
