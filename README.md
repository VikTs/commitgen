# CommitGen

AI-powered tool to generate commit messages from git diff. 


## Tech Stack
- Python 3.9
- Groq API

## Getting started

### Installation

```
python3 -m venv venv        
source venv/bin/activate
pip install -r requirements.txt
```

### Setup Groq API key

1. Go to https://console.groq.com
2. Create an API key
3. Add it to .env under AI_API_KEY


## Usage

1. Stage your changes:
```
git add .
```

2. Generate commit message:
```
python3 main.py
```
