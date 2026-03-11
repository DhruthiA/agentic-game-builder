class RepairAgent:

    def __init__(self, client):
        self.client = client

    def repair(self, html, css, js):

        prompt = f"""
The following browser game has errors.

Fix the code so it runs correctly.

Return ONLY three sections:

===INDEX_HTML===
{html}

===STYLE_CSS===
{css}

===GAME_JS===
{js}
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response.choices[0].message.content