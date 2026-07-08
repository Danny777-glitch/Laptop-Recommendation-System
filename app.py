import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Laptop Recommendation System", page_icon="💻", layout="wide")

st.markdown("""
    <style>
    .block-container { padding-top: 2.5rem !important; padding-bottom: 0rem !important; }
    .main { background-color: #f8f9fa; }
    
    div[data-testid="stSlider"] { margin-bottom: -10px !important; padding-bottom: 0px !important; }
    div[data-testid="stSelectbox"] { margin-bottom: -10px !important; padding-bottom: 0px !important; }
    div[data-testid="stHorizontalBlock"] { gap: 1rem !important; margin-bottom: -5px !important; }
    
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 6px;
        margin-top: 5px !important;
    }
    .stButton>button:hover { background-color: #FF1493; color: white; }
    
    .card, .top-card {
        padding: 8px 16px !important;
        border-radius: 10px;
        box-shadow: 0 3px 5px rgba(0,0,0,0.04);
        margin-bottom: 6px !important;
    }
    .card { background-color: white; border-left: 5px solid #FF69B4; }
    .top-card {
        background-color: #FFF0F5;
        border-left: 5px solid #FF1493;
        box-shadow: 0 3px 8px rgba(255, 105, 180, 0.12);
    }
    
    div[data-testid="stMarkdown"] div p { margin-bottom: 0px !important; }
    h2, h3, p { margin: 0 !important; padding: 0 !important; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("datasets/laptops_Featured.csv")

df = load_data()
artifacts = joblib.load("models/model_artifacts.joblib")

model = artifacts["model"]
label_encoders = artifacts["label_encoders"]
feature_columns = artifacts["feature_columns"]

st.markdown("<h2 style='text-align: center; color: #FF69B4; margin: 0; padding: 0; font-size: 26px; font-weight: bold;'>💻 AI-Powered Laptop Expert</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #C71585; margin: 2px 0 8px 0 !important; font-size: 13px; font-weight: 600;'>Find the absolute best hardware match calibrated by XGBoost ML inference</p>", unsafe_allow_html=True)

st.markdown("<h4 style='margin-bottom: 2px !important; font-size: 14px; color: #3A3B3C; font-weight: 800;'>🛠️ Configure Your Preferences</h4>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    cpu_score = st.slider("Target CPU Capability", 1, 10, 8)
    gpu_score = st.slider("Target GPU Capability", 1, 10, 7)

with col2:
    ram_gb = st.selectbox("System RAM Layout", sorted(df["RAM_GB"].dropna().unique()))
    storage_gb = st.selectbox("SSD Storage Capacity", sorted(df["Storage_GB"].dropna().unique()))

with col3:
    refresh_hz = st.selectbox("Display Refresh Rate", sorted(df["Refresh_Hz"].dropna().unique()))
    resolution_score = st.selectbox("Screen Resolution Tier", sorted(df["Resolution_Score"].dropna().unique()))

if st.button("🚀 Analyze & Recommend Best Matches"):
    
    user_input = pd.DataFrame([{
        "Brand": 0,
        "CPU_Score": cpu_score,
        "GPU_Score": gpu_score,
        "RAM_GB": ram_gb,
        "Storage_GB": storage_gb,
        "Refresh_Hz": refresh_hz,
        "Resolution_Score": resolution_score
    }])

    predicted_score = model.predict(user_input)[0]

    result = df.copy()
    result["Difference"] = abs(result["Performance_Score"] - predicted_score)
    result = result.sort_values(by="Difference").head(3)

    st.markdown("<hr style='margin: 6px 0; border: none; border-top: 1px dashed #ddd;'/>", unsafe_allow_html=True)
    
    m1, m2 = st.columns(2)
    with m1:
        st.markdown(f"📊 **Estimated Performance Rating:** <span style='color:#FF1493; font-weight:bold; font-size:15px;'>{predicted_score:.2f} / 100</span>", unsafe_allow_html=True)
    with m2:
        st.markdown("🎯 **Curated Matches Found:** <span style='color:#C71585; font-weight:bold; font-size:15px;'>Top 3 Alternatives</span>", unsafe_allow_html=True)

    st.markdown("<h4 style='margin-top: 4px !important; margin-bottom: 4px !important; font-size: 14px; font-weight: bold; color: #3A3B3C;'>🏆 Top Recommended Systems For You</h4>", unsafe_allow_html=True)

    for idx, (_, row) in enumerate(result.iterrows()):
        card_style = "top-card" if idx == 0 else "card"
        medal = "🥇 Best Match" if idx == 0 else "🥈 Runner Up" if idx == 1 else "🥉 Alternative Match"
        
        laptop_name = "Laptop System Model"
        for col in row.index:
            if "product" in col.lower() or "name" in col.lower() or "model" in col.lower():
                laptop_name = str(row[col])
                break
        
        brand_name = "Unknown Brand"
        for col in row.index:
            if "brand" in col.lower():
                brand_name = str(row[col])
                break

        st.markdown(f"""
            <div class="{card_style}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px;">
                    <span style="background-color: #FF69B4; color: white; padding: 2px 8px; border-radius: 20px; font-size: 11px; font-weight: bold; display: inline-block;">{medal}</span>
                    <h3 style="margin: 0 !important; padding: 0 !important; color: #222; font-size: 19px; font-weight: 900;">Streamlit Output: ₹{int(row['Price']):,}</h3>
                </div>
                <h2 style="margin: 4px 0 !important; font-size: 17px; font-weight: bold; color: #111; line-height: 1.2;">{laptop_name}</h2>
                <p style="color: #555; font-size: 13px; margin: 2px 0 6px 0 !important;"><b>Brand:</b> {brand_name} | <b>Engineered Performance Score:</b> {row['Performance_Score']:.1f}/100</p>
                <hr style="margin: 4px 0; border: none; border-top: 1px solid #eee; padding: 0;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px; font-size: 13px; color: #333; font-weight: bold;">
                    <div>🧠 <b>Processor:</b> {row['Processor']}</div>
                    <div>🎮 <b>Graphics Core:</b> {row['GPU']}</div>
                    <div>⚡ <b>Memory:</b> {row['RAM']}</div>
                    <div>🗄️ <b>Storage Drive:</b> {row['Storage']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)