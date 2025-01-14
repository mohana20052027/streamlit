import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import pandasai as pdai
from pdai.llm.openai import OpenAI


load_dotenv()
openai_api_key= os.getenv('OPENAI_API_KEY')

def chat_with_csv(df,prompt):
    llm = OpenAI()
    pandas_api= PandasAI(llm)
    result= pandas_ai.run(df,prompt=prompt)
    print(result)
    return result

st.set_page_config(layout='wide')
st.title("ChatCSV powered by LLM")

input_csv = st.file_uploader("Upload your CSV file", type=['csv'])

if input_csv is not None:
    col1, col2= st.columns([1,1])
    with col1:
        st.info("CSV uploaded successfully")
        data= pd.read_csv(input_csv)
        st.dataframe(data)
    with col2:
        st.info("chat with your csv")
        input_text= st.text_area("Enter your query")
        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info("Your query:"+input_text)
                result= chat_with_csv(data,input_text)
                st.success(result)

