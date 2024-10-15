import re
import argparse
import google.generativeai as genai


def main(args):
    genai.configure(api_key=args.api)

    # Create the model
    generation_config = {
        "temperature": 0.5,
        "top_p": 0.8,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        )

    try:
        chat_session = model.start_chat(
            history=[]
            )
        
        response = chat_session.send_message(args.prompt)
        text = re.findall(r'\{\{(.*?)\}\}',response.text)[0].strip()

    except Exception as e:
        text = ""
    
    with open('README.md', 'w+') as f:
        f.write(text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api', type=str, default='')
    parser.add_argument('--prompt', type=str, default="")
    args = parser.parse_args()

    main(args)
