# Drug Information Explorer

A local Streamlit learning app for pharmacy students to search and revise ten commonly studied medicines.

## Run & Operate

- `uv run streamlit run app.py --server.address 0.0.0.0 --server.port 8000` — run the Streamlit app
- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages

The Streamlit app uses the local Python data in `drug_data.py`; it does not need a database, API credentials, or authentication.

## Stack

- Python 3.11
- Streamlit
- Local Python data; no application database or external API

## Where things live

- `app.py` — Streamlit navigation, search, drug detail, flashcards, and quiz
- `drug_data.py` — editable local medicine summaries and references
- `README.md` — run instructions, project explanation, and beginner exercises

## Architecture decisions

- Keep the ten-medicine learning dataset local and editable in plain Python.
- Link summaries to MedlinePlus and DailyMed instead of using paid APIs.
- Keep the app educational and omit personalized treatment recommendations and doses.

## Product

Students can search generic medicine names, review sourced summaries, study with flashcards, take five-question quizzes, and see a daily featured medicine.

## User preferences

- Keep the application beginner-friendly, commented, and easy to modify while learning Python.
- Use a minimal, professional, mobile-friendly interface with white, blue, and green accents.

## Gotchas

- Run Streamlit on port 8000 so it does not overlap with the shared API server on port 5000.
- Medication information is educational and can vary by country and product; refer to current local sources for clinical work.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
