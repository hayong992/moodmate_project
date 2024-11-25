import streamlit as st
import openai
import os

# OpenAI API 키 설정
openai.api_key = "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"

# Streamlit 인터페이스
st.title("오늘의 MoodMate 🎵🍕🌟")
st.write("당신의 기분에 맞는 음악, 음식, 활동을 추천해드릴게요!")

# 사용자의 기분 입력
user_mood = st.text_input("오늘 기분은 어떤가요? (간단히 적어주세요, 예: 행복해, 피곤해, 우울해)")

# 기분에 따른 추천 생성
if user_mood:
    with st.spinner("추천을 생성 중입니다..."):
        prompt = f"""
        오늘의 기분은 '{user_mood}'입니다. 기분에 맞는 추천을 제공해주세요:
        1. 음악 추천 (제목과 가수)
        2. 음식 추천 (예: 간단한 요리 또는 배달 음식)
        3. 활동 추천 (예: 실내 또는 야외 활동)
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
            )
            recommendations = response.choices[0].text.strip()
            st.success("추천이 완료되었습니다!")
            st.write(recommendations)
        except Exception as e:
            st.error(f"추천 생성 중 오류가 발생했습니다: {e}")

# Footer
st.write("🌟 MoodMate와 함께 즐거운 하루 되세요! 🌟")