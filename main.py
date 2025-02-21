import streamlit as st

st.set_page_config(page_title="Salim's Portfolio", page_icon="🧊", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/salim.png")

with col2:
    st.title("Lawal Salim")
    content = """

    I currently a masters student in the Erasmus Mundus Software Engineering for Green Deal (SE4GD) program. I have previously headed the Information and Communication Technology (ICT) department of File Solutions Ltd. 
    I had my Bachelor of Engineering degree (B.Eng.) in Computer Engineering from Ahmadu Bello University, Zaria, Nigeria in 2019. 
    I am also a Professional Data Analyst and a System Administrator with over three (3) years of working experience in the ICT sector. 
    My professional career began as an Associate Consultvant in Information Technology at Carter Consulting Ltd in July 2019, where I was involved in several projects such as the project lighthouse (an Artificial Intelligence engine for revenue tracking and optimization) for the Federal Ministry of Finance (FMF), Nigeria.
    Also, I'm a passionate sustainability enthusiast deeply concerned about the impact of human activities on the environment. 
    My current focus is on researching data-driven, software engineering solutions to enhance energy efficiency and promote sustainable energy usage in Africa, and the world at large."""
    
    st.write(content)

content2 = """
## Education

**University of L'Aquila, Italy**
MSc. Computer Science 
September 2024 - December 2024

**Lappeenranta-Lahti University of Technology (LUT), Finland**
MSc. Software Engineering 
January 2025 - June 2025
"""

st.write(content2)