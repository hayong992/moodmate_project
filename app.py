import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "your-api-key"

# Streamlit 앱 제목
st.title("오늘의 MoodMate 🎵🍕🌟")
st.write("당신의 기분에 맞는 음악, 음식, 활동을 추천해드릴게요!")

# 사용자로부터 기분 입력 받기
user_mood = st.text_input("오늘 기분은 어떤가요?")

if user_mood:
    with st.spinner("추천을 생성 중입니다..."):
        try:
            # OpenAI API에서 새로운 방식으로 ChatCompletion 호출
            response = openai.completions.create(
                model="text-davinci-003",  # 사용할 모델
                prompt=f"오늘 기분은 '{user_mood}'입니다. 그에 맞는 음악, 음식, 활동을 추천해주세요.",
                max_tokens=150,
                temperature=0.7
            )
            # 추천 결과 처리
            recommendations = response["choices"][0]["text"].strip()
            st.success("추천이 완료되었습니다!")
            st.write(recommendations)
        except Exception as e:
            # 오류 처리
            st.error(f"추천 생성 중 오류가 발생했습니다: {e}")
