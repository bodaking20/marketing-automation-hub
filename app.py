import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Boda The Ghost | Full Ecosystem", page_icon="⚡", layout="wide")

# تصميم UI متطور (Glassmorphism & Cyber Glow)
st.markdown("""
    <style>
    /* الخلفية والتنسيق العام */
    .stApp { background: radial-gradient(circle at top right, #1a1f2c, #0b0e14); color: #ffffff; }
    
    /* تصميم الكروت بنمط Neo-Glass */
    .card-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.4s ease;
        height: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 25px;
    }
    .card-container:hover {
        border-color: #00d4ff;
        transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.15);
    }
    
    /* العناوين */
    .main-header {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #fff, #00d4ff, #fff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    /* أزرار الروابط */
    .action-btn {
        display: block;
        text-align: center;
        padding: 12px;
        background: linear-gradient(90deg, #00d4ff, #004e92);
        color: white !important;
        border-radius: 12px;
        text-decoration: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .action-btn:hover { opacity: 0.9; box-shadow: 0 5px 15px rgba(0, 212, 255, 0.4); }
    
    .social-bar {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">Boda The Ghost</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #8b949e;'>Automation Architect & Software Developer</p>", unsafe_allow_html=True)
st.write("---")

# --- Grid System للأدوات ---
st.markdown("## 🚀 My Digital Ecosystem")

# الصف الأول
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card-container">
        <div>
            <h2 style="color: #00d4ff;">📖 Quran-V1</h2>
            <p style="color: #b1b1b1;">أداة القرآن الكريم المجانية - صدقة جارية، تتيح لك الوصول للمصحف الشريف برمجياً وبواجهة سهلة الاستخدام.</p>
        </div>
        <a href="https://github.com/bodaking20/Quran-V1" target="_blank" class="action-btn">Source Code (GitHub)</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card-container">
        <div>
            <h2 style="color: #00d4ff;">🖥️ Side-By-Side Merger</h2>
            <p style="color: #b1b1b1;">أداة تقسيم ودمج الشاشة الاحترافية لتسهيل العمل على أكثر من ملف أو فيديو في وقت واحد بدقة عالية.</p>
        </div>
        <a href="https://github.com/bodaking20/SIDE-BY-SIDE-MERGER" target="_blank" class="action-btn">View Repository</a>
    </div>
    """, unsafe_allow_html=True)

# الصف الثاني (أدوات تخطي الحقوق)
col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="card-container" style="border-color: #ff4b2b;">
        <div>
            <h2 style="color: #ff4b2b;">⚽ Football Rights Bypass</h2>
            <p style="color: #b1b1b1;">أداة حصرية لتخطي حقوق البث لمباريات كرة القدم وإعادة رفعها بدون حظر (حقوق الطبع والنشر).</p>
        </div>
        <a href="https://wa.me/201118973019?text=أريد%20الاشتراك%20في%20أداة%20تخطي%20حقوق%20الكورة" class="action-btn" style="background: #ff4b2b;">إشترك الآن (WhatsApp)</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card-container" style="border-color: #ff4b2b;">
        <div>
            <h2 style="color: #ff4b2b;">🎬 Cinema Rights Bypass</h2>
            <p style="color: #b1b1b1;">أداة متطورة لتخطي حقوق المسلسلات والأفلام العالمية لضمان استمرارية البث والنشر بدون قيود.</p>
        </div>
        <a href="https://wa.me/201118973019?text=أريد%20الاشتراك%20في%20أداة%20تخطي%20حقوق%20المسلسلات" class="action-btn" style="background: #ff4b2b;">إشترك الآن (WhatsApp)</a>
    </div>
    """, unsafe_allow_html=True)

# --- Contact Section ---
st.write("---")
st.markdown("<h2 style='text-align: center;'>📲 Connect With Me</h2>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="social-bar">
        <a href="https://wa.me/201118973019" style="text-decoration:none; color:#25d366; font-size: 25px;">WhatsApp</a>
        <a href="https://instagram.com/l0gwy" style="text-decoration:none; color:#E1306C; font-size: 25px;">Instagram</a>
        <a href="https://facebook.com/boda151" style="text-decoration:none; color:#1877F2; font-size: 25px;">Facebook</a>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 💀 The Ghost System")
st.sidebar.write("جميع الأدوات مشفرة ومحمية.")
st.sidebar.markdown("---")
st.sidebar.info("Status: Fully Operational")
