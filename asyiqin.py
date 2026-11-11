
import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="A Little Birthday Wish 💗",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PERSONAL DETAILS
# ==========================================

HER_NAME = "Iqin"
YOUR_NAME = "Aiman"

# ==========================================
# CUSTOM CSS DESIGN
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@500;600&display=swap');

.stApp {
    background: linear-gradient(
        160deg,
        #fff8f6,
        #fce9ef,
        #fff5ed
    );
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 720px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #8e425e !important;
}

p {
    color: #70515d;
    line-height: 1.85;
}

div.stButton > button {
    background: #cb7994;
    color: white;
    border: none;
    border-radius: 24px;
    padding: 0.7rem 1.2rem;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #a95676;
    color: white;
    border: none;
}

.letter {
    background: rgba(255,255,255,0.83);
    border: 1px solid #f1d6df;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 30px rgba(150, 80, 110, 0.07);
}

.letter p {
    color: #70515d;
    line-height: 1.9;
}

.small-note {
    color: #987483;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# APPRECIATION CARDS
# ==========================================

COMPLIMENTS = [
    (
        "🌷",
        "Your kindness",
        "The little ways you care about people are worth appreciating."
    ),
    (
        "✨",
        "Your own light",
        "You have your own personality, dreams, and way of seeing the world."
    ),
    (
        "🦋",
        "Your independence",
        "You deserve the freedom to grow, explore, and be yourself."
    )
]


# ==========================================
# SESSION STATE
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "welcome"


def go_to(page):
    st.session_state.page = page


# ==========================================
# PAGE 1: WELCOME SCREEN
# ==========================================

if st.session_state.page == "welcome":

    st.markdown(
        "<h1 style='text-align:center;'>"
        "A Little Birthday Wish 🌷"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2 style='text-align:center;'>For {HER_NAME} ♡</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        "<div style='font-size:75px;text-align:center;'>💌</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='text-align:center;'>
        A little something I made for your special day.<br>
        I hope it brings a smile to your face.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "Open your little surprise 💗",
        use_container_width=True
    ):
        go_to("birthday")
        st.rerun()


# ==========================================
# PAGE 2: BIRTHDAY SURPRISE
# ==========================================

elif st.session_state.page == "birthday":

    st.markdown("# Happy Birthday! 🎂")

    st.markdown(
        "I hope today brings you little moments "
        "that make you genuinely happy."
    )

    st.write("")

    if st.button(
        "A little birthday magic ✨",
        use_container_width=True
    ):
        st.balloons()

    st.divider()

    st.subheader("Three little things worth celebrating")

    # Interactive appreciation cards

    for emoji, title, message in COMPLIMENTS:

        with st.expander(f"{emoji}  {title}"):
            st.write(message)

    st.write("")

    st.markdown(
        """
        <p style='text-align:center;'>
        Keep being yourself, chasing your dreams,
        and making your own beautiful memories. ♡
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "Read a little letter 💌",
        use_container_width=True
    ):
        go_to("letter")
        st.rerun()


# ==========================================
# PAGE 3: PERSONAL BIRTHDAY LETTER
# ==========================================

elif st.session_state.page == "letter":

    st.markdown("# A little note for you 💗")

    st.markdown("""
    <div class="letter">

    <p>Happy birthday! 🌷</p>

    <p>
    I wanted to make something a little different for your
    special day, so I made this small website just for you.
    </p>

    <p>
    I've been reflecting on things between us, and I've
    realised that expecting constant updates and replies
    wasn't fair to you. I understand that you have your
    own time, your own life, and things that matter to you.
    You shouldn't have to feel pressured to reply just
    to keep me happy.
    </p>

    <p>
    I'm sorry for the times I made you feel that pressure.
    I'm learning that caring about someone also means
    respecting their space, trusting them, and managing
    my own feelings instead of putting that responsibility
    on them.
    </p>

    <p>
    I know that saying these things is only a start.
    Real change comes from what I do consistently,
    and I have work to do on myself.
    </p>

    <p>
    Even though things between us have changed, I still
    appreciate the memories we've shared,
    and I genuinely wish good things for you.
    </p>

    <p>
    I hope your new year of life brings you peace,
    happiness, exciting opportunities, and people who
    make you feel loved and free to be yourself.
    </p>

    <p>
    You don't need to reply to this letter or say anything
    in return. I simply wanted to wish you a happy birthday
    and give you something made with care.
    </p>

    <p>
    Happy birthday. Take care of yourself, always. ❤️
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Signature

    st.markdown(
        f"""
        <div style='text-align:right;'>
            <p><i>With care,</i></p>
            <p><i>{YOUR_NAME}</i></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <p style='text-align:center;'>
        May life be kind to you. 🌸
        </p>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "Back to the birthday wishes 🌷",
        use_container_width=True
    ):
        go_to("birthday")
        st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.write("")

st.markdown(
    """
    <p style='text-align:center;font-size:12px;'>
    Made with care ♡
    </p>
    """,
    unsafe_allow_html=True
)
