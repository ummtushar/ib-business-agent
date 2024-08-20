from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from groq import Groq
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the Groq client with the API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate a case study using the Groq API
def generate_case_study(text):
    prompt = f"""Based on the following IB Business Management HL course material, create a case study with detailed questions and answers that are aligned with the IB Diploma Business Manageent Exam 1,2 and 3exam standards:

    Material: {text}

    REMEMBER THAT THE QUESTIONS SHOULD BE OPEN ENDED AND NOT MULTIPLE CHOICE, TRUE/FALSE ETC!!

    Case Study with Questions and Answers:
    """
    
    # Prepare the API call
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=8000,
        temperature=0.7,
        top_p=1
    )
    
    return response.choices[0].message.content.strip()

# Streamlit app layout
st.title("IB Diploma Business Management Case Study Generator")

st.write("Upload your documents from different modules to generate a case study with questions and answers aligned with IB Diploma standards.")

# Upload multiple PDF files
uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    # Extract text from each PDF and combine
    combined_text = ""
    for uploaded_file in uploaded_files:
        combined_text += extract_text_from_pdf(uploaded_file) + "\n"
    
    # Display extracted text (optional)
    st.write("Extracted Text:")
    st.text_area("Extracted Text", combined_text, height=200)
    
    # Generate case study
    if st.button("Generate Case Study"):
        with st.spinner('Generating case study...'):
            case_study = generate_case_study(combined_text)
            if "Error" in case_study:
                st.error(case_study)
            else:
                st.success("Case Study Generated!")
                st.write(case_study)
                
                # Option to download the case study
                st.download_button("Download Case Study", case_study, "case_study.txt")
