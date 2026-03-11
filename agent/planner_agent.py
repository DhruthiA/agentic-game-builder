from templates.prompt_templates import planning_prompt


class PlannerAgent:

    def __init__(self, client):
        self.client = client

    def run(self, idea, answers):

        prompt = planning_prompt.format(
            idea=idea,
            answers=answers
        )

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content