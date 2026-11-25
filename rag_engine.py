
import os
from pypdf import PdfReader


# Load university knowledge from text files
def load_knowledge():

    knowledge = ""

    data_folder = "data"

    if not os.path.exists(data_folder):
        return knowledge

    for filename in os.listdir(data_folder):

        if filename.endswith(".txt"):

            file_path = os.path.join(data_folder, filename)

            with open(file_path, "r", encoding="utf-8") as file:

                content = file.read()

                knowledge += (
                    f"\n\n[SOURCE: {filename}]\n"
                    + content
                )

    return knowledge


# Extract PDF text with page numbers
def extract_pdf_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    extracted_text = ""

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if page_text:

            extracted_text += (
                f"\n\n[SOURCE: Uploaded PDF - Page {page_number}]\n"
                + page_text
            )

    return extracted_text


# Retrieve relevant information
def retrieve_context(question, knowledge, max_chars=6000):

    if not knowledge.strip():
        return ""

    question_words = set(question.lower().split())

    sections = knowledge.split("[SOURCE:")

    scored_sections = []

    for section in sections:

        if not section.strip():
            continue

        section_words = set(section.lower().split())

        score = len(question_words.intersection(section_words))

        if score > 0:

            scored_sections.append((score, section))

    # Sort sections by relevance
    scored_sections.sort(
        key=lambda item: item[0],
        reverse=True
    )

    selected_context = ""

    for score, section in scored_sections:

        if len(selected_context) + len(section) > max_chars:
            continue

        selected_context += "\n[SOURCE:" + section

    return selected_context
