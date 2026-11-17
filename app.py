"""Drug Information Explorer: a local Streamlit learning app for pharmacy students By Samarth."""

from datetime import date
import random

import streamlit as st

from drug_data import DRUGS


st.set_page_config(
    page_title="PharmaNova By Samarth",
    page_icon="D",
    layout="centered",
)

# A small amount of CSS adds the requested blue/green accents. Streamlit still
# handles the layout and responsive behavior.
st.markdown(
    """
    <style>
      :root {
        --ink: #17324d;
        --blue: #2563a6;
        --green: #167c68;
        --soft-blue: #eff6fc;
        --soft-green: #edf8f4;
      }
      .stApp { background: #ffffff; color: var(--ink); }
      h1, h2, h3 { color: var(--ink); letter-spacing: -0.02em; }
      [data-testid="stMetric"] {
        background: var(--soft-blue);
        border: 1px solid #dceaf5;
        border-radius: 12px;
        padding: 14px 16px;
      }
      .stButton > button {
        border-radius: 9px;
        border-color: #b8d8e8;
        color: var(--blue);
      }
      .stButton > button:hover {
        border-color: var(--green);
        color: var(--green);
      }
      a { color: var(--blue) !important; }
      .safety-note {
        background: var(--soft-green);
        border-left: 4px solid var(--green);
        border-radius: 8px;
        padding: 12px 16px;
        margin: 8px 0 18px;
      }
      @media (max-width: 640px) {
        .block-container { padding-top: 1.25rem; padding-bottom: 2rem; }
      }
</style>
    """,
    unsafe_allow_html=True,
)


def find_matches(search_text):
    """Return drugs whose generic name or common generic synonym matches."""
    query = search_text.strip().casefold()
    if not query:
        return DRUGS

    return [
        drug
        for drug in DRUGS
        if query in drug["generic_name"].casefold()
        or any(query in alias.casefold() for alias in drug["aliases"])
    ]


def render_bullet_list(items):
    """Show a short list of learning points in Streamlit."""
    for item in items:
        st.markdown(f"- {item}")


def render_drug_details(drug):
    """Render the complete learning profile for one medicine."""
    st.subheader(drug["generic_name"])
    if drug["aliases"]:
        st.caption("Also known as: " + ", ".join(drug["aliases"]))

    st.markdown(f"**Pharmacological class**  \n{drug['class_name']}")
    st.markdown("#### Mechanism of action")
    st.write(drug["mechanism"])

    left, right = st.columns(2)
    with left:
        st.markdown("#### Therapeutic uses")
        render_bullet_list(drug["therapeutic_uses"])
    with right:
        st.markdown("#### Common adverse effects and key toxicities")
        render_bullet_list(drug["adverse_effects"])

    st.markdown("#### Important precautions")
    render_bullet_list(drug["precautions"])

    st.markdown("#### Clinical pearls")
    render_bullet_list(drug["clinical_pearls"])

    with st.expander("Authoritative references"):
        st.caption(
            "These are educational paraphrases. Check the current product label "
            "and local guidance for clinical use."
        )
        for reference in drug["references"]:
            st.markdown(f"- [{reference['title']}]({reference['url']})")


def get_flashcards():
    """Build editable revision cards from drug_data.py."""
    prompts = [
        ("class_name", "What is the pharmacological class?"),
        ("mechanism", "How does it work?"),
        ("therapeutic_uses", "What are common therapeutic uses?"),
        ("clinical_pearls", "What is one useful clinical pearl?"),
    ]
    cards = []
    for drug in DRUGS:
        for field, question in prompts:
            answer = drug[field]
            if isinstance(answer, list):
                answer = "; ".join(answer)
            cards.append(
                {
                    "drug_name": drug["generic_name"],
                    "question": question,
                    "answer": answer,
                }
            )
    return cards


def start_new_quiz():
    """Select five different medicines and create four-option class questions."""
    selected_drugs = random.sample(DRUGS, k=5)
    questions = []
    all_classes = list({drug["class_name"] for drug in DRUGS})

    for drug in selected_drugs:
        correct_answer = drug["class_name"]
        other_classes = [name for name in all_classes if name != correct_answer]
        options = random.sample(other_classes, k=3) + [correct_answer]
        random.shuffle(options)
        questions.append(
            {
                "drug_name": drug["generic_name"],
                "correct_answer": correct_answer,
                "options": options,
            }
        )

    st.session_state.quiz_questions = questions
    st.session_state.quiz_submitted = False
    st.session_state.quiz_score = None
    for index in range(5):
        st.session_state.pop(f"quiz_answer_{index}", None)


def render_explore_page():
    st.title("PharmaNova")
    st.caption("Learn Pharmacology • Explore Medicines • Test Your Knowledge")
    st.markdown(
        '<div class="safety-note"><strong>Educational resource only.</strong> '
        "This app is not a medical advice tool. It does not provide "
        "personalized treatment recommendations or medication doses.</div>",
        unsafe_allow_html=True,
    )

    # A date-seeded generator picks a random medicine but keeps it stable
    # throughout the day, including when Streamlit reruns the page.
    daily_drug = random.Random(date.today().isoformat()).choice(DRUGS)
    with st.container(border=True):
        st.caption(f"DRUG OF THE DAY · {date.today():%A, %B %d}")
        st.subheader(daily_drug["generic_name"])
        st.write(daily_drug["class_name"])
        st.write(daily_drug["clinical_pearls"][0])
        if st.button("Explore today's medicine", key="daily_drug_button"):
            st.session_state.drug_search = daily_drug["generic_name"]
            st.rerun()

    st.markdown("### Search the medicine library")
    search_text = st.text_input(
        "Search by generic name",
        placeholder="Try metformin or salbutamol",
        key="drug_search",
    )
    matches = find_matches(search_text)

    if not matches:
        st.info("No matching medicines. Try another generic name.")
        return

    selected_name = st.selectbox(
        "Matching medicines",
        options=[drug["generic_name"] for drug in matches],
        index=0 if len(matches) == 1 else None,
        placeholder="Choose a medicine",
    )
    if selected_name:
        selected_drug = next(
            drug for drug in matches if drug["generic_name"] == selected_name
        )
        with st.container(border=True):
            render_drug_details(selected_drug)
    else:
        st.caption(
            f"{len(matches)} medicine(s) available. Keep typing to narrow the list."
        )


def render_flashcards_page():
    st.title("Flashcards")
    st.caption("Reveal the answer, then move on when you are ready.")
    cards = get_flashcards()
    if "flashcard_index" not in st.session_state:
        st.session_state.flashcard_index = 0
    if "flashcard_revealed" not in st.session_state:
        st.session_state.flashcard_revealed = False

    card_index = st.session_state.flashcard_index % len(cards)
    card = cards[card_index]
    st.progress((card_index + 1) / len(cards))
    st.caption(f"Card {card_index + 1} of {len(cards)}")

    with st.container(border=True):
        st.caption(card["drug_name"])
        st.subheader(card["question"])
        if st.session_state.flashcard_revealed:
            st.write(card["answer"])
        else:
            st.write("Think of the answer, then reveal it.")

    reveal_col, next_col = st.columns(2)
    with reveal_col:
        if st.button(
            "Hide answer" if st.session_state.flashcard_revealed else "Reveal answer",
            key="flashcard_reveal",
            use_container_width=True,
        ):
            st.session_state.flashcard_revealed = (
                not st.session_state.flashcard_revealed
            )
            st.rerun()
    with next_col:
        if st.button("Next card", key="flashcard_next", use_container_width=True):
            st.session_state.flashcard_index += 1
            st.session_state.flashcard_revealed = False
            st.rerun()


def render_quiz_page():
    st.title("Five-question quiz")
    st.caption("Match each medicine to its pharmacological class.")

    if "quiz_questions" not in st.session_state:
        start_new_quiz()

    if st.session_state.quiz_submitted:
        score = st.session_state.quiz_score
        st.metric("Your score", f"{score} / 5")
        for index, question in enumerate(st.session_state.quiz_questions):
            chosen = st.session_state.get(f"quiz_answer_{index}")
            is_correct = chosen == question["correct_answer"]
            label = "Correct" if is_correct else "Review"
            st.markdown(f"**{index + 1}. {question['drug_name']} — {label}**")
            st.write(f"Correct class: {question['correct_answer']}")
        if st.button("Start a new five-question quiz", key="new_quiz_after_score"):
            start_new_quiz()
            st.rerun()
        return

    with st.form("drug_quiz"):
        for index, question in enumerate(st.session_state.quiz_questions):
            st.markdown(
                f"**{index + 1}. What is the pharmacological class of "
                f"{question['drug_name']}?**"
            )
            st.radio(
                f"Choose one for question {index + 1}",
                options=question["options"],
                index=None,
                key=f"quiz_answer_{index}",
                label_visibility="collapsed",
            )
        submitted = st.form_submit_button("Check answers", type="primary")

    if submitted:
        answers = [
            st.session_state.get(f"quiz_answer_{index}") for index in range(5)
        ]
        if any(answer is None for answer in answers):
            st.warning("Please answer all five questions before checking your score.")
        else:
            st.session_state.quiz_score = sum(
                answer == question["correct_answer"]
                for answer, question in zip(
                    answers, st.session_state.quiz_questions
                )
            )
            st.session_state.quiz_submitted = True
            st.rerun()


def render_about_page():
    st.title("About PharmaNova")

    st.markdown("### Our Purpose")

    st.write(
        "PharmaNova is an interactive learning platform designed "
        "to make pharmacology easier to explore, understand, and revise. "
        "It brings essential drug information, revision flashcards, "
        "and knowledge-based quizzes together in one place."
    )

    st.markdown("### What PharmaNova Offers")

    st.markdown(
        """
        - **Drug Explorer:** Access essential pharmacological information.
        - **Flashcards:** Strengthen memory through active recall.
        - **Quizzes:** Test and reinforce pharmacology knowledge.
        - **Drug of the Day:** Discover and revise a medicine daily.
        """
    )

    st.markdown("### About the Creator")

    st.write(
        "PharmaNova is a personal educational project created "
        "by Samarth Ambi, a pharmacy student with an interest "
        "in pharmacology and healthcare innovation."
    )

    st.markdown("### References")

    st.write(
        "Educational content is supported by publicly available "
        "drug information resources, including MedlinePlus and DailyMed."
    )

    st.markdown("### Disclaimer")

    st.caption(
        "PharmaNova is intended for educational purposes only. "
        "The information provided should not replace professional "
        "medical advice or official prescribing information."
    )


page = st.radio(
    "Main navigation",
    ["Explore", "Flashcards", "Quiz", "About"],
    horizontal=True,
    label_visibility="collapsed",
)

if page == "Explore":
    render_explore_page()
elif page == "Flashcards":
    render_flashcards_page()
elif page == "Quiz":
    render_quiz_page()
else:
    render_about_page()
    st.divider()

st.markdown(
    """
    <div style="text-align: center; color: #64748b; font-size: 13px;">
         PharmaNova <br>
        Created by <strong>Samarth Ambi</strong><br>
        Made for learning
    </div>
    """,
    unsafe_allow_html=True
)