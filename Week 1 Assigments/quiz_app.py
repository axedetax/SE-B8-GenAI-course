import streamlit as st
import random
import json
import folium
from streamlit_folium import st_folium

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="India States Quiz",
    page_icon="🇮🇳",
    layout="wide"
)

# -------------------------------------------------
# QUIZ DATA — 28 STATES
# -------------------------------------------------
quiz_data = [
    {
        "state": "Andhra Pradesh",
        "capital": "Amaravati",
        "options": ["Amaravati", "Hyderabad", "Visakhapatnam", "Chennai"]
    },
    {
        "state": "Arunachal Pradesh",
        "capital": "Itanagar",
        "options": ["Dispur", "Imphal", "Itanagar", "Gangtok"]
    },
    {
        "state": "Assam",
        "capital": "Dispur",
        "options": ["Dispur", "Shillong", "Agartala", "Aizawl"]
    },
    {
        "state": "Bihar",
        "capital": "Patna",
        "options": ["Patna", "Ranchi", "Lucknow", "Raipur"]
    },
    {
        "state": "Chhattisgarh",
        "capital": "Raipur",
        "options": ["Raipur", "Bhopal", "Ranchi", "Nagpur"]
    },
    {
        "state": "Goa",
        "capital": "Panaji",
        "options": ["Panaji", "Mumbai", "Pune", "Mangaluru"]
    },
    {
        "state": "Gujarat",
        "capital": "Gandhinagar",
        "options": ["Ahmedabad", "Surat", "Gandhinagar", "Rajkot"]
    },
    {
        "state": "Haryana",
        "capital": "Chandigarh",
        "options": ["Chandigarh", "Delhi", "Jaipur", "Shimla"]
    },
    {
        "state": "Himachal Pradesh",
        "capital": "Shimla",
        "options": ["Shimla", "Dehradun", "Srinagar", "Chandigarh"]
    },
    {
        "state": "Jharkhand",
        "capital": "Ranchi",
        "options": ["Patna", "Ranchi", "Raipur", "Bhubaneswar"]
    },
    {
        "state": "Karnataka",
        "capital": "Bengaluru",
        "options": ["Mysuru", "Panaji", "Bengaluru", "Chennai"]
    },
    {
        "state": "Kerala",
        "capital": "Thiruvananthapuram",
        "options": ["Kochi", "Thiruvananthapuram", "Chennai", "Bhopal"]
    },
    {
        "state": "Madhya Pradesh",
        "capital": "Bhopal",
        "options": ["Indore", "Bhopal", "Jabalpur", "Raipur"]
    },
    {
        "state": "Maharashtra",
        "capital": "Mumbai",
        "options": ["Mumbai", "Pune", "Nagpur", "Surat"]
    },
    {
        "state": "Manipur",
        "capital": "Imphal",
        "options": ["Imphal", "Aizawl", "Kohima", "Shillong"]
    },
    {
        "state": "Meghalaya",
        "capital": "Shillong",
        "options": ["Dispur", "Shillong", "Gangtok", "Agartala"]
    },
    {
        "state": "Mizoram",
        "capital": "Aizawl",
        "options": ["Aizawl", "Imphal", "Agartala", "Kohima"]
    },
    {
        "state": "Nagaland",
        "capital": "Kohima",
        "options": ["Imphal", "Kohima", "Shillong", "Dispur"]
    },
    {
        "state": "Odisha",
        "capital": "Bhubaneswar",
        "options": ["Bhubaneswar", "Ranchi", "Patna", "Raipur"]
    },
    {
        "state": "Punjab",
        "capital": "Chandigarh",
        "options": ["Amritsar", "Chandigarh", "Ludhiana", "Patiala"]
    },
    {
        "state": "Rajasthan",
        "capital": "Jaipur",
        "options": ["Jaipur", "Udaipur", "Jodhpur", "Ajmer"]
    },
    {
        "state": "Sikkim",
        "capital": "Gangtok",
        "options": ["Gangtok", "Shillong", "Itanagar", "Dispur"]
    },
    {
        "state": "Tamil Nadu",
        "capital": "Chennai",
        "options": ["Chennai", "Bengaluru", "Hyderabad", "Kochi"]
    },
    {
        "state": "Telangana",
        "capital": "Hyderabad",
        "options": ["Hyderabad", "Amaravati", "Bengaluru", "Nagpur"]
    },
    {
        "state": "Tripura",
        "capital": "Agartala",
        "options": ["Agartala", "Aizawl", "Shillong", "Dispur"]
    },
    {
        "state": "Uttar Pradesh",
        "capital": "Lucknow",
        "options": ["Kanpur", "Lucknow", "Agra", "Varanasi"]
    },
    {
        "state": "Uttarakhand",
        "capital": "Dehradun",
        "options": ["Shimla", "Dehradun", "Haridwar", "Nainital"]
    },
    {
        "state": "West Bengal",
        "capital": "Kolkata",
        "options": ["Patna", "Kolkata", "Ranchi", "Bhubaneswar"]
    }
]

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    random.shuffle(quiz_data)

if "score" not in st.session_state:
    st.session_state.score = 0

# -------------------------------------------------
# CURRENT QUESTION
# -------------------------------------------------
question = quiz_data[st.session_state.current_question]

# -------------------------------------------------
# KID FRIENDLY UI STYLES
# -------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to bottom, #E3F2FD, #FFF9C4);
    }

    h1 {
        font-family: Comic Sans MS;
    }

    .stButton > button {
        background-color: #FF9800;
        color: white;
        border-radius: 15px;
        height: 3em;
        width: 15em;
        font-size: 20px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #4CAF50;
        transform: scale(1.08);
    }

    div[data-testid="stRadio"] label {
        background-color: #000000;
        color: #000000;
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
        border: 2px solid #000000;
        font-size: 18px;
        font-weight: bold;
    }

    div[data-testid="stRadio"] p {
        color: #000000 !important;
    }

    div[data-testid="stRadio"] span {
        color: #000000 !important;
    }

    div[data-testid="stRadio"] label:hover {
        background-color: #FFE082;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.markdown(
    """
    <h1 style='text-align:center;color:#FF6F00;'>🌟 🇮🇳 India States & Capitals Quiz 🌟</h1>
    <h3 style='text-align:center;color:#1565C0;'>🧒 Learn Geography the Fun Way! 👧</h3>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# LOAD GEOJSON
# -------------------------------------------------
with open("india_states.geojson", "r", encoding="utf-8") as f:
    india_geojson = json.load(f)

# -------------------------------------------------
# MAP CREATION
# -------------------------------------------------
m = folium.Map(
    location=[22.5, 80],
    zoom_start=4.8,
    tiles="CartoDB positron"
)

# -------------------------------------------------
# HIGHLIGHT FUNCTION
# -------------------------------------------------
def style_function(feature):

    state_name = feature["properties"].get("NAME_1", "")

    if state_name.lower() == question["state"].lower():
        return {
            "fillColor": "green",
            "color": "black",
            "weight": 3,
            "fillOpacity": 0.8,
        }

    return {
        "fillColor": "lightgray",
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.3,
    }

# -------------------------------------------------
# HOVER EFFECTS
# -------------------------------------------------
highlight_function = lambda x: {
    "fillColor": "orange",
    "color": "red",
    "weight": 3,
    "fillOpacity": 0.7,
}

# -------------------------------------------------
# ADD GEOJSON TO MAP
# -------------------------------------------------
folium.GeoJson(
    india_geojson,
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.GeoJsonTooltip(
        fields=["NAME_1"],
        aliases=["State:"],
        sticky=True
    )
).add_to(m)

# -------------------------------------------------
# DISPLAY MAP
# -------------------------------------------------
st.subheader(
    f"Find the capital of: {question['state']}"
)

st.markdown(
    "### 🗺️ Hover over the map to explore the states"
)

st_folium(
    m,
    width=900,
    height=500
)

# -------------------------------------------------
# QUIZ OPTIONS
# -------------------------------------------------
selected_answer = st.radio(
    "Choose the correct capital:",
    question["options"]
)

# -------------------------------------------------
# SUBMIT ANSWER
# -------------------------------------------------
if st.button("Submit Answer"):

    # CORRECT ANSWER
    if selected_answer == question["capital"]:

        st.session_state.score += 1

        st.success("✅ Correct Answer!")

        # CLAP SOUND
        audio_file = open("Clap.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        st.balloons()

        st.markdown(
            """
            <style>
            div.stButton > button {
                animation: pulse 1s infinite;
            }

            @keyframes pulse {
                0% {transform: scale(1);}
                50% {transform: scale(1.05);}
                100% {transform: scale(1);}
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # WRONG ANSWER
    else:

        st.error(
            f"❌ Oops! Wrong Answer. Correct answer is {question['capital']}"
        )

        # WRONG SOUND
        audio_file = open("wrong.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

    # NEXT QUESTION
    if st.session_state.current_question < len(quiz_data) - 1:
        st.session_state.current_question += 1
        st.rerun()

if st.session_state.current_question == len(quiz_data) - 1:

    st.markdown("---")

    st.header(
        f"🏆 Final Score: {st.session_state.score}/{len(quiz_data)}"
    )

    percentage = (
        st.session_state.score / len(quiz_data)
    ) * 100

    st.subheader(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        st.success("🌟 Perfect Score!")

    elif percentage >= 70:
        st.success("👏 Excellent Work!")

    elif percentage >= 40:
        st.warning("👍 Good Try!")

    else:
        st.error("📚 Keep Practicing!")
    