from google import genai
from google.genai import types
import datetime


def timestamp_module():
  timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")
  return timestamp

def generate(prompt):
  client = genai.Client(
      vertexai=True,
      project="vertex-ai-practice-458613",
      location="us-central1",
  )


  model = "gemini-2.0-flash-001"
  contents = [
    types.Content(
      role="user",
      parts=[types.Part(text=prompt)
      ]
    )
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 2,
    top_p = 0.95,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],


    system_instruction=[
          types.Part.from_text(text="""-You are a log analyser. Help analyse the logs. 
           - You have to analyse the latest log based on date and time. Dont analyse the 
           entire log. 
           - If logs for same day multiple time is available, take the latest batch based on time. Analyse 
           only the latest batch which are on same hour but separated by few seconds and micro seconds.
           - Mention which all the time stamp of lags in the batch of log which is being analysed.
           - Look for general trend. If there is deviation from general trend, then raise concern.
           - Give 3 important bullet points on the log. Compare the time taken by text case execution 
           from previous logs and compare the trend. If there is some unpreceded increase in time, analyse it 
           and brief about it.
           - Also give some suggestion if there are errors""")],

  )

  full_response = ""
  for chunk in client.models.generate_content_stream(
          model=model,
          contents=contents,
          config=generate_content_config,
  ):
    if chunk.text:
      full_response += chunk.text

  return full_response


file_object = open(r"C:\Users\91638\PycharmProjects\Hybrid framework\Logs\automation.log", "r")

prompt=file_object.read()

summary=generate(prompt)

timestamp=timestamp_module()
file_path=f"C:\\Users\\91638\\.jenkins\\workspace\\Hybrid framework Pipeline\\LogSummary\\log_summary_{timestamp}.txt"
with open(file_path, "w") as file:
  file.write(summary)