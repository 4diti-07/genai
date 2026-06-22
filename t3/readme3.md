
This project is a Streamlit-based AI Image Generator that allows users to generate images from text prompts using the Hugging Face Inference API. Users can choose different artistic styles such as Anime, Cyberpunk, Fantasy, Sketch, and Realistic.

#Features
* Streamlit frontend
* Text input for image prompts
* Style selection using radio buttons
* AI image generation using Hugging Face API
* Display generated images
* Prompt history
* Environment variable support for API keys

#Requirements

```text
T3/
│
├── app.py
├── api.py
├── prompts.py
├── .env
├── README.md
└── .gitignore


#Adding the API Key

Create a `.env` file in the project folder and add:

```env
HF_TOKEN=your_huggingface_token_here
```

You can get a token from:

https://huggingface.co/settings/tokens


#to run
Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

#Example

**Prompt:** A futuristic Indian city at night

**Style:** Cyberpunk

**Output:** An AI-generated image with a futuristic cyberpunk aesthetic.

#Technologies Used
* Python
* Streamlit
* Hugging Face Inference API
* Requests
* Python-dotenv

---
Image generation speed depends on the Hugging Face API and internet connection. Sometimes the API may take longer to respond or temporarily fail if free usage limits are reached.

