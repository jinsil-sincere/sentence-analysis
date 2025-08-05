# pip install python-dotenv
# pip install langchain
# pip install openai
# pip install streamlit

# from dotenv import load_dotenv
# load_dotenv()
# chat = ChatOpenAI(openai_api_key="sk-...")

from langchain_openai import ChatOpenAI
llm=ChatOpenAI(model="gpt-3.5-turbo")


# stramlit run main.py
import streamlit as st

st.title('This is a new test')

content = st.text_input('내가 지금 가장 듣고 싶은 말은?')
if st.button('입력 완료'):
   with st.spinner('분석 중 입니다'):
   result = llm.predict("내가 지금 제일 듣고 싶은 말은"+content+"이다 - 라는 응답에 대해 욕구 중심으로 정신역동적으로 해석해줘")
   st.write(result)



# content = st.text_input('내가 가장 뿌듯할 때는?')
# result = llm.predict("내가 가장 뿌듯할 때는"+content+"이다 - 라는 응답에 대해 욕구 중심으로 정신역동적으로 해석해줘")

# content = st.text_input('내가 가장 속상한 상황은?')
# result = llm.predict("내가 가장 속상한 상황은"+content+"이다 - 라는 응답에 대해 욕구 중심으로 정신역동적으로 해석해줘")


