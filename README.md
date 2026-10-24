# Drug Information Explorer

A beginner-friendly Streamlit study app for pharmacy students. It includes a
local library of ten medicines, searchable drug summaries, revision flashcards,
a five-question quiz, and a daily featured medicine.

## Safety and intended use

This is an educational resource, not a medical advice tool. It does not provide
personalized treatment recommendations or medication doses. Drug approvals,
formulations, and precautions can vary by country and product. Always read the
current local product information and authoritative clinical guidance.

## Run the app

The app uses Python and Streamlit. From the project folder, run:

```bash
uv run streamlit run app.py --server.address 0.0.0.0 --server.port 8000
```

The app is also configured to open in the Replit preview.

## Project structure

### `app.py`

This is the user interface and app behavior:

- `find_matches()` filters the medicine list as the search text changes.
- `render_drug_details()` displays the selected medicine and its references.
- `get_flashcards()` turns the local data into question-and-answer cards.
- `start_new_quiz()` randomly selects five medicines and prepares the answer
  choices.
- The page-rendering functions make the Explore, Flashcards, Quiz, and About
  screens.

Streamlit reruns `app.py` when someone interacts with a widget. Values in
`st.session_state` keep the active flashcard and quiz answers between reruns.

### `drug_data.py`

This file holds the local medicine data in a Python list of dictionaries. Each
medicine has the same set of fields. Edit a dictionary here to change its
summary, add an alias, or update a reference. No database or external API is
used.

### `README.md`

This guide covers how to run the app, how the main parts fit together, and
practice exercises for modifying the code.

## How the main parts work

1. `app.py` imports `DRUGS` from `drug_data.py`.
2. The Explore page searches each generic name and its listed aliases.
3. The selected dictionary is rendered as a profile, including source links.
4. Flashcards are generated from the class, mechanism, uses, and clinical-pearl
   fields so they stay in sync with the local data.
5. The quiz samples five different medicines and asks about their
   pharmacological classes. Answers are checked locally in the browser session.
6. The Drug of the Day uses the current date to select one medicine. It does
   not call a service or use an API.

## Small coding exercises

1. **Add a medicine:** Add a new dictionary to `DRUGS` in `drug_data.py`. Copy
   the existing field names and include reliable reference links.
2. **Add a search alias:** Add a second generic synonym to a medicine's `aliases`
   list, then check that searching for it finds the medicine.
3. **Change the flashcards:** Add a prompt for `precautions` in
   `get_flashcards()` and try the new card in the app.
4. **Add a quiz question type:** Extend `start_new_quiz()` to quiz on a different
   field, such as therapeutic uses. Use only content already present in the
   local data for correct answers and distractors.
5. **Improve a source note:** Open one medicine's MedlinePlus and DailyMed
   references, verify a summary, and rewrite one bullet in your own words.

## Sources

Each medicine in `drug_data.py` links to its MedlinePlus drug-information page
and a DailyMed search for product labeling. MedlinePlus pages are maintained by
the U.S. National Library of Medicine; DailyMed is the National Library of
Medicine's drug-label resource. The app provides short paraphrases rather than
reproducing source text.
