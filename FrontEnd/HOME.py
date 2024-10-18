import streamlit as st
import matplotlib.pyplot as plt

# Function to load external CSS for styling
def loadCSS(filepath=""):
    with open(filepath) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

# Load custom CSS file
loadCSS("FrontEnd/css/style.css")

# Create a navigation bar using markdown and HTML
navbar = """
<nav style="background-color:#2c3e50; padding: 10px; text-align: center;">
    <a href='#home' style='margin: 0 15px; text-decoration: none; color: white;'>Home</a>
    <a href='#about' style='margin: 0 15px; text-decoration: none; color: white;'>About</a>
    <a href='#chat' style='margin: 0 15px; text-decoration: none; color: white;'>Chat</a>
    <a href='#login' style='margin: 0 15px; text-decoration: none; color: white;'>Login/Signup</a>
</nav>
"""

# Display the navigation bar
st.markdown(navbar, unsafe_allow_html=True)

# Title and image on the home page with a two-column layout
col1, col2 = st.columns([1, 1])

with col1:
    # Title of the platform
    st.markdown("<h1 style='font-size: 2.5em; color: #2c3e50;'>Legal Bot</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='font-size: 1.2em; color: #34495e;'>
        Legal Bot is your AI-powered assistant, providing seamless access to legal research tools, 
        making complex legal systems more accessible.
        </p>
    """, unsafe_allow_html=True)

with col2:
    # You can add a legal-themed image here (replace 'legal_image.png' with your actual image path)
    st.image("https://png.pngtree.com/thumb_back/fh260/background/20230715/pngtree-3d-rendered-concept-illustration-of-legal-justice-and-rules-image_3882668.jpgFrontEnd/images/legal_image.png", caption="Legal Intelligence Platform", use_column_width=True)

# Display user statistics with bar graphs or pie charts
st.header("Legal Bot User Statistics")

# Sample data for demonstration (Replace with actual data)
data = {
    'Metrics': ['Total Users', 'Logins', 'Queries Processed', 'Website Visits'],
    'Count': [500, 1200, 2000, 4500]
}
df = pd.DataFrame(data)

# Bar chart of the statistics
st.subheader("Bar Graph of User Statistics")
fig, ax = plt.subplots()
ax.bar(df['Metrics'], df['Count'], color=['#3498db', '#2ecc71', '#f1c40f', '#e74c3c'])
ax.set_ylabel('Count')
ax.set_title('User Engagement Metrics')

# Display bar chart
st.pyplot(fig)

# Optionally, show pie chart for a different representation
st.subheader("Pie Chart of User Statistics")
fig, ax = plt.subplots()
ax.pie(df['Count'], labels=df['Metrics'], autopct='%1.1f%%', colors=['#3498db', '#2ecc71', '#f1c40f', '#e74c3c'], startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display pie chart
st.pyplot(fig)

# Footer message
st.markdown("<p style='text-align: center; font-size: 0.8em;'>Legal Bot © 2024 - Making Legal Research Accessible for All</p>", unsafe_allow_html=True)
