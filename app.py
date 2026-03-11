import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Boda The Ghost | Automation Hub", page_icon="👤", layout="wide")

# تصميم الـ UI باستخدام CSS (Neumorphism & Dark Mode)
st.markdown("""
    <style>
    /* تغيير الخلفية العامة */
    .stApp { background-color: #0b0e14; color: #e0e0e0; }
    
    /* تصميم الـ Cards */
    .tool-card {
        background: #161b22;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #30363d;
        box-shadow: 5px 5px 15px #05070a, -2px -2px 10px #1c2128;
        transition: 0.3s;
        margin-bottom: 20px;
    }
    .tool-card:hover {
        transform: translateY(-5px);
        border-color: #58a6ff;
        box-shadow: 0px 0px 20px rgba(88, 166, 255, 0.2);
    }
    
    /* تصميم أزرار التواصل */
    .social-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px;
        border-radius: 12px;
        text-decoration: none;
        color: white;
        font-weight: bold;
        margin: 10px 0;
        transition: 0.3s;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .social-btn:hover { opacity: 0.8; transform: scale(1.02); }
    
    /* الهيدر */
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#fff, #58a6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<h1 class="main-title">Boda The Ghost</h1>', unsafe_allow_html=True)
st.markdown("### `Marketing Automation Expert & Data Architect`")
st.write("متخصص في بناء الأنظمة الذكية التي تدمج بين قوة البيانات وسرعة الأتمتة لتحقيق أقصى عائد إعلاني.")

st.write("---")

# --- Tools Section (الـ Cards) ---
st.markdown("## 🛠️ Intelligent Modules")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="tool-card">
        <h3 style="color: #58a6ff;">🎯 WhatsApp Validator</h3>
        <p style="color: #8b949e;">أداة متطورة لفحص دقة البيانات وتصفية أرقام الواتساب النشطة باستخدام تقنيات الـ API لضمان وصول حملاتك لوجهتها الصحيحة.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Validator 🚀", key="wa_tool"):
        st.toast("System: Initializing WhatsApp Module...")

with col2:
    st.markdown("""
    <div class="tool-card">
        <h3 style="color: #58a6ff;">📊 Competitor Tracking</h3>
        <p style="color: #8b949e;">نظام مراقبة ذكي يتتبع تحركات المنافسين، الإعلانات النشطة، وتغيرات الأسعار لحظياً لإبقائك دائماً في الصدارة.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Monitor 📈", key="comp_tool"):
        st.toast("System: Fetching Market Data...")

# --- Contact Section ---
st.write("---")
st.markdown("## 🔗 Direct Channels")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<a href="https://wa.me/201118973019" class="social-btn" style="background: #218838;">🟢 WhatsApp Account</a>', unsafe_allow_html=True)

with c2:
    st.markdown('<a href="https://instagram.com/l0gwy" class="social-btn" style="background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);">📸 Instagram: @l0gwy</a>', unsafe_allow_html=True)

with c3:
    st.markdown('<a href="https://facebook.com/boda151" class="social-btn" style="background: #0b84ee;">🔵 Facebook: boda151</a>', unsafe_allow_html=True)

# --- Footer ---
st.sidebar.markdown("### 🛠️ Control Panel")
st.sidebar.info("جميع الأدوات تعمل ببيئة معزولة لضمان خصوصية البيانات.")
st.sidebar.markdown("---")
st.sidebar.write("Developed by: **Boda The Ghost** 💀")
