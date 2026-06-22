#this file binds all the other files together and runs the streamlit app

import streamlit as st
from api import generate_image
from prompts import STYLE_PROMPTS
st.set_page_config(page_title="AI Image Generator")

st.title("🎨 AI Image Generator")
st.write("Generate images using AI and different artistic styles.")

if "history" not in st.session_state:
    st.session_state.history = []

prompt = st.text_input(
    "Enter your image prompt" 
)

style = st.radio(
    "Choose a style",
    list(STYLE_PROMPTS.keys())
)

generate = st.button("Generate Image")

if generate and prompt:

    final_prompt = (
        f"{prompt}, "
        f"{STYLE_PROMPTS[style]}"
    )

    st.write("### Final Prompt")
    st.write(final_prompt)

    image = generate_image(final_prompt)

    if image:

        st.image(
            image,
            caption=final_prompt,
            use_container_width=True
        )

        st.session_state.history.append(final_prompt)

    else:
        st.error("Failed to generate image.")

st.write("---")
st.write("## Prompt History")

for item in reversed(st.session_state.history):
    st.write("•", item)