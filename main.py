# pip install langchain-openai
# pip install python-dotenv
# pip install openai
# pip install streamlit

#%%
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

#%%
import streamlit as st

st.set_page_config(page_title='심리 분석 서비스', layout='wide')

st.title('내 마음 분석 서비스')

st.markdown(
    """
    <style>
    .stTextInput > div > div > input { font-size: 18px; }
    </style>
    """,
    unsafe_allow_html=True,
)

#%%
st.markdown("##### 🔑 OpenAI API 키")
openai_api_key = st.text_input(
    "OpenAI API Key", 
    type="password", 
    help="sk-로 시작하는 OpenAI API 키를 입력해주세요. 키는 저장되지 않습니다.",
    placeholder="sk-..."
)

st.markdown("---")

# 문항: 제목(####) + 아래 입력 칸 형식
st.markdown("##### 💬 내가 지금 가장 듣고 싶은 말은:")
content1 = st.text_input(
    "내가 지금 가장 듣고 싶은 말",
    key='input1',
    label_visibility='collapsed',
    placeholder='(                                                               ) 이다.'
)

st.markdown("##### 🙂 내가 가장 뿌듯할 때는:")
content2 = st.text_input(
    "내가 가장 뿌듯할 때",
    key='input2',
    label_visibility='collapsed',
    placeholder='(                                                               ) 이다.'
)

st.markdown("##### 😔 내가 가장 속상한 상황은:")
content3 = st.text_input(
    "내가 가장 속상한 상황",
    key='input3',
    label_visibility='collapsed',
    placeholder='(                                                               ) 이다.'
)

st.markdown('<div style="height: 28px;"></div>', unsafe_allow_html=True)
submit_clicked = st.button('입력 완료')

if submit_clicked:
    if not (content1 and content2 and content3):
        st.warning("모든 질문에 답해주세요!")
    elif not openai_api_key:
        st.error("OpenAI API 키를 입력해주세요.")
    elif not openai_api_key.startswith('sk-'):
        st.error("❌ 올바른 OpenAI API 키를 입력해주세요. (sk-로 시작해야 합니다)")
    else:
        st.success("✅ API 키가 확인되었습니다!")
        
        llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=openai_api_key, temperature=0.1)
        
        with st.spinner('분석 중입니다...'):
            try:
                combined_prompt = f"""
다음 세 가지 응답을 종합적으로 분석해줘:

1. 내가 지금 가장 듣고 싶은 말은 "{content1}" 이다.
2. 내가 가장 뿌듯할 때는 "{content2}" 이다.  
3. 내가 가장 속상한 상황은 "{content3}" 이다.

이 응답을 바탕으로 욕구 중심으로 정신역동적으로 종합 해석해줘. 

너는 심리평가 전문가이면서, 20년 이상의 심리상담 경력을 가진 대가야.
분석내용은 뻔하지 않으면서도 내용이 깊이 있고 스스로 몰랐던 자신의 마음에 대해 통찰할 수 있게, 
표현은 중학생이상아라면 누구라도 이해할 수 되도록 쉽고 명확하게 제시해줘.
소제목을 포함해서 가독성 있게 제시해주고 (소제목 크기는 크지 않고 자연스럽게)
읽고 나서 위로받는 느낌이 들 수 있게, 따뜻하고 공감적인 톤으로 존댓말로 작성해줘.
이 사람에게만 핏한 서술을 해줘.

뻔한 인사말의 도입부(서론) 없이 바로 핵심 분석으로 시작해줘.
"우리는 모두", "사람은 누구나" '당신의 정신적 건강에 큰 도움이 될 것입니다.'같은 일반론적/보편적 서술이나 상투적 표현은 쓰지 마.
"""
                response = llm.invoke(combined_prompt)
                result = getattr(response, 'content', str(response))
                
                st.markdown("### 📋 종합 분석결과")
                st.write(result)
            except Exception as e:
                st.error(f"분석 중 오류가 발생했습니다: {str(e)}")
                st.info("API 키가 올바른지 확인해주세요.")
