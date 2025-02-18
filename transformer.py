from transformers import pipeline

# Load pre-trained model for Question Answering
qa_pipeline = pipeline("question-answering")

# Function to answer a question based on the extracted text
def get_answer(context, question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Question input
question_input = st.text_input("Ask a Question")
if question_input:
    # Use the text extracted from PDF or URL
    context = text_from_pdf if uploaded_pdf else text_from_url
    answer = get_answer(context, question_input)
    st.write(f"Answer: {answer}")
