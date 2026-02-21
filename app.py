import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="S",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 50px 20px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.4);
        margin-bottom: 30px;
    }
    
    .main-header h1 {
        font-size: 2.8em;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        font-weight: 800;
        letter-spacing: 1px;
    }
    
    .main-header p {
        font-size: 1.1em;
        margin-top: 15px;
        opacity: 0.95;
        font-weight: 500;
    }
    
    .welcome-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 35px 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.3);
        margin: 20px 0;
    }
    
    .welcome-box h3 {
        font-size: 1.5em;
        margin-bottom: 12px;
        font-weight: 700;
    }
    
    .welcome-box p {
        font-size: 1em;
        line-height: 1.6;
        opacity: 0.98;
    }
    
    .detector-box {
        background: linear-gradient(135deg, #f0f4ff 0%, #e8f4f8 100%);
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.15);
    }
    
    .detector-box h4 {
        color: #667eea;
        margin-bottom: 12px;
        font-weight: 700;
    }
    
    .detector-box p {
        color: #333;
        line-height: 1.6;
    }
    
    .model-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e0e8ff;
        margin: 15px 0;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.1);
        transition: all 0.3s ease;
    }
    
    .model-card:hover {
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.2);
        border-color: #667eea;
        transform: translateY(-2px);
    }
    
    .model-card h4 {
        color: #667eea;
        margin-bottom: 12px;
        font-weight: 700;
        font-size: 1.15em;
    }
    
    .model-card p, .model-card li {
        color: #555;
        line-height: 1.7;
        font-size: 0.95em;
    }
    
    .model-card ul {
        margin-left: 20px;
        margin-top: 10px;
    }
    
    .stMetricValue {
        font-size: 2.5em !important;
        font-weight: 800 !important;
    }
    
    .stMetricDelta {
        font-size: 1em !important;
    }
    
    .success-box {
        background: #d4edda !important;
        border: 2px solid #28a745 !important;
        border-radius: 10px;
        padding: 20px !important;
        color: #155724;
    }
    
    .warning-box {
        background: #f8d7da !important;
        border: 2px solid #dc3545 !important;
        border-radius: 10px;
        padding: 20px !important;
        color: #721c24;
    }
    
    .info-tip {
        background: #e8f4f8 !important;
        border: 3px solid #667eea !important;
        border-radius: 10px;
        padding: 20px !important;
        color: #333;
    }
    
    .info-tip h4 {
        color: #667eea;
        font-weight: 700;
        margin-bottom: 12px;
    }
    
    .info-tip ul {
        margin-left: 20px;
    }
    
    .info-tip li {
        margin: 8px 0;
        font-weight: 500;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 20px;
        background-color: #f0f4ff !important;
        border-radius: 8px 8px 0 0;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #667eea !important;
        color: white !important;
    }
    
    hr {
        border: 1px solid #e0e8ff !important;
        margin: 20px 0 !important;
    }
    
    </style>
""", unsafe_allow_html=True)

# Welcome Section
st.markdown("""
    <div class="main-header">
        <h1>🛡️ Phishing Website Detection System</h1>
        <p>⚡ Powered by Machine Learning | By Kumar Aryan</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("")  # spacing

# Welcome Info Boxes
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Accuracy", "99.06%", "Random Forest")
with col2:
    st.metric("Websites Analyzed", "26,584", "Total Dataset")
with col3:
    st.metric("ML Models", "7", "Different Models")

st.markdown("")  # spacing

# Main Description
st.markdown("""
    <div class="welcome-box">
        <h3>🎯 Welcome to Your Phishing Detection Assistant!</h3>
        <p>This advanced <b>Machine Learning</b> application detects phishing websites by analyzing their <b>HTML content</b> - not just the URL. 
        Simply enter any website URL and our AI will determine if it's <b>legitimate</b> or <b>potentially phishing</b>.</p>
    </div>
""", unsafe_allow_html=True)


st.divider()

# Create Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Detector", "About Project", "Model Performance", "Features"])

# ========== TAB 1: PHISHING DETECTOR ==========
with tab1:
    st.markdown("### 🚨 Phishing Website Detector")
    
    detector_col1, detector_col2 = st.columns([2, 1])
    
    with detector_col1:
        st.markdown("""
            <div class="detector-box">
                <h4>🤖 Select an ML Model</h4>
                <p>Choose which machine learning model you want to use for detection:</p>
            </div>
        """, unsafe_allow_html=True)
        
        choice = st.selectbox(
            "Select Model:",
            [
                'Random Forest (Recommended - 99.06%)',
                'Decision Tree (98.43%)',
                'K-Neighbours (97.84%)',
                'AdaBoost (97.78%)',
                'Support Vector Machine (97.78%)',
                'Neural Network (97.61%)',
                'Gaussian Naive Bayes (49.25%)'
            ],
            help="Choose the model based on your preference"
        )
        
        # Model Selection Logic
        model_mapping = {
            'Random Forest (Recommended - 99.06%)': ml.rf_model,
            'Decision Tree (98.43%)': ml.dt_model,
            'K-Neighbours (97.84%)': ml.kn_model,
            'AdaBoost (97.78%)': ml.ab_model,
            'Support Vector Machine (97.78%)': ml.svm_model,
            'Neural Network (97.61%)': ml.nn_model,
            'Gaussian Naive Bayes (49.25%)': ml.nb_model
        }
        
        model = model_mapping.get(choice, ml.rf_model)
        st.info(f"✓ {choice.split('(')[0]} model is selected!")
        
    with detector_col2:
        st.markdown("""
            <div class="info-tip">
                <h4>💡 Model Selection Tips:</h4>
                <ul>
                    <li><b>🌟 Random Forest</b> - Best overall (99.06%)</li>
                    <li><b>⚡ Decision Tree</b> - Fast processing (98.43%)</li>
                    <li><b>🧠 Neural Network</b> - Most advanced (97.61%)</li>
                    <li><b>🎯 K-Neighbours</b> - Good accuracy (97.84%)</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # URL Input Section
    st.markdown("### 🌐 Enter Website URL")
    
    url_col1, url_col2 = st.columns([3, 1])
    
    with url_col1:
        url = st.text_input(
            "URL Input:",
            placeholder="https://www.example.com",
            label_visibility="collapsed"
        )
    
    with url_col2:
        check_button = st.button("Check", type="primary", use_container_width=True)
    
    st.divider()
    
    # Detection Logic
    if check_button:
        if not url:
            st.error("Please enter a URL!")
        else:
            with st.spinner("Analyzing website..."):
                try:
                    response = re.get(url, verify=False, timeout=4)
                    if response.status_code != 200:
                        st.error(f"HTTP connection failed. Status code: {response.status_code}")
                    else:
                        soup = BeautifulSoup(response.content, "html.parser")
                        vector = [fe.create_vector(soup)]
                        result = model.predict(vector)
                        
                        if result[0] == 0:
                            st.success("✅ LEGITIMATE WEBSITE")
                            st.markdown("""
                                <div class="success-box">
                                    <h3 style="color: #155724; margin-bottom: 10px;">✅ This website appears to be LEGITIMATE!</h3>
                                    <p style="font-size: 1.05em;">It's safe to proceed with this website.</p>
                                </div>
                            """, unsafe_allow_html=True)
                            st.balloons()
                        else:
                            st.warning("⚠️ POTENTIAL PHISHING WEBSITE")
                            st.markdown("""
                                <div class="warning-box">
                                    <h3 style="color: #721c24; margin-bottom: 10px;">🚨 CAUTION! This website is POTENTIALLY PHISHING!</h3>
                                    <p style="font-size: 1.05em;"><b>Recommendation:</b> Do not enter any personal information or credentials on this website.</p>
                                </div>
                            """, unsafe_allow_html=True)
                            st.snow()
                        
                        # Show Analysis Details
                        with st.expander("📋 Show Detection Details", expanded=False):
                            col_a, col_b, col_c = st.columns(3)
                            with col_a:
                                st.metric("URL", url[:30] + "..." if len(url) > 30 else url)
                            with col_b:
                                st.metric("Model", choice.split('(')[0].strip())
                            with col_c:
                                st.metric("Result", "✅ Legitimate" if result[0] == 0 else "⚠️ Phishing")
                            
                except re.exceptions.RequestException as e:
                    st.error("Connection error: Cannot reach the website")
                    st.info("The website might be offline or not accessible.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

# ========== TAB 2: ABOUT PROJECT ==========
with tab2:
    st.markdown("### 📚 About This Project")
    st.markdown("")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="model-card">
            <h4>🎯 Our Approach</h4>
            <p>This project uses <b>supervised learning</b> to classify phishing and legitimate websites. The approach focuses on <b>content-based features</b> extracted from HTML rather than URL-based features alone.</p>
            <p><b>🛠️ Technology Stack:</b></p>
            <ul style="margin-left: 20px;">
                <li>Python 3.x</li>
                <li>scikit-learn</li>
                <li>BeautifulSoup4</li>
                <li>Streamlit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="model-card">
            <h4>👨‍💻 Creator</h4>
            <p><b>Kumar Aryan</b></p>
            <p>This is an educational project designed to demonstrate machine learning applications in cybersecurity and web safety.</p>
            <p style="margin-top: 15px; font-size: 0.9em; color: #999;">
            ⭐ Star this project on GitHub if you found it useful!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="model-card">
            <h4>📊 Dataset Overview</h4>
            <p><b>Total Websites Analyzed:</b> 26,584</p>
            <p style="margin-top: 8px;"><b>✅ Legitimate Sites:</b> 16,060 (60.4%)</p>
            <p style="margin-top: 8px;"><b>⚠️ Phishing Sites:</b> 10,524 (39.6%)</p>
            <p style="margin-top: 12px; font-size: 0.9em;"><b>📌 Data Sources:</b></p>
            <ul style="margin-left: 20px; font-size: 0.9em;">
                <li>phishtank.org</li>
                <li>tranco-list.eu</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Show Pie Chart
        st.markdown("#### 📈 Dataset Distribution")
        labels = 'Phishing', 'Legitimate'
        phishing_rate = int(ml.phishing_df.shape[0] / (ml.phishing_df.shape[0] + ml.legitimate_df.shape[0]) * 100)
        legitimate_rate = 100 - phishing_rate
        sizes = [phishing_rate, legitimate_rate]
        explode = (0.1, 0)
        fig, ax = plt.subplots(figsize=(8, 6))
        colors = ['#ff6b6b', '#51cf66']
        ax.pie(sizes, explode=explode, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%', colors=colors, textprops={'fontsize': 12, 'weight': 'bold'})
        ax.axis('equal')
        st.pyplot(fig)
    
    with col2:
        st.markdown("""
        <div class="model-card">
            <h4>🔧 Features Analyzed</h4>
            <p>The system analyzes <b>30+ HTML-based features</b> including:</p>
            <ul style="margin-left: 20px; margin-top: 12px;">
                <li><b>🔗 Links & Anchors</b> - External links</li>
                <li><b>📝 Form Elements</b> - Input fields, buttons</li>
                <li><b>🏷️ HTML Tags</b> - Scripts, iframes, media</li>
                <li><b>📋 Page Structure</b> - Titles, headings, text</li>
                <li><b>🔓 Hidden Elements</b> - Suspicious patterns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📥 Download Dataset")
        @st.cache_data
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        
        csv = convert_df(ml.df)
        st.download_button(
            label="📥 Download Full Dataset (CSV)",
            data=csv,
            file_name='phishing_legitimate_data.csv',
            mime='text/csv',
            use_container_width=True
        )

# ========== TAB 3: MODEL PERFORMANCE ==========
with tab3:
    st.markdown("### 📊 ML Model Performance Comparison")
    st.markdown("")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### 🏆 Performance Metrics")
        st.dataframe(ml.df_results, use_container_width=True, hide_index=False)
    
    with col2:
        st.markdown("""
        <div class="model-card">
            <h4>🔑 Model Abbreviations</h4>
            <ul style="margin-left: 15px;">
                <li><b>NB</b> - Naive Bayes</li>
                <li><b>SVM</b> - Support Vector Machine</li>
                <li><b>DT</b> - Decision Tree</li>
                <li><b>RF</b> - Random Forest ⭐</li>
                <li><b>AB</b> - AdaBoost</li>
                <li><b>NN</b> - Neural Network</li>
                <li><b>KN</b> - K-Neighbours</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Show sample data
    st.markdown("#### 📋 Dataset Preview")
    number = st.slider("Select number of rows to display", 5, 50, 10)
    st.dataframe(ml.legitimate_df.head(number), use_container_width=True, hide_index=True)

# ========== TAB 4: FEATURES ==========
with tab4:
    st.markdown("### ℹ️ HTML Features Analyzed")
    st.markdown("")
    
    st.markdown("""
    <div class="model-card">
        <h4>🔍 Content-Based Detection</h4>
        <p>Unlike URL-based detection, this system analyzes the actual HTML content of websites to identify phishing indicators. This approach is more reliable because phishing sites often use legitimate-looking domains with suspicious content.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="model-card">
            <h4>🔗 Link & Navigation</h4>
            <ul style="margin-left: 15px;">
                <li>External links</li>
                <li>Anchor tags</li>
                <li>URL mismatches</li>
                <li>Suspicious domains</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="model-card">
            <h4>📝 Form & Input</h4>
            <ul style="margin-left: 15px;">
                <li>Input fields</li>
                <li>Password fields</li>
                <li>Email inputs</li>
                <li>Submit buttons</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="model-card">
            <h4>📄 Content & Media</h4>
            <ul style="margin-left: 15px;">
                <li>Script tags</li>
                <li>Images & media</li>
                <li>Iframes</li>
                <li>Embedded objects</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Important Info
    st.markdown("### ⚠️ Important Reminders")
    st.warning("""
    🔴 **Phishing websites have SHORT LIFECYCLES** (typically days to weeks)
    
    Always verify suspicious websites with up-to-date security information!
    """)
    
    st.info("""
    ✅ **This tool should be used as a supplementary check**, not as the sole authority for website safety.
    """)
    
    st.markdown("""
    <div class="model-card">
        <h4>🛡️ Additional Security Tips</h4>
        <ul style="margin-left: 15px;">
            <li>Check for HTTPS and valid SSL certificates</li>
            <li>Verify the sender's email address carefully</li>
            <li>Never click links in suspicious emails</li>
            <li>Use browser security extensions</li>
            <li>Report phishing sites to authorities</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("---")
    st.markdown("### � Quick Links")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[📜 GitHub](https://github.com)")
    with col2:
        st.markdown("[📧 Contact](mailto:kumararyan@example.com)")
    
    st.markdown("---")
    
    st.markdown("### ℹ️ About This App")
    st.info("""
    **🛡️ Phishing Website Detection**
    
    Version: 1.0
    
    Powered by Machine Learning
    
    Author: Kumar Aryan
    
    ---
    
    This app uses advanced ML models to detect phishing websites through content analysis.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    st.metric("Dataset Size", "26,584")
    st.metric("Best Accuracy", "99.06%")






