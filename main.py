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
    "테러": "💣💥", "바운디드": "🌌👑", "재즈": "🎶🎷", "ส펙터": "👻🔮",
    "이색": "🌈✨", "노틸러스": "🐚🌊", "아쿠아틱": "💧✨",
    "만년서리": "❄️💎", "태양": "☀️✨", "달": "🌙✨", "와트": "⚡👑⚡",
    "힘": "⚡🔥", "카와이": "🎀💖✨", "석영": "💎✨", "출혈": "🩸⚔️",
    "시데리움": "🌟🛡️", "콜라": "🥤🫧", "빙하": "🧊❄️", "재": "🌫️🔥",
    "자력": "🧲💫", "글록": "🔫💥", "아쿠아마린": "🌊💎", "사파이어": "💙💎", "잉크": "🖋️🖤",
    "에메랄드": "💚💎", "루비": "❤️💎", "분노": "😡💢", "토파즈": "💛💎",
    "결정화": "🔮✨", "현기증": "😵‍💫🌀", "원자": "⚛️✨", "수소": "🧪✨", "레어": "💙📦", "자연": "🌿🍃",
    "굿": "👍✨", "희귀": "💧📘", "일반": "⚪📦",
}

# 백만배 행운 뽑기 함수
def roll_with_million_luck():
  current_weights = list(base_weights)
  luck_mult = 1000000
  eligible_indices = [idx for idx, item in enumerate(items) if denominators[item] >= luck_mult]
  for idx in range(len(items)):
    if idx not in eligible_indices:
      current_weights[idx] = 0
    else:
      current_weights[idx] = current_weights[idx] * luck_mult
  return random.choices(items, weights=current_weights, k=1)[0]

# 세션 상태 초기화
if "game_started" not in st.session_state:
  st.session_state.game_started = False
if "turn_summary" not in st.session_state:
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
if "turn_logs" not in st.session_state:
  st.session_state.turn_logs = []

def init_game():
  participants = [{
      "id": 0,
      "name": "나 (플레이어)",
      "is_player": True,
      "status": "playing", # playing, eliminated, winner
      "score": 0,
      "last_aura": "-",
      "last_denom": 0,
      "last_rank": 0,
  }]
  for i in range(1, 100):
    participants.append({
        "id": i,
        "name": f"AI_{i:02d}",
        "is_player": False,
        "status": "playing",
        "score": 0,
        "last_aura": "-",
        "last_denom": 0,
        "last_rank": 0,
    })
  st.session_state.participants = participants
  st.session_state.turn = 0
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
  st.session_state.turn_logs = []
  st.session_state.game_started = True

st.title("⚔️ 아우라 100인 서바이벌 포인트 배틀")

if not st.session_state.game_started:
  st.markdown("""
  ### 📜 포인트 서바이벌 규칙 안내
  - **참가 인원**: 총 **100명** (나 1명 + AI 99명) / **모든 뽑기 백만배 행운 기본 적용**
  - **포인트 시스템**: 매 턴마다 생존자 전원이 1뽑씩 진행하고, **가장 높은 아우라(희귀도 기준)를 뽑은 사람이 1등(100점), 2등은 99점... 순차적으로 점수가 누적**됩니다.
  - **매턴 1명 탈락**: 매 턴이 끝날 때마다 **누적 점수가 가장 낮은 플레이어 1명이 탈락**합니다!
  - **최후의 1인**: 오직 1명이 남을 때까지 턴이 계속 진행되며 살아남는 사람이 최종 우승합니다.
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
  p_status_str = "🏆 최종 우승!" if player_info["status"] == "winner" else ("💀 탈락 (관전 중)" if player_info["status"] == "eliminated" else f"🎮 생존 중 (점수: {player_info['score']}점)")
  st.metric("내 상태", p_status_str)

st.divider()

# 턴 진행 로직
def process_point_turn():
  st.session_state.turn += 1
  alive = [p for p in participants if p["status"] == "playing"]
  
  turn_results = []
  for p in alive:
    aura = roll_with_million_luck()
    denom = denominators[aura]
    p["last_aura"] = aura
    p["last_denom"] = denom
    turn_results.append(p)

  # 이번 턴 순위 결정 (denom이 클수록 높은 순위)
  turn_results.sort(key=lambda x: x["last_denom"], reverse=True)

  total_alive = len(alive)
  new_logs = []
  for idx, p in enumerate(turn_results):
    # 1등에게 100점, 2등에게 99점 부여 (인원이 적어지면 1등 점수는 생존자 수 기준 혹은 100점 기준으로 비례 분배 등 조정 가능, 여기서는 100점 만점 기준 차등 부여)
    earned_score = max(1, 100 - int((idx / max(1, total_alive - 1)) * 99)) if total_alive > 1 else 100
    p["score"] += earned_score
    p["last_rank"] = idx + 1
    
    new_logs.append({
        "name": p["name"],
        "is_player": p["is_player"],
        "aura": p["last_aura"],
        "denom": p["last_denom"],
        "rank": idx + 1,
        "earned": earned_score,
        "total_score": p["score"]
    })

  # 이번 턴 가장 점수가 낮았던(혹은 이번 턴 꼴등) 1명 탈락 처리
  # 규칙: "매라운드마다 제일 점수낮은 플레이어 하나가 탈락" -> 전체 누적 점수가 가장 낮은 사람 탈락
  lowest_player = min(alive, key=lambda x: (x["score"], x["last_denom"]))
  lowest_player["status"] = "eliminated"

  if len(alive) - 1 <= 1:
    for p in alive:
      if p["status"] == "playing" and p != lowest_player:
        p["status"] = "winner"

  st.session_state.turn_logs = new_logs
  st.session_state.turn_summary = f"📢 [{st.session_state.turn}턴 결과] 이번 턴 1위: {turn_results[0]['name']} ({turn_results[0]['last_aura']}) | 누적 점수 최하위로 **{lowest_player['name']}님이 탈락**하셨습니다!"

# 상단 컨트롤 버튼
if not is_game_over:
  btn_label = f"🎲 {curr_turn + 1}턴 진행 (1뽑 및 포인트 집계)" if player_info["status"] == "playing" else f"👁️ {curr_turn + 1}턴 관전 진행 (AI 포인트 집계)"
  if st.button(btn_label, type="primary", use_container_width=True):
    process_point_turn()
    st.rerun()
else:
  winner = next((p for p in participants if p["status"] == "winner" or (p["status"] == "playing")), None)
  if winner and winner["is_player"]:
    st.balloons()
    st.success("🏆 축하합니다! 100인 포인트 서바이벌에서 최종 우승하셨습니다!")
  else:
    st.error("💀 서바이벌이 종료되었습니다. 최종 우승자를 확인하세요!")
  if st.button("🔄 새 게임 시작하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()

st.info(st.session_state.turn_summary)

# 탭 또는 화면 분할: 왼쪽은 이번 턴 로그, 오른쪽은 참가자 현황 카드(네모칸 그리드)
col_log, col_cards = st.columns([1, 1.4])

with col_log:
  st.subheader(f"📋 이번 턴({curr_turn}턴) 순위 및 획득 점수")
  with st.container(height=600, border=True):
    if not st.session_state.turn_logs:
      st.caption("아직 진행된 턴이 없습니다. 위 버튼을 눌러 게임을 시작하세요.")
    else:
      for log in st.session_state.turn_logs:
        name_str = f"**👉 {log['name']}**" if log["is_player"] else f"**{log['name']}**"
        aura_str = f"{icons.get(log['aura'], '✨')} {log['aura']} (`1 in {log['denom']:,}`)"
        st.markdown(f"**{log['rank']}위** | {name_str} : {aura_str} | 획득 `+{log['earned']}점` (누적: **{log['total_score']}점**)")

with col_cards:
  st.subheader("👥 생존자 및 참가자 현황 (카드 그리드)")
  
  # 정렬: 생존자 우선, 누적 점수 높은 순
  sorted_participants = sorted(
      participants,
      key=lambda x: (0 if x["status"] in ["playing", "winner"] else 1, -x["score"])
  )

  with st.container(height=600, border=True):
    # 한 줄에 3~4명씩 네모칸 형식으로 나열하기 위해 3열 컬럼 생성
    cols_per_row = 3
    for i in range(0, len(sorted_participants), cols_per_row):
      row_items = sorted_participants[i : i + cols_per_row]
      grid_cols = st.columns(cols_per_row)
      
      for idx, p in enumerate(row_items):
        with grid_cols[idx]:
          with st.container(border=True):
            if p["status"] == "playing":
              status_txt = "🟢 생존"
              border_color = ""
            elif p["status"] == "winner":
              status_txt = "🏆 우승"
            else:
              status_txt = "💀 탈락"

            me_mark = " (나)" if p["is_player"] else ""
            st.markdown(f"**{p['name']}{me_mark}**")
            st.caption(f"상태: {status_txt} | 누적: **{p['score']}점**")
            
            if p["last_denom"] > 0:
              st.markdown(f"최근: {icons.get(p['last_aura'], '✨')} `{p['last_aura']}`")
            else:
              st.markdown("최근: 대기 중")
