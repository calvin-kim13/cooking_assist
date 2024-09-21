import argparse

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
    user_prompt = f"I'm looking for a recipe that serves {args.serving_size} people, uses the following ingredients: [{args.ingredients}], and falls under {args.cuisine} cuisine. Please ensure it's free from {args.allergies}. I'd also like tips for substitutions if I want to modify the recipe in the future."
else:
    user_prompt = f"I'm looking for a recipe that serves {args.serving_size} people, uses the following ingredients: [{args.ingredients}], and falls under {args.cuisine} cuisine. I'd also like tips for substitutions if I want to modify the recipe in the future."

print(user_prompt)
