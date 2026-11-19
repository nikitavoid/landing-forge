"""LandingForge — describe a business in one line, get a ready landing page.

Usage:
    python forge.py "Cozy coffee shop in Minsk with homemade desserts"
    python forge.py "Online English school for kids" --color "#ff8906" --out school.html
"""

import argparse
import re
import sys
import webbrowser
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-opus-5-5"

SYSTEM = """You are a senior web designer. Create a complete, modern, responsive
landing page as ONE self-contained HTML file (inline CSS, no external JS).
Include: hero with headline and call-to-action, 3 benefits, how it works,
testimonials, pricing or offer, FAQ, contact section and footer.
Use the accent color given by the user. Write realistic marketing copy in the
language of the description. Output only the HTML, starting with <!doctype html>."""


def generate(description: str, color: str) -> str:
    client = anthropic.Anthropic()
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=64000,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"Business: {description}\nAccent color: {color}"}],
        output_config={"effort": "medium"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    ) as stream:
        for event in stream:
            if event.type == "content_block_delta" and event.delta.type == "text_delta":
                print(".", end="", flush=True)  # progress dots
        message = stream.get_final_message()
    print()
    if message.stop_reason == "refusal":
        sys.exit("The model declined this request. Try another description.")
    html = "".join(b.text for b in message.content if b.type == "text")
    # remove ```html fences if the model added them
    return re.sub(r"^```(?:html)?\s*|\s*```$", "", html.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a landing page with AI")
    parser.add_argument("description", help="what the business is about")
    parser.add_argument("--color", default="#7f5af0", help="accent color (hex)")
    parser.add_argument("--out", default="landing.html", help="output file")
    parser.add_argument("--no-open", action="store_true", help="don't open the browser")
    args = parser.parse_args()

    print(f"⚒️  Forging a landing page for: {args.description}")
    try:
        html = generate(args.description, args.color)
    except anthropic.APIError as e:
        sys.exit(f"API error: {e}")

    out = Path(args.out)
    out.write_text(html, encoding="utf-8")
    print(f"✅ Saved to {out.resolve()}")
    if not args.no_open:
        webbrowser.open(out.resolve().as_uri())


if __name__ == "__main__":
    main()
