import streamlit as st
import google.generativeai as genai

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Gemini RAG App", page_icon="🤖", layout="centered")
st.title("🤖 Gemini RAG Demo App")

# Gemini API Key input (for demo purposes)
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # Dummy retriever for demonstration
    def retriever_info(query):
        """
        Here you could replace this with actual RAG logic like
        vector search, database lookup, or PDF retrieval.
        For now, we simply return the query itself as context.
        """
        return f"Retrieved context for: {query}"

    # Main RAG function
    def rag_query(query):
        retrieved_info = retriever_info(query)
        augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"

        model_name = "gemini-2.0-flash"  # try "gemini-pro" if flash not available
        model = genai.GenerativeModel(model_name)

        response = model.generate_content(
            augmented_prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 300
            }
        )
        return response.text.strip()

    # -------------------------------
    # UI Section
    # -------------------------------
    query = st.text_area("💬 Ask a question:", "Tell me about Elon Musk")

    if st.button("🔍 Generate Response"):
        if not query.strip():
            st.warning("Please enter a query first.")
        else:
            with st.spinner("Generating response..."):
                try:
                    answer = rag_query(query)
                    st.success("✅ Response Generated!")
                    st.markdown(f"**Answer:**\n\n{answer}")
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Please enter your Gemini API key to start.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Google Gemini API")
