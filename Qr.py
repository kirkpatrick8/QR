import streamlit as st
import qrcode
from io import BytesIO
import base64

def generate_qr_code(data, color, bg_color, box_size):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=4,
    )
    
    # Add data
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create image
    qr_image = qr.make_image(fill_color=color, back_color=bg_color)
    
    # Convert to bytes
    buffered = BytesIO()
    qr_image.save(buffered, format="PNG")
    return buffered.getvalue()

# Set page config
st.set_page_config(page_title="QR Code Generator", layout="centered")

# Title
st.title("QR Code Generator")

# Input fields
data = st.text_area("Enter text or URL", "https://www.example.com")
color = st.color_picker("Choose QR code color", "#000000")
bg_color = st.color_picker("Choose background color", "#FFFFFF")
box_size = st.slider("QR Code Size", min_value=1, max_value=20, value=10)

# Generate button
if st.button("Generate QR Code"):
    if data:
        qr_bytes = generate_qr_code(data, color, bg_color, box_size)
        # Display QR code
        st.image(qr_bytes, caption="Your QR Code")
        
        # Download button
        b64_qr = base64.b64encode(qr_bytes).decode()
        href = f'<a href="data:image/png;base64,{b64_qr}" download="qr_code.png">Download QR Code</a>'
        st.markdown(href, unsafe_allow_html=True)
    else:
        st.error("Please enter some text or URL")

# Instructions
with st.expander("How to use"):
    st.write("""
    1. Enter any text or URL in the text area
    2. Choose colors for the QR code and background
    3. Adjust the size using the slider
    4. Click 'Generate QR Code'
    5. Download your QR code using the download link
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
