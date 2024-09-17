import streamlit as st

# Définition du style de la sidebar
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

css_orange_sep = '<div style="height: 4px; background-color: orange; margin: 0px; width: 85%;"></div>'

css_styles_demo = [
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

css_styles_methode = [
                """
                button {
                    background: linear-gradient(to right, #ff7e5f, #feb47b);
                    color: white;
                    border: none;
                    border-color: white;
                    border-radius: 25px;
                    padding: 15px 50px;
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
