import openai
import json

# Load your API key from an environment variable
openai.api_key = os.getenv(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")


def handle_form(request):
  # Get the prompt from the form data
  prompt = request.form["prompt"]

  # Call the GPT-3.5 API with the prompt
  response = openai.Completion.create(
    engine="text-bison-001",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
  )

  # Get the completion from the response
  completion = response["choices"][0]["text"]

return json.dumps({"completion": completion})