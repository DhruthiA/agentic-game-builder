import os


class GameAgentController:

    def __init__(self, clarifier, planner, builder):
        self.clarifier = clarifier
        self.planner = planner
        self.builder = builder

    def run(self, idea):

        print("\n--- Clarification Phase ---\n")

        questions = self.clarifier.run(idea)
        print(questions)

        answers = input("\nEnter answers:\n")

        print("\n--- Planning Phase ---\n")

        plan = self.planner.run(idea, answers)
        print(plan)

        print("\n--- Execution Phase ---\n")

        files = self.builder.run(plan)

        if not files:
            print("Game generation failed")
            return

        os.makedirs("output", exist_ok=True)

        for name, code in files.items():

            path = os.path.join("output", name)

            with open(path, "w", encoding="utf-8") as f:
                f.write(code)

        print("\nGame generated successfully!")
        print("Open output/index.html in your browser")