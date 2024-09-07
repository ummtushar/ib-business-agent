# ib-business-agent

AI Agent to generate past papers using text-to-text technique

https://github.com/user-attachments/assets/937764d4-7c57-4eaf-8ba0-ed3dcb9ae17e

# IB Diploma Business Management Case Study Generator

## Overview

This Streamlit application allows users to generate case studies tailored for the IB Diploma Business Management HL course. By uploading relevant course materials in PDF format, users can generate detailed case studies with open-ended questions and answers that align with IB Diploma Exam standards.

## Features

- **PDF Upload**: Users can upload multiple PDF files containing IB Business Management course materials.
- **Text Extraction**: The app extracts text from the uploaded PDFs.
- **Case Study Generation**: Using the Groq API, the app generates a case study with questions and answers based on the extracted text.
- **Download Option**: Generated case studies can be downloaded as a text file.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/business-management-case-study-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd business-management-case-study-generator
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Set up your environment variables:
    - Create a `.env` file in the project root.
    - Add your Groq API key to the `.env` file:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501`.

3. Upload your PDF files containing the course material.

4. Click on the "Generate Case Study" button to generate the case study.

5. Once generated, you can view the case study directly in the app and download it as a text file.

## Dependencies

- `streamlit`: For building the web app interface.
- `PyPDF2`: For extracting text from PDF files.
- `Groq`: For generating the case studies using AI.

## License

This project is licensed under the CC BY NC License.

## Contact

For any questions or feedback, please contact Tushar Gupta at [tusharg69115@gmail.com].
