import streamlit as st
from transformers import pipeline
import torch

# Set page config
st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="wide"
)

# Initialize the summarization pipeline
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn", device=0 if torch.cuda.is_available() else -1)

def main():
    st.title("📝 Text Summarizer")
    st.write("Enter your text below and get a concise summary!")

    # Text input area
    text_input = st.text_area(
        "Enter your text here:",
        height=300,
        placeholder="Paste your text here..."
    )

    # Add a button to generate summary
    if st.button("Generate Summary"):
        if not text_input:
            st.warning("Please enter some text to summarize.")
            return

        try:
            # Load the summarizer
            summarizer = load_summarizer()

            # Show a spinner while processing
            with st.spinner("Generating summary..."):
                # Split text into chunks if it's too long (BART has a max input length)
                max_chunk_length = 1024
                chunks = [text_input[i:i + max_chunk_length] for i in range(0, len(text_input), max_chunk_length)]
                
                summaries = []
                for chunk in chunks:
                    # Generate summary for each chunk
                    summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
                    summaries.append(summary[0]['summary_text'])
                
                # Combine summaries if there were multiple chunks
                final_summary = " ".join(summaries)

            # Display the summary
            st.subheader("Summary:")
            st.write(final_summary)

            # Show some stats
            st.info(f"Original text length: {len(text_input)} characters")
            st.info(f"Summary length: {len(final_summary)} characters")
            st.info(f"Compression ratio: {len(final_summary)/len(text_input):.2%}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 