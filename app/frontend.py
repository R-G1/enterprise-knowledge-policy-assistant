import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/ask"


st.set_page_config(
    page_title="Enterprise Knowledge & Policy Assistant",
    page_icon="📚",
    layout="centered"
)


st.title("📚 Enterprise Knowledge & Policy Assistant")

st.write(
    "Ask questions about company policies and get answers "
    "based on the available enterprise documents."
)


question = st.text_area(
    "Enter your question:",
    placeholder="e.g. How many annual leave days can I carry forward?",
    height=100
)


if st.button("Ask Question"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching company policies..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120
                )

                response.raise_for_status()

                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

                st.subheader("Sources")

                for source in data["sources"]:
                    st.write(f"- {source}")

            except requests.exceptions.RequestException as error:
                st.error(
                    "Could not connect to the FastAPI backend. "
                    "Make sure the API server is running."
                )
                st.code(str(error))