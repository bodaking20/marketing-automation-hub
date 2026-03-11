import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Boda The Ghost | Marketing Automation", page_icon="🕵️‍♂️", layout="wide")

# CSS لتحسين شكل المربعات والأزرار
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #007bff; color: white; font-weight: bold; }
    .contact-button { display: inline-block; padding: 10px 20px; background-color: #25d366; color: white; border-radius: 5px; text-decoration: none; margin: 5px; }
    .card { background-color: #1e2130; padding: 20px; border-radius: 15px; border: 1px solid #30363d; height: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- القسم الأول: التعريف الشخصي (Home) ---
st.title("🕵️‍♂️ Boda The Ghost")
st.subheader("Marketing Automation Expert & Data Strategist")
st.write("""
أهلاً بك! أنا **بودا**، متخصص في ابتكار حلول الأتمتة للتسويق الرقمي. 
هدفي هو تحويل العمليات اليدوية المرهقة إلى أنظمة ذكية توفر الوقت وتزيد من دقة النتائج.
""")

# --- القسم الثاني: مربعات الأدوات ---
st.write("---")
st.header("🛠️ My Marketing Tools")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div class="card">
    <h3>🎯 WhatsApp Validator</h3>
    <p>أداة ذكية لفحص قوائم الأرقام والتأكد من وجود حسابات واتساب نشطة قبل بدء الحملات.</p>
    </div>""", unsafe_allow_html=True)
    if st.button("Open WhatsApp Tool"):
        st.info("Coming Soon: جاري ربط الأداة بقواعد البيانات...")

with col2:
    st.markdown("""<div class="card">
    <h3>📊 Competitor Monitor</h3>
    <p>مراقبة لحظية لتغيرات السوق وتحليل استراتيجيات المنافسين بشكل تلقائي.</p>
    </div>""", unsafe_allow_html=True)
    if st.button("Open Monitor Tool"):
        st.info("Coming Soon: الأداة تحت التطوير حالياً.")

# --- القسم الثالث: طرق التواصل ---
st.write("---")
st.header("📲 Let's Connect")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f'<a href="https://wa.me/201118973019" class="contact-button" style="background-color: #25d366;">WhatsApp: 01118973019</a>', unsafe_allow_html=True)

with c2:
    st.markdown('<a href="https://instagram.com/l0gwy" class="contact-button" style="background-color: #E1306C;">Instagram: @l0gwy</a>', unsafe_allow_html=True)

with c3:
    st.markdown('<a href="https://facebook.com/boda151" class="contact-button" style="background-color: #1877F2;">Facebook: boda151</a>', unsafe_allow_html=True)

st.sidebar.success("Select a tool above to start!")
st.sidebar.markdown("---")
st.sidebar.write("Developed with 💻 by Boda")
