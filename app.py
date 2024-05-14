import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

with open('db/texts.json','r') as jn:
    texts = json.load(jn)

def get_embeddings(texts):
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings


def search_similar_thoughts(user_thought, texts, embeddings):
    user_embedding = get_embeddings([user_thought])[0]
    similarities = cosine_similarity([user_embedding], embeddings)[0]
    sorted_indices = np.argsort(similarities)[::-1]
    similar_texts = [(texts[i], similarities[i]) for i in sorted_indices]
    return similar_texts

def main():
    load_dotenv()
    st.set_page_config(page_title="Juxta",
                       page_icon=":thought_balloon:")
    st.write(css, unsafe_allow_html=True)

    st.header("Connect Your Thoughts :thought_balloon:")
    user_thought = st.text_input("Enter your thought:")
    
    if user_thought:
        st.write("Searching ...")
        # st.write("User Thought:", user_thought)
        embeddings = get_embeddings(texts)
        
        similar_texts = search_similar_thoughts(user_thought, texts, embeddings)
        
        result = False

        for text, similarity in similar_texts[:4]:
            # st.write(f"Similarity: {similarity:.2f}")
            if similarity>0.3:
                st.write(text)
                st.write("---")
                result = True
        
        if not result:
            st.write(f"No similar Thoughts before")

        if st.button("Add to Notes"):
            texts.append(user_thought)
            embeddings = get_embeddings(texts)  # Re-embed texts after addition
            st.write("User thought added successfully!")

if __name__ == '__main__':
    main()
    with open('db/texts.json','w') as jn:
        json.dump(texts,jn,indent=4)
