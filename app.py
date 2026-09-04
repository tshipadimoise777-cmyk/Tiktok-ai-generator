import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="Générateur vidéo IA TikTok", layout="centered")

st.title("🎬 Générateur de Vidéos TikTok IA")
st.subheader("Transformez vos histoires en vidéos virales")

# Récupération de la clé API Gemini
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("La clé GEMINI_API_KEY est introuvable dans les Secrets Streamlit.")
else:
    genai.configure(api_key=api_key)

    # Formulaire principal
    with st.form("video_form"):
        story_prompt = st.text_area(
            "Entrez l'histoire ou le prompt de votre vidéo :",
            placeholder="Exemple : Une maman désespérée arrive en urgence à l'hôpital...",
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
            with st.spinner("Génération du script TikTok avec Gemini en cours..."):
                try:
                    prompt_instructions = f"""
                    Tu es un expert en création de contenu viral TikTok de 35 à 45 secondes.
                    Génère une structure complète basée sur les éléments suivants :

                    - Histoire : {story_prompt}
                    - Style visuel : {style_visuel}
                    - Ton de la voix off : {style_voix}
                    - Langue : {language}

                    Organise la réponse clairement ainsi :
                    1. 🎯 HOOK ACCROCHEUR (0 à 3 secondes)
                    2. 📜 DÉCOUPAGE DES SCÈNES (Horodatage, Description visuelle, Voix off)
                    3. 💡 APPEL À L'ACTION / CTA
                    4. 🎨 PROMPTS GÉNÉRATIFS DÉTAILLÉS (pour CapCut / Midjourney)
                    """

                    # Modèle mis à jour selon l'indication d'erreur
                    model = genai.GenerativeModel("gemini-3.6-flash")
                    response = model.generate_content(prompt_instructions)

                    st.success("Génération terminée avec succès !")
                    st.markdown("---")
                    st.markdown(response.text)

                except Exception as e:
                    st.error(f"Erreur lors de la génération : {e}")
