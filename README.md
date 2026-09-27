# MindAlive

Desktop learning project in Python with a CustomTkinter interface, cognitive mini-games and an optional Gemini assistant. The code is a prototype; it is not a clinical or professional service.

## Run locally

Use a Python environment with a graphical desktop. From the repository root:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python MindAlive.py
```

Activate the virtual environment before installing packages if desired. For the AI feature, set `GEMINI_API_KEY` in your operating-system environment. Example in PowerShell: `$env:GEMINI_API_KEY = "your-key"`; in Bash: `export GEMINI_API_KEY="your-key"`. Never commit a real key. Without a key, the games remain available and the assistant reports that it is unconfigured.

## Scope and verification

The repo contains memory, sequence, association, hangman and word-search activities, plus an optional chat. The optional portrait assets `assets/ana.png` and `assets/sandro.png` are not included; the app handles their absence. The code has been checked for Python syntax; the graphical interface and external API were not run here. API access may incur provider limits or costs.

## Next evidence for a portfolio

Add a screenshot or short screen recording of a local run, note your OS and Python version, and describe a concrete interaction. Avoid presenting generated answers as verified facts.
