
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║                  SWOT Analysis AI Agent WebAPP (v1.0.0)                        ║
# ║                          Last Updated: 2025-03-11                              ║
# ║                           License: Proprietary                                 ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ OBJECTIVE:                                                                     ║
# ║   To deliver an AI-driven web application that automates comprehensive SWOT    ║
# ║   analysis by transforming organizational data into actionable insights.       ║
# ║   The tool evaluates Strengths, Weaknesses, Opportunities, and Threats (SWOT)  ║
# ║   provides interactive visualizations for enhanced strategic planning.         ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ IMPORTED LIBRARY VERSIONS:                                                     ║
# ║   • Python: 3.9+                                                               ║
# ║   • Streamlit: 1.31.0                                                          ║
# ║   • Pandas: 2.1.4                                                             ║
# ║   • Plotly: 5.18.0                                                            ║
# ║   • LangChain: 0.1.8                                                          ║
# ║   • langchain-google-genai: 0.0.7                                             ║
# ║   • FAISS: 1.7.4                                                              ║
# ║   • NumPy: 1.26.3                                                             ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ SYSTEM CONFIGURATION:                                                          ║
# ║   • Operating System: [OS Name]                                                ║
# ║   • CPU Cores: [Number of CPU Cores]                                           ║
# ║   • Working Directory: [Current Directory]                                     ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ ARCHITECTURE & DESIGN:                                                         ║
# ║   - Frontend: Streamlit with custom CSS styling                                ║
# ║   - NLP Engine: Google Generative AI (Gemini 1.5 Pro)                          ║
# ║   - Vector Database: FAISS for similarity search                               ║
# ║   - Framework: LangChain for Retrieval-Augmented Generation (RAG)              ║
# ║   - Visualization: Plotly for interactive SWOT charts                          ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ KEY FEATURES:                                                                  ║
# ║   • Automated conversion of organizational data into SWOT components           ║
# ║   • AI-powered SWOT analysis with detailed insights                            ║
# ║   • Interactive visualizations (radar & bar charts)                            ║
# ║   • Custom prompt templates and RAG implementation                             ║
# ║   • Flexible input options (text area and file upload)                         ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ USAGE:                                                                         ║
# ║   1. Install dependencies: pip install -r requirements.txt                     ║
# ║   2. Set required environment variables (e.g., GOOGLE_API_KEY)                 ║
# ║   3. Run the app: streamlit run swot-analysis-app.py                           ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ DATA SOURCES:                                                                  ║
# ║   • User-provided organizational information                                   ║
# ║   • Predefined SWOT concept documents and analysis templates                   ║
# ║   • Historical and sample SWOT data                                            ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ WORKFLOW:                                                                      ║
# ║   1. Data collection via text input or file upload                             ║
# ║   2. Vectorization and retrieval of SWOT concepts using FAISS                  ║
# ║   3. AI-driven SWOT analysis generation using Google Generative AI (Gemini 1.5)║
# ║   4. Extraction and visualization of SWOT components                           ║
# ║   5. Presentation of detailed reports and interactive charts                   ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ SECURITY & PRIVACY:                                                            ║
# ║   • Secure management of API keys via environment variables                    ║
# ║   • No persistence of sensitive user data between sessions                     ║
# ║   • Limited external API calls (only authorized AI services)                   ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ FUTURE IMPROVEMENTS:                                                           ║
# ║   • Integration with persistent databases for enhanced data management         ║
# ║   • Multi-user support with role-based access controls                         ║
# ║   • Extended support for additional file formats and advanced NLP models       ║
# ║   • Enhanced visualization customization and export capabilities               ║
# ╠════════════════════════════════════════════════════════════════════════════════╣
# ║ CONTACT:                                                                       ║
# ║   For support or feature requests, please contact:                             ║
# ║   swot-support@[yourcompany].com                                               ║
# ╚════════════════════════════════════════════════════════════════════════════════╝


import os, getpass
import streamlit as st
import sys
import docx
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import time
import plotly.graph_objects as go
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="SWOT Analysis Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced futuristic styling
st.markdown("""
<style>
    /* Main background with gradient animation */
    .main {
        background: linear-gradient(-45deg, #2b5876, #4e4376, #2b5876, #4e4376);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        padding: 20px;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* App container */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Glass morphism for containers */
    .search-container, .result-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .search-container:hover, .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
    }
    
    /* Futuristic title container */
    .title-container {
        background: linear-gradient(120deg, #000428, #004e92);
        padding: 30px;
        border-radius: 15px;
        color: white;
        margin-bottom: 35px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
        position: relative;
        overflow: hidden;
    }
    
    .title-container:before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.1) 100%);
        transform: rotate(45deg);
        z-index: 0;
        animation: shine 5s infinite;
    }
    
    @keyframes shine {
        0% { left: -50%; }
        100% { left: 150%; }
    }
    
    .title-container h1 {
        font-weight: 800;
        letter-spacing: 2px;
        position: relative;
        z-index: 1;
        text-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* SWOT-specific card styling with enhanced effects */
    .strengths {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(76, 175, 80, 0.15) 100%);
        border-left: 6px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2);
        transition: all 0.3s ease;
    }
    
    .weaknesses {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.05) 0%, rgba(244, 67, 54, 0.15) 100%);
        border-left: 6px solid #F44336;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(244, 67, 54, 0.2);
        transition: all 0.3s ease;
    }
    
    .opportunities {
        background: linear-gradient(135deg, rgba(33, 150, 243, 0.05) 0%, rgba(33, 150, 243, 0.15) 100%);
        border-left: 6px solid #2196F3;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(33, 150, 243, 0.2);
        transition: all 0.3s ease;
    }
    
    .threats {
        background: linear-gradient(135deg, rgba(255, 152, 0, 0.05) 0%, rgba(255, 152, 0, 0.15) 100%);
        border-left: 6px solid #FF9800;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(255, 152, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .strengths:hover, .weaknesses:hover, .opportunities:hover, .threats:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    /* Neon buttons */
    .stButton>button {
        background: linear-gradient(90deg, #8E2DE2, #4A00E0);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.7rem 1.5rem;
        font-weight: bold;
        font-size: 16px;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(138, 43, 226, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 25px rgba(138, 43, 226, 0.6);
        letter-spacing: 1.5px;
    }
    
    .stButton>button:active {
        transform: translateY(1px);
    }
    
    .stButton>button:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(120deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transform: translateX(-100%);
        transition: 0.6s;
    }
    
    .stButton>button:hover:before {
        transform: translateX(100%);
    }
    
    /* Text inputs and areas */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        padding: 12px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #4A00E0;
        box-shadow: 0 0 0 3px rgba(74, 0, 224, 0.15);
    }
    
    /* Tables and dataframes */
    .dataframe {
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 10px;
        overflow: hidden;
        width: 100%;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    .dataframe th {
        background: linear-gradient(90deg, #4b6cb7, #182848);
        color: white;
        padding: 12px;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 14px;
        letter-spacing: 1px;
    }
    
    .dataframe td {
        padding: 12px;
        border-bottom: 1px solid #f0f0f0;
        transition: background-color 0.2s ease;
    }
    
    .dataframe tr:last-child td {
        border-bottom: none;
    }
    
    .dataframe tr:hover td {
        background-color: rgba(74, 0, 224, 0.05);
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background-color: #4A00E0;
        border-radius: 10px;
        height: 8px;
    }
    
    .stProgress > div > div {
        background-color: rgba(74, 0, 224, 0.2);
        border-radius: 10px;
        height: 8px;
    }
    
    /* Sidebar styling */
    .css-1v3fvcr {
        background: linear-gradient(180deg, #1a1a2e, #16213e);
    }
    
    /* Markdown content */
    h2, h3, h4 {
        color: #16213e;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    p, li {
        font-size: 16px;
        line-height: 1.6;
    }
    
    /* Custom animated info boxes */
    .stInfo {
        background: linear-gradient(90deg, rgba(33, 150, 243, 0.1), rgba(33, 150, 243, 0.2));
        border-left: 5px solid #2196F3;
        padding: 20px;
        border-radius: 10px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(33, 150, 243, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(33, 150, 243, 0); }
        100% { box-shadow: 0 0 0 0 rgba(33, 150, 243, 0); }
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #8E2DE2, #4A00E0);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #4A00E0, #8E2DE2);
    }
</style>
""", unsafe_allow_html=True)

# Set environment variables
def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

# Initialize environment
if 'initialized' not in st.session_state:
    _set_env("GOOGLE_API_KEY")
    st.session_state.initialized = True

# Define SWOT analysis documents for FAISS vector store
swot_documents = [
    # Strengths concepts
    "Strengths in a SWOT analysis represent internal capabilities and advantages that help an organization excel. These include technological innovations, skilled workforce, strong brand reputation, efficient processes, and financial resources.",
    "Organizational strengths can be identified through digital transformation initiatives, AI-powered systems, automation capabilities, flexible work policies, and a culture that promotes innovation and continuous improvement.",
    "Strategic strengths include market position, competitive advantage, proprietary technology, strong leadership, and effective operational frameworks that deliver consistent results.",
    "Workforce strengths include diverse talent pool, specialized expertise, strong team collaboration, effective leadership, employee engagement, and professional development programs.",
    "Operational strengths may include streamlined processes, quality management systems, efficient supply chain, scalable infrastructure, and adaptable business models that respond quickly to changes.",
    
    # Weaknesses concepts
    "Weaknesses in a SWOT analysis identify internal limitations that may hinder organizational performance. These can include legacy systems, inefficient processes, skill gaps, communication barriers, and resource constraints.",
    "Technical weaknesses often manifest as integration problems between new and old systems, data silos, security vulnerabilities, and inadequate infrastructure to support growth initiatives.",
    "Organizational weaknesses may involve unclear communication channels, resistance to change, hierarchical bottlenecks, insufficient training programs, and gaps in knowledge management.",
    "Financial weaknesses could include high operational costs, limited access to capital, cash flow challenges, or insufficient budget allocation for innovation and research initiatives.",
    "Market-related weaknesses might involve limited product range, gaps in service offerings, inconsistent customer experience, weak market presence, or inadequate distribution channels.",
    
    # Opportunities concepts
    "Opportunities in a SWOT analysis represent external possibilities that an organization can capitalize on. These include emerging markets, technological trends, regulatory changes, competitor weaknesses, and partnership prospects.",
    "Market opportunities involve expansion into international regions, development of new product lines, strategic acquisitions, diversification of supplier networks, and adoption of innovative business models.",
    "Collaborative opportunities include partnerships with technology startups, academic institutions, industry consortiums, and research organizations to accelerate innovation and market penetration.",
    "Technological opportunities encompass adoption of emerging technologies like AI, machine learning, blockchain, IoT, and cloud computing to enhance product offerings or improve operational efficiency.",
    "Sustainability opportunities include developing eco-friendly products, implementing green manufacturing processes, reducing carbon footprint, and meeting growing consumer demand for responsible business practices.",
    
    # Threats concepts
    "Threats in a SWOT analysis identify external challenges that could negatively impact an organization. These include competitive pressures, changing market dynamics, regulatory constraints, economic downturns, and technological disruptions.",
    "Competitive threats often come from rivals implementing advanced technologies like AI agents, aggressive market strategies, new entrants with disruptive models, and industry consolidation that affects market share.",
    "Environmental threats encompass geopolitical tensions, supply chain disruptions, changing consumer preferences, talent shortages, and cybersecurity risks that could compromise operations.",
    "Regulatory threats include changing compliance requirements, industry standards, data protection laws, trade policies, and environmental regulations that increase operational complexity or costs.",
    "Technological threats involve rapid innovation requiring constant adaptation, obsolescence of current products or systems, cybersecurity vulnerabilities, and disruptive technologies that challenge the business model.",
    
    # SWOT methodology
    "A comprehensive SWOT analysis involves systematic evaluation of internal factors (strengths and weaknesses) and external factors (opportunities and threats) using quantitative and qualitative data from multiple sources.",
    "Effective SWOT analysis requires cross-functional input, objective assessment, prioritization of factors based on impact, and alignment with strategic objectives and organizational vision.",
    "SWOT analysis outcomes should inform strategic planning, resource allocation, risk management, and continuous improvement initiatives to maximize advantages and minimize vulnerabilities.",
    "The SWOT framework should be updated regularly as market conditions change, with continual monitoring of identified factors and emerging trends that could affect the organization.",
    "Advanced SWOT methodologies may include weighted scoring systems, impact-likelihood matrices, and scenario planning to refine strategic responses to identified factors.",
]

# Initialize the RAG components
@st.cache_resource
def initialize_rag():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    faiss_store = FAISS.from_texts(swot_documents, embeddings)
    retriever = faiss_store.as_retriever(search_kwargs={"k": 7})
    
    # Create a custom prompt template for SWOT analysis
    prompt_template = """
    You are an expert business analyst specializing in conducting comprehensive SWOT analyses.
    
    Use the following retrieved context information to enhance your analysis:
    {context}
    
    Based on the organizational information provided by the user, conduct a detailed and insightful SWOT analysis for:
    {question}
    
    Your analysis must include:
    1. STRENGTHS: Identify 6-8 significant internal capabilities, resources, and advantages. Be specific about technological advantages, workforce strengths, operational efficiencies, and strategic assets.
    
    2. WEAKNESSES: Identify 6-8 critical internal limitations and challenges. Be detailed about organizational barriers, resource constraints, process inefficiencies, and capability gaps.
    
    3. OPPORTUNITIES: Analyze 6-8 promising external possibilities that could be capitalized upon. Identify market openings, technological trends, partnership possibilities, and emerging customer needs.
    
    4. THREATS: Identify 6-8 substantial external challenges that could negatively impact the organization. Cover competitive pressures, industry disruptions, regulatory changes, and environmental factors.
    
    For each item, provide 2-3 sentences of explanation that includes specific examples and potential impact. Format your response in markdown with clear headings for each SWOT component. Use bullet points for each item.
    
    Be creative, insightful, and specific. Avoid generic statements. Your analysis should provide actionable insights that could genuinely help the organization's strategic planning.
    """
    
    PROMPT = PromptTemplate(
        template=prompt_template, 
        input_variables=["context", "question"]
    )
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-latest",
        temperature=0.7,  # Increased temperature for more creative responses
        max_tokens=2000
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return qa_chain

# Function to generate SWOT analysis
def generate_swot_analysis(org_info, qa_chain):
    response = qa_chain.run(org_info)
    return response

# Function to extract SWOT components from analysis text
def extract_swot_components(analysis_text):
    sections = {
        "strengths": [],
        "weaknesses": [],
        "opportunities": [],
        "threats": []
    }
    
    current_section = None
    
    # Split the text into lines
    lines = analysis_text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers (more flexible pattern matching)
        if 'STRENGTHS' in line.upper():
            current_section = "strengths"
        elif 'WEAKNESSES' in line.upper():
            current_section = "weaknesses"
        elif 'OPPORTUNITIES' in line.upper():
            current_section = "opportunities"
        elif 'THREATS' in line.upper():
            current_section = "threats"
        
        # Add content to current section if we're in a section and line has content
        elif current_section and line:
            # Check for bullet points with more patterns
            if (line.startswith('- ') or line.startswith('* ') or 
                (len(line) > 1 and line[0].isdigit() and line[1:3] in ['. ', ') ']) or
                line.startswith('•')):
                
                # Extract the full bullet point with its description
                full_point = line
                
                # Look ahead for continuation lines (indented or part of same bullet)
                j = i + 1
                while j < len(lines) and j < i + 5:  # Look up to 5 lines ahead
                    next_line = lines[j].strip()
                    
                    # Stop if we hit another bullet or section header
                    if (next_line.startswith('- ') or next_line.startswith('* ') or 
                        (len(next_line) > 1 and next_line[0].isdigit() and next_line[1:3] in ['. ', ') ']) or
                        next_line.startswith('•') or
                        any(header in next_line.upper() for header in ['STRENGTHS', 'WEAKNESSES', 'OPPORTUNITIES', 'THREATS'])):
                        break
                    
                    # If not empty and not a separator, add it to the current bullet point
                    if next_line and not next_line == '---':
                        full_point += " " + next_line
                        j += 1
                    else:
                        j += 1
                        continue
                
                sections[current_section].append(full_point)
        
        i += 1
    
    # Fallback: If no components were extracted, try to extract at least something
    if all(len(items) == 0 for items in sections.values()):
        # Simple fallback extraction for each section
        for section_name in ["strengths", "weaknesses", "opportunities", "threats"]:
            section_start = analysis_text.upper().find(section_name.upper())
            if section_start != -1:
                # Find the next section or end of text
                next_sections = [analysis_text.upper().find(other.upper()) for other in ["WEAKNESSES", "OPPORTUNITIES", "THREATS"] 
                                if analysis_text.upper().find(other.upper()) > section_start]
                section_end = min(next_sections) if next_sections else len(analysis_text)
                
                # Extract section content
                section_content = analysis_text[section_start:section_end]
                
                # Look for bullet points or numbered items
                for line in section_content.split('\n'):
                    line = line.strip()
                    if (line.startswith('- ') or line.startswith('* ') or 
                        (len(line) > 1 and line[0].isdigit() and line[1:3] in ['. ', ') ']) or
                        line.startswith('•')):
                        sections[section_name].append(line)
    
    # If still empty, create placeholders to avoid zero values in charts
    for section_name in sections:
        if not sections[section_name]:
            for i in range(1, 7):  # Add 6 placeholder items
                sections[section_name].append(f"- {section_name.title()} {i}")
    
    return sections

# Function to create visualization for SWOT analysis
def create_swot_visualization(swot_components):
    # Count the number of items in each component
    counts = {
        "Strengths": len(swot_components["strengths"]),
        "Weaknesses": len(swot_components["weaknesses"]),
        "Opportunities": len(swot_components["opportunities"]),
        "Threats": len(swot_components["threats"])
    }
    
    # Create radar chart
    categories = list(counts.keys())
    values = list(counts.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='SWOT Components',
        line_color='#4b6cb7',
        fillcolor='rgba(75, 108, 183, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) + 2]
            )
        ),
        showlegend=False,
        title="SWOT Analysis Overview",
        title_font_size=20,
        height=450,
        width=450,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    return fig

# Function to create bar chart for SWOT components
def create_swot_bar_chart(swot_components):
    # Count the number of items in each component
    counts = {
        "Strengths": len(swot_components["strengths"]),
        "Weaknesses": len(swot_components["weaknesses"]),
        "Opportunities": len(swot_components["opportunities"]),
        "Threats": len(swot_components["threats"])
    }
    
    # Define colors for each category
    colors = {
        "Strengths": "#4CAF50",
        "Weaknesses": "#F44336",
        "Opportunities": "#2196F3",
        "Threats": "#FF9800"
    }
    
    # Create bar chart
    fig = go.Figure()
    
    for category, count in counts.items():
        fig.add_trace(go.Bar(
            x=[category],
            y=[count],
            name=category,
            marker_color=colors[category],
            text=[count],
            textposition='auto'
        ))
    
    fig.update_layout(
        title="SWOT Components Distribution",
        title_font_size=20,
        height=450,
        width=450,
        margin=dict(l=50, r=50, t=100, b=50),
        yaxis=dict(title='Number of Items'),
        showlegend=False
    )
    
    return fig

# Sidebar with app information
with st.sidebar:
    # Enhanced title with icon and styling
    st.markdown("""
    <div style="background: linear-gradient(90deg, #8E2DE2, #4A00E0); 
                padding: 15px; 
                border-radius: 10px; 
                margin-bottom: 20px;
                box-shadow: 0 4px 12px rgba(142, 45, 226, 0.3);">
        <h1 style="color: white; 
                  margin: 0; 
                  text-align: center; 
                  font-size: 1.8rem;
                  text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
            🔍 SWOT Analysis Tool
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Tool description in a glass-morphism card
    st.markdown("""
    <div style="background: rgba(255, 255, 255, 0.1); 
                backdrop-filter: blur(5px); 
                padding: 15px; 
                border-radius: 10px; 
                border-left: 4px solid #4A00E0;
                margin-bottom: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
        <p style="margin: 0;">This tool helps organizations conduct comprehensive SWOT analyses using advanced AI techniques.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key features with animated icons
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(74, 0, 224, 0.05), rgba(142, 45, 226, 0.1)); 
                padding: 15px; 
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);">
        <h3 style="color: #4A00E0; 
                  margin-top: 0;
                  font-size: 1.2rem;
                  border-bottom: 2px solid rgba(74, 0, 224, 0.2);
                  padding-bottom: 8px;">
            <span style="display: inline-block; animation: pulse 2s infinite;">✨</span> Key Features
        </h3>
        <ul style="list-style-type: none; padding-left: 5px;">
            <li style="margin-bottom: 8px; display: flex; align-items: center;">
                <span style="color: #4A00E0; margin-right: 10px;">🤖</span> AI-powered SWOT analysis generation
            </li>
            <li style="margin-bottom: 8px; display: flex; align-items: center;">
                <span style="color: #4A00E0; margin-right: 10px;">🔄</span> Vector-based concept retrieval using FAISS
            </li>
            <li style="margin-bottom: 8px; display: flex; align-items: center;">
                <span style="color: #4A00E0; margin-right: 10px;">💎</span> Powered by Gemini 1.5 Pro
            </li>
            <li style="margin-bottom: 8px; display: flex; align-items: center;">
                <span style="color: #4A00E0; margin-right: 10px;">📊</span> Interactive visualization of results
            </li>
            <li style="margin-bottom: 8px; display: flex; align-items: center;">
                <span style="color: #4A00E0; margin-right: 10px;">📋</span> Detailed breakdown of all SWOT components
            </li>
        </ul>
        <p style="font-style: italic; 
                 text-align: center; 
                 margin-top: 15px;
                 font-size: 0.9rem;
                 color: #666;">
            <span style="display: inline-block; animation: float 3s ease-in-out infinite;">🛠️</span> Built with LangChain, FAISS, Streamlit, and Google Generative AI
        </p>
    </div>
    
    <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
            100% { transform: translateY(0px); }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.subheader("Sample Organizations")
    
    sample_orgs = {
        "Tech Startup - AI Solutions": """
            TechMinds is a 3-year-old tech startup with 50 employees focused on AI-driven customer service solutions. 
            They've developed proprietary NLP algorithms that can understand customer sentiment with 92% accuracy and 
            resolve common inquiries without human intervention. Their engineering team consists of 30 PhD-level AI 
            specialists from top universities, but their marketing department has only 5 employees with limited budget.
            
            Their flagship product "CustomerAI" has gained 120% user growth over the past year in the North American 
            market, with particularly strong adoption in fintech and e-commerce sectors. They've secured $8.5M in 
            Series A funding and have a runway of approximately 18 months.
            
            Current challenges include scaling their infrastructure to meet growing demand, addressing data privacy 
            concerns from potential European clients, and competing against established CRM giants who are rapidly 
            developing their own AI capabilities. Their customer acquisition cost is currently $15,000, which is 
            higher than industry average, and their sales cycle averages 3-4 months.
            
            They're considering strategic partnerships with larger CRM providers, exploring international expansion, 
            and debating whether to diversify into adjacent markets like HR automation or remain focused on customer 
            service solutions.
        """,
        
        "Healthcare Network - Regional Provider": """
            HealthBridge Network is a regional healthcare system operating for 45 years with 5 hospitals, 20 clinics, 
            and over 8,000 employees serving a population of approximately 2 million people across three states. They're 
            currently implementing a $45M electronic health records system and expanding telemedicine services, which grew 
            350% during the pandemic.
            
            Their workforce demographics show challenges with 35% of nurses and 28% of physicians approaching retirement 
            age within 5 years. Their main hospital facilities average 32 years in age, with two requiring significant 
            infrastructure upgrades estimated at $95M. Their patient satisfaction scores have consistently remained 
            above regional averages (4.2/5 vs 3.8/5), and they maintain strong relationships with community organizations 
            through their outreach programs that serve 50,000+ underinsured residents annually.
            
            Regulatory compliance costs have increased 23% in the past two years, while insurance reimbursement rates 
            have only increased 4%. They face growing competition from three urgent care chains and a new specialty 
            surgical center in their primary service area. Their rural clinics struggle with staffing and technological 
            limitations, with broadband access issues affecting telemedicine implementation in 35% of their service area.
            
            They're evaluating potential mergers with complementary healthcare networks, considering specialized service 
            lines in oncology and cardiology to increase market differentiation, and exploring innovative payment models 
            with major employers in the region to establish direct service contracts.
        """,
        
        "ManufacturingPlus - Industrial Equipment": """
            ManufacturingPlus is a 72-year-old industrial equipment manufacturer with 1,200 employees across 4 production 
            facilities and global distribution to 43 countries. Annual revenue is $280M with EBITDA margins declining 
            from 18% to 14% over the past three years due to increased material costs and competitive pricing pressures.
            
            They've recently invested $35M in automation technology that reduced production time by 40% and defect rates 
            by 65%, but required retraining 30% of their workforce. Their R&D department (45 engineers) has developed 
            17 patents in the past decade, though their innovation rate lags behind key competitors. Customer retention 
            remains strong at 85% for clients over 5+ years, but new customer acquisition has slowed to 3% annual growth.
            
            Supply chain disruptions have increased lead times from 45 to 72 days, causing customer satisfaction to drop 
            11 percentage points. Three major competitors have emerged from Asian markets with pricing 25-30% lower than 
            ManufacturingPlus, though with quality metrics that score 20% lower in independent testing.
            
            Environmental regulations in their primary markets are expected to tighten significantly in the next 18 months, 
            requiring capital investments estimated at $18-22M. The executive team is divided on whether to pursue 
            geographical expansion into emerging markets, increase customization capabilities to differentiate from 
            lower-cost competitors, or diversify into service-based revenue streams through predictive maintenance offerings 
            and equipment-as-a-service models.
        """,
        
        "TechEd Solutions - Educational Technology": """
            TechEd Solutions is an 8-year-old educational technology company with 175 employees that provides interactive 
            learning platforms to K-12 schools, universities, and corporate training departments. Their flagship product 
            suite includes adaptive learning algorithms that personalize content delivery based on individual learning 
            patterns, which has shown to improve knowledge retention by 47% in controlled studies.
            
            The company experienced 215% revenue growth during the pandemic as remote learning became essential, but growth 
            has stabilized at 28% annually as schools return to hybrid models. Their current customer base includes 1,350 
            educational institutions serving approximately 2.1 million students. Their development team has strong expertise 
            in gamification and learning science with 70% of technical staff holding advanced degrees in relevant fields.
            
            Recent challenges include integrating their platform with legacy school management systems (requiring 35% of 
            development resources), addressing growing data privacy concerns from parents' groups and regulators, and 
            managing the 3.5x increase in server capacity needed during peak usage periods. Customer acquisition costs 
            have risen from $8,500 to $12,700 per institution due to longer sales cycles in public education (averaging 
            7-9 months).
            
            The company is evaluating strategic directions including expanding into international English-speaking markets, 
            developing specialized content for STEM education, creating standalone consumer products for homeschooling 
            families, and exploring potential acquisition targets among content creation companies to vertically integrate 
            their offering.
        """,
        
        "NovaEdge Industries - Digital Transformation": """
            NovaEdge Industries is a 25-year-old manufacturing conglomerate with 3,800 employees across 7 production facilities and 12 distribution centers generating $750M in annual revenue. They're undergoing comprehensive digital transformation to address efficiency challenges and competitive pressures, having allocated $85M over three years for modernization efforts.
            They've implemented AI-powered quality control systems that reduced defect rates by 78% and predictive maintenance algorithms that decreased downtime by 42%. Their flexible work policy implementation for non-production staff (approximately 1,200 employees) has improved retention by 23% and expanded their talent recruitment geography. Four innovation labs established across different divisions have generated 28 potential product improvements, with 12 already in implementation phases.
            Significant challenges include legacy systems integration, with 65% of their technology infrastructure being over 10 years old and requiring complex middleware solutions. Interdepartmental communication remains siloed, with satisfaction surveys showing only 37% of employees feel information flows effectively between divisions. Competition has intensified with three major rivals adopting similar digital transformation initiatives and two new market entrants utilizing completely cloud-native, AI-first approaches to manufacturing.
            Strategic considerations include potential expansion into Southeast Asian markets where demand is projected to grow 38% over five years, establishing technology partnerships with 3-5 carefully selected startups for accelerated innovation, and addressing regulatory changes expected in their primary markets that will increase compliance reporting requirements by an estimated 200+ hours per month. Supply chain vulnerabilities exposed during recent global disruptions showed critical dependencies on single-source suppliers for 23% of essential components.
        """,
        
        "EcoRetail - Sustainable Consumer Goods": """
            EcoRetail is a 6-year-old sustainable consumer goods company with 210 employees that designs, manufactures, and 
            sells eco-friendly household products through 1,200+ retail partners and their own e-commerce platform. Their 
            product line includes 78 items across cleaning supplies, personal care, and home essentials, all using plastic-free 
            packaging and biodegradable formulations.
            
            The company has achieved 65% year-over-year growth for three consecutive years, with current annual revenue of $42M. 
            Their social media presence has grown organically to 2.8M followers across platforms, providing marketing reach at 
            30% of the cost of traditional advertising. Their dedicated sustainability team has secured third-party certifications 
            for carbon neutrality, fair trade sourcing, and non-toxic ingredients for the entire product catalog.
            
            Challenges include managing rapid growth while maintaining product quality, with recent expansion straining their 
            quality control systems and resulting in a 3% return rate (up from 1.2%). Supply chain complexities for specialized 
            sustainable materials have caused stockouts on 14 popular products during peak seasons. Price points average 15-30% 
            higher than conventional alternatives, creating adoption barriers in more price-sensitive market segments.
            
            Several major conventional consumer goods companies have launched competing "green" product lines with significantly 
            larger marketing budgets, though independent testing has shown many competitors' products contain less sustainable 
            ingredients. The regulatory landscape is evolving favorably with several states introducing legislation that would 
            require improved environmental disclosures that would benefit EcoRetail's transparent practices.
            
            Strategic options under consideration include expanding production capacity through a new manufacturing facility, 
            developing subscription models to improve customer retention and predictable revenue, exploring international markets 
            starting with Canada and the UK, and potentially raising Series B funding to accelerate growth before larger competitors 
            can capture market share.
        """
    }
    
    # Create buttons for sample organizations with relevant icons
    for org_name, org_desc in sample_orgs.items():
        # Assign custom icons based on organization type
        if "Tech Startup" in org_name:
            icon = "🤖"  # Robot/AI icon for tech startup
        elif "Healthcare" in org_name:
            icon = "🏥"  # Hospital icon for healthcare
        elif "Manufacturing" in org_name:
            icon = "🏭"  # Factory icon for manufacturing
        elif "Educational" in org_name:
            icon = "🎓"  # Graduation cap for educational technology
        elif "Digital Transformation" in org_name:
            icon = "💻"  # Computer icon for digital transformation
        elif "Consumer Goods" in org_name or "Retail" in org_name:
            icon = "🛒"  # Shopping cart for retail/consumer goods
        else:
            icon = "🏢"  # Default office building icon
            
        if st.button(f"{icon} {org_name}", key=org_name):
            st.session_state.org_info = org_desc

# Main content
st.markdown("<div class='title-container'><h1>SWOT Analysis Generator</h1><p>Powered by RAG & Gemini 1.5 Pro</p></div>", unsafe_allow_html=True)

# Input container
st.markdown("<div class='search-container'>", unsafe_allow_html=True)

# Add tabs for text input and file upload
input_tab, upload_tab = st.tabs(["Text Input", "File Upload"])

with input_tab:
    org_info = st.text_area(
        "Provide information about your organization:",
        height=200,
        value=st.session_state.get('org_info', ''),
        placeholder="Enter detailed information about your organization including operations, market position, challenges, strengths, etc."
    )

with upload_tab:
    uploaded_file = st.file_uploader("Upload organization information document (TXT, PDF, DOCX)", type=["txt", "pdf", "docx"])
    if uploaded_file is not None:
        # For simplicity, only handling text files in this example
        # In a real application, you would add PDF and DOCX processing
        if uploaded_file.type == "text/plain":
            org_info = uploaded_file.getvalue().decode("utf-8")
            st.session_state.org_info = org_info
        else:
            st.info("PDF and DOCX processing would be implemented in a full application. For now, please use text input.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate_button = st.button("🔍 Generate SWOT Analysis", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Initialize the RAG system
qa_chain = initialize_rag()

# Process query
if generate_button or (org_info and st.session_state.get('org_info') != org_info):
    st.session_state.org_info = org_info
    if org_info:
        with st.spinner("Analyzing organization information..."):
            # Add a slight delay and animation for better UX
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # Generate SWOT analysis
            swot_analysis = generate_swot_analysis(org_info, qa_chain)
            st.session_state.swot_analysis = swot_analysis
            
            # Extract SWOT components for visualization
            swot_components = extract_swot_components(swot_analysis)
            st.session_state.swot_components = swot_components
            
            # Display success message
            st.success("SWOT Analysis generated successfully!")

# Display results if available
if st.session_state.get('swot_analysis'):
    # Create tabs for viewing analysis
    overview_tab, detailed_tab, visual_tab = st.tabs(["Overview", "Detailed Analysis", "Visualizations"])
    
    with overview_tab:
        # Get components from session state
        swot_components = st.session_state.get('swot_components', {
            "strengths": [],
            "weaknesses": [],
            "opportunities": [],
            "threats": []
        })
        
        # Display SWOT grid with components
        st.markdown("## SWOT Analysis Overview")
        
        # Create a 2x2 grid for SWOT components
        col1, col2 = st.columns(2)
        
        with col1:
            # Strengths
            st.markdown("<div class='result-card strengths'>", unsafe_allow_html=True)
            st.markdown("### 💪 Strengths")
            if swot_components["strengths"]:
                for item in swot_components["strengths"][:3]:  # Show only top 3 for overview
                    st.markdown(f"{item}")
                if len(swot_components["strengths"]) > 3:
                    st.markdown(f"*...and {len(swot_components['strengths']) - 3} more*")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Opportunities
            st.markdown("<div class='result-card opportunities'>", unsafe_allow_html=True)
            st.markdown("### 🚀 Opportunities")
            if swot_components["opportunities"]:
                for item in swot_components["opportunities"][:3]:  # Show only top 3 for overview
                    st.markdown(f"{item}")
                if len(swot_components["opportunities"]) > 3:
                    st.markdown(f"*...and {len(swot_components['opportunities']) - 3} more*")
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col2:
            # Weaknesses
            st.markdown("<div class='result-card weaknesses'>", unsafe_allow_html=True)
            st.markdown("### 🔍 Weaknesses")
            if swot_components["weaknesses"]:
                for item in swot_components["weaknesses"][:3]:  # Show only top 3 for overview
                    st.markdown(f"{item}")
                if len(swot_components["weaknesses"]) > 3:
                    st.markdown(f"*...and {len(swot_components['weaknesses']) - 3} more*")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Threats
            st.markdown("<div class='result-card threats'>", unsafe_allow_html=True)
            st.markdown("### ⚠️ Threats")
            if swot_components["threats"]:
                for item in swot_components["threats"][:3]:  # Show only top 3 for overview
                    st.markdown(f"{item}")
                if len(swot_components["threats"]) > 3:
                    st.markdown(f"*...and {len(swot_components['threats']) - 3} more*")
            st.markdown("</div>", unsafe_allow_html=True)
    
    with detailed_tab:
        # Display full SWOT analysis
        st.markdown("## Complete SWOT Analysis")
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(st.session_state.swot_analysis)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with visual_tab:
        # Display visualizations
        st.markdown("## SWOT Analysis Visualizations")
        
        # Create two columns for visualizations
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Radar chart
            radar_fig = create_swot_visualization(st.session_state.swot_components)
            st.plotly_chart(radar_fig)
        
        with viz_col2:
            # Bar chart
            bar_fig = create_swot_bar_chart(st.session_state.swot_components)
            st.plotly_chart(bar_fig)
        
        # Add a description of the visualizations
        st.markdown("""
        The visualizations above provide a quick overview of your SWOT analysis:
        
        - **Radar Chart**: Shows the balance between different SWOT components. A well-rounded shape indicates balanced coverage across all areas.
        - **Bar Chart**: Highlights the number of items identified in each category, helping you identify areas that may need more attention.
        
        A comprehensive SWOT analysis typically has a balanced distribution of elements across all four categories.
        """)


# Adding a section to display library versions
def display_version_info():
    # Create a collapsible section for version information
    with st.expander("System Information", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            
            st.text(f"Python: {sys.version.split()[0]}")
            st.text(f"Streamlit: {st.__version__}")
        
        with col2:
            st.write("**Libraries:**")
            st.text(f"LangChain: {__import__('langchain').__version__}")
            # st.text(f"LangChain Google GenAI: {__import__('langchain_google_genai').__version__}")
            st.text(f"FAISS: {__import__('faiss').__version__}")
            st.text(f"PyPDF2: {__import__('PyPDF2').__version__}")
            st.text(f"Docx: {docx.__version__}")

display_version_info()     