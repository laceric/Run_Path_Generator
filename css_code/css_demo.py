import streamlit as st

#############################################################################################################    VARIABLES
css_sidebar = f"""
                <style>
                    [data-testid="stSidebar"] > div:first-child {{
                    background: linear-gradient(to bottom, #ff7e5f, #feb47b);
                    color: #ff7e5f;
                    }}

                    [data-testid="stSidebarNavLink"] > .st-emotion-cache-1rtdyuf{{
                    color: #FFFFFF;
                    }}

                    [data-testid="stSidebarNavLink"] > .st-emotion-cache-6tkfeg{{
                    color: #FFFFFF;
                    }}
                </style>
                """

css_styles_methode = [
                    """
                    button {
                        background: linear-gradient(to right, #ff7e5f, #feb47b);
                        color: white;
                        border: none;
                        border-color: white;
                        border-radius: 25px;
                        padding: 15px 75px;
                        text-transform: uppercase;
                        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.7);
                        transition: background 0.3s ease, transform 0.3s ease;
                    }
                    """
                    ,
                    """
                    button:hover {
                        transition: background 0.2s ease, transform 0.2s ease;
                        transform: translateY(-3px);
                        box-shadow: 0px 5px 15px rgba(0, 0, 0, 1); 
                    }
                    """
                    ,
                    """
                    p {
                        font-weight: 600;
                        font-size: 30px;
                    }
                    """
                        ]

css_styles_GPX = [
                """
                button {
                        width: 240px; /* Largeur du bouton */
                        height: 98px; /* Hauteur du bouton */
                        background: white;
                        border: 8px solid #feb47b;
                        border-radius: 30px;
                        text-transform: uppercase;
                        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.7);
                        transition: background 0.3s ease, transform 0.3s ease;
                    }
                """
                ,
                """
                button:hover {
                    background: linear-gradient(to right, #ff7e5f, #feb47b);
                    color: white;
                    transition: background 0.2s ease, transform 0.2s ease;
                    transform: translateY(-3px);
                    box-shadow: 0px 5px 15px rgba(0, 0, 0, 1); 
                }
                """
                ,
                """
                p {
                    font-weight: 500;
                    font-size: 25px;
                }
                """
                    ]

css_styles_restart = [
                """
                button {
                        width: 100px; /* Largeur du bouton */
                        height: 60px; /* Hauteur du bouton */
                        background: linear-gradient(to right, #ff7e5f, #feb47b);
                        color: white;
                        border: none;
                        border-color: white;
                        border-radius: 25px;
                        text-transform: uppercase;
                        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.7);
                        transition: background 0.3s ease, transform 0.3s ease;
                    }
                """
                ,
                """
                button:hover {
                    background-color: #004280; /* Change la couleur de fond au survol */
                    color: white; /* Change la couleur du texte au survol */
                    transition: background 0.2s ease, transform 0.2s ease;
                    transform: translateY(-3px);
                    box-shadow: 0px 5px 15px rgba(0, 0, 0, 1); 
                }
                """
                    ]

css_box_info = '''
                    <style>
                        div[data-testid="stAlert"] > .st-au {
                            background-color: #FFF;
                            border: 3px solid #feb47b;
                            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.7);
                    }

                    </style>
                    '''

css_box_error = '''
                    <style>
                        div[data-testid="stAlert"] > .st-be {
                            border: 3px solid rgb(206, 87, 97);
                            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.7);
                    }

                    </style>
                    '''

css_metrics_card_param = '''
                    <style>
                    div[data-testid="stMetric"] {
                        background-color: #FFF;
                        border: 5px solid #feb47b;
                        padding: 5% 5% 5% 10%;
                        border-radius: 30px; 
                    }

                    div[data-testid="stAlert"] > .st-c2 {
                        background-color: #FFF;
                        border: 3px solid #feb47b;
                        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.7);
                    }
                    </style>
                    '''
#############################################################################################################    FONCTIONS
def show_loading_gif():
    # HTML pour afficher le GIF
    st.markdown(
        f"""
        <div id="loader">
            <img src="data:image/gif;base64,{st.image("running_man.gif", width=200).image_data}"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    # CSS pour ajustement de la box du gif
    st.markdown(
        f"""
            <style>
            [data-testid="stImage"]{{
            margin-left: 220px;
            margin-top: 180px;
            }}
        """,
        unsafe_allow_html=True
    )

    # Masquer le GIF loader après la fin de la tâche
    st.markdown(
        """
        <style>
        #loader {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def hide_loading_gif():
    # Hide the GIF loader after the task is completed
    st.markdown(
        f"""
            <style>
            [data-testid="stImage"]{{
            display: none;
            }}
        """,
        unsafe_allow_html=True
    )