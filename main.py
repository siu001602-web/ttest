import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="아우라 100인 서바이벌 포인트 배틀", page_icon="⚔️", layout="wide"
)

# 등급 리스트 정의 (희귀도 높은 순)
items = [
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

denominators = {
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

base_weights = [max(1, int(7500000000000 / denominators[item])) for item in items]

icons = {
    "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭": "🖐️✨🌌👑", "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻": "🕸️🌙✨🦋",
    "사도:베일": "🎃👁️", "수확가": "🎃🗡️", "악몽의 하늘": "🎃🌌",
    "𝓘𝓬𝓮𝓐𝓰𝓮": "❄️🧊👑", "𝓜𝓪𝓶𝓶𝓸𝓽𝓱": "🦣❄️🧊",
    "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧": "🌈💎✨", "𝓢𝔂𝓶𝓹𝓱𝓸𝓷𝔂♤": "🎼🎻✨♠️", "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐": "🌌💠💫",
    "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒": "🌊🐉🌀", "감시자": "👁️‍🗨️⚡",
    "아쿠아리움": "🐠🌊🏛️", "선원": "⚓⛵🌊", "샤킨": "🦈🌊⚡", "포세이돈": "🔱🌊🌊", "에바네샌트": "🌀✨🌌",
    "기원": "🌌✨", "망령": "👻⚡",
    "듀라한": "🎃🗡️", "영혼 사냥꾼": "🎃👻", "묘화": "🎃🔥", "밤나팔꽃": "🎃🌸", "바이탈": "🎃💉", "룬(나이트)": "🎃🛡️", "펌프": "🎃✨",
    "블리자드": "❄️🌨️🌀", "이상": "🌀❓🌌", "크로마틱": "🌈💫", "자장가": "🌌🎵💤",
    "그래피티": "🎨✨", "헬리오스": "☀️🔥", "속력": "⚡💨", "황혼": "🌆✨💜",
    "아파타이트": "💠💎", "대마법사": "🧙‍♂️✨", "아케인": "🔮👑", "워록": "💀🔥",
    "테러": "💣💥", "바운디드": "🌌👑", "재즈": "🎶🎷", "스펙터": "👻🔮",
    "이색": "🌈✨", "노틸러스": "🐚🌊", "아쿠아틱": "💧✨",
    "만년서리": "❄️💎", "태양": "☀️✨", "달": "🌙✨", "와트": "⚡👑⚡",
    "힘": "⚡🔥", "카와이": "🎀💖✨", "석영": "💎✨", "출혈": "🩸⚔️",
    "시데리움": "🌟🛡️", "콜라": "🥤🫧", "빙하": "🧊❄️", "재": "🌫️🔥",
    "자력": "🧲💫", "글록": "🔫💥", "아쿠아마린": "🌊💎", "사파이어": "💙💎", "잉크": "🖋️🖤",
    "에메랄드": "💚💎", "루비": "❤️💎", "분노": "😡💢", "토파즈": "💛💎",
    "결정화": "🔮✨", "현기증": "😵‍💫🌀", "원자": "⚛️✨", "수소": "🧪✨", "레어": "💙📦", "자연": "🌿🍃",
    "굿": "👍✨", "희귀": "💧📘", "일반": "⚪📦",
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

def roll_with_million_luck(extra_luck_mult=1):
  current_weights = list(base_weights)
  luck_mult = 1000000 * extra_luck_mult
  eligible_indices = [idx for idx, item in enumerate(items) if denominators[item] >= luck_mult]
  for idx in range(len(items)):
    if idx not in eligible_indices:
      current_weights[idx] = 0
    else:
      current_weights[idx] = current_weights[idx] * luck_mult
  return random.choices(items, weights=current_weights, k=1)[0]

if "game_started" not in st.session_state:
  st.session_state.game_started = False
if "turn_summary" not in st.session_state:
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
if "turn_logs" not in st.session_state:
  st.session_state.turn_logs = []

def init_game():
  ai_names = random.sample(AI_NAMES_POOL, 99)
  participants = [{
      "id": 0,
      "name": "나 (플레이어)",
      "is_player": True,
      "status": "playing",
      "score": 0,
      "prev_overall_rank": 0,
      "curr_overall_rank": 0,
      "rank_diff": 0,
      "last_aura": "-",
      "last_denom": 0,
      "history": [],
      "ever_got_100m": False,  # 1억 이상 아우라 획득 여부
      "buff_origin_turns": 0,
      "buff_prism_turns": 0,
      "locked_turns": 0,
  }]
  for i in range(1, 100):
    participants.append({
        "id": i,
        "name": ai_names[i - 1],
        "is_player": False,
        "status": "playing",
        "score": 0,
        "prev_overall_rank": 0,
        "curr_overall_rank": 0,
        "rank_diff": 0,
        "last_aura": "-",
        "last_denom": 0,
        "history": [],
        "ever_got_100m": False,
        "buff_origin_turns": 0,
        "buff_prism_turns": 0,
        "locked_turns": 0,
    })
  st.session_state.participants = participants
  st.session_state.turn = 0
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
  st.session_state.turn_logs = []
  st.session_state.game_started = True

st.title("⚔️ 아우라 100인 서바이벌 포인트 배틀")

if not st.session_state.game_started:
  st.markdown("""
  ### 📜 레인보우 칭호 시스템 안내
  - 게임 도중 **1억 이상(1 in 100,000,000 이상)**의 초희귀 아우라를 단 한 번이라도 뽑은 참가자는 이름이 화려한 **레인보우 색상**으로 영구 변경됩니다!
  - 각 1억 이상 아우라 고유의 강력한 특수 능력도 함께 발동합니다.
  """)
  if st.button("🚀 포인트 배틀 시작하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()
  st.stop()

participants = st.session_state.participants
curr_turn = st.session_state.turn
player_info = participants[0]

alive_participants = [p for p in participants if p["status"] == "playing"]
is_game_over = len(alive_participants) <= 1

col_t1, col_t2, col_t3 = st.columns(3)
with col_t1:
  st.metric("진행 턴 수", f"{curr_turn} 턴")
with col_t2:
  st.metric("남은 생존자", f"{len(alive_participants)}명")
with col_t3:
  p_status_str = "🏆 최종 우승!" if player_info["status"] == "winner" else ("💀 탈락 (관전 중)" if player_info["status"] == "eliminated" else f"🎮 생존 중 (누적: {player_info['score']}점)")
  st.metric("내 상태", p_status_str)

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

def get_styled_name(p):
  name_text = f"{p['name']} (나)" if p["is_player"] else p["name"]
  if p["ever_got_100m"]:
    # 레인보우 텍스트 스타일 적용
    return f"<span style='background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #00ffff, #0077ff, #9b00ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900;'>{name_text} ✨</span>"
  else:
    return f"<b>{name_text}</b>"

# 턴 진행 로직
def process_point_turn():
  st.session_state.turn += 1
  t = st.session_state.turn
  alive = [p for p in participants if p["status"] == "playing"]
  
  turn_results = []
  special_events = []

  for idx, p in enumerate(alive):
    if p["locked_turns"] > 0:
      p["locked_turns"] -= 1
      p["last_aura"] = "🔒 [잠김]"
      p["last_denom"] = 0
      p["history"].append({"turn": t, "aura": "🔒 [잠김]", "denom": 0})
      turn_results.append(p)
      special_events.append(f"🔒 {p['name']}님은 잠금 상태라 뽑기를 하지 못하고 꼴찌 처리되었습니다!")
      continue

    extra_mult = 1
    if p["buff_prism_turns"] > 0:
      extra_mult *= 2
      p["buff_prism_turns"] -= 1

    aura = roll_with_million_luck(extra_mult)
    denom = denominators[aura]
    p["last_aura"] = aura
    p["last_denom"] = denom
    p["history"].append({"turn": t, "aura": aura, "denom": denom})
    
    # 1억 이상 뽑았을 경우 레인보우 칭호 획득 체크!
    if denom >= 100000000:
      p["ever_got_100m"] = True

    turn_results.append(p)

    # 1억 이상 아우라 특수 능력 발동 판정
    if denom >= 100000000:
      if aura == "𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭":
        p["buff_origin_turns"] = 3
        special_events.append(f"🖐️ **[태초의 권능 발동!]** {p['name']}님이 [𝓣𝓱𝓮 𝓞𝓻𝓲𝓰𝓲𝓷 𝓗𝓪𝓷𝓭]을(를) 뽑아 3턴 동안 1등으로 확정됩니다!")
      elif aura == "𝓓𝓻𝓮𝓪𝓶𝓬𝓪𝓽𝓬𝓱𝓮𝓻":
        for neighbor_idx in [idx - 1, idx + 1]:
          if 0 <= neighbor_idx < len(alive):
            alive[neighbor_idx]["locked_turns"] = 2
        special_events.append(f"🕸️ **[드림캐쳐 발동!]** {p['name']}님의 주변 인물들이 2턴 동안 꿈속에 갇힙니다!")
      elif aura == "𝓘𝓬𝓮𝓐𝓰𝓮":
        for neighbor_idx in [idx - 1, idx + 1]:
          if 0 <= neighbor_idx < len(alive):
            alive[neighbor_idx]["locked_turns"] = 1
        special_events.append(f"❄️ **[아이스 에이지 발동!]** {p['name']}님의 한파로 주변 인물들이 1턴 동안 얼어붙습니다!")
      elif aura == "༒ 𝕷𝕰𝕁𝕴𝕬𝕿𝕳𝕬𝕹 ༒":
        other_alive = [x for x in alive if x != p]
        if other_alive:
          top_one = max(other_alive, key=lambda x: x["score"])
          top_one["status"] = "eliminated"
          special_events.append(f"🐉 **[절대포식 발동!]** 리바이어던을 뽑은 {p['name']}님이 현재 누적 1등인 {top_one['name']}님을 집어삼켜 탈락시켰습니다!")
      elif aura == "수확가":
        neighbors = []
        if idx > 0: neighbors.append(alive[idx - 1])
        if idx < len(alive) - 1: neighbors.append(alive[idx + 1])
        if neighbors:
          target = random.choice(neighbors)
          stolen = target["score"] // 2
          target["score"] -= stolen
          p["score"] += stolen
          special_events.append(f"🗡️ **[영혼 수확!]** {p['name']}님이 {target['name']}님의 점수 절반({stolen}점)을 흡수했습니다!")
      elif aura == "✧ 𝓗𝔂𝓹𝓮𝓻 𝓟𝓻𝓲𝓼𝓶 ✧":
        p["buff_prism_turns"] = 2
        special_events.append(f"💎 **[프리즘 공명]** {p['name']}님의 행운이 2턴 동안 2배 증폭됩니다!")
      elif aura == "𝓢𝓹𝓮𝓬𝓽𝓻𝓪𝓕𝓵𝓸𝔀 𖤐":
        if idx > 0:
          above_person = alive[idx - 1]
          above_person["status"] = "eliminated"
          special_events.append(f"💠 **[스펙트라 플로우!]** {p['name']}님이 순위표 바로 위에 있던 {above_person['name']}님을 즉시 제거했습니다!")

  for p in alive:
    if p["buff_origin_turns"] > 0:
      p["buff_origin_turns"] -= 1
      p["last_denom"] = 999999999999

  turn_results.sort(key=lambda x: x["last_denom"], reverse=True)

  total_alive = len(alive)
  for rank_idx, p in enumerate(turn_results):
    earned_score = max(1, 100 - int((rank_idx / max(1, total_alive - 1)) * 99)) if total_alive > 1 else 100
    p["score"] += earned_score
    p["last_turn_rank"] = rank_idx + 1
    p["last_earned"] = earned_score

  alive_sorted_by_score = sorted(alive, key=lambda x: (x["score"], x["last_denom"]), reverse=True)
  for overall_idx, p in enumerate(alive_sorted_by_score, 1):
    if t == 1:
      p["prev_overall_rank"] = overall_idx
      p["curr_overall_rank"] = overall_idx
      p["rank_diff"] = 0
    else:
      p["prev_overall_rank"] = p["curr_overall_rank"]
      p["curr_overall_rank"] = overall_idx
      p["rank_diff"] = p["prev_overall_rank"] - p["curr_overall_rank"]

  elimination_count = 2 if any(p["last_aura"] == "악몽의 하늘" for p in turn_results) else 1
  
  eliminated_this_turn = []
  for _ in range(elimination_count):
    active_pool = [x for x in alive_sorted_by_score if x["status"] == "playing"]
    if active_pool:
      low_p = active_pool[-1]
      low_p["status"] = "eliminated"
      eliminated_this_turn.append(low_p)
      alive_sorted_by_score.remove(low_p)

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
        "aura": p["last_aura"],
        "denom": p["last_denom"],
        "turn_rank": p["last_turn_rank"],
        "earned": p["last_earned"],
        "total_score": p["score"],
        "rank_diff": p["rank_diff"],
        "eliminated_now": is_elim,
        "ever_got_100m": p["ever_got_100m"]
    })

  elim_names = ", ".join([e["name"] for e in eliminated_this_turn])
  summary_text = f"📢 [{t}턴 결과] 이번 턴 1위: **{turn_results[0]['name']}** ({turn_results[0]['last_aura']}) | 최하위 탈락자: **{elim_names}**"
  if special_events:
    summary_text += " | ✨ [특수 능력 발동]: " + " / ".join(special_events)

  st.session_state.turn_logs = new_logs
  st.session_state.turn_summary = summary_text

if not is_game_over:
  btn_label = f"🎲 {curr_turn + 1}턴 진행 (특수 능력 & 포인트 집계)" if player_info["status"] == "playing" else f"👁️ {curr_turn + 1}턴 관전 진행"
  if st.button(btn_label, type="primary", use_container_width=True):
    process_point_turn()
    st.rerun()
else:
  winner = next((p for p in participants if p["status"] in ["winner", "playing"]), None)
  if winner and winner["is_player"]:
    st.balloons()
    st.success("🏆 축하합니다! 1억 이상 아우라의 레인보우 권능을 뚫고 최종 우승하셨습니다!")
  elif winner:
    st.success(f"👑 서바이벌 종료! 최후의 1인 최종 우승자는 **[{winner['name']}]**입니다!")
  if st.button("🔄 새 게임 시작하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()

st.info(st.session_state.turn_summary)

col_left, col_right = st.columns([1, 1.4])

with col_left:
  if is_game_over:
    winner = next((p for p in participants if p["status"] in ["winner", "playing"]), None)
    st.subheader(f"🏆 최종 우승자 [{winner['name']}] 아우라 기록")
    with st.container(height=600, border=True):
      st.markdown(f"**총 누적 점수:** `{winner['score']}점` (총 {len(winner['history'])}턴 생존)")
      st.divider()
      best_win_aura = max(winner["history"], key=lambda x: x["denom"])
      st.success(f"🌟 **최고 기록 아우라:** {icons.get(best_win_aura['aura'], '✨')} **{best_win_aura['aura']}** (`1 in {best_win_aura['denom']:,}`)")
      st.markdown("#### 📜 턴별 획득 아우라 전체 목록")
      for h in winner["history"]:
        st.markdown(
            f"- **{h['turn']}턴**: {icons.get(h['aura'], '✨')} **{h['aura']}** (`1 in {h['denom']:,}`)"
        )
  else:
    st.subheader(f"📋 이번 턴({curr_turn}턴) 순위 및 점수")
    with st.container(height=600, border=True):
      if not st.session_state.turn_logs:
        st.caption("아직 진행된 턴이 없습니다. 위 버튼을 눌러 게임을 시작하세요.")
      else:
        for log in st.session_state.turn_logs:
          diff_html = get_rank_diff_html(log["rank_diff"], curr_turn)
          
          # 로그에서도 레인보우 이름 적용
          log_name_text = f"{log['name']} (나)" if log["is_player"] else log['name']
          if log["ever_got_100m"]:
            name_str = f"<span style='background: linear-gradient(90deg, #ff0000, #ff7f00, #ffff00, #00ff00, #00ffff, #0077ff, #9b00ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 900;'>{log_name_text} ✨</span>"
          else:
            name_str = f"<b>{log_name_text}</b>"

          aura_str = f"{icons.get(log['aura'], '✨')} {log['aura']} (1 in {log['denom']:,})" if log['denom'] > 0 else f"{log['aura']}"
          elim_badge = " <span style='color:#ff4b4b; font-weight:bold;'>[💀 탈락]</span>" if log["eliminated_now"] else ""
          
          st.markdown(
              f"<div style='padding: 4px 0; border-bottom: 1px solid rgba(128,128,128,0.2);'>"
              f"<b>{log['turn_rank']}위</b> | {name_str} {diff_html} : {aura_str} "
              f"| <code>+{log['earned']}점</code> (누적 <b>{log['total_score']}점</b>){elim_badge}"
              f"</div>",
              unsafe_allow_html=True,
          )

with col_right:
  st.subheader("👥 참가자 현황판 (레인보우 칭호 & 누적 순위)")
  
  sorted_participants = sorted(
      participants,
      key=lambda x: (0 if x["status"] in ["playing", "winner"] else 1, -x["score"])
  )

  with st.container(height=600, border=True):
    cols_per_row = 3
    for i in range(0, len(sorted_participants), cols_per_row):
      row_items = sorted_participants[i : i + cols_per_row]
      grid_cols = st.columns(cols_per_row)
      
      for idx, p in enumerate(row_items):
        with grid_cols[idx]:
          with st.container(border=True):
            if p["status"] in ["playing", "winner"]:
              rank_badge = f"#{p['curr_overall_rank']} " if curr_turn > 0 else ""
              diff_html = get_rank_diff_html(p["rank_diff"], curr_turn) if curr_turn > 0 else ""
              status_txt = "🏆 우승" if p["status"] == "winner" else "🟢 생존"
            else:
              rank_badge = ""
              diff_html = ""
              status_txt = "💀 탈락"

            styled_name = get_styled_name(p)
            st.markdown(
                f"<div style='font-size:15px;'><b>{rank_badge}</b>{styled_name} {diff_html}</div>",
                unsafe_allow_html=True,
            )
            st.caption(f"{status_txt} | 누적: **{p['score']}점**")
            
            if p["last_denom"] > 0:
              st.markdown(f"최근: {icons.get(p['last_aura'], '✨')} `{p['last_aura']}`")
            else:
              st.markdown(f"최근: {p['last_aura']}")
