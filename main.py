import streamlit as st

# 1. 페이지 기본 설정 (타이틀, 레이아웃, 아이콘)
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

# 2. 커스텀 CSS (따뜻한 크림·노란색 톤 & 큰 글씨 설정)
st.markdown("""
    <style>
    /* 전체 배경색 - 따뜻한 크림 톤 */
    .stApp {
        background-color: #FFFDF0;
        color: #2D3436;
        font-family: 'Pretendard', sans-serif;
    }
    
    /* 셀렉트박스 및 드롭다운 큰 글씨 */
    div[data-baseweb="select"] {
        font-size: 1.25rem !important;
    }
    
    /* 헤더 스타일 */
    .title-text {
        color: #D35400;
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .sub-text {
        color: #636E72;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* 결과 카드 스타일 */
    .result-card {
        background-color: #FFFFFF;
        border: 3px solid #FFEAA7;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 8px 20px rgba(255, 159, 67, 0.15);
        margin-top: 10px;
    }
    
    .pokemon-title {
        font-size: 2rem;
        font-weight: bold;
        color: #2D3436;
        margin-bottom: 5px;
    }
    
    .badge {
        display: inline-block;
        background-color: #FFE866;
        color: #D35400;
        font-weight: bold;
        padding: 6px 16px;
        border-radius: 15px;
        font-size: 1.1rem;
        margin-bottom: 15px;
    }
    
    .info-box {
        background-color: #FFFDF0;
        border-left: 5px solid #FF9F43;
        padding: 15px;
        border-radius: 8px;
        font-size: 1.15rem;
        line-height: 1.7;
        margin-top: 15px;
        word-break: keep-all;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 16가지 MBTI 및 단짝 포켓몬 데이터 정의
POKEMON_DATA = {
    "ISTJ": {
        "mbti_desc": "신중하고 철두철미한 원칙주의자",
        "ko_name": "거북왕",
        "en_name": "Blastoise",
        "type": "💧 물",
        "feature": "단단한 껍질과 안정감 있는 방어력을 자랑하는 묵묵한 대장 포켓몬",
        "reason": "책임감이 강하고 규칙을 중시하는 ISTJ처럼, 거북왕은 신뢰할 수 있는 든든함으로 언제나 제자리를 지켜줍니다. 맡은 바 책임을 끝까지 수행하는 모습이 완벽히 닮아있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png"
    },
    "ISFJ": {
        "mbti_desc": "헌신적이고 다정한 성실한 수호자",
        "ko_name": "해피너스",
        "en_name": "Blissey",
        "type": "⚪ 노말",
        "feature": "상처받은 포켓몬이나 사람을 보면 행복의 알을 나누어 주는 친절한 포켓몬",
        "reason": "타인을 따뜻하게 챙기고 배려하는 ISFJ의 온화함이 해피너스와 빼닮았습니다. 조용히 주변 사람들의 마음을 치유하고 든든한 안식처가 되어주는 최상의 단짝입니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png"
    },
    "INFJ": {
        "mbti_desc": "깊은 통찰력을 지닌 신비로운 예지자",
        "ko_name": "뮤",
        "en_name": "Mew",
        "type": "🔮 초능력",
        "feature": "모든 포켓몬의 유전자를 지니고 있다고 하며 신비로운 존재감을 발산하는 포켓몬",
        "reason": "조용하지만 겉보기보다 넓은 통찰력과 이상을 품고 있는 INFJ와 잘 어울립니다. 신비로우면서도 순수한 영혼으로 깊은 이해와 교감을 나눌 수 있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png"
    },
    "INTJ": {
        "mbti_desc": "철두철미한 계획과 비전을 가진 전략가",
        "ko_name": "뮤츠",
        "en_name": "Mewtwo",
        "type": "🔮 초능력",
        "feature": "극강의 지능과 전투 능력을 바탕으로 철저하게 판단하고 행동하는 포켓몬",
        "reason": "독립적이고 완벽을 추구하며 본질을 파악하려는 INTJ의 명석한 두뇌와 똑 닮아있습니다. 목표를 향해 전략적으로 접근하는 최고의 지적 동반자입니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"
    },
    "ISTP": {
        "mbti_desc": "냉철한 이성과 뛰어난 상황 판단력의 해결사",
        "ko_name": "루카리오",
        "en_name": "Lucario",
        "type": "🥊 격투 / ⚙️ 강철",
        "feature": "상대방의 파동을 감지하고 차분하고 침착하게 문제를 해결하는 포켓몬",
        "reason": "말보다 행동이 앞서며 위기 상황에서도 도구와 환경을 침착하게 활용하는 ISTP의 모습입니다. 루카리오의 냉철함과 실용적인 도덕성은 손발이 딱 맞습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png"
    },
    "ISFP": {
        "mbti_desc": "온순하고 유연한 감성적인 예술가",
        "ko_name": "메타몽",
        "en_name": "Ditto",
        "type": "⚪ 노말",
        "feature": "어떤 모습으로든 유연하게 변신하며 주변에 편안하게 스며드는 포켓몬",
        "reason": "상대방에게 자신을 강요하지 않고 자유로우며 물 흐르듯 적응하는 ISFP의 성향과 어울립니다. 어떤 상황에서든 따뜻하고 다정하게 조화를 이룹니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png"
    },
    "INFP": {
        "mbti_desc": "상상력이 풍부하고 따뜻한 이상주의자",
        "ko_name": "이브이",
        "en_name": "Eevee",
        "type": "⚪ 노말",
        "feature": "무한한 가능성을 품고 있어 다양한 모습으로 진화할 수 있는 귀여운 포켓몬",
        "reason": "자신의 마음속에 다채로운 가능성과 내면의 가치를 소중히 품고 사는 INFP의 모습입니다. 이브이의 무궁무진한 진화 가능성은 INFP의 꿈과 닮아있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
    },
    "INTP": {
        "mbti_desc": "지적 호기심이 넘치는 분석적인 아이디어가",
        "ko_name": "후딘",
        "en_name": "Alakazam",
        "type": "🔮 초능력",
        "feature": "IQ 5000 이상의 놀라운 지능으로 세상의 모든 현상을 탐구하는 포켓몬",
        "reason": "원리와 법칙을 계속해서 깊게 탐구하는 INTP의 학구적 호기심에 어울립니다. 후딘의 지적이고 복잡한 사고 구조는 INTP와 정서적인 깊은 지적 교감을 만듭니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"
    },
    "ESTP": {
        "mbti_desc": "에너지가 넘치고 순발력 뛰어난 자발적 모험가",
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "type": "⚡ 전기",
        "feature": "톡톡 튀는 스파크와 통통 튀는 발걸음으로 도전을 즐기는 대표 포켓몬",
        "reason": "망설이지 않고 액션을 취하며 새로운 경험을 즐기는 ESTP의 자신감 넘치는 에너지와 딱 맞아떨어집니다. 둘이 함께하면 스릴 넘치는 일상이 펼쳐집니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
    },
    "ESFP": {
        "mbti_desc": "밝고 열정적인 분위기 메이커 슈퍼스타",
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "type": "⚪ 노말 / 🧚 페어리",
        "feature": "사람들의 관심을 즐기며 사랑스러운 노래로 마법 같은 순간을 만드는 포켓몬",
        "reason": "사람들과 어울리는 것을 좋아하고 어디서나 미소를 주는 ESFP의 연예인 같은 기질을 완벽히 보여줍니다. 함께 있는 것만으로도 주위 분위기를 밝게 바꿔줍니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"
    },
    "ENFP": {
        "mbti_desc": "창의적이고 열정적인 긍정 에너지 활동가",
        "ko_name": "망나뇽",
        "en_name": "Dragonite",
        "type": "🐉 드래곤 / 🕊️ 비행",
        "feature": "바다를 건너며 어려움에 처한 이들을 돕고 상냥하고 낙천적인 상상의 포켓몬",
        "reason": "모험과 자유를 사랑하며 특유의 밝고 친근한 따뜻함으로 주위를 끌어당기는 ENFP와 가장 잘 어울립니다. 부드러우면서도 넓은 마음을 가진 환상의 짝꿍입니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png"
    },
    "ENTP": {
        "mbti_desc": "독창적이고 장난기 가득한 창의적 토론가",
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "type": "👻 고스트 / ☠️ 독",
        "feature": "유쾌한 장난과 예측 불가능한 아이디어로 사람들을 놀라게 만드는 포켓몬",
        "reason": "틀에 갇히지 않는 유쾌함과 비범한 통찰력을 가진 ENTP의 매력과 정통으로 통합니다. 팬텀의 장난스러운 미소 뒤에 숨겨진 지혜로움은 최고의 궁합입니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"
    },
    "ESTJ": {
        "mbti_desc": "체계적이고 당당한 실용주의 리더",
        "ko_name": "윈디",
        "en_name": "Arcanine",
        "type": "🔥 불꽃",
        "feature": "위풍당당한 기품과 신의를 지키며 목표를 향해 힘차게 달려가는 전설 포켓몬",
        "reason": "주변을 솔선수범하여 이끌고 확실한 목표 의식을 지닌 ESTJ의 당당함이 윈디의 늠름한 자태와 일치합니다. 리더십과 충성심으로 강력한 끈끈함을 선사합니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png"
    },
    "ESFJ": {
        "mbti_desc": "친절하고 사교성이 뛰어난 모임의 리더",
        "ko_name": "라이츄",
        "en_name": "Raichu",
        "type": "⚡ 전기",
        "feature": "밝은 미소와 사교적인 성격으로 모두와 금방 친해지는 다정한 포켓몬",
        "reason": "주변 사람들을 살뜰히 챙기고 따뜻한 모임 문화를 만드는 ESFJ에게 어울립니다. 라이츄의 다정하고 활력 있는 온기는 사람들을 모으는 힘이 있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/26.png"
    },
    "ENFJ": {
        "mbti_desc": "타인을 이끄는 열정적인 언변가 지도자",
        "ko_name": "토게키스",
        "en_name": "Togekiss",
        "type": "🧚 페어리 / 🕊️ 비행",
        "feature": "서로 존중하는 이들에게 행복과 은혜를 가져다주는 평화의 선구자 포켓몬",
        "reason": "타인의 성장을 돕고 따뜻한 용기를 불어넣는 ENFJ의 리더십과 단짝을 이룹니다. 토게키스가 전하는 평화로운 행복은 ENFJ가 꿈꾸는 세상과 맞닿아 있습니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png"
    },
    "ENTJ": {
        "mbti_desc": "대담하고 목표 지향적인 용감한 지도자",
        "ko_name": "리자몽",
        "en_name": "Charizard",
        "type": "🔥 불꽃 / 🕊️ 비행",
        "feature": "뜨거운 불꽃과 강인한 승부욕으로 난관을 정면 돌파하는 영웅 포켓몬",
        "reason": "비전을 세우고 강한 추진력으로 난관을 헤쳐나가는 ENTJ의 결단력과 당당함을 상징합니다. 리자몽의 뜨거운 열정은 결승점까지 함께 달릴 힘을 줍니다.",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
    }
}

# 4. 앱 헤더 화면 출력
st.markdown('<div class="title-text">⚡ MBTI로 찾아보는 나의 단짝 포켓몬 ⚡</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">당신의 MBTI 유형을 선택하면 딱 맞는 포켓몬 친구를 소개해 드려요!</div>', unsafe_allow_html=True)

# 5. MBTI 선택 입력
mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택해주세요:",
    options=["선택하세요..."] + mbti_list,
    index=0
)

# 6. 결과 출력 처리
if selected_mbti != "선택하세요...":
    # 축하 효과 (풍선 애니메이션)
    st.balloons()
    
    data = POKEMON_DATA[selected_mbti]
    
    # 2컬럼 레이아웃 (좌: 이미지, 우: 포켓몬 상세 정보)
    col1, col2 = st.columns([1, 1.2], gap="medium")
    
    with col1:
        st.image(data["image"], use_container_width=True)
        
    with col2:
        st.markdown(f'<span class="badge">MBTI : {selected_mbti}</span>', unsafe_allow_html=True)
        st.markdown(f'<div class="pokemon-title">{data["ko_name"]} <span style="font-size:1.2rem; color:#7F8C8D;">({data["en_name"]})</span></div>', unsafe_allow_html=True)
        st.markdown(f"**속성 타입:** {data['type']}")
        st.markdown(f"**주요 특징:** {data['feature']}")
        
    # 하단 설명 박스
    st.markdown(f"""
        <div class="info-box">
            <strong>💛 어울리는 이유:</strong><br>
            {data['reason']}
        </div>
    """, unsafe_allow_html=True)

else:
    st.info("👆 위 목록에서 MBTI를 선택해 주세요!")
