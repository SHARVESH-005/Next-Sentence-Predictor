# Next Sentence Predictor using GPT-2

This project is a lightweight Streamlit-based app that uses OpenAI's GPT-2 model to generate the next sentence from a user-provided prompt. It was developed as part of the **IBM Generative AI Developer Essentials Certification**.

---

## Objective

To build an intuitive interface where users can input a sentence, and the app generates a contextually relevant continuation using a pretrained transformer model.

---

## Tech Stack

| Technology      | Purpose                           |
|------------------|-----------------------------------|
| Python           | Programming Language              |
| Streamlit        | UI framework for web apps         |
| HuggingFace Transformers | GPT-2 model access         |
| PyTorch          | Model backend                     |

---

## How It Works

1. The app loads the `gpt2` tokenizer and language model.
2. A user inputs a seed sentence.
3. The model generates a continuation using top-k and nucleus sampling.
4. Output is displayed interactively using Streamlit.

---

## Installation

1. **Clone this repo**

```bash
git clone https://github.com/your-username/gpt2-next-sentence.git
cd gpt2-next-sentence
