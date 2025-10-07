 Gemini RAG Demo App








An interactive Retrieval-Augmented Generation (RAG) demo app built with Streamlit and Google Gemini API.
Ask any question, get AI-generated responses enhanced with retrieval context, and dynamically adjust AI generation parameters. The app features a modern gradient UI and responsive sidebar controls.

 Features

Dynamic Query Handling – Responds to any question, not fixed answers.

Retrieval-Augmented Generation (RAG) – Combines user query with context for accurate responses.

Adjustable AI Parameters:

temperature – controls randomness

max_output_tokens – response length limit

top_p – nucleus sampling

top_k – top-k sampling

Modern UI – Gradient background, styled input fields, buttons.

Responsive Sidebar – Adjust parameters in real-time before generating responses.

 Technologies Used

Python – Backend logic

Streamlit – Interactive web UI

Google Gemini API – Generative AI

CSS Styling – Gradient backgrounds, styled inputs, buttons

 How It Works

User Input: Type a query in the text area.

Context Retrieval: A retriever function generates context for the query. (Currently placeholder; can be extended to PDFs, databases, or embeddings.)

Prompt Augmentation: Combines query + retrieved context.

AI Generation: Sends the prompt to Google Gemini API via generate_content.

Response Display: Shows the AI response along with the parameters used.

 Problems Faced & Solutions

Fixed Response: Initially returned only "Tell me about Elon Musk".
Solution: Implemented a dynamic retriever function to handle any query.

No Parameter Control: Users couldn’t tweak AI output.
Solution: Added sidebar sliders for temperature, max_output_tokens, top_p, and top_k.

Plain UI: Basic interface lacked appeal.
Solution: Added gradient background and styled input/buttons for modern design.

Error Handling: App could fail on empty or invalid input.
Solution: Added input validation and exception handling.

 Requirements

Python ≥ 3.8

Streamlit

Google Generative AI SDK (google-generativeai)

Install dependencies:

pip install -r requirements.txt

 Usage

Clone the repository:

git clone https://github.com/yourusername/gemini-rag-demo.git
cd gemini-rag-demo


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Enter Google Gemini API key.

Type a query, adjust parameters in the sidebar, and click Generate Response.

View the AI response and the parameters used.
