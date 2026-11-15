import base64
from datetime import datetime
import hashlib
json = __import__("json")
os = __import__("os")
random = __import__("random")
sqlite3 = __import__("sqlite3")
time = __import__("time")
colorsys = __import__("colorsys")
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

def init_db():
  conn = sqlite3.connect("survival_users.db", check_same_thread=False)
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            data TEXT
        )
    """)
  conn.commit()
  conn.close()

init_db()

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

def save_user_data_to_db():
  if not st.session_state.get("logged_in", False):
    return
  username = st.session_state.username
  save_data = {
      "coins": st.session_state.get("coins", 0),
      "wins": st.session_state.get("wins", 0),
  }
  conn = sqlite3.connect("survival_users.db", check_same_thread=False)
  cursor = conn.cursor()
  cursor.execute(
      "UPDATE users SET data = ? WHERE username = ?",
      (json.dumps(save_data, ensure_ascii=False), username),
  )
  conn.commit()
  conn.close()

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "username" not in st.session_state:
  st.session_state.username = ""
if "coins" not in st.session_state:
  st.session_state.coins = 1000
if "wins" not in st.session_state:
  st.session_state.wins = 0

# 서바이벌 게임 상태 변수
if "survival_stage" not in st.session_state:
  st.session_state.survival_stage = 0  # 0: 대기중, 1: 1라운드, 2: 2라운드, 3: 3라운드(결승), 4: 최종 종료
if "player_alive" not in st.session_state:
  st.session_state.player_alive = True
if "ai_survivors" not in st.session_state:
  st.session_state.ai_survivors = []
if "player_aura" not in st.session_state:
  st.session_state.player_aura = None
if "survival_logs" not in st.session_state:
  st.session_state.survival_logs = []
if "round_processed" not in st.session_state:
  st.session_state.round_processed = False
if "final_winner_info" not in st.session_state:
  st.session_state.final_winner_info = None

if not st.session_state.logged_in:
  st.title("⚔️ 아우라 100인 서바이벌 배틀로얄 — 로그인")
  l_user = st.text_input("아이디", key="login_user")
  l_pass = st.text_input("비밀번호", type="password", key="login_pass")
  col_l1, col_l2 = st.columns(2)
  with col_l1:
    if st.button("로그인", type="primary", use_container_width=True):
      if l_user.strip() and l_pass.strip():
        conn = sqlite3.connect("survival_users.db", check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT password, data FROM users WHERE username = ?", (l_user,))
        row = cursor.fetchone()
        conn.close()
        if row and row[0] == hash_password(l_pass):
          st.session_state.logged_in = True
          st.session_state.username = l_user
          saved_data = json.loads(row[1])
          st.session_state.coins = saved_data.get("coins", 1000)
          st.session_state.wins = saved_data.get("wins", 0)
          st.rerun()
        else:
          st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
  with col_l2:
    if st.button("회원가입", type="secondary", use_container_width=True):
      if l_user.strip() and l_pass.strip():
        conn = sqlite3.connect("survival_users.db", check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username = ?", (l_user,))
        if cursor.fetchone():
          st.error("이미 존재하는 아이디입니다.")
        else:
          cursor.execute("INSERT INTO users (username, password, data) VALUES (?, ?, ?)",
                         (l_user, hash_password(l_pass), json.dumps({"coins": 1000, "wins": 0})))
          conn.commit()
          conn.close()
          st.success("회원가입 완료! 로그인해주세요.")
  st.stop()

# 백만배 행운 뽑기 함수 (서바이벌 전용)
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

# AI 라운드 시뮬레이션 함수 (목표 인원수만큼 통과할 때까지 뽑기 진행)
def simulate_ai_round(ai_list, threshold_denom, target_survivor_count):
  passed_ais = []
  # 실제 경쟁 느낌을 위해 각 AI가 여러 번 시도하여 조건을 달성한 선착순 인원을 뽑음
  candidates = list(ai_list)
  random.shuffle(candidates)
  
  # 라운드마다 최대 20턴 동안 AI들이 뽑기를 시도해 선착순 마감
  for _ in range(25):
    if len(passed_ais) >= target_survivor_count:
      break
    for ai_name in list(candidates):
      if len(passed_ais) >= target_survivor_count:
        break
      res = roll_with_million_luck()
      if denominators[res] >= threshold_denom:
        passed_ais.append({"name": ai_name, "aura": res, "denom": denominators[res]})
        candidates.remove(ai_name)
        
  # 만약 운이 나빠 목표 인원을 못 채웠다면 남은 AI 중 상위 결과로 채움
  while len(passed_ais) < target_survivor_count and candidates:
    ai_name = candidates.pop(0)
    res = roll_with_million_luck()
    passed_ais.append({"name": ai_name, "aura": res, "denom": denominators[res]})
    
  return passed_ais

st.title("⚔️ 아우라 100인 서바이벌 배틀로얄")

status_badge = "🟢 생존 중" if st.session_state.player_alive else "💀 탈락 (관전 모드)"
st.markdown(
    f"👤 참가자: **`{st.session_state.username}`**님 ({status_badge}) | "
    f"💰 코인: **{st.session_state.coins} G** | 🏆 우승 횟수: **{st.session_state.wins}회**"
)
st.divider()

# 0단계: 게임 시작 전 (대기실)
if st.session_state.survival_stage == 0:
  st.subheader("🎯 배틀로얄 규칙 안내")
  st.markdown("""
  - **총 100명** (플레이어 1명 + AI 99명)이 참전하는 목숨을 건 서바이벌!
  - 모든 뽑기에는 **백만배 행운(1,000,000배)**이 기본 적용됩니다.
  - **1라운드**: 5천만($50,000,000$) 이상 아우라 뽑기 (**선착순 50명** 생존)
  - **2라운드**: 7천만($70,000,000$) 이상 아우라 뽑기 (**선착순 25명** 생존)
  - **3라운드 (결승)**: 남은 생존자들과 아우라 확률 비교! **가장 확률이 높은(희귀도가 낮은) 아우라를 뽑은 사람은 탈락**, **1억($100,000,000$) 이하 아우라를 뽑은 사람은 결승 직행!**
  - ⚠️ **중도 탈락 시에도 경기는 멈추지 않으며, 관전 모드로 전환되어 AI들의 최종 결승전까지 계속 진행됩니다.**
  """)
  
  if st.button("🚀 100인 배틀로얄 시작하기", type="primary", use_container_width=True):
    st.session_state.ai_survivors = [f"AI_참가자_{i:02d}" for i in range(1, 100)]
    st.session_state.player_alive = True
    st.session_state.round_processed = False
    st.session_state.final_winner_info = None
    st.session_state.survival_stage = 1
    st.session_state.survival_logs = ["[게임 시작] 총 100명(플레이어 + AI 99명)이 1라운드 전장에 입장했습니다!"]
    st.rerun()

# 1라운드
elif st.session_state.survival_stage == 1:
  st.subheader("🟢 1라운드: 5천만($50,000,000$) 이상 아우라 생존전 (선착순 50명)")
  
  if not st.session_state.round_processed:
    btn_label = "🎲 1라운드 아우라 뽑기 진행!" if st.session_state.player_alive else "👁️ 1라운드 AI 경기 관전하기"
    if st.button(btn_label, type="primary", use_container_width=True):
      p_passed = False
      if st.session_state.player_alive:
        p_result = roll_with_million_luck()
        p_denom = denominators[p_result]
        st.session_state.player_aura = p_result
        p_passed = p_denom >= 50000000
        
        if p_passed:
          st.session_state.survival_logs.insert(0, f"✅ [플레이어 통과] [{p_result}] (가치: {p_denom:,}) 획득!")
        else:
          st.session_state.player_alive = False
          st.session_state.survival_logs.insert(0, f"💀 [플레이어 탈락] [{p_result}] (가치: {p_denom:,}) — 5천만 미달! 관전 모드로 전환됩니다.")

      # 플레이어 통과 여부에 따라 AI 통과 인원 조절 (총 50명 맞추기)
      ai_target = 49 if p_passed else 50
      passed_ais = simulate_ai_round(st.session_state.ai_survivors, 50000000, ai_target)
      st.session_state.ai_survivors = [a["name"] for a in passed_ais]
      
      top_ai = max(passed_ais, key=lambda x: x["denom"])
      st.session_state.survival_logs.insert(
          0, f"📢 [1라운드 마감] 선착순 50명 확정! (AI 최고 기록: {top_ai['name']} - {top_ai['aura']})"
      )
      st.session_state.round_processed = True
      st.rerun()
  else:
    if st.session_state.player_alive:
      st.success(f"🎉 1라운드 생존 성공! [{st.session_state.player_aura}] 획득으로 50인에 안착했습니다!")
    else:
      st.error(f"💀 1라운드에서 탈락하셨습니다 ({st.session_state.player_aura}). 하지만 경기는 계속됩니다! AI 50명의 2라운드를 관전하세요.")
      
    if st.button("➡️ 2라운드로 이동", type="primary", use_container_width=True):
      st.session_state.round_processed = False
      st.session_state.survival_stage = 2
      st.rerun()

# 2라운드
elif st.session_state.survival_stage == 2:
  st.subheader("🟡 2라운드: 7천만($70,000,000$) 이상 아우라 생존전 (선착순 25명)")
  
  if not st.session_state.round_processed:
    btn_label = "🎲 2라운드 아우라 뽑기 진행!" if st.session_state.player_alive else "👁️ 2라운드 AI 경기 관전하기"
    if st.button(btn_label, type="primary", use_container_width=True):
      p_passed = False
      if st.session_state.player_alive:
        p_result = roll_with_million_luck()
        p_denom = denominators[p_result]
        st.session_state.player_aura = p_result
        p_passed = p_denom >= 70000000
        
        if p_passed:
          st.session_state.survival_logs.insert(0, f"✅ [플레이어 2R 통과] [{p_result}] (가치: {p_denom:,}) 획득!")
        else:
          st.session_state.player_alive = False
          st.session_state.survival_logs.insert(0, f"💀 [플레이어 2R 탈락] [{p_result}] (가치: {p_denom:,}) — 7천만 미달! 관전 모드로 전환됩니다.")

      ai_target = 24 if p_passed else 25
      passed_ais = simulate_ai_round(st.session_state.ai_survivors, 70000000, ai_target)
      st.session_state.ai_survivors = [a["name"] for a in passed_ais]
      
      top_ai = max(passed_ais, key=lambda x: x["denom"])
      st.session_state.survival_logs.insert(
          0, f"📢 [2라운드 마감] 결승 진출자 25명 확정! (AI 최고 기록: {top_ai['name']} - {top_ai['aura']})"
      )
      st.session_state.round_processed = True
      st.rerun()
  else:
    if st.session_state.player_alive:
      st.success(f"🎉 2라운드 생존 성공! [{st.session_state.player_aura}] 획득으로 최종 결승전(25인)에 진출합니다!")
    else:
      st.warning(f"👁️ [관전 모드] 현재 AI 생존자 25명이 최종 결승전 진출을 확정지었습니다.")
      
    if st.button("🔥 3라운드 (최종 결승전)으로 이동", type="primary", use_container_width=True):
      st.session_state.round_processed = False
      st.session_state.survival_stage = 3
      st.rerun()

# 3라운드 (결승전)
elif st.session_state.survival_stage == 3:
  st.subheader("🔴 3라운드: 최후의 결승전 (확률 비교 & 1억 이하 직행 룰)")
  st.markdown("""
  - **결승 판정 규칙**: 25명의 결승 진출자가 마지막 아우라를 뽑습니다.
  - **1억($100,000,000$) 이하** 아우라를 뽑은 참가자는 **결승 직행(생존)** 처리됩니다.
  - 나머지 참가자 중 **가장 확률이 높은(희귀도가 낮은) 아우라를 뽑은 최하위 1명**이 탈락하며, 살아남은 최후의 생존자들이 우승을 차지합니다!
  """)

  btn_label = "🏆 결승전 최종 아우라 뽑기 및 판정!" if st.session_state.player_alive else "👁️ 결승전 최종 결과 관전하기!"
  if st.button(btn_label, type="primary", use_container_width=True):
    contestants = []
    
    if st.session_state.player_alive:
      p_result = roll_with_million_luck()
      p_denom = denominators[p_result]
      st.session_state.player_aura = p_result
      contestants.append({
          "name": st.session_state.username,
          "aura": p_result,
          "denom": p_denom,
          "is_player": True,
          "direct_pass": p_denom <= 100000000
      })

    for ai_name in st.session_state.ai_survivors:
      ai_item = roll_with_million_luck()
      ai_denom = denominators[ai_item]
      contestants.append({
          "name": ai_name,
          "aura": ai_item,
          "denom": ai_denom,
          "is_player": False,
          "direct_pass": ai_denom <= 100000000
      })

    # 직행(1억 이하)이 아닌 참가자들 중 가장 가치(denom)가 낮은 사람(가장 확률이 높은 사람) 탈락 판정
    non_direct = [c for c in contestants if not c["direct_pass"]]
    eliminated_person = min(non_direct, key=lambda x: x["denom"]) if non_direct else None

    # 최고 희귀도 아우라를 뽑은 MVP 찾기
    mvp_contestant = max(contestants, key=lambda x: x["denom"])

    player_survived = False
    if st.session_state.player_alive:
      if eliminated_person and eliminated_person["is_player"]:
        st.session_state.player_alive = False
        st.session_state.survival_logs.insert(0, f"💀 [결승 탈락] 플레이어님이 가장 확률이 높은 [{st.session_state.player_aura}]을(를) 뽑아 아쉽게 탈락했습니다!")
      else:
        player_survived = True
        st.session_state.wins += 1
        st.session_state.coins += 5000
        save_user_data_to_db()
        st.session_state.survival_logs.insert(0, f"🏆 [결승 최종 생존!] 플레이어님이 [{st.session_state.player_aura}]으로 최종 생존에 성공했습니다! (+5,000 G)")

    elim_msg = f"{eliminated_person['name']} ({eliminated_person['aura']})" if eliminated_person else "없음 (전원 1억 이하 직행!)"
    st.session_state.survival_logs.insert(
        0, f"👑 [대회 종료] 결승 MVP: {mvp_contestant['name']} [{mvp_contestant['aura']}] | 결승 탈락자: {elim_msg}"
    )
    st.session_state.final_winner_info = {
        "mvp": mvp_contestant,
        "eliminated": eliminated_person,
        "player_survived": player_survived,
        "all_contestants": sorted(contestants, key=lambda x: x["denom"], reverse=True)
    }
    st.session_state.survival_stage = 4
    st.rerun()

# 4단계: 최종 결과 화면
elif st.session_state.survival_stage == 4:
  st.subheader("🏁 100인 아우라 서바이벌 최종 결과")
  info = st.session_state.final_winner_info

  if info:
    if info["player_survived"]:
      st.balloons()
      st.success(f"🏆 축하합니다! [{st.session_state.player_aura}]으로 최종 생존하셨습니다! (+5,000 G 획득)")
    else:
      st.info("👁️ 관전 종료! 당신은 중도 탈락했지만 100인 배틀로얄이 끝까지 진행되어 최종 승자가 가려졌습니다.")

    mvp = info["mvp"]
    elim = info["eliminated"]
    col_r1, col_r2 = st.columns(2)
    with col_r1:
      st.metric("👑 결승전 최고 희귀도 MVP", f"{mvp['name']}", f"{mvp['aura']} (1 in {mvp['denom']:,})")
    with col_r2:
      if elim:
        st.metric("💀 결승전 최하위 탈락자", f"{elim['name']}", f"{elim['aura']} (1 in {elim['denom']:,})")
      else:
        st.metric("💀 결승전 최하위 탈락자", "없음", "전원 1억 이하 직행!")

    with st.expander("📊 결승 진출자 25명 전체 결과표 보기", expanded=True):
      for idx, c in enumerate(info["all_contestants"], 1):
        tag = "✨ [1억 이하 직행]" if c["direct_pass"] else ("💀 [최하위 탈락]" if elim and c["name"] == elim["name"] else "✅ [생존]")
        me_mark = " 👈 (나)" if c["is_player"] else ""
        st.write(f"**{idx}위.** {c['name']}{me_mark} — {icons.get(c['aura'], '✨')} **{c['aura']}** (`1 in {c['denom']:,}`) | {tag}")

  if st.button("🔄 새 배틀로얄 시작하기", type="primary", use_container_width=True):
    st.session_state.survival_stage = 0
    st.rerun()

st.divider()
st.markdown("### 📜 실시간 배틀로얄 중계 로그")
for log in st.session_state.survival_logs[:12]:
  st.text(log)
