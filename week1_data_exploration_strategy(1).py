"""Week 1: Data Exploration Strategy Roadmap"""
student_name = "Faiz Akhtar"
estimated_hours = "30–35 hours"

objectives = [
    "Acquire a reliable public dataset.",
    "Understand structure, quality, and distributions.",
    "Clean and prepare the data.",
    "Identify trends, patterns, outliers, and relationships.",
    "Create meaningful statistics and visualizations.",
    "Review hypotheses using evidence.",
    "Produce reproducible documentation."
]

tools = {
    "Python": "Main programming language",
    "Pandas": "Data loading and cleaning",
    "NumPy": "Numerical operations",
    "Matplotlib": "Flexible visualization",
    "Seaborn": "Statistical visualization",
    "Jupyter Notebook": "Interactive analysis",
    "Git/GitHub": "Version control and documentation"
}

timeline = [
    ("Problem Definition", 3),
    ("Dataset Research", 4),
    ("Acquisition and Inspection", 5),
    ("Cleaning and Preparation", 6),
    ("Exploratory Analysis", 7),
    ("Interpretation and Validation", 4),
    ("Documentation and Review", 5)
]

risks = {
    "Poor data quality": "Profile data early and document cleaning rules.",
    "Unclear definitions": "Read metadata and verify units.",
    "Too many variables": "Prioritize variables linked to project questions.",
    "Outliers": "Inspect distributions and use only justified treatment.",
    "Correlation vs causation": "Do not make causal claims without evidence.",
    "Reproducibility": "Document transformations and organize code.",
    "Time constraints": "Follow milestones and prioritize key questions."
}

def print_roadmap():
    print("=" * 60)
    print("WEEK 1: DATA EXPLORATION STRATEGY ROADMAP")
    print("=" * 60)
    print(f"Student: {student_name}")
    print(f"Estimated effort: {estimated_hours}")

    print("\nOBJECTIVES")
    for i, item in enumerate(objectives, 1):
        print(f"{i}. {item}")

    print("\nTOOLS")
    for name, purpose in tools.items():
        print(f"- {name}: {purpose}")

    print("\nTIMELINE")
    total = 0
    for phase, hours in timeline:
        total += hours
        print(f"- {phase}: {hours} hours")
    print(f"Total planned time: {total} hours")

    print("\nRISKS AND MITIGATION")
    for risk, solution in risks.items():
        print(f"- {risk}: {solution}")

if __name__ == "__main__":
    print_roadmap()
