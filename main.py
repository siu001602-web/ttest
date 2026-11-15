import random
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="아우라 100인 서바이벌 배틀로얄", page_icon="⚔️", layout="wide"
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

# 백만배 행운 뽑기 함수 (1 in 1,000,000 이상만 출현)
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

# 게임 초기화 함수
def init_game():
  participants = [{
      "id": 0,
      "name": "나 (플레이어)",
      "is_player": True,
      "status": "playing",      # playing, passed_r1, passed_r2, direct_finals, eliminated, winner
      "last_aura": "-",
      "last_denom": 0,
      "best_aura": "-",
      "best_denom": 0,
  }]
  for i in range(1, 100):
    participants.append({
        "id": i,
        "name": f"AI_{i:02d}",
        "is_player": False,
        "status": "playing",
        "last_aura": "-",
        "last_denom": 0,
        "best_aura": "-",
        "best_denom": 0,
    })
  st.session_state.participants = participants
  st.session_state.round = 1
  st.session_state.turn = 0
  st.session_state.logs = ["[게임 시작] 총 100명이 1라운드에 돌입했습니다! '다음 턴 진행' 버튼을 눌러주세요."]
  st.session_state.game_started = True

if "game_started" not in st.session_state:
  st.session_state.game_started = False

st.title("⚔️ 아우라 100인 서바이벌 배틀로얄 (실시간 턴제)")

if not st.session_state.game_started:
  st.markdown("""
  ### 📜 게임 규칙 안내
  - **참가 인원**: 총 **100명** (나 1명 + AI 99명) / **모든 뽑기 백만배 행운 기본 적용**
  - **턴제 진행**: 버튼을 누를 때마다 생존 중인 모든 참가자가 **1턴(1뽑)**씩 진행합니다.
  - **1라운드 (선착순 50명)**: **5천만(1 in 50,000,000) 이상** 희귀도 아우라를 뽑으면 1라운드 통과! (선착순 50명이 차면 나머지 탈락)
  - **2라운드 (선착순 25명)**: **7천만(1 in 70,000,000) 이상** 희귀도 아우라를 뽑으면 2라운드 통과! (선착순 25명이 차면 나머지 탈락)
  - **⚡ 결승 직행 특전**: 1·2라운드 도중 **확률이 1억분의 1보다 낮은 아우라(1 in 100,000,000 이상)**를 뽑으면 즉시 **결승전(3라운드) 직행**!
  - **3라운드 (결승전)**: 결승 진출자 전원이 동시에 1뽑을 진행하여 **가장 확률이 높은(희귀도가 가장 낮은) 아우라를 뽑은 1명이 탈락**하고 나머지가 최종 우승!
  - *(내가 중도 탈락하더라도 관전 모드로 결승전까지 계속 진행할 수 있습니다)*
  """)
  if st.button("🚀 100인 배틀로얄 입장하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()
  st.stop()

# 현재 상태 요약
participants = st.session_state.participants
curr_round = st.session_state.round
curr_turn = st.session_state.turn

player_info = participants[0]
p_status_map = {
    "playing": "🎲 도전 중",
    "passed_r1": "✅ 1R 통과 (대기)",
    "passed_r2": "✅ 2R 통과 (결승 대기)",
    "direct_finals": "⚡ 결승 직행 확정!",
    "eliminated": "💀 탈락 (관전 중)",
    "winner": "🏆 최종 우승!",
}

col_top1, col_top2, col_top3, col_top4 = st.columns(4)
with col_top1:
  round_names = {1: "🟢 1라운드 (5천만↑ 50명)", 2: "🟡 2라운드 (7천만↑ 25명)", 3: "🔴 3라운드 (최종 결승전)", 4: "🏁 대회 종료"}
  st.metric("현재 라운드", round_names.get(curr_round, ""))
with col_top2:
  st.metric("진행 턴 수", f"{curr_turn} 턴")
with col_top3:
  st.metric("내 상태", p_status_map.get(player_info["status"], ""))
with col_top4:
  st.metric("내 최고 아우라", f"{player_info['best_aura']}", f"1 in {player_info['best_denom']:,}" if player_info['best_denom'] > 0 else "")

st.divider()

# 턴 진행 로직
def process_next_turn():
  st.session_state.turn += 1
  t = st.session_state.turn
  r = st.session_state.round
  turn_events = []

  # 1라운드 또는 2라운드 진행
  if r in [1, 2]:
    target_limit = 50 if r == 1 else 25
    req_denom = 50000000 if r == 1 else 70000000
    pass_tag = "passed_r1" if r == 1 else "passed_r2"

    # 현재 라운드 이미 확보된 통과자 수 (직행자 포함)
    already_passed = [p for p in participants if p["status"] in [pass_tag, "direct_finals"]]
    slots_left = target_limit - len(already_passed)

    # 아직 도전 중인(playing) 인원들 랜덤 순서로 뽑기 진행 (선착순 공정성)
    active_players = [p for p in participants if p["status"] == "playing"]
    random.shuffle(active_players)

    for p in active_players:
      aura = roll_with_million_luck()
      denom = denominators[aura]
      p["last_aura"] = aura
      p["last_denom"] = denom
      if denom > p["best_denom"]:
        p["best_aura"] = aura
        p["best_denom"] = denom

      # 1억 이상(확률 1억분의 1 이하) 뽑으면 즉시 결승 직행!
      if denom >= 100000000 and slots_left > 0:
        p["status"] = "direct_finals"
        slots_left -= 1
        turn_events.append(f"⚡ [결승 직행!] {p['name']}님이 [{aura}] (1 in {denom:,})을(를) 뽑아 결승으로 직행합니다!")
      elif denom >= req_denom and slots_left > 0:
        p["status"] = pass_tag
        slots_left -= 1
        if p["is_player"]:
          turn_events.append(f"🎉 [나 통과!] {p['name']}님이 [{aura}] (1 in {denom:,})으로 {r}라운드를 통과했습니다!")

    # 선착순 인원이 모두 찼다면 나머지 playing 인원은 전부 탈락 처리 후 다음 라운드로
    now_passed = [p for p in participants if p["status"] in [pass_tag, "direct_finals"]]
    if len(now_passed) >= target_limit:
      for p in participants:
        if p["status"] == "playing":
          p["status"] = "eliminated"
      
      st.session_state.logs.insert(0, f"📢 [{r}라운드 종료] 선착순 {target_limit}명이 모두 결정되어 나머지 참가자가 탈락했습니다!")
      for ev in reversed(turn_events):
        st.session_state.logs.insert(0, ev)

      # 다음 라운드 준비
      if r == 1:
        for p in participants:
          if p["status"] == "passed_r1":
            p["status"] = "playing"  # 2라운드 도전자로 전환 (direct_finals는 유지)
        st.session_state.round = 2
        st.session_state.logs.insert(0, "🟡 [2라운드 시작] 생존자 50명(결승 직행자 포함)이 7천만 이상 아우라 도전을 시작합니다!")
      elif r == 2:
        for p in participants:
          if p["status"] in ["passed_r2", "direct_finals"]:
            p["status"] = "playing"  # 3라운드 결승전 진출
        st.session_state.round = 3
        st.session_state.logs.insert(0, "🔴 [3라운드 결승전 시작] 최후의 25명이 결승전에 진출했습니다! 가장 확률이 높은(가치가 낮은) 아우라를 뽑는 1명이 탈락합니다!")
    else:
      st.session_state.logs.insert(0, f"⏱️ [{r}라운드 {t}턴 결과] 현재 통과자: {len(now_passed)} / {target_limit}명 (남은 자리: {target_limit - len(now_passed)}석)")
      for ev in reversed(turn_events):
        st.session_state.logs.insert(0, ev)

  # 3라운드 (결승전) 진행
  elif r == 3:
    finalists = [p for p in participants if p["status"] == "playing"]
    for p in finalists:
      aura = roll_with_million_luck()
      denom = denominators[aura]
      p["last_aura"] = aura
      p["last_denom"] = denom
      if denom > p["best_denom"]:
        p["best_aura"] = aura
        p["best_denom"] = denom

    # 결승전 진출자 중 가장 확률이 높은(희귀도가 낮은, 즉 denom이 가장 작은) 1명 탈락
    lowest_player = min(finalists, key=lambda x: x["last_denom"])
    lowest_player["status"] = "eliminated"

    for p in finalists:
      if p["status"] != "eliminated":
        p["status"] = "winner"

    mvp_player = max(finalists, key=lambda x: x["last_denom"])
    st.session_state.logs.insert(
        0, f"💀 [결승 탈락자] {lowest_player['name']}님이 가장 확률이 높은 [{lowest_player['last_aura']}] (1 in {lowest_player['last_denom']:,})을(를) 뽑아 최종 탈락했습니다!"
    )
    st.session_state.logs.insert(
        0, f"🏆 [최종 우승 확정!] 결승 MVP {mvp_player['name']}님([{mvp_player['last_aura']}])을 포함한 24명이 최종 생존에 성공했습니다!"
    )
    st.session_state.round = 4

# 컨트롤 버튼 영역
if curr_round in [1, 2]:
  btn_text = f"🎲 다음 턴 진행 ({curr_round}라운드 1뽑 실행)" if player_info["status"] == "playing" else f"👁️ 다음 턴 관전하기 ({curr_round}라운드 AI 진행)"
  if st.button(btn_text, type="primary", use_container_width=True):
    process_next_turn()
    st.rerun()
elif curr_round == 3:
  if st.button("🏆 결승전 최종 운명의 1뽑 실행!", type="primary", use_container_width=True):
    process_next_turn()
    st.rerun()
else:
  if player_info["status"] == "winner":
    st.balloons()
    st.success(f"🎉 축하합니다! 치열한 100인 서바이벌에서 최종 생존하셨습니다! (최종 아우라: {player_info['last_aura']})")
  else:
    st.error("💀 아쉽게도 이번 배틀로얄에서는 탈락하셨습니다. 다시 도전해보세요!")
  if st.button("🔄 새 게임 시작하기", type="primary", use_container_width=True):
    init_game()
    st.rerun()

# 중계 로그 & 100명 전체 순위표
col_log, col_board = st.columns([1, 1.3])

with col_log:
  st.subheader("📜 실시간 경기 중계 로그")
  with st.container(height=550, border=True):
    for log in st.session_state.logs[:40]:
      st.markdown(f"- {log}")

with col_board:
  st.subheader("📊 100명 실시간 현황판 (최고 등급 순 정렬)")
  # 가장 좋은 것(best_denom이 높은 순, 같으면 last_denom 높은 순)을 뽑은 사람이 제일 위로 올라가도록 정렬
  sorted_participants = sorted(
      participants,
      key=lambda x: (x["best_denom"], x["last_denom"]),
      reverse=True
  )

  status_badge_table = {
      "playing": "🎲 도전중",
      "passed_r1": "✅ 1R통과",
      "passed_r2": "✅ 2R통과",
      "direct_finals": "⚡ 결승직행",
      "eliminated": "💀 탈락",
      "winner": "🏆 우승",
  }

  with st.container(height=550, border=True):
    for rank, p in enumerate(sorted_participants, 1):
      badge = status_badge_table.get(p["status"], "")
      name_str = f"**👉 {p['name']}**" if p["is_player"] else p["name"]
      last_str = f"{icons.get(p['last_aura'], '')} {p['last_aura']} (`1 in {p['last_denom']:,}`)" if p["last_denom"] > 0 else "대기 중"
      best_str = f"{p['best_aura']} (`1 in {p['best_denom']:,}`)" if p["best_denom"] > 0 else "-"
      
      st.markdown(
          f"**{rank}위** | {badge} | {name_str} — 이번 턴: {last_str} | 최고 기록: {best_str}"
      )
