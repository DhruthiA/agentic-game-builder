import re
from templates.prompt_templates import builder_prompt


class BuilderAgent:

    def __init__(self, client):
        self.client = client

    def clean(self, text):

        text = text.replace("```html", "")
        text = text.replace("```css", "")
        text = text.replace("```javascript", "")
        text = text.replace("```", "")

        return text.strip()

    def extract_sections(self, text):

        # Format 1
        html = re.search(r"===INDEX_HTML===([\s\S]*?)===STYLE_CSS===", text)
        css = re.search(r"===STYLE_CSS===([\s\S]*?)===GAME_JS===", text)
        js = re.search(r"===GAME_JS===([\s\S]*)", text)

        # Format 2
        if not html:
            html = re.search(r"INDEX_HTML([\s\S]*?)STYLE_CSS", text)

        if not css:
            css = re.search(r"STYLE_CSS([\s\S]*?)GAME_JS", text)

        if not js:
            js = re.search(r"GAME_JS([\s\S]*)", text)

        if not html or not css or not js:
            return None

        return {
            "index.html": self.clean(html.group(1)),
            "style.css": self.clean(css.group(1)),
            "game.js": self.clean(js.group(1))
        }

    def run(self, plan):

        prompt = builder_prompt.format(plan=plan)

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content

        files = self.extract_sections(content)

        if not files:
            print("\nCould not parse generated files\n")
            print(content)
            return None

        return files