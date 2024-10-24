import io
import qrcode
import streamlit as st

# Page config
st.set_page_config(page_title="QR Code Generator", layout="wide")

# Header
st.header("QR Code Generator")

# Input for QR code content
data = st.text_input(
    "Enter the text you want to encode into QR Code",
    value="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)

if data:
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and display the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    st.image(buffer, caption="QR Code", width=300)
