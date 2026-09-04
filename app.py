import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Générateur vidéo IA TikTok", layout="centered")

st.title("🎬 Générateur de Vidéos TikTok IA")
st.subheader("Transformez vos histoires en vidéos virales")

# Formulaire principal
with st.form("video_form"):
    story_prompt = st.text_area(
        "Entrez l'histoire ou le prompt de votre vidéo :",
        placeholder="Exemple : L'histoire incroyable d'un trésor caché...",
        height=150
    )

    col1, col2 = st.columns(2)
    with col1:
        style_visuel = st.selectbox(
            "Style visuel des personnages :",
            ["Photoréaliste Cinématique", "Cyberpunk", "Sombre & Mystérieux"]
        )
    with col2:
        style_voix = st.selectbox(
            "Ton de la voix off :",
            ["Grave & Mystérieux", "Énergique & Dynamique"]
        )

    language = st.selectbox("Langue de la vidéo :", ["Français", "Anglais"])

    submit_button = st.form_submit_button("🚀 Générer la Structure Vidéo")

if submit_button:
    if not story_prompt.strip():
        st.warning("Veuillez saisir une histoire.")
    else:
        st.success("Formulaire validé ! Traitement en cours...")
