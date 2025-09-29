import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Removedor de Fundo", page_icon="🖼️", layout="centered")

st.title("🖼️ Removedor de Fundo")
st.write("Carregue uma imagem e remova o fundo automaticamente!")

# Upload da imagem
uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Abrir a imagem e converter para RGB
    input_image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Imagem Original")
    st.image(input_image, use_container_width=True)

    # Remover fundo
    output_image = remove(input_image)

    # Converter saída também para RGB (ou RGBA se quiser preservar transparência)
    if output_image.mode != "RGBA":
        output_image = output_image.convert("RGBA")

    st.subheader("Imagem sem Fundo")
    st.image(output_image, use_container_width=True)

    # Botão para download
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Baixar imagem sem fundo",
        data=byte_im,
        file_name="output.png",
        mime="image/png"
    )
