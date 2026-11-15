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

# 세션 상태 기본값 초기화
if "game_started" not in st.session_state:
  st.session_state.game_started = False
if "turn_summary" not in st.session_state:
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
if "turn_logs" not in st.session_state:
  st.session_state.turn_logs = []

# 게임 초기화 함수
def init_game():
  participants = [{
      "id": 0,
      "name": "나 (플레이어)",
      "is_player": True,
      "status": "playing",
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
  st.session_state.turn_summary = "게임이 시작되었습니다! '다음 턴 진행' 버튼을 눌러주세요."
  st.session_state.turn_logs = []
  st.session_state.game_started = True

st.title("⚔️ 아우라 100인 서바이벌 배틀로얄")

if not st.session_state.game_started:
  st.markdown("""
  ### 📜 게임 규칙 안내
  - **참가 인원**: 총 **100명** (나 1명 + AI 99명) / **모든 뽑기 백만배 행운 기본 적용**
  - **턴제 진행**: 버튼을 누를 때마다 생존 중인 모든 참가자가 **1턴(1뽑)**씩 진행하며, 매 턴 결과가 새롭게 초기화되어 표시됩니다.
  - **1라운드 (선착순 50명)**: **5천만(1 in 50,000,000) 이상** 희귀도 아우라를 뽑으면 1라운드 통과!
  - **2라운드 (선착순 25명)**: **7천만(1 in 70,000,000) 이상** 희귀도 아우라를 뽑으면 2라운드 통과!
  - **3라운드 (결승전)**: 결승 진출자 25명이 동시에 1뽑을 진행하여 **가장 확률이 높은(희귀도가 가장 낮은) 아우라를 뽑은 1명이 탈락**하고 나머지가 최종 우승!
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

# 턴 진행 로직 (매 턴마다 로그 초기화)
def process_next_turn():
  st.session_state.turn += 1
  t = st.session_state.turn
  r = st.session_state.round
  
  new_turn_logs = []

  # 1라운드 또는 2라운드 진행
  if r in [1, 2]:
    target_limit = 50 if r == 1 else 25
    req_denom = 50000000 if r == 1 else 70000000
    pass_tag = "passed_r1" if r == 1 else "passed_r2"

    already_passed = [p for p in participants if p["status"] == pass_tag]
    slots_left = target_limit - len(already_passed)

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

      if denom >= req_denom and slots_left > 0:
        p["status"] = pass_tag
        slots_left -= 1
        new_turn_logs.append({
            "name": p["name"],
            "is_player": p["is_player"],
            "aura": aura,
            "denom": denom,
            "result": f"✅ {r}R 통과!",
            "passed": True
        })
      else:
        new_turn_logs.append({
            "name": p["name"],
            "is_player": p["is_player"],
            "aura": aura,
            "denom": denom,
            "result": "⏳ 계속 도전",
            "passed": False
        })

    new_turn_logs.sort(key=lambda x: x["denom"], reverse=True)
    st.session_state.turn_logs = new_turn_logs

    now_passed = [p for p in participants if p["status"] == pass_tag]
    if len(now_passed) >= target_limit:
      for p in participants:
        if p["status"] == "playing":
          p["status"] = "eliminated"
      
      st.session_state.turn_summary = f"📢 [{r}라운드 종료!] 선착순 {target_limit}명이 모두 확정되어 나머지 참가자가 탈락했습니다!"

      if r == 1:
        for p in participants:
          if p["status"] == "passed_r1":
            p["status"] = "playing"
        st.session_state.round = 2
      elif r == 2:
        for p in participants:
          if p["status"] == "passed_r2":
            p["status"] = "playing"
        st.session_state.round = 3
    else:
      st.session_state.turn_summary = f"⏱️ [{r}라운드 {t}턴 결과] 현재 통과자: {len(now_passed)} / {target_limit}명 (남은 자리: {target_limit - len(now_passed)}석)"

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

    lowest_player = min(finalists, key=lambda x: x["last_denom"])
    lowest_player["status"] = "eliminated"

    for p in finalists:
      if p["status"] != "eliminated":
        p["status"] = "winner"
      new_turn_logs.append({
          "name": p["name"],
          "is_player": p["is_player"],
          "aura": p["last_aura"],
          "denom": p["last_denom"],
          "result": "💀 최하위 탈락" if p["status"] == "eliminated" else "🏆 최종 우승!",
          "passed": p["status"] == "winner"
      })

    new_turn_logs.sort(key=lambda x: x["denom"], reverse=True)
    st.session_state.turn_logs = new_turn_logs
    st.session_state.turn_summary = (
        f"🏆 [결승전 종료!] 가장 확률이 높은 [{lowest_player['last_aura']}]을(를) 뽑은 {lowest_player['name']}님이 탈락하고, 24명이 최종 우승했습니다!"
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

st.info(st.session_state.turn_summary)

# 왼쪽: 이번 턴 뽑기 로그 / 오른쪽: 전체 최고 아우라 TOP 3
col_log, col_top3 = st.columns([1.2, 1])

with col_log:
  st.subheader(f"📋 이번 턴({curr_turn}턴) 뽑기 결과")
  with st.container(height=550, border=True):
    if not st.session_state.turn_logs:
      st.caption("아직 진행된 턴이 없습니다. 위 버튼을 눌러 턴을 진행해주세요.")
    else:
      for idx, log in enumerate(st.session_state.turn_logs, 1):
        name_display = f"**👉 {log['name']}**" if log["is_player"] else f"**{log['name']}**"
        aura_display = f"{icons.get(log['aura'], '✨')} {log['aura']} (`1 in {log['denom']:,}`)"
        if log["passed"]:
          st.success(f"**{idx}위** | {name_display} : {aura_display} — **{log['result']}**")
        else:
          st.markdown(f"**{idx}위** | {name_display} : {aura_display} — {log['result']}")

with col_top3:
  st.subheader("👑 전체 최고 아우라 TOP 3")
  sorted_by_best = sorted(
      [p for p in participants if p["best_denom"] > 0],
      key=lambda x: x["best_denom"],
      reverse=True
  )

  medals = ["🥇 1위", "🥈 2위", "🥉 3위"]
  for i in range(3):
    with st.container(border=True):
      if i < len(sorted_by_best):
        top_p = sorted_by_best[i]
        p_tag = " (나)" if top_p["is_player"] else ""
        st.markdown(f"### {medals[i]} — {top_p['name']}{p_tag}")
        st.markdown(f"**{icons.get(top_p['best_aura'], '✨')} {top_p['best_aura']}** (`1 in {top_p['best_denom']:,}`)")
      else:
        st.markdown(f"### {medals[i]} — 기록 없음")
        st.caption("턴이 진행되면 최고 기록이 표시됩니다.")

  st.divider()
  st.markdown("#### 📊 생존 인원 요약")
  alive_cnt = len([p for p in participants if p["status"] in ["playing", "passed_r1", "passed_r2", "winner"]])
  elim_cnt = len([p for p in participants if p["status"] == "eliminated"])
  st.write(f"• 🟢 **현재 생존 인원**: {alive_cnt}명")
  st.write(f"• 💀 **탈락 인원**: {elim_cnt}명")
