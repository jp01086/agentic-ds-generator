import streamlit as st
from agents.analyzer import analyze_problem
from agents.selector import select_data_structure
from agents.generator_cpp import generate_cpp
from knowledge.complexity_db import complexity_db
from visualizer import visualize_priority_queue
from agents.explainer import explain_rejection


st.set_page_config(
    page_title="Agentic AI Data Structure Generator",
    page_icon="🧠",
    layout="wide"
)

st.title("Agentic AI Data Structure Generator")

st.write("Describe a programming problem. The system will analyze it and recommend a data structure.")

problem = st.text_area("Problem Description")

if st.button("Generate Solution"):

    if problem.strip() == "":
        st.warning("Please enter a problem description.")
    else:

        # ---------------- STEP 1 ----------------
        st.subheader("Step 1: Problem Analysis")
        analysis = analyze_problem(problem)
        st.write(analysis)

        # ---------------- STEP 2 ----------------
        st.subheader("Step 2: Data Structure Selection")
        ds = select_data_structure(analysis)
        st.success(f"Recommended Data Structure: {ds.upper()}")

        # ---------------- STEP 2.5 ----------------
        st.subheader("Why Not Other Data Structures")

        reasons = explain_rejection(problem, ds)

        st.write(reasons)

        ds_key = ds.lower()

        if ds_key in complexity_db:
            info = complexity_db[ds_key]

            st.subheader("Complexity Analysis")

            st.write("**Time Complexity:**", info["time"])
            st.write("**Space Complexity:**", info["space"])
            st.write("**Why this data structure:**", info["reason"])



        # ---------------- STEP 3 ----------------
        st.subheader("Step 3: C++ Implementation")
        code = generate_cpp(ds)
        st.code(code, language="cpp")
        st.download_button(
            label="Download C++ Code",
            data=code,
            file_name="generated_solution.cpp",
            mime="text/plain"
        )

        # ---------------- STEP 4 ----------------
        st.subheader("Step 4: Visualization")

        if ds_key == "priority queue":

            input_elements = st.text_input(
                "Enter elements to visualize (comma separated)",
                "10,30,20"
            )

            if input_elements:
                elements = list(map(int, input_elements.split(",")))

                fig = visualize_priority_queue(elements)
                st.pyplot(fig)

        else:
            st.info("Visualization currently supported for Priority Queue.")