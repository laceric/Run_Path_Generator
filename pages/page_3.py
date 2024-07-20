import streamlit as st
import streamlit.components.v1 as components

# Ajouter du CSS pour styliser le bouton
button_css = """
<style>
.custom-button {
    display: inline-block;
    padding: 0.5em 1em;
    font-size: 1em;
    font-weight: bold;
    color: #ffffff;
    background-color: #4CAF50;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
}
.custom-button:hover {
    background-color: #45a049;
}
</style>
"""

# Créer le bouton personnalisé avec HTML et JavaScript
button_html = """
<a href="javascript:void(0)" class="custom-button" onclick="sendMessage()">Custom Button</a>
<script>
function sendMessage() {
    const streamlitDoc = window.parent.document;
    const hiddenInput = streamlitDoc.getElementById('custom-button-clicked');
    hiddenInput.value = "clicked";
    hiddenInput.dispatchEvent(new Event('change'));
}
</script>
"""

# Afficher le CSS et le bouton HTML
components.html(button_css + button_html, height=80)

# Ajouter un champ d'entrée caché pour détecter le clic
st.markdown(
    """
    <input type="hidden" id="custom-button-clicked">
    <script>
    document.getElementById('custom-button-clicked').addEventListener('change', function() {
        fetch("/_stcore/streamlit/js?msg=custom_button_clicked");
    });
    </script>
    """,
    unsafe_allow_html=True
)

# Gestion du clic sur le bouton personnalisé
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.experimental_get_query_params().get('msg') == ['custom_button_clicked']:
    st.session_state.button_clicked = True
    # st.experimental_set_query_params()  # Reset the query params

# Afficher un message si le bouton personnalisé a été cliqué
if st.session_state.button_clicked:
    st.write("Bouton personnalisé cliqué !")
