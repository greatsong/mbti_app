import streamlit as st

st.set_page_config(
    page_title="MBTI 독서 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 MBTI 청소년 문학 & 포켓몬 추천")
st.subheader("✨ 나의 성향과 닮은 캐릭터와 책을 만나보세요!")

st.write("""
MBTI는 우리가 **세상을 바라보는 방식과 행동 스타일**을 이해하는 데 도움을 줍니다.  
여기에서는 MBTI 성향을 바탕으로 **포켓몬 캐릭터와 청소년 문학 작품**을 함께 추천합니다.
""")

mbti = st.selectbox(
    "🧠 MBTI 유형을 선택하세요",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

data = {

"INTJ":{
"pokemon":"뮤츠",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
"pokemon_reason":"뮤츠는 뛰어난 지능과 독립적인 성향을 가진 포켓몬입니다. 세상을 깊이 이해하려는 INTJ의 전략적 사고와 잘 어울립니다.",
"book":"모모",
"author":"미하엘 엔데",
"book_reason":"INTJ는 삶의 구조와 의미를 깊이 탐구하는 성향이 있습니다. '모모'는 시간과 삶의 가치에 대해 철학적인 질문을 던지는 작품입니다."
},

"INTP":{
"pokemon":"알akazam",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
"pokemon_reason":"알akazam은 매우 높은 지능을 가진 포켓몬입니다. 논리와 사고를 좋아하는 INTP와 잘 어울립니다.",
"book":"어린 왕자",
"author":"생텍쥐페리",
"book_reason":"이 책은 인간 관계와 삶의 의미를 철학적으로 탐구합니다. INTP의 탐구적 사고와 잘 맞습니다."
},

"ENTJ":{
"pokemon":"리자몽",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"pokemon_reason":"리자몽은 강력한 리더십과 자신감을 가진 포켓몬입니다. ENTJ의 리더 기질과 잘 어울립니다.",
"book":"헝거게임",
"author":"수잔 콜린스",
"book_reason":"불의한 사회 구조 속에서 리더십을 발휘하는 이야기로 ENTJ 성향과 잘 맞습니다."
},

"ENTP":{
"pokemon":"팬텀",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
"pokemon_reason":"팬텀은 장난기 많고 창의적인 포켓몬입니다. 새로운 아이디어를 좋아하는 ENTP와 잘 맞습니다.",
"book":"셜록 홈즈",
"author":"아서 코난 도일",
"book_reason":"기발한 추리와 논리적 사고가 필요한 이야기입니다."
},

"INFJ":{
"pokemon":"루기아",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
"pokemon_reason":"루기아는 깊은 지혜와 균형을 상징하는 포켓몬입니다. INFJ의 통찰력과 잘 어울립니다.",
"book":"나미야 잡화점의 기적",
"author":"히가시노 게이고",
"book_reason":"사람들의 고민을 통해 삶의 의미를 찾는 따뜻한 이야기입니다."
},

"INFP":{
"pokemon":"이브이",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
"pokemon_reason":"이브이는 다양한 가능성을 가진 포켓몬입니다. INFP의 이상주의와 잘 어울립니다.",
"book":"빨강머리 앤",
"author":"루시 모드 몽고메리",
"book_reason":"상상력이 풍부한 앤의 성장 이야기입니다."
},

"ENFP":{
"pokemon":"피카츄",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"pokemon_reason":"피카츄는 밝고 에너지가 넘치는 포켓몬입니다. ENFP의 긍정적인 에너지와 잘 어울립니다.",
"book":"완득이",
"author":"김려령",
"book_reason":"유쾌하면서도 따뜻한 성장 이야기입니다."
},

"ISTJ":{
"pokemon":"거북왕",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
"pokemon_reason":"거북왕은 안정감 있고 책임감이 강한 포켓몬입니다.",
"book":"마당을 나온 암탉",
"author":"황선미",
"book_reason":"책임과 선택의 의미를 생각하게 하는 작품입니다."
},

"ESTP":{
"pokemon":"루카리오",
"image":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
"pokemon_reason":"루카리오는 행동력과 전투 감각이 뛰어난 포켓몬입니다.",
"book":"해리포터",
"author":"J.K. 롤링",
"book_reason":"모험과 도전이 가득한 판타지 이야기입니다."
}

}

if st.button("✨ 추천 받기"):

    st.balloons()

    info = data.get(mbti)

    if info:

        st.header(f"🧠 {mbti} 유형 추천")

        st.subheader("⚡ 당신과 닮은 포켓몬")

        st.image(info["image"], width=200)

        st.write(f"**{info['pokemon']}**")

        st.write(info["pokemon_reason"])

        st.subheader("📚 추천 도서")

        st.markdown(f"**{info['book']}**  |  {info['author']}")

        st.write(info["book_reason"])

    else:
        st.warning("이 유형은 아직 추가되지 않았습니다.")
