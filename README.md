# 🤖 Interactive AI-Powered Web Resume

A modern, high-performance interactive resume dashboard built with Python and Streamlit. Beyond showcasing engineering and analytics experience, this application features a production-ready **AI Role Alignment Scanner** that dynamically evaluates corporate job descriptions against the candidate's profile in real-time.

## 🚀 Live Demo
👉 [digital-resume-mahesh.streamlit.app](https://digital-resume-mahesh.streamlit.app/)

## 🛠 Tech Stack & Architecture
- **Frontend / UI:** Streamlit (Custom CSS styling & responsive layout)
- **Data Visualization:** Plotly Express (Dynamic Skills Treemaps & Gantt Experience Timelines)
- **Data Infrastructure:** Pandas & Request JSON Handling
- **AI Core:** Google Gemini LLM API (Executed via native REST architecture to optimize performance)

## ✨ Core Features
- **📊 Interactive Experience & Skills Analytics:** Replaces walls of text with interactive Plotly visualization frameworks, displaying core competencies and a comprehensive professional career timeline at scale.
- **🚀 Measurable Impact Project Deep-Dives:** A dedicated project repository tab isolating enterprise use cases, exact tech stacks, and hard financial/time-saving metrics ($3M+ saved, 1,500+ hours automated).
- **🤖 Built-in AI ATS Scanner (Tab 3):** An intelligent recruiter command center. Recruiters can paste an active Job Description (JD) to get an immediate, dynamic fit analysis. Because the LLM evaluates the text probabilistically, it provides a realistic, human-like variance in scoring that closely mimics a real recruiter's review.

## ⚙️ How the AI ATS Feature Works
1. **Contextual Evaluation:** The engine packages the pasted JD and cross-references it against structured candidate variables (12+ years experience, Supply Chain MBA, Python/SQL technical data history).
2. **Dynamic Calibration:** Utilizing Gemini's out-of-the-box creative intelligence to evaluate nuanced semantic context, phrasing, and skill overlap.
3. **Regex Extraction Engine:** Safely processes tokenized plain-text payloads into clean Streamlit visual components (`st.metric`, `st.success`, `st.warning`, `st.error`) alongside dynamic tech-overlap badges.

## 🔒 Security & Deployment
- Built with **Zero-Dependency Security Principles**—leveraging raw REST architecture to securely process keys without exposing massive local client frameworks.
- Utilizes **Streamlit Cloud Secrets Management (`st.secrets`)** to isolate and protect production environment tokens, completely preventing key exposure in public repository commits.
