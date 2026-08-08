# GenerativeAI LangChain Models

This repository contains a small set of LangChain practice scripts for Python integrations with OpenAI, Anthropic, and Google Gemini.

## What’s Included

- [`1.LLMs/`](1.LLMs)
  - [`1_llm_demo.py`](1.LLMs/1_llm_demo.py): basic LangChain LLM example using `langchain_openai.OpenAI`
- [`2.ChatModels/`](2.ChatModels)
  - [`1_chatmodel_openai.py`](2.ChatModels/1_chatmodel_openai.py): OpenAI chat model example
  - [`2_chatmodel_anthropic.py`](2.ChatModels/2_chatmodel_anthropic.py): Anthropic chat model example
  - [`3_chatmode_google.py`](2.ChatModels/3_chatmode_google.py): Google Gemini chat model example
- [`3.EmbeddedModels/`](3.EmbeddedModels): placeholder folder for future embedded or local model examples
- [`requirements.txt`](requirements.txt): Python dependencies for the workspace
- [`test.py`](test.py): simple LangChain version check
- [`.gitignore`](.gitignore): ignores the virtual environment, `.env`, editor files, and Python cache

## Requirements

- Python 3.13 or newer
- A virtual environment in `venv/`
- API keys for the providers you want to test:
  - `OPENAI_API_KEY`
  - `GOOGLE_API_KEY` or `GEMINI_API_KEY`
  - `ANTHROPIC_API_KEY`

## Setup

1. Create and activate the virtual environment if it does not already exist.

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install the dependencies.

```powershell
venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. Create a `.env` file in the repository root and add the API keys you need.

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Running Examples

Use the venv Python interpreter to run any script directly.

```powershell
venv\Scripts\python.exe 2.ChatModels\3_chatmode_google.py
```

If you only want to confirm the environment is working, run the version check script.

```powershell
venv\Scripts\python.exe test.py
```

## Notes

- The scripts load environment variables through `python-dotenv`.
- Some examples require active API billing or available quota.
- The Google Gemini example currently uses `gemini-2.0-flash`.
- The repository root is already configured to ignore `.env`, `venv/`, `.vscode/`, and Python cache files.

## Remote Repository

This workspace is connected to `https://github.com/Aryajais911/GenerativeAi`.
