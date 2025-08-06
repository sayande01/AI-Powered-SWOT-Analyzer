# AI-Powered SWOT Analysis Web App 📊

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.8-green.svg)](https://www.langchain.com/)
[![Google Gemini 1.5 Pro](https://img.shields.io/badge/Google%20Gemini-1.5%20Pro-orange.svg)](https://ai.google.dev/models/gemini)

## 🌟 Overview

The **AI-Powered SWOT Analysis Web App** is a cutting-edge tool designed to automate and enhance strategic planning by transforming raw organizational data into structured, actionable SWOT insights. Built with a focus on **Generative AI (GenAI)**, this application utilizes **Google Gemini 1.5 Pro** via **LangChain** and a **Retrieval-Augmented Generation (RAG)** architecture to provide deep, contextual analyses. Users can input organizational information via text or file upload, receiving a detailed SWOT breakdown complemented by interactive visualizations.

This project is a great demonstration of applying advanced NLP and LLM techniques to real-world business challenges, making it an excellent addition to a Data Science and AI portfolio.

## ✨ Key Features

* **Automated SWOT Generation**: Converts unstructured organizational data into a comprehensive SWOT analysis using AI.
* **Intelligent Insights**: Leverages **Google Gemini 1.5 Pro** for nuanced and context-aware analysis.
* **Retrieval-Augmented Generation (RAG)**: Employs **LangChain** and **FAISS** to retrieve relevant SWOT concepts, enhancing the quality and specificity of the generated analysis.
* **Interactive Visualizations**: Presents SWOT components through dynamic radar and bar charts using Plotly for quick strategic overview.
* **Flexible Input**: Supports direct text input and file uploads (TXT, PDF, DOCX - *PDF/DOCX processing is a planned feature for full implementation*).
* **User-Friendly Interface**: Developed with **Streamlit** for an intuitive and responsive web experience, featuring modern glass-morphism and gradient styling.

## ⚙️ Architecture & Technologies

* **Frontend**: Streamlit with custom CSS for a modern, futuristic UI.
* **NLP Engine**: Google Generative AI (`gemini-1.5-pro-latest`) for powerful text generation and understanding.
* **Vector Database**: **FAISS** (Facebook AI Similarity Search) for efficient similarity search and retrieval of SWOT concepts.
* **Framework**: **LangChain** for orchestrating the RAG pipeline, prompt management, and seamless integration with the LLM and vector store.
* **Visualization**: **Plotly** for creating interactive and informative charts.
* **Data Handling**: Pandas for data manipulation.

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

* Python 3.9+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/AI-Powered-SWOT-Analyzer.git](https://github.com/your-username/AI-Powered-SWOT-Analyzer.git)
    cd AI-Powered-SWOT-Analyzer
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file in your project root with the following content:
    ```
    streamlit==1.31.0
    langchain==0.1.8
    langchain-google-genai==0.0.7
    faiss-cpu==1.7.4 # or faiss-gpu if you have a compatible GPU
    numpy==1.26.3
    plotly==5.18.0
    pandas==2.1.4
    python-docx # for docx file handling
    PyPDF2 # for pdf file handling
    ```
    Then install:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  **Set your Google API Key:**
    The application requires a Google API Key to access the Gemini 1.5 Pro model. You can obtain one from the [Google AI Studio](https://ai.google.dev/).

    Set it as an environment variable:
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
    (On Windows, use `set GOOGLE_API_KEY="YOUR_API_KEY_HERE"` in Command Prompt or `$env:GOOGLE_API_KEY="YOUR_API_KEY_HERE"` in PowerShell).

    Alternatively, the app will prompt you for the API key if it's not set.

### Running the Application

1.  **Run the Streamlit app:**
    ```bash
    streamlit run complete-swot-analysis-appv2.py
    ```

    The application will open in your default web browser.

## 💡 How to Use

1.  **Provide Organizational Information**:
    * **Text Input**: Type or paste detailed information about an organization (e.g., its operations, market position, challenges, strengths, recent initiatives) into the provided text area.
    * **File Upload**: Upload a `.txt`, `.pdf`, or `.docx` file containing the organizational data.

2.  **Generate Analysis**: Click the "Generate SWOT Analysis" button. The AI will process the information and produce a comprehensive SWOT breakdown.

3.  **Explore Results**:
    * **Overview Tab**: Get a quick summary of the key strengths, weaknesses, opportunities, and threats.
    * **Detailed Analysis Tab**: View the complete, in-depth SWOT analysis generated by the AI.
    * **Visualizations Tab**: See interactive radar and bar charts illustrating the distribution and balance of your SWOT components.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## 📄 License

This project is released under a Proprietary License.

## 📧 Contact

For any questions or inquiries, please open an issue in this repository.
