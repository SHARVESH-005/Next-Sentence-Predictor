import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

st.title("Next Sentence Predictor")
st.write("Enter a sentence and generate what comes next.")

user_input = st.text_input("Type your sentence:")

if st.button("Generate Next Sentence"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        output_ids = model.generate(
            input_ids,
            max_new_tokens=30,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            eos_token_id=tokenizer.eos_token_id
        )
        output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        st.markdown("### Predicted Continuation:")
        st.write(output)
