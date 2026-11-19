# ⚒️ LandingForge

Describe a business in one sentence and get a complete, responsive landing page in a single HTML file.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/Output-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![AI](https://img.shields.io/badge/AI-LLM-7f5af0?style=flat-square)

## Features

- 🧱 Full page structure: hero, benefits, steps, reviews, pricing, FAQ, contacts
- 🎨 Custom accent color
- 📱 Mobile-friendly layout
- 📄 One self-contained file, ready to upload to any hosting or GitHub Pages

## Quick start

```bash
git clone https://github.com/nikitavoid/landing-forge
cd landing-forge
pip install -r requirements.txt
cp .env.example .env   # add your Anthropic API key

python forge.py "Cozy coffee shop in Minsk with homemade desserts"
python forge.py "Online English school for kids" --color "#ff8906" --out school.html
```

The page opens in your browser as soon as it's ready.

## Options

| Flag | Default | Description |
|---|---|---|
| `--color` | `#7f5af0` | Accent color |
| `--out` | `landing.html` | Output file |
| `--no-open` | — | Don't open the browser |

## License

MIT
