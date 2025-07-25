import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pypdf import PdfReader

# ─────────────────────────────────────────────────────────────────────
# App Configuration & Initialization
# ─────────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Resume Coach", layout="wide")
st.title("🧾 Portfolio Builder + Job Coach")

with st.sidebar:
    st.header("📌 Navigation")
    menu = st.selectbox("Choose a feature", [
        "Resume Generator", "Cover Letter Generator",
        "CV Analyzer", "LinkedIn Summary Generator",
        "Mock Interview Chatbot"
    ])

st.sidebar.markdown("---")
st.sidebar.success("🔁 Powered by LLaMA3 via Ollama")

# Load LLM
@st.cache_resource
def load_model():
    return Ollama(model="llama3.2")

llm = load_model()


# ─────────────────────────────────────────────────────────────────────
# Utility: Generic Chain Runner
# ─────────────────────────────────────────────────────────────────────
def run_chain(prompt_template, input_values):
    prompt = PromptTemplate(input_variables=list(input_values.keys()), template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(**input_values)


# ─────────────────────────────────────────────────────────────────────
# 1. Resume Generator
# ─────────────────────────────────────────────────────────────────────
if menu == "Resume Generator":
    st.subheader("📄 Resume Generator")
    with st.form("resume_form"):
        job_title = st.text_input("Job Title")
        experience = st.text_area("Work Experience Summary")
        skills = st.text_area("List of Skills (comma separated)")
        submitted = st.form_submit_button("Generate Resume")

    if submitted:
        with st.spinner("Generating your resume..."):
            resume_prompt = """
            Generate a professional resume for a {job_title} role.
            Experience: {experience}
            Skills: {skills}
            Format it in a clean, ATS-friendly markdown layout with sections and bullet points.
            """
            output = run_chain(resume_prompt, {
                "job_title": job_title,
                "experience": experience,
                "skills": skills
            })
            st.success("✅ Resume Generated!")
            st.code(output, language="markdown")


# ─────────────────────────────────────────────────────────────────────
# 2. Cover Letter Generator
# ─────────────────────────────────────────────────────────────────────
elif menu == "Cover Letter Generator":
    st.subheader("✉️ Cover Letter Generator")
    with st.form("cover_form"):
        job_title = st.text_input("Job Title")
        company = st.text_input("Company Name")
        motivation = st.text_area("Why are you interested in this role?")
        achievements = st.text_area("Key Achievements or Experience")
        submitted = st.form_submit_button("Generate Cover Letter")

    if submitted:
        with st.spinner("Crafting your cover letter..."):
            cover_prompt = """
            Write a formal cover letter for a {job_title} position at {company}.
            Reason for interest: {motivation}
            Key achievements: {achievements}
            Use a confident and professional tone.
            """
            output = run_chain(cover_prompt, {
                "job_title": job_title,
                "company": company,
                "motivation": motivation,
                "achievements": achievements
            })
            st.success("✅ Cover Letter Ready!")
            st.code(output, language="markdown")


# ─────────────────────────────────────────────────────────────────────
# 3. CV Analyzer
# ─────────────────────────────────────────────────────────────────────
elif menu == "CV Analyzer":
    st.subheader("🔎 CV Analyzer")
    uploaded = st.file_uploader("Upload your Resume (PDF)", type=['pdf'])

    if uploaded:
        text = ""
        reader = PdfReader(uploaded)
        for page in reader.pages:
            text += page.extract_text()

        st.text_area("Extracted Text", value=text, height=300)

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing your resume..."):
                analyze_prompt = """
                Analyze the following resume text and provide improvement suggestions.
                Mention missing sections, formatting issues, or unclear language.

                Resume:
                {cv_text}
                """
                feedback = run_chain(analyze_prompt, {"cv_text": text})
                st.markdown("### 🛠️ Suggestions for Improvement:")
                st.write(feedback)


# ─────────────────────────────────────────────────────────────────────
# 4. LinkedIn Summary Generator
# ─────────────────────────────────────────────────────────────────────
elif menu == "LinkedIn Summary Generator":
    st.subheader("🔗 LinkedIn Summary Generator")
    with st.form("linkedin_form"):
        name = st.text_input("Your Name")
        profession = st.text_input("Your Profession")
        goals = st.text_area("Career Goals or Aspirations")
        key_skills = st.text_area("Key Skills")
        submitted = st.form_submit_button("Generate LinkedIn Summary")

    if submitted:
        with st.spinner("Creating your summary..."):
            linkedin_prompt = """
            Write a compelling LinkedIn summary for {name}, a {profession}.
            Highlight their career goals: {goals}
            Mention skills like: {key_skills}
            Use a friendly yet professional tone.
            """
            summary = run_chain(linkedin_prompt, {
                "name": name,
                "profession": profession,
                "goals": goals,
                "key_skills": key_skills
            })
            st.success("✅ Summary Generated!")
            st.code(summary)


# ─────────────────────────────────────────────────────────────────────
# 5. Mock Interview Chatbot
# ─────────────────────────────────────────────────────────────────────
elif menu == "Mock Interview Chatbot":
    st.subheader("🧠 Mock Interview Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Your Response:", key="chat_input")

    if st.button("Send") and user_input:
        conversation = "\n".join([f"Candidate: {q}\nCoach: {a}" for q, a in st.session_state.chat_history])
        interview_prompt = """
        You are an HR interview coach. Continue the interview session.
        Provide one new question or constructive feedback.

        Previous dialogue:
        {conversation}

        Candidate's response:
        {user_input}
        """
        reply = run_chain(interview_prompt, {
            "conversation": conversation,
            "user_input": user_input
        })

        st.session_state.chat_history.append((user_input, reply))

    # Display chat history
    for i, (question, reply) in enumerate(st.session_state.chat_history):
        st.markdown(f"**👤 You:** {question}")
        st.markdown(f"**🎓 Coach:** {reply}")
