import os
import platform
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

machine_details = platform.uname()
while True:
    req = input("> ")
    if req == "exit":
        break
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"# Shell script to {req} on a {machine_details.system} with version {machine_details.release} on a {machine_details.machine}\n",
      temperature=0,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    code = response.choices[0].text
    print(code)
    run = input("Run the above code? (Y/N): ")
    if run.lower() == "yes" or run.lower() == "y":
        os.system(code)
