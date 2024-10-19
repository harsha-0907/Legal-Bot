import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Function to load external CSS for styling
def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

# Load custom CSS file
loadCSS("FrontEnd/css/style.css")

st.write("<-- NAVBAR to the Left")

# This is the Home Page
st.title("WELCOME TO THE LEGAL-BOT")
cnt = 0
#st.header(f"Number of happy Users {cnt} Footfall {cnt}")

categories = ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Oceania']
people_unable_to_access = [318.2e6, 215e6, 3.5e6, 900e6, 4.23e9, 12.6e6]  # In millions

st.markdown("<br></br>", unsafe_allow_html=True)

# Streamlit subtitle
st.header('People that require our Help!')

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(12,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
bars = ax.bar(categories, people_unable_to_access, color='#FFB6C1')  # Color to match theme

# Customize font properties to match the body font
ax.set_xlabel('Continent', fontsize=18, color='#FFB6C1')
ax.set_ylabel('Number of People (in billions and millions)', fontsize=18, color='#FFB6C1')

# Set y-axis ticks and font properties (scale for millions and billions)
ax.tick_params(axis='y', labelsize=12, labelcolor='#555555')
ax.set_yscale('log')  # Use log scale to make large differences easier to visualize
ax.set_yticks([1e6, 1e7, 1e8, 1e9])
ax.get_yaxis().set_ticklabels(['1M', '10M', '100M', '1B'], fontsize=15, color='#555555')

# Rotate the X-axis labels to ensure the continent names are visible
plt.xticks(ha='center', fontsize=12, color='#FFB6C1')

# Add grid lines with a lighter color for a cleaner look
ax.grid(True, which='both', axis='y', linestyle='--', color='#CCCCCC', linewidth=0.1)

# Show the graph in Streamlit
st.pyplot(fig)