# Agentic AI Data Structure Generator

An AI-powered system that analyzes programming problems and recommends the most suitable data structure.

The system uses multiple AI agents to:

* Understand the problem description
* Select the optimal data structure
* Generate a C++ implementation
* Visualize the structure interactively

---

## Live Demo

Deployed using Streamlit:

https://agentic-ds-generator-yanubwmcxgsbbfcdstyz.streamlit.app

---

## Features

* AI-based problem analysis
* Automatic data structure recommendation
* C++ code generation
* Interactive visualization
* Modular multi-agent architecture

---

## Project Architecture

```
agents/
    analyzer.py        → Understands the programming problem
    selector.py        → Chooses the best data structure
    generator_cpp.py   → Generates C++ implementation
    explainer.py       → Explains why other structures were rejected

knowledge/
    complexity_db.py   → Time & space complexity database

templates/
    *.cpp              → C++ templates for different structures

app.py                 → Streamlit frontend
visualizer.py          → Graph visualization logic
```

---

## Example

Input:

```
Design a printer scheduling system where highest priority job runs first
```

Output:

* Recommended structure: **Priority Queue**
* Generated C++ implementation
* Visualization of the structure

---

## Tech Stack

* Python
* Streamlit
* Groq API
* NetworkX
* Matplotlib

---

## Installation

Clone the repository:

```
git clone https://github.com/jp01086/agentic-ds-generator.git
cd agentic-ds-generator
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## Future Improvements

* Support more data structures
* Add algorithm complexity comparison
* Enable interactive structure manipulation
* Support additional programming languages

---

## Author

John Preetham
B.Tech Computer Science
