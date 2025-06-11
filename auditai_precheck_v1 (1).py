import streamlit as st
import pandas as pd

st.set_page_config(page_title="AuditAI PreCheck", layout="wide")

st.title("🔍 AuditAI PreCheck")
st.markdown("**Bienvenue !** Cette version est une **démo simplifiée** en attendant l'intégration complète.")

uploaded_gl = st.file_uploader("📂 Importer le Grand Livre (Excel)", type=["xlsx", "csv"])
uploaded_balance = st.file_uploader("📂 Importer la Balance générale (Excel)", type=["xlsx", "csv"])

if uploaded_gl and uploaded_balance:
    st.success("✅ Fichiers reçus. Analyse en cours...")

    try:
        df_gl = pd.read_excel(uploaded_gl) if uploaded_gl.name.endswith("xlsx") else pd.read_csv(uploaded_gl)
        df_balance = pd.read_excel(uploaded_balance) if uploaded_balance.name.endswith("xlsx") else pd.read_csv(uploaded_balance)

        st.subheader("📑 Aperçu Grand Livre")
        st.dataframe(df_gl.head())

        st.subheader("📑 Aperçu Balance Générale")
        st.dataframe(df_balance.head())

        st.info("🔧 L'analyse complète sera activée dans la version intégrale.")
    except Exception as e:
        st.error(f"❌ Erreur de traitement : {e}")
else:
    st.warning("📥 Veuillez importer les deux fichiers pour démarrer l'analyse.")
