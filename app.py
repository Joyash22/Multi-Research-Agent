import streamlit as st

st.set_page_config(page_title="Research Agent", page_icon="🔎", layout="centered")

st.title("🔎 Multi-Agent Research System")
st.caption("Search → Read → Write → Critique")

topic = st.text_input("Research topic", placeholder="e.g. Impact of AI agents on software engineering")
run = st.button("Run Research")

if run:
    if not topic.strip():
        st.warning("Please enter a research topic.")
    else:
        with st.status("Agents are working...", expanded=True) as status:
            st.write("🔍 Search agent → Reader agent → Writer → Critic")
            try:
                # Imported here so the UI always renders even if agents/pipeline fail to load
                from pipeline import run_research_pipeline

                st.session_state["result"] = run_research_pipeline(topic.strip())
                st.session_state["topic"] = topic.strip()
                status.update(label="Research complete", state="complete", expanded=False)
            except Exception as e:
                st.session_state.pop("result", None)
                status.update(label="Pipeline failed", state="error")
                st.exception(e)

result = st.session_state.get("result")

if result:
    st.divider()
    st.subheader(f"Results: {st.session_state.get('topic', '')}")

    tab_report, tab_feedback, tab_search, tab_scrape = st.tabs(
        ["📄 Report", "🧐 Critic Feedback", "🔍 Search Results", "🌐 Scraped Content"]
    )

    with tab_report:
        st.markdown(result.get("report", ""))
        st.download_button(
            "Download report (.md)",
            data=str(result.get("report", "")),
            file_name="research_report.md",
            mime="text/markdown",
        )
    with tab_feedback:
        st.markdown(result.get("feedback", ""))
    with tab_search:
        st.markdown(result.get("search_results", ""))
    with tab_scrape:
        st.markdown(result.get("scraped_content", ""))