import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="아우라 종합 시뮬레이터", page_icon="⚔️", layout="wide"
)

# 1. 배틀로얄용 등급 리스트 정의 (희귀도 높은 순)
items_battle = [
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭", "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻", "사도:베일", "수확가", "악몽의 하늘", "𝓘𝓬𝓮𝓐𝓰𝓮", "𝓜𝓪𝓶𝓶𝓸𝓽𝓱",
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤", "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐", "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒", "감시자",
    "아쿠아리움", "선원", "샤킨", "포세이돈", "에바네샌트",
    "기원", "망령", "듀라한", "영혼 사냥꾼", "묘화", "밤나팔꽃", "바이탈", "룬(나이트)", "펌프",
    "블리자드", "이상", "크로마틱", "자장가",
    "그래피티", "헬리오스", "속력", "황혼",
    "아파타이트", "대마법사", "아케인", "워록",
    "테러", "바운디드", "재즈", "스펙터",
    "이색", "노틸러스", "아쿠아틱",
    "만년서리", "태양", "달", "와트",
    "힘", "카와이", "석영", "출혈",
    "시데리움", "콜라", "빙하", "재",
    "자력", "글록", "아쿠아마린", "사파이어", "잉크",
    "에메랄드", "루비", "분노", "토파즈",
    "결정화", "현기증", "원자", "수소", "레어", "자연",
    "굿", "희귀", "일반",
]

denominators_battle = {
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": 7500000000, "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": 2222222222,
    "사도:베일": 800000000, "수확가": 666000000, "악몽의 하늘": 190000000,
    "𝓘𝓬𝓮𝓐𝓰𝓮": 1500000000, "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": 300000000,
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": 200000000, "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": 175000000, "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": 100000000,
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": 1730400000, "감시자": 45000000,
    "아쿠아리움": 80000000, "선원": 12000000, "샤킨": 10000000, "포세이돈": 4000000, "에바네샌트": 3360000,
    "기원": 6500000, "망령": 4100000,
    "듀라한": 72000000, "영혼 사냥꾼": 40000000, "묘화": 21000000, "밤나팔꽃": 10000000, "바이탈": 6000000, "룬(나이트)": 1000000, "펌프": 200000,
    "블리자드": 27315000, "이상": 24691356, "크로마틱": 20000000, "자장가": 17000000,
    "그래피티": 12000000, "헬리오스": 9000000, "속력": 7630000, "황혼": 6000000,
    "아파타이트": 3133133, "대마법사": 1766000, "아케인": 1000000, "워록": 660000,
    "테러": 400000, "바운디드": 200000, "재즈": 160000, "스펙터": 140000,
    "이색": 99999, "노틸러스": 70000, "아쿠아틱": 40000,
    "만년서리": 73500, "태양": 50000, "달": 50000, "와트": 32768,
    "힘": 16384, "카와이": 12300, "석영": 8192, "출혈": 4444,
    "시데리움": 4096, "콜라": 3999, "빙하": 2304, "재": 2300,
    "자력": 2048, "글록": 1700, "아쿠아마린": 900, "사파이어": 800, "잉크": 700,
    "에메랄드": 500, "루비": 350, "분노": 256, "토파즈": 150,
    "결정화": 128, "현기증": 123, "원자": 1180, "수소": 1111, "레어": 16, "자연": 8,
    "굿": 5, "희귀": 4, "일반": 2,
}

base_weights_battle = [max(1, int(7500000000000 / denominators_battle[item])) for item in items_battle]

# 2. 마스터 핸드 뽑기 창 전용 등급 및 확률 정의
items_gacha = [
    "🌟 𝓜𝓪𝓼𝓽𝓮𝓻 𝓗𝓪𝓷𝓭 🌟", "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭", "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻", "𝓘𝓬𝓮𝓐𝓰𝓮", 
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒", "사도:베일", "수확가", "𝓜𝓪𝓶𝓶𝓸𝓽𝓱", 
    "악몽의 하늘", "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤", "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐", 
    "감시자", "아쿠아리움", "선원", "샤킨", "포세이돈", "에바네샌트", 
    "기원", "망령", "듀라한", "대마법사", "아케인"
]

denominators_gacha = {
    "🌟 𝓜𝓪𝓼𝓽𝓮𝓻 𝓗𝓪𝓷𝓭 🌟": 50000000000,
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": 7500000000, 
    "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": 2222222222, 
    "𝓘𝓬𝓮𝓐𝓰𝓮": 1500000000, 
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": 1730400000, 
    "사도:베일": 800000000, 
    "수확가": 666000000, 
    "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": 300000000, 
    "악몽의 하늘": 190000000, 
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": 200000000, 
    "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": 175000000, 
    "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": 100000000, 
    "감시자": 45000000,
    "아쿠아리움": 80000000, 
    "선원": 12000000, 
    "샤킨": 10000000, 
    "포세이돈": 4000000, 
    "에바네샌트": 3360000,
    "기원": 6500000, 
    "망령": 4100000,
    "듀라한": 72000000,
    "대마법사": 1766000, 
    "아케인": 1000000
}

base_weights_gacha = [max(1, int(500000000000000 / denominators_gacha[item])) for item in items_gacha]

icons = {
    "🌟 𝓜𝓪𝓼𝓽𝓮𝓻 𝓗𝓪𝓷𝓭 🌟": "🖐️💫👑🔥",
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": "🖐️✨🌌👑", "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": "🕸️🌙✨🦋",
    "사도:베일": "🎃👁️", "수확가": "🎃🗡️", "악몽의 하늘": "🎃🌌",
    "𝓘𝓬𝓮𝓐𝓰𝓮": "❄️🧊👑", "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": "🦣❄️🧊",
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": "🌈💎✨", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": "🎼🎻✨♠️", "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": "🌌💠💫",
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": "🌊🐉🌀", "감시자": "👁️‍🗨️⚡",
    "아쿠아리움": "🐠🌊🏛️", "선원": "⚓⛵🌊", "샤킨": "🦈🌊⚡", "포세이돈": "🔱🌊🌊", "에바네샌트": "🌀✨🌌",
    "기원": "🌌✨", "망령": "👻⚡", "듀라한": "🎃🛡️",
    "대마법사": "🧙‍♂️✨", "아케인": "🔮👑",
}

AI_NAMES_POOL = [
    "별빛수호자", "그림자사냥꾼", "운명의주사위", "우주여행자", "푸른늑대", "붉은용기사", "새벽의별", "은하수방랑자", "천둥번개", "얼음여왕",
    "불꽃심장", "바람의노래", "황금기사", "심연의눈", "달빛검객", "태양의아들", "폭풍전사", "신비한마법사", "고대의현자", "어둠의군주",
    "빛의사도", "영혼수확자", "시간여행자", "차원문지기", "무지개빛", "수정구슬", "백야의늑대", "적월의기사", "창공의매", "대지의수호자",
    "파도의노래", "심해탐험가", "구름위의산책", "별똥별", "혜성처럼", "블랙홀", "화이트나이트", "다크섀도우", "실버스타", "골든크라운",
    "루비드래곤", "사파이어윙", "에메랄드포레스트", "다이아몬드", "토파즈스파크", "아메시스트", "오팔광채", "진주조개", "호박보석", "비취옥",
    "청룡의기운", "백호의포효", "주작의날개", "현무의방패", "기린의축복", "봉황의눈물", "해태의심판", "도깨비불", "구미호", "산신령",
    "용왕의아들", "선녀와나무꾼", "홍길동", "전우치", "이순신", "세종대왕", "광개토대왕", "을지문덕", "강감찬", "계백장군",
    "아르테미스", "아폴론", "포세이돈후예", "제우스의번개", "아테나지혜", "헤르메스발걸음", "아레스전쟁", "헤파이스토스", "디오니소스", "하데스그림자",
    "오딘의까마귀", "토르의망치", "로키의장난", "프레이야", "발키리", "펜리르", "요르문간드", "헤임달", "티르", "발두르",
    "아서왕", "란슬롯", "멀린", "가웨인", "퍼시벌", "트리스탄", "갤러해드", "모드레드", "기네비어"
]

JOBS = {
    "도박사": "🎰 1억 이상 확률 2배! (100만 미만 획득 시 점수 0점, 아케인은 생존 가능)",
    "수집가": "📚 신규 아우라 최초 획득 시 보너스 점수 +20점",
    "암살자": "🗡️ 매 턴 순위표 아래 사람 점수 -15점 차감"
}

def check_synergies(owned_set):
  has_aqua = {"아쿠아리움", "샤킨", "포세이돈"}.issubset(owned_set)
  has_slow_ok = {"아쿠아리움", "샤킨", "포세이돈", "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒"}.issubset(owned_set)
  has_halloween = {"듀라한", "망령", "수확가"}.issubset(owned_set)
  has_welcome_hell = {"사도:베일", "악몽의 하늘"}.issubset(owned_set)
  has_music = {"자장가", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤"}.issubset(owned_set)
  return has_aqua, has_slow_ok, has_halloween, has_welcome_hell, has_music

def roll_battle_luck(extra_luck_mult=1.0, is_gambler=False, has_aqua_synergy=False):
  current_weights = list(base_weights_battle)
  luck_mult = 1000000.0 * extra_luck_mult
  min_denom = max(1, int(luck_mult))
  
  for idx, item in enumerate(items_battle):
    d = denominators_battle[item]
    if d < min_denom:
      current_weights[idx] = 0
    else:
      w = current_weights[idx] * luck_mult
      if is_gambler and d >= 100000000:
        w *= 2.0
      if has_aqua_synergy and item == "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒":
        w *= 2.0
      current_weights[idx] = max(1, int(w))
      
  return random.choices(items_battle, weights=current_weights, k=1)[0]

def roll_gacha_luck():
  current_weights = list(base_weights_gacha)
  luck_mult = 1000000
  eligible_indices = [idx for idx, item in enumerate(items_gacha) if denominators_gacha[item] >= luck_mult]
  for idx in range(len(items_gacha)):
    if idx not in eligible_indices:
      current_weights[idx] = 0
    else:
      current_weights[idx] = current_weights[idx] * luck_mult
  return random.choices(items_gacha, weights=current_weights, k=1)[0]

def get_boss_win_chance(best_denom):
  if best_denom >= 300000000: return 100
  elif best_denom >= 100000000: return 70
  elif best_denom >= 50000000: return 50
  elif best_denom >= 10000000: return 30
  elif best_denom >= 1000000: return 10
  return 5

if "game_started" not in st.session_state:
  st.session_state.game_started = False
if "turn_summary" not in st.session_state:
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
if "turn_logs" not in st.session_state:
  st.session_state.turn_logs = []

if "gacha_total_tries" not in st.session_state:
  st.session_state.gacha_total_tries = 0
if "gacha_first_records" not in st.session_state:
  st.session_state.gacha_first_records = {item: None for item in items_gacha}
if "gacha_latest_history" not in st.session_state:
  st.session_state.gacha_latest_history = []

def init_game(selected_job):
  ai_names = random.sample(AI_NAMES_POOL, 99)
  job_keys = list(JOBS.keys())
  participants = [{
      "id": 0,
      "name": "나 (플레이어)",
      "is_player": True,
      "job": selected_job,
      "status": "playing",
      "score": 0,
      "prev_overall_rank": 0,
      "curr_overall_rank": 0,
      "rank_diff": 0,
      "last_aura": "-",
      "last_denom": 0,
      "best_denom": 0,
      "best_aura": "-",
      "history": [],
      "owned_auras": set(),
      "best_100m_aura": None,
      "potions": 0,
      "use_potion_next": False,
      "buff_origin_turns": 0,
      "buff_prism_turns": 0,
      "buff_boss_turns": 0,
      "buff_music_turns": 0,
      "debuff_slow_turns": 0,
      "locked_turns": 0,
  }]
  for i in range(1, 100):
    participants.append({
        "id": i,
        "name": ai_names[i - 1],
        "is_player": False,
        "job": random.choice(job_keys),
        "status": "playing",
        "score": 0,
        "prev_overall_rank": 0,
        "curr_overall_rank": 0,
        "rank_diff": 0,
        "last_aura": "-",
        "last_denom": 0,
        "best_denom": 0,
        "best_aura": "-",
        "history": [],
        "owned_auras": set(),
        "best_100m_aura": None,
        "potions": 0,
        "use_potion_next": False,
        "buff_origin_turns": 0,
        "buff_prism_turns": 0,
        "buff_boss_turns": 0,
        "buff_music_turns": 0,
        "debuff_slow_turns": 0,
        "locked_turns": 0,
    })
  st.session_state.participants = participants
  st.session_state.turn = 0
  st.session_state.turn_summary = f"게임 시작! 직업: **[{selected_job}]** - '1턴 진행' 버튼을 눌러주세요."
  st.session_state.turn_logs = []
  st.session_state.game_started = True

st.title("⚔️ 아우라 종합 시뮬레이터")

tab_battle, tab_gacha, tab_synergy, tab_hof = st.tabs([
    "⚔️ 100인 포인트 배틀로얄", 
    "🎰 마스터 핸드 뽑기 창", 
    "📖 시너지 도감 & 설명", 
    "🏆 명예의 전당"
])

with tab_battle:
  if not st.session_state.game_started:
    st.markdown("""
    ### 📜 시스템 안내
    - **🎭 히든 직업**: 도박사(1억 이상 2배 / **100만 미만 획득 시 점수 0점** - 아케인은 생존), 수집가(+20점), 암살자(-15점)
    - **👑 10턴 주기 솔로 보스 레이드**: 승리 시 3턴간 행운 5배 폭증(🚀)!
    - **🧬 아우라 시너지**: 수족관(`[아쿠아]`, `[느려도 괜찮아]`), `[해피 할로윈]` (10턴마다 발동), `[웰컴 투더 헬]`, `[음악에 몸을 맡겨봐]`
    """)
    
    selected_job = st.radio(
        "🎭 플레이할 히든 직업을 선택하세요:",
        options=list(JOBS.keys()),
        format_func=lambda x: f"{x} — {JOBS[x]}"
    )
    
    if st.button("🚀 선택한 직업으로 배틀 시작하기", type="primary", use_container_width=True):
      init_game(selected_job)
      st.rerun()
    st.stop()

  participants = st.session_state.participants
  curr_turn = st.session_state.turn
  player_info = participants[0]

  alive_participants = [p for p in participants if p["status"] == "playing"]
  is_game_over = len(alive_participants) <= 1

  col_t1, col_t2, col_t3, col_t4 = st.columns(4)
  with col_t1:
    st.metric("진행 턴 수", f"{curr_turn} 턴", f"보스전까지 {10 - (curr_turn % 10)}턴" if curr_turn % 10 != 0 or curr_turn == 0 else "🔥 보스 턴!")
  with col_t2:
    st.metric("남은 생존자", f"{len(alive_participants)}명")
  with col_t3:
    st.metric("내 직업 / 최고 아우라", f"{player_info['job']}", f"{player_info['best_aura']}")
  with col_t4:
    p_status_str = "🏆 최종 우승!" if player_info["status"] == "winner" else ("💀 탈락" if player_info["status"] == "eliminated" else f"🎮 생존 (포션: {player_info['potions']}개)")
    st.metric("내 상태", p_status_str)

  status_icons = []
  if player_info.get("buff_music_turns", 0) > 0: status_icons.append(f"🎼 **음악 시너지 버프 (행운 50배!)** ({player_info['buff_music_turns']}턴 남음)")
  if player_info["buff_boss_turns"] > 0: status_icons.append(f"🚀 **보스 버프 (행운 5배)** ({player_info['buff_boss_turns']}턴 남음)")
  if player_info["use_potion_next"]: status_icons.append("🚀 **포션 대기중 (행운 2배)**")
  if player_info["buff_prism_turns"] > 0: status_icons.append(f"🚀 **프리즘 버프 (행운 2배)** ({player_info['buff_prism_turns']}턴 남음)")
  if player_info["debuff_slow_turns"] > 0: status_icons.append("🌀 **디버프 피격 (행운 2배 감소)**")

  if status_icons:
    st.warning("⚡ [내 행운 상태 변화]: " + " | ".join(status_icons))
  else:
    st.info("⚡ [내 행운 상태]: ⚪ 일반 상태 (버프/디버프 없음)")

  st.divider()

  def get_rank_diff_html(diff, curr_turn_num):
    if curr_turn_num <= 1:
      return "<span style='color:#888; font-size:12px;'>(NEW)</span>"
    if diff > 0:
      return f"<span style='color:#ff4b4b; font-weight:bold; font-size:13px;'>▲{diff}</span>"
    elif diff < 0:
      return f"<span style='color:#1c83e1; font-weight:bold; font-size:13px;'>▼{abs(diff)}</span>"
    else:
      return "<span style='color:#888; font-size:12px;'>-</span>"

  aura_colors = {
      "🌟 𝓜𝓪𝓼𝓽𝓮𝓻 𝓗𝓪𝓷𝓭 🌟": "background: linear-gradient(90deg, #ffcc00, #ff3366, #9900ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;",
      "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": "background: linear-gradient(90deg, #b92b27, #1565c0); -webkit-background-clip: text; -webkit-text-fill-color: transparent;",
      "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": "color: #ce93d8; text-shadow: 0 0 5px #ab47bc;",
      "𝓘𝓬𝓮𝓐𝓰𝓮": "color: #80d8ff; text-shadow: 0 0 5px #00b0ff;",
      "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": "color: #00e676; text-shadow: 0 0 5px #00c853;",
      "사도:베일": "color: #ffab40; text-shadow: 0 0 5px #ff9100;",
      "수확가": "color: #ff5252; text-shadow: 0 0 5px #ff1744;",
      "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": "color: #90caf9; text-shadow: 0 0 5px #42a5f5;",
      "악몽의 하늘": "color: #b388ff; text-shadow: 0 0 5px #7c4dff;",
      "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": "background: linear-gradient(90deg, #ff00de, #00ffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;",
      "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": "color: #ffd740; text-shadow: 0 0 5px #ffc107;",
      "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": "color: #69f0ae; text-shadow: 0 0 5px #00e676;"
  }

  def get_styled_name(p):
    name_text = f"{p['name']} (나)" if p["is_player"] else p["name"]
    if p["best_100m_aura"] and p["best_100m_aura"] in aura_colors:
      style = aura_colors[p["best_100m_aura"]]
      return f"<span style='{style} font-weight: 900;'>{name_text} ✨</span>"
    else:
      return f"<b>{name_text}</b>"

  def toggle_potion():
    if player_info["potions"] > 0:
      player_info["use_potion_next"] = not player_info["use_potion_next"]

  def process_point_turn():
    st.session_state.turn += 1
    t = st.session_state.turn
    alive = [p for p in participants if p["status"] == "playing"]
    
    turn_results = []
    special_events = []

    for idx, p in enumerate(alive):
      _, has_slow, _, _, _ = check_synergies(p["owned_auras"])
      if has_slow:
        for neighbor_idx in [idx - 1, idx + 1]:
          if 0 <= neighbor_idx < len(alive):
            alive[neighbor_idx]["debuff_slow_turns"] = 1
        if p["is_player"]:
          special_events.append("🐌 **[느려도 괜찮아 발동]** 양옆 참가자의 행운이 감소(🌀)되었습니다!")

    for idx, p in enumerate(alive):
      if p["locked_turns"] > 0:
        p["locked_turns"] -= 1
        p["last_aura"] = "🔒 [잠김]"
        p["last_denom"] = 0
        p["history"].append({"turn": t, "aura": "🔒 [잠김]", "denom": 0})
        turn_results.append(p)
        special_events.append(f"🔒 {p['name']}님은 잠금 상태라 꼴찌 처리되었습니다!")
        continue

      extra_mult = 1.0
      if p.get("buff_music_turns", 0) > 0:
        extra_mult *= 50.0
        p["buff_music_turns"] -= 1

      if p["buff_prism_turns"] > 0:
        extra_mult *= 2.0
        p["buff_prism_turns"] -= 1
      
      if p["buff_boss_turns"] > 0:
        extra_mult *= 5.0
        p["buff_boss_turns"] -= 1

      if p["debuff_slow_turns"] > 0:
        extra_mult *= 0.5
        p["debuff_slow_turns"] -= 1
      
      if p["is_player"] and p["use_potion_next"] and p["potions"] > 0:
        p["potions"] -= 1
        p["use_potion_next"] = False
        extra_mult *= 2.0
        special_events.append("🧪 **[행운 포션 사용!]** 플레이어님의 행운이 증가(🚀)했습니다!")
      elif not p["is_player"] and p["potions"] > 0 and random.random() < 0.3:
        p["potions"] -= 1
        extra_mult *= 2.0

      has_aqua, _, _, _, _ = check_synergies(p["owned_auras"])
      is_gambler = (p["job"] == "도박사")

      aura = roll_battle_luck(extra_mult, is_gambler=is_gambler, has_aqua_synergy=has_aqua)
      denom = denominators_battle[aura]
      p["last_aura"] = aura
      p["last_denom"] = denom
      p["history"].append({"turn": t, "aura": aura, "denom": denom})
      
      if denom > p["best_denom"]:
        p["best_denom"] = denom
        p["best_aura"] = aura

      is_new_aura = aura not in p["owned_auras"]
      p["owned_auras"].add(aura)
      if p["job"] == "수집가" and is_new_aura:
        p["score"] += 20
        if p["is_player"]:
          special_events.append(f"📚 **[수집가 보너스]** 신규 아우라 `{aura}` 발견 (📈 +20점)!")

      if denom >= 100000000:
        if p["best_100m_aura"] is None or denominators_battle[p["best_100m_aura"]] < denom:
          p["best_100m_aura"] = aura

      turn_results.append(p)

      if denom >= 100000000:
        if aura == "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭":
          p["buff_origin_turns"] = 3
          ai_alive = [x for x in alive if not x["is_player"] and x != p and x["status"] == "playing"]
          random.shuffle(ai_alive)
          cut_count = len(ai_alive) // 2
          eliminated_by_origin = ai_alive[:cut_count]
          for victim in eliminated_by_origin:
            victim["status"] = "eliminated"
          special_events.append(f"🖐️ **[태초의 권능!]** 오리진 핸드 발동! AI **{cut_count}명** 즉시 소멸!")
        elif aura == "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻":
          total_absorbed = 0
          for neighbor_idx in [idx - 1, idx + 1]:
            if 0 <= neighbor_idx < len(alive):
              target_n = alive[neighbor_idx]
              target_n["locked_turns"] = 2
              absorbed = target_n["score"] // 3
              target_n["score"] -= absorbed
              p["score"] += absorbed
              total_absorbed += absorbed
          special_events.append(f"🕸️ **[드림캐쳐]** 주변 인물 2턴 잠금 및 총 점수 1/3({total_absorbed}점) 흡수!")
        elif aura == "𝓘𝓬𝓮𝓐𝓰𝓮":
          for neighbor_idx in [idx - 1, idx + 1]:
            if 0 <= neighbor_idx < len(alive):
              alive[neighbor_idx]["locked_turns"] = 1
          special_events.append(f"❄️ **[아이스 에이지]** 주변 인물 1턴 얼어붙음!")
        elif aura == "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒":
          other_alive = [x for x in alive if x != p and x["status"] == "playing"]
          if other_alive:
            top_one = max(other_alive, key=lambda x: x["score"])
            top_one["status"] = "eliminated"
            p["score"] = top_one["score"] + 100
            special_events.append(f"🐉 **[리바이어던]** 1등({top_one['name']}) 제거 및 자리 탈취!")
        elif aura == "수확가":
          neighbors = []
          if idx > 0: neighbors.append(alive[idx - 1])
          if idx < len(alive) - 1: neighbors.append(alive[idx + 1])
          if neighbors:
            target = random.choice(neighbors)
            stolen = target["score"] // 2
            target["score"] -= stolen
            p["score"] += stolen
            special_events.append(f"🗡️ **[수확가]** {target['name']}님의 점수 절반 흡수!")
        elif aura == "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧":
          p["buff_prism_turns"] = 2
          special_events.append(f"💎 **[프리즘]** 행운 증가(🚀)!")
        elif aura == "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐":
          if idx > 0:
            above_person = alive[idx - 1]
            above_person["status"] = "eliminated"
            special_events.append(f"💠 **[스펙트라]** 윗사람 즉시 제거!")

    for p in alive:
      if p["buff_origin_turns"] > 0:
        p["buff_origin_turns"] -= 1
        p["last_denom"] = 999999999999

    current_alive_after_powers = [p for p in alive if p["status"] == "playing"]
    turn_results = [p for p in turn_results if p in current_alive_after_powers]
    turn_results.sort(key=lambda x: x["last_denom"], reverse=True)

    total_alive = len(current_alive_after_powers)
    for rank_idx, p in enumerate(turn_results):
      if p["job"] == "도박사" and p["last_denom"] < 1000000:
        earned_score = 0
        if p["is_player"]:
          special_events.append(f"🎰 **[도박사 리스크]** 100만 미만(`{p['last_aura']}`) 획득으로 이번 턴 점수 0점 하락(📉)!")
      else:
        earned_score = max(1, 100 - int((rank_idx / max(1, total_alive - 1)) * 99)) if total_alive > 1 else 100
      
      p["score"] += earned_score
      p["last_turn_rank"] = rank_idx + 1
      p["last_earned"] = earned_score

    alive_sorted_by_score = sorted(current_alive_after_powers, key=lambda x: (x["score"], x["last_denom"]), reverse=True)

    # [시너지: 해피 할로윈] (듀라한+망령+수확가) - 10턴마다 1번 발동
    if t % 10 == 0:
      for idx, p in enumerate(alive_sorted_by_score):
        _, _, has_halloween, _, _ = check_synergies(p["owned_auras"])
        if has_halloween:
          start_range = max(0, idx - 5)
          end_range = min(len(alive_sorted_by_score), idx + 6)
          candidates = [alive_sorted_by_score[i] for i in range(start_range, end_range) if i != idx]
          if candidates:
            target = random.choice(candidates)
            stolen_score = target["score"] // 2
            target["score"] -= stolen_score
            p["score"] += stolen_score
            target["last_earned"] = target.get("last_earned", 0) // 2
            if p["is_player"]:
              special_events.append(f"🎃 **[해피 할로윈 발동!]** 10턴 주기로 근처 10위 내 {target['name']}님의 점수 절반({stolen_score}점) 강탈!")

    # [암살자] 점수 차감
    for overall_idx, p in enumerate(alive_sorted_by_score):
      if p["job"] == "암살자" and overall_idx + 1 < len(alive_sorted_by_score):
        target_below = alive_sorted_by_score[overall_idx + 1]
        target_below["score"] = max(0, target_below["score"] - 15)
        if p["is_player"]:
          special_events.append(f"🗡️ **[암살자 스킬]** 바로 아래 순위({target_below['name']})의 점수 하락(📉 -15점)!")

    alive_sorted_by_score = sorted(current_alive_after_powers, key=lambda x: (x["score"], x["last_denom"]), reverse=True)
    for overall_idx, p in enumerate(alive_sorted_by_score, 1):
      if t == 1:
        p["prev_overall_rank"] = overall_idx
        p["curr_overall_rank"] = overall_idx
        p["rank_diff"] = 0
      else:
        p["prev_overall_rank"] = p["curr_overall_rank"]
        p["curr_overall_rank"] = overall_idx
        p["rank_diff"] = p["prev_overall_rank"] - p["curr_overall_rank"]

    if t % 10 == 0:
      boss_winners = []
      for p in alive_sorted_by_score:
        win_chance = get_boss_win_chance(p["best_denom"])
        is_win = random.randint(1, 100) <= win_chance
        if is_win:
          p["buff_boss_turns"] = 3
          boss_winners.append(p["name"])
          if p["is_player"]:
            special_events.append(f"👑 **[보스 레이드 승리!]** 행운 대폭 증가(🚀 5배)!")
        else:
          if p["is_player"]:
            special_events.append(f"🛡️ **[보스 레이드 패배]** 토벌 실패")
      if boss_winners:
        special_events.append(f"⚔️ [{t}턴 보스 토벌 성공자 {len(boss_winners)}명]: 행운 증가(🚀 3턴)")

    elimination_count = 2 if any(p["last_aura"] == "악몽의 하늘" for p in turn_results) else 1

    # [시너지: 웰컴 투더 헬] (사도:베일 + 악몽의 하늘) 추가 탈락자 발생
    welcome_hell_extra_elim = 0
    for idx, p in enumerate(alive_sorted_by_score):
      _, _, _, has_welcome_hell, _ = check_synergies(p["owned_auras"])
      if has_welcome_hell:
        welcome_hell_extra_elim += 1
        if p["is_player"]:
          special_events.append(f"🎪 **[웰컴 투더 헬!]** 근처 10위 내 전장에서 추가 탈락자 발생!")

    total_elimination_count = elimination_count + welcome_hell_extra_elim

    eliminated_this_turn = []
    for _ in range(total_elimination_count):
      active_pool = [x for x in alive_sorted_by_score if x["status"] == "playing"]
      if active_pool:
        low_p = active_pool[-1]
        low_p["status"] = "eliminated"
        eliminated_this_turn.append(low_p)
        alive_sorted_by_score.remove(low_p)

    # [시너지: 음악에 몸을 맡겨봐] (자장가 + 심포니)
    grid_sorted = sorted(participants, key=lambda x: (0 if x["status"] in ["playing", "winner"] else 1, -x["score"]))
    for g_idx, p in enumerate(grid_sorted):
      if p["status"] == "playing":
        _, _, _, _, has_music = check_synergies(p["owned_auras"])
        if has_music:
          row_start = (g_idx // 3) * 3
          row_members = grid_sorted[row_start : row_start + 3]
          if any(m != p and m["last_denom"] >= 100000000 for m in row_members):
            p["buff_music_turns"] = 1
            if p["is_player"]:
              special_events.append("🎼 **[음악에 몸을 맡겨봐!]** 같은 줄 참가자가 1억 이상 아우라를 뽑아 다음 턴 행운 50배 폭증(🚀)!")

    for p in participants:
      if p["status"] == "playing":
        p["potions"] += 1

    final_alive = [p for p in participants if p["status"] == "playing"]
    if len(final_alive) <= 1:
      for p in final_alive:
        p["status"] = "winner"
        p["curr_overall_rank"] = 1

    new_logs = []
    for p in turn_results:
      is_elim = p in eliminated_this_turn
      new_logs.append({
          "name": p["name"],
          "is_player": p["is_player"],
          "job": p["job"],
          "aura": p["last_aura"],
          "denom": p["last_denom"],
          "turn_rank": p.get("last_turn_rank", 99),
          "earned": p.get("last_earned", 0),
          "total_score": p["score"],
          "rank_diff": p["rank_diff"],
          "eliminated_now": is_elim,
          "best_100m_aura": p["best_100m_aura"],
          "buff_boss": p["buff_boss_turns"] > 0,
          "buff_prism": p["buff_prism_turns"] > 0,
          "buff_music": p.get("buff_music_turns", 0) > 0,
          "debuff_slow": p["debuff_slow_turns"] > 0
      })

    elim_names = ", ".join([e["name"] for e in eliminated_this_turn]) if eliminated_this_turn else "없음"
    summary_text = f"📢 [{t}턴 결과] 1위: **{turn_results[0]['name']}** ({turn_results[0]['last_aura']}) | 탈락: **{elim_names}** (🧪 포션 +1)"
    if special_events:
      summary_text += " | ✨ " + " / ".join(special_events)

    st.session_state.turn_logs = new_logs
    st.session_state.turn_summary = summary_text

  with st.container(border=True):
    col_p_info1, col_p_info2, col_p_info3, col_p_info4 = st.columns([1.8, 1.8, 1.8, 1])
    with col_p_info1:
      st.markdown(f"🧪 **보유 행운 포션**: `{player_info['potions']}개`")
    with col_p_info2:
      status_msg = "🟢 [포션 사용 대기 🚀]" if player_info["use_potion_next"] else "⚪ [미사용]"
      st.markdown(f"포션 상태: {status_msg}")
    with col_p_info3:
      boss_chance = get_boss_win_chance(player_info["best_denom"])
      st.markdown(f"👑 **보스 승리 확률**: `{boss_chance}%`")
    with col_p_info4:
      if player_info["status"] == "playing" and player_info["potions"] > 0:
        btn_label = "포션 취소" if player_info["use_potion_next"] else "🧪 포션 마시기"
        if st.button(btn_label, use_container_width=True, type="primary" if not player_info["use_potion_next"] else "secondary"):
          toggle_potion()
          st.rerun()

  if not is_game_over:
    next_t = curr_turn + 1
    boss_tag = " [👑 보스 레이드!]" if next_t % 10 == 0 else ""
    btn_label = f"🎲 {next_t}턴 진행{boss_tag}" if player_info["status"] == "playing" else f"👁️ {next_t}턴 관전{boss_tag}"
    if st.button(btn_label, type="primary", use_container_width=True):
      process_point_turn()
      st.rerun()
  else:
    winner = next((p for p in participants if p["status"] in ["winner", "playing"]), None)
    if winner and winner["is_player"]:
      st.balloons()
      st.success("🏆 축하합니다! 최종 우승하셨습니다!")
    elif winner:
      st.success(f"👑 최종 우승자는 **[{winner['name']}]**입니다!")
    if st.button("🔄 새 게임 시작하기", type="primary", use_container_width=True):
      st.session_state.game_started = False
      st.rerun()

  st.info(st.session_state.turn_summary)

  col_left, col_right = st.columns([1, 1.4])
  with col_left:
    if is_game_over:
      winner = next((p for p in participants if p["status"] in ["winner", "playing"]), None)
      st.subheader(f"🏆 최종 우승자 [{winner['name']}] 기록")
      with st.container(height=600, border=True):
        st.markdown(f"**직업:** `{winner['job']}` | **누적 점수:** `{winner['score']}점`")
        st.divider()
        best_win_aura = max(winner["history"], key=lambda x: x["denom"])
        st.success(f"🌟 **최고 기록:** {icons.get(best_win_aura['aura'], '✨')} **{best_win_aura['aura']}** (`1 in {best_win_aura['denom']:,}`)")
        for h in winner["history"]:
          st.markdown(f"- **{h['turn']}턴**: {icons.get(h['aura'], '✨')} **{h['aura']}** (`1 in {h['denom']:,}`)")
    else:
      st.subheader(f"📋 이번 턴({curr_turn}턴) 순위")
      with st.container(height=600, border=True):
        if not st.session_state.turn_logs:
          st.caption("아직 진행된 턴이 없습니다.")
        else:
          for log in st.session_state.turn_logs:
            diff_html = get_rank_diff_html(log["rank_diff"], curr_turn)
            log_name_text = f"{log['name']} (나)" if log["is_player"] else log['name']
            if log["best_100m_aura"] and log["best_100m_aura"] in aura_colors:
              style = aura_colors[log["best_100m_aura"]]
              name_str = f"<span style='{style} font-weight: 900;'>{log_name_text} ✨</span>"
            else:
              name_str = f"<b>{log_name_text}</b>"

            job_tag = f"<span style='color:#888; font-size:12px;'>[{log['job']}]</span>"
            
            status_badge = ""
            if log.get("buff_boss") or log.get("buff_prism") or log.get("buff_music"): status_badge += " <span style='color:#ff4b4b;'>🚀증가</span>"
            if log.get("debuff_slow"): status_badge += " <span style='color:#1c83e1;'>🌀감소</span>"

            aura_str = f"{icons.get(log['aura'], '✨')} {log['aura']} (1 in {log['denom']:,})" if log['denom'] > 0 else f"{log['aura']}"
            elim_badge = " <span style='color:#ff4b4b; font-weight:bold;'>[💀 탈락]</span>" if log["eliminated_now"] else ""
            
            st.markdown(f"<div style='padding: 4px 0; border-bottom: 1px solid rgba(128,128,128,0.2);'><b>{log['turn_rank']}위</b> | {name_str} {job_tag}{status_badge} {diff_html} : {aura_str} | <code>+{log['earned']}점</code> (누적 <b>{log['total_score']}점</b>){elim_badge}</div>", unsafe_allow_html=True)

  with col_right:
    st.subheader("👥 참가자 현황판")
    
    filter_col1, filter_col2 = st.columns([1.5, 1])
    with filter_col1:
      filter_option = st.selectbox(
          "참가자 필터",
          ["전체 보기", "생존자만 보기", "1억 이상 아우라 보유자", "시너지 보유자"],
          label_visibility="collapsed"
      )
    with filter_col2:
      search_query = st.text_input("이름 검색", placeholder="참가자 검색", label_visibility="collapsed")

    filtered_participants = participants
    if filter_option == "생존자만 보기":
      filtered_participants = [p for p in participants if p["status"] == "playing"]
    elif filter_option == "1억 이상 아우라 보유자":
      filtered_participants = [p for p in participants if p["best_denom"] >= 100000000]
    elif filter_option == "시너지 보유자":
      filtered_participants = [p for p in participants if any(check_synergies(p["owned_auras"]))]

    if search_query:
      filtered_participants = [p for p in filtered_participants if search_query in p["name"]]

    sorted_participants = sorted(filtered_participants, key=lambda x: (0 if x["status"] in ["playing", "winner"] else 1, -x["score"]))
    
    with st.container(height=520, border=True):
      if not sorted_participants:
        st.caption("조건에 맞는 참가자가 없습니다.")
      else:
        cols_per_row = 3
        for i in range(0, len(sorted_participants), cols_per_row):
          row_items = sorted_participants[i : i + cols_per_row]
          grid_cols = st.columns(cols_per_row)
          for idx, p in enumerate(row_items):
            with grid_cols[idx]:
              is_eliminated = (p["status"] == "eliminated")
              bg_css = "background-color: rgba(255, 0, 0, 0.15); padding: 4px; border-radius: 6px;" if is_eliminated else ""
              
              st.markdown(f"<div style='{bg_css}'>", unsafe_allow_html=True)
              with st.container(border=True):
                rank_badge = f"#{p['curr_overall_rank']} " if curr_turn > 0 and p["status"] in ["playing", "winner"] else ""
                diff_html = get_rank_diff_html(p["rank_diff"], curr_turn) if curr_turn > 0 and p["status"] in ["playing", "winner"] else ""
                status_txt = "🏆 우승" if p["status"] == "winner" else ("🟢 생존" if p["status"] == "playing" else "💀 탈락")
                styled_name = get_styled_name(p)
                
                p_aq, p_sl, p_hw, p_wh, p_mu = check_synergies(p["owned_auras"])
                syn_tags = ""
                if p_mu: syn_tags += " 🎼"
                if p_wh: syn_tags += " 🎪"
                if p_hw: syn_tags += " 🎃"
                if p_sl: syn_tags += " 🐌"
                elif p_aq: syn_tags += " 🌊"
                
                p_badge = ""
                if p["buff_boss_turns"] > 0 or p["buff_prism_turns"] > 0 or p.get("buff_music_turns", 0) > 0: p_badge += " 🚀"
                if p["debuff_slow_turns"] > 0: p_badge += " 🌀"
                
                st.markdown(f"<div style='font-size:14px;'><b>{rank_badge}</b>{styled_name}{syn_tags}{p_badge} {diff_html}</div>", unsafe_allow_html=True)
                st.caption(f"{status_txt} | [{p['job']}] | 누적: **{p['score']}점**")
                
                with st.expander("🔍 상세 정보"):
                  st.markdown(f"**최고 아우라**: {icons.get(p['best_aura'], '✨')} `{p['best_aura']}`")
                  st.markdown(f"**보유 포션**: {p['potions']}개")
                  st.markdown(f"**수집한 아우라 종류**: {len(p['owned_auras'])}개")
                  if p["history"]:
                    recent_history = p["history"][-3:]
                    st.markdown("**최근 3턴 기록**:")
                    for rh in recent_history:
                      st.caption(f"- {rh['turn']}턴: {rh['aura']} (1 in {rh['denom']:,})")
              st.markdown("</div>", unsafe_allow_html=True)

  st.divider()
  st.subheader("🍀 이번 게임 실시간 최고 행운 랭킹 (TOP 10)")
  all_battle_luck = []
  for p in participants:
    for h in p["history"]:
      if h["denom"] > 0 and h["aura"] != "🔒 [잠김]":
        all_battle_luck.append({
            "name": p["name"],
            "is_player": p["is_player"],
            "job": p["job"],
            "turn": h["turn"],
            "aura": h["aura"],
            "denom": h["denom"]
        })
  if all_battle_luck:
    all_battle_luck.sort(key=lambda x: x["denom"], reverse=True)
    with st.container(border=True):
      for r_idx, rec in enumerate(all_battle_luck[:10], 1):
        p_label = f"{rec['name']} (나)" if rec['is_player'] else rec['name']
        icon = icons.get(rec['aura'], "✨")
        st.markdown(f"**{r_idx}위** | 👤 **{p_label}** ([{rec['job']}]) — **{rec['turn']}턴**에 {icon} `{rec['aura']}` 획득! (`1 in {rec['denom']:,}`)")
  else:
    st.caption("아직 턴이 진행되지 않았습니다.")


with tab_gacha:
  st.subheader("🎰 마스터 핸드 전용 백만배 행운 뽑기 창")
  st.markdown("백만배 행운이 적용된 상태로 **아케인**부터 최고 등급인 **마스터 핸드**까지 직접 뽑고, 각 등급별 최초 획득 횟수를 확인해보세요!")

  def execute_gacha(count):
    for _ in range(count):
      st.session_state.gacha_total_tries += 1
      tries = st.session_state.gacha_total_tries
      aura = roll_gacha_luck()
      denom = denominators_gacha[aura]
      
      if st.session_state.gacha_first_records[aura] is None:
        st.session_state.gacha_first_records[aura] = tries
        
      st.session_state.gacha_latest_history.insert(0, {"tries": tries, "aura": aura, "denom": denom})
      if len(st.session_state.gacha_latest_history) > 10:
        st.session_state.gacha_latest_history.pop()

  col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
  with col_btn1:
    if st.button("🎲 1회 뽑기", type="primary", use_container_width=True):
      execute_gacha(1)
      st.rerun()
  with col_btn2:
    if st.button("✨ 5회 연속 뽑기", type="primary", use_container_width=True):
      execute_gacha(5)
      st.rerun()
  with col_btn3:
    if st.button("🔄 기록 초기화", use_container_width=True):
      st.session_state.gacha_total_tries = 0
      st.session_state.gacha_first_records = {item: None for item in items_gacha}
      st.session_state.gacha_latest_history = []
      st.rerun()

  st.divider()

  col_gacha_left, col_gacha_right = st.columns([3, 4])

  with col_gacha_left:
    st.markdown(f"### 📊 누적 뽑기 횟수: `{st.session_state.gacha_total_tries}회`")
    st.markdown("#### 🏆 등급별 최초 획득 기록")
    
    with st.container(height=450, border=True):
      acquired_records = {k: v for k, v in st.session_state.gacha_first_records.items() if v is not None}
      slowest_aura = max(acquired_records, key=acquired_records.get) if acquired_records else None

      for item in items_gacha:
        tries_got = st.session_state.gacha_first_records[item]
        icon = icons.get(item, "✨")
        denom_str = f"1 in {denominators_gacha[item]:,}"
        
        if tries_got is not None:
          slow_badge = " 🐢 **[제일 늦게 뜸!]**" if item == slowest_aura else ""
          st.markdown(f"- {icon} **{item}** (`{denom_str}`) : **{tries_got}회째** 최초 획득!{slow_badge}")
        else:
          st.markdown(f"- {icon} <span style='color:gray;'>{item} (`{denom_str}`) : 미획득</span>", unsafe_allow_html=True)

  with col_gacha_right:
    st.markdown("#### 📜 최근 뽑기 결과 (최신 10개)")
    with st.container(height=450, border=True):
      if not st.session_state.gacha_latest_history:
        st.caption("아직 뽑은 기록이 없습니다.")
      else:
        for hist in st.session_state.gacha_latest_history:
          icon = icons.get(hist["aura"], "✨")
          st.markdown(f"• **{hist['tries']}회차** | {icon} **{hist['aura']}** (`1 in {hist['denom']:,}`)")


with tab_synergy:
  st.subheader("📖 아우라 시너지 도감 및 상세 설명")
  st.markdown("게임 내에서 특정 아우라 조합을 모으면 발동하는 **강력한 시너지 효과**들을 한눈에 확인하세요!")

  st.markdown("---")

  col_s1, col_s2 = st.columns(2)

  with col_s1:
    with st.container(border=True):
      st.markdown("### 🎃 1. 해피 할로윈 (10턴 주기 발동)")
      st.markdown("**조합 아우라**: 듀라한 + 망령 + 수확가")
      st.markdown("**이모티콘**: 🎃👻🗡️")
      st.markdown("""
      > **효과 설명**:
      > **매 10턴마다** 해당 턴 순위표에서 본인 근처 **10등 사이(상하 5위 이내)**에 있는 플레이어 중 **1명의 점수 절반을 강탈**합니다! 
      > 점수를 뺏긴 대상은 이번 턴에 획득할 점수를 **반토막(절반)**밖에 받지 못하는 치명적인 디버프를 받습니다.
      """)

    with st.container(border=True):
      st.markdown("### 🌊 2. 아쿠아 (수족관)")
      st.markdown("**조합 아우라**: 아쿠아리움 + 샤킨 + 포세이돈")
      st.markdown("**이모티콘**: 🐠🦈🔱")
      st.markdown("""
      > **효과 설명**:
      > 심해의 기운이 모여, 최고 등급 아우라 중 하나인 **레비아탄(`༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒`)이 등장할 확률이 2배 증가**합니다!
      """)

    with st.container(border=True):
      st.markdown("### 🎼 3. 음악에 몸을 맡겨봐")
      st.markdown("**조합 아우라**: 자장가 + 심포니(`𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤`)")
      st.markdown("**이모티콘**: 🎼🎶")
      st.markdown("""
      > **효과 설명**:
      > 참가자 현황판에서 **본인과 같은 가로줄(행)에 있는 사람** 중 누군가 **1억 이상의 아우라**를 뽑는다면, 그 **다음 턴에 행운이 50배 증가(🚀)**합니다!
      """)

  with col_s2:
    with st.container(border=True):
      st.markdown("### 🎪 4. 웰컴 투더 헬")
      st.markdown("**조합 아우라**: 사도:베일 + 악몽의 하늘")
      st.markdown("**이모티콘**: 🎃👁️🌌")
      st.markdown("""
      > **효과 설명**:
      > 지옥의 문이 열리며, 본인 근처 사이 **10등 이내의 전장에서 매 턴마다 추가 탈락자가 1명씩 더 발생**합니다! 
      > 주변 플레이어들의 생존을 위협하는 공포의 시너지입니다.
      """)

    with st.container(border=True):
      st.markdown("### 🐌 5. 느려도 괜찮아 (수족관 심화)")
      st.markdown("**조합 아우라**: 아쿠아리움 + 샤킨 + 포세이돈 + 레비아탄")
      st.markdown("**이모티콘**: 🐠🦈🔱🌊")
      st.markdown("""
      > **효과 설명**:
      > 수족관의 최종 완성 형태! 매 턴마다 **본인의 양옆(위아래 순위)에 있는 사람들에게 행운 2배 감소 디버프(🌀)**를 영구적으로 부여합니다.
      """)


with tab_hof:
  st.subheader("🏆 명예의 전당 (Hall of Fame)")
  st.markdown("아우라 시뮬레이터 배틀로얄 역사에 빛나는 전설적인 우승자들의 기록관입니다.")

  st.markdown("---")

  col_season1, col_season2 = st.columns(2)

  # 🌟 시즌 1 우승자 카드
  with col_season1:
    with st.container(border=True):
      st.markdown("### 🥇 시즌 1 챔피언")
      st.markdown("👑 **우승자**: `실버스타`")
      st.markdown("- **최종 점수**: `4,968점`")
      st.markdown("- **사용 시너지**: `느려도 괜찮아 🐌`")
      st.caption("완벽한 디버프 진형을 구축하여 100인 배틀로얄의 정상에 오른 기념비적인 시즌 1 우승 기록입니다.")

  # 🌟 시즌 2 우승자 카드
  with col_season2:
    with st.container(border=True):
      st.markdown("### 🥇 시즌 2 챔피언")
      st.markdown("👑 **우승자**: `헤파이스토스`")
      st.markdown("- **최종 점수**: `4,815점`")
      st.markdown("- **사용 시너지**: `시너지 없음`")
      st.caption("어떠한 시너지 조합에도 의존하지 않고 오직 순수한 실력과 운만으로 왕좌를 차지한 시즌 2 우승 기록입니다.")

  col_season3, col_season4 = st.columns(2)

  # 🌟 시즌 3 우승자 카드
  with col_season3:
    with st.container(border=True):
      st.markdown("### 🥇 시즌 3 챔피언")
      st.markdown("👑 **우승자**: `무지개빛`")
      st.markdown("- **최종 점수**: `8,646점`")
      st.markdown("- **사용 시너지**: `아쿠아 🌊`, `웰컴 투더 헬 🎪`")
      st.caption("심해의 축복과 지옥의 전장을 동시에 지배하며 압도적인 점수 차로 왕좌에 오른 시즌 3 챔피언입니다.")

  # 🌟 시즌 4 우승자 카드 (신규 등재)
  with col_season4:
    with st.container(border=True):
      st.markdown("### 🥇 시즌 4 챔피언")
      st.markdown("👑 **우승자**: `오딘의 까마귀`")
      st.markdown("- **최종 점수**: `4,923점`")
      st.markdown("- **사용 시너지**: `아쿠아 🌊`")
      st.caption("심해의 기운(아쿠아)을 활용해 흔들림 없는 상위권 운영을 선보이며 시즌 4 왕좌를 차지한 챔피언입니다.")

  st.markdown("---")
  st.markdown("### 🍀 역대 가장 운이 좋은 사람 랭킹 (전체 게임 통산 실시간 집계)")
  st.markdown("현재 진행 중이거나 지금까지 플레이한 모든 턴 중에서 **가장 희귀하고 확률이 낮은(분모가 큰) 아우라**를 뽑은 행운의 주인공들을 실시간으로 집계합니다!")

  if st.session_state.game_started and 'participants' in st.session_state:
    all_history_records = []
    for p in st.session_state.participants:
      for h in p["history"]:
        if h["denom"] > 0 and h["aura"] != "🔒 [잠김]":
          all_history_records.append({
              "name": p["name"],
              "is_player": p["is_player"],
              "job": p["job"],
              "turn": h["turn"],
              "aura": h["aura"],
              "denom": h["denom"]
          })
    
    if all_history_records:
      all_history_records.sort(key=lambda x: x["denom"], reverse=True)
      
      with st.container(height=400, border=True):
        for rank_idx, rec in enumerate(all_history_records[:15], 1):
          p_label = f"{rec['name']} (나)" if rec['is_player'] else rec['name']
          icon = icons.get(rec['aura'], "✨")
          st.markdown(f"**{rank_idx}위** | 👤 **{p_label}** ([{rec['job']}]) — {rec['turn']}턴차에 {icon} `{rec['aura']}` 획득! (`1 in {rec['denom']:,}`)")
    else:
      st.info("아직 수집된 뽑기 기록이 없습니다. 게임을 진행해 주세요!")
  else:
    st.info("현재 진행 중인 게임이 없습니다. 배틀로얄 게임을 시작하고 턴을 진행하면 실시간으로 랭킹이 채워집니다!")
