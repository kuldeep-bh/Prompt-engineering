import streamlit as st
import google.generativeai as genai

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Gemini RAG App", page_icon="🤖", layout="centered")
st.title("🤖 Gemini RAG Demo App")

# Gemini API Key input
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # -------------------------------
    # Dummy retriever for demonstration
    # -------------------------------
    def retriever_info(query):
        """
        Placeholder for real RAG logic.
        Returns a context string for the query.
        """
        return f"Retrieved context for: {query}"

    # -------------------------------
    # Main RAG function
    # -------------------------------
    def rag_query(query, temperature, max_tokens, top_p, top_k):
        retrieved_info = retriever_info(query)
        augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"

        model_name = "gemini-2.0-flash"
        model = genai.GenerativeModel(model_name)

        response = model.generate_content(
            augmented_prompt,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens,
                "top_p": top_p,
                "top_k": top_k
            }
        )
        return response.text.strip()

    # -------------------------------
    # Sidebar for parameters
    # -------------------------------
    st.sidebar.header("⚙️ Generation Parameters")
    temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
    max_tokens = st.sidebar.slider("Max Output Tokens", min_value=50, max_value=1000, value=300, step=50)
    top_p = st.sidebar.slider("Top-p (nucleus sampling)", min_value=0.0, max_value=1.0, value=0.9, step=0.05)
    top_k = st.sidebar.slider("Top-k", min_value=0, max_value=100, value=40, step=5)

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
                    answer = rag_query(query, temperature, max_tokens, top_p, top_k)
                    st.success("✅ Response Generated!")
                    st.markdown(f"**Answer:**\n\n{answer}")

                    # Display the parameters used
                    st.markdown("---")
                    st.markdown("**Used Parameters:**")
                    st.markdown(f"- Temperature: {temperature}")
                    st.markdown(f"- Max Output Tokens: {max_tokens}")
                    st.markdown(f"- Top-p: {top_p}")
                    st.markdown(f"- Top-k: {top_k}")
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Please enter your Gemini API key to start.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Google Gemini API")
