import streamlit as st
from streamlit_lottie import st_lottie

from utils import *

import pandas as pd
import numpy as np
from PIL import Image

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask

def main():
    """
    Main Function for the streamlit App
    """
    st.set_page_config(
        page_icon="🤳",
        page_title = "Fantastic QR Code Gen",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/fantasticqrcode',
        'Report a bug': "https://github.com/smaranjitghose/fantasticqrcode/issues",
        'About': "## A minimalistic application to generate QR Codes using python"
        }
    )

    st.title("Fantastic QR Code Generator")
    hide_footer()
    # Load and display animation
    anim = lottie_local("assets/animations/scanner.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=300,
            width=300,
            key=None,
            )
    # Data Input       
    data_in = st.text_input(label="Enter URL (or text)")
    # Parameters to Modify the QR Code
    col1, col2 = st.columns(2)
    with col1:
        fill_color = st.color_picker('Pick Fill Color', '#000000')
    with col2:
        back_color = st.color_picker('Pick Background Color', '#ffffff')

    # Create a QRCode object
    qr = qrcode.QRCode(version=4,
        box_size=10,
        border=4)
    # Pass the input data to the object and generate the output
    qr.add_data(data_in)
    qr.make(fit=True)
    # Covert the QRCode to an image with desired features
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    # Save the rendered QRCode image to assets sub-directory
    img.save("./assets/qrcode.png")

    # Read the Generated QR Code Image
    with open('./assets/qrcode.png', "rb") as file:
        # Display QR Code Image
        image = Image.open(file)
        st.image(image,caption="Result")
        # Download Button
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="fantasticqrcode.png",
                mime="image/png"
            )


if __name__ == "__main__":
    main()