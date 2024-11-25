import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "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"

# Streamlit 앱
st.title("오늘의 MoodMate 🎵🍕🌟")
st.write("당신의 기분에 맞는 음악, 음식, 활동을 추천해드릴게요!")

# 사용자 입력
user_mood = st.text_input("오늘 기분은 어떤가요?")

# 입력에 따라 추천 생성
if user_mood:
    with st.spinner("추천을 생성 중입니다..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # 모델 지정
                messages=[
                    {"role": "system", "content": "당신은 친절한 추천 전문가입니다."},
                    {"role": "user", "content": f"오늘 기분은 '{user_mood}'입니다. 추천을 만들어주세요."},
                ],
                temperature=0.7,
            )
            recommendations = response["choices"][0]["message"]["content"].strip()
            st.success("추천이 완료되었습니다!")
            st.write(recommendations)
        except Exception as e:
            st.error(f"추천 생성 중 오류가 발생했습니다: {e}")

