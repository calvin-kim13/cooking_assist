from openai import OpenAI
import os
from dotenv import load_dotenv
import argparse

load_dotenv()


class AIcontext:

    def __init__(self):
        # these are passed in from the CLI
        self.api_key = os.getenv("OPEN_API_KEY")

        if not self.api_key:
            raise ValueError("API key not found")

        

    def run_arg_parser(self):
        # Create an ArgumentParser object
        parser = argparse.ArgumentParser(description="A simple argument parser example")

        # Add arguments
        parser.add_argument(
            "--cuisine",
            choices=["Korean", "Indian", "American", "Italian", "Arabic"],
            help="Cuisine Type",
            required=True,
            )
        parser.add_argument(
            "--ingredients", type=str, help="List of Ingredients", required=True
        )
        parser.add_argument("--allergies", type=str, help="Allergies", required=False)
        parser.add_argument("--serving_size", type=float, help="Serving Size", required=True)

    # Parse the arguments
        args = parser.parse_args()

        if args.allergies:
            self.user_prompt = f"I'm looking for a recipe that serves {args.serving_size} people, uses the following ingredients: [{args.ingredients}], and falls under {args.cuisine} cuisine. Please ensure it's free from {args.allergies}. I'd also like tips for substitutions if I want to modify the recipe in the future."
        else:
            self.user_prompt = f"I'm looking for a recipe that serves {args.serving_size} people, uses the following ingredients: [{args.ingredients}], and falls under {args.cuisine} cuisine. I'd also like tips for substitutions if I want to modify the recipe in the future."

    def api_request_chatgpt(self):

        # we want to basically

        client = OpenAI(api_key=self.api_key)

        SYSTEM_PROMPT = """You are a friendly, knowledgeable cooking assistant who is familiar with a wide variety of cuisines and dishes. 
        You love sharing different recipes and food, and your goal is to generate personalized recipes for for people to 
        try within the comfort of their own kitchens. When generating recipes, please make sure to include: the name of the dish, 
        the ingredients, the cooking steps, the type of cuisines, and allergy information. If a user asks about 
        topics outside of our area of expertise, politely inform that you are unable to provide assistance. Also ensure 
        that your recipes are clear, organized, and easy-to-follow and they match the demands of the user. Try to strike 
        a balance between simple words and cooking-specific terminology and use your best judgement to adjust the level of complexity. """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT}, 
                {"role": "user", "content": self.user_prompt}
            ]
        )

        finalize_response = response.choices[0].message.content

        return finalize_response


if __name__ == "__main__":
    CreateLLM = AIcontext()
    CreateLLM.run_arg_parser()
    final_response = CreateLLM.api_request_chatgpt()
    print(final_response)

