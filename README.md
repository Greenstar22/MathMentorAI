# MathMentorAI: A Reproducible Pipeline for Stepwise Feedback on Handwritten Math Work
MathMentor AI is a prototype web application that
provides teacher-like, stepwise feedback on students’ handwritten
mathematics work. The system accepts a photographed solution,
extracts text with OCR, queries WolframAlpha for a canonical
solution, and runs a fine-tuned analysis model to produce structured
JSON feedback: step comparisons, a core-misconception
label, and topic-level scoring. This page documents the system
design, the dataset curation and fine-tuning pipeline, implementation
choices, limitations, and a fully specified reproducible
classroom evaluation protocol.


🚀 **Features**

  - Handwriting OCR: Extracts text and symbolic expressions from photographed math solutions. ​
  - Canonical Solution Lookup: Queries WolframAlpha for step-by-step solutions. ​
  - Fine-Tuned Analysis Model: Compares student solutions with canonical solutions to identify misconceptions and provide structured feedback. ​
  - JSON Feedback: Generates step-level feedback, misconception labels, and topic-level scoring. ​
  - Progress Tracking: Stores user scores and topic-level analytics in Firebase Firestore. ​
  - Reproducibility: Fully documented pipeline for dataset curation, fine-tuning, and classroom evaluation. ​


🛠️ **Technology Stack** ​

  - Frontend: TypeScript, Next.js (React) ​
  - Styling: Tailwind CSS, ShadCN/UI ​
  - Backend Orchestration: Genkit flows (AI/API choreography) ​
  - Authentication & Database: Firebase Authentication, Firestore ​
  - Hosting: Firebase App Hosting ​
  - Ground-Truth Solver: WolframAlpha API ​
  - Model Training: OpenAI GPT-4o-mini base model, fine-tuned on a supervised JSONL dataset ​


📂 **Repository Structure** ​
TODO


📖 **How It Works**

  - Upload: Students upload a photo of their handwritten math work. ​
  - OCR: The system extracts text and symbolic expressions using OCR. ​
  - Solution Lookup: WolframAlpha provides a canonical solution and step breakdown. ​
  - Analysis: A fine-tuned model compares the student’s solution with the canonical solution, identifying errors and misconceptions. ​
  - Feedback: The system generates structured JSON feedback, which is displayed to the student and stored in Firestore for progress tracking. ​


📊 **Evaluation Protocol** ​
A reproducible classroom evaluation protocol is provided to measure the system’s effectiveness. ​ Key metrics include:

  - OCR Accuracy: Character-level and token-level match percentages. ​
  - Grader-Teacher Agreement: Percent agreement and Cohen’s kappa for final answers and step-level errors. ​
  - Pedagogical Usefulness: Likert scale surveys for students and teachers. ​
  - Time-to-Feedback: Median and IQR. ​


📈 **Fine-Tuning Metadata** ​

  - Fine-tune job ID: ftjob-Wp1c5YNXWLQ16ntnKQ1yKwIx ​
  - Output model: ft:gpt-4o-mini-2024-07-18:personal:analysis:CVWRy0wx ​
  - Trained tokens: 111,678 ​
  - Epochs: 3 ​
  - Batch size: 1 ​
  - Learning rate multiplier: 1.8 ​
  - Train loss: 0.097 ​
  - Valid loss: 0.028 ​
  - Runtime: 43 minutes ​


📋 **Limitations**

  - OCR Sensitivity: Messy handwriting or low-quality images may lead to extraction errors. ​
  - Solver Dependency: WolframAlpha may not provide step breakdowns for all problems. ​
  - Model Judgment: Unconventional solution strategies may be misclassified as misconceptions. ​
  - No User Testing Yet: Empirical validation is pending classroom trials. ​


🔮 **Future Work**​

  - Editable OCR review step for students. ​
  - Improved fallbacks for problems without WolframAlpha step breakdowns. ​
  - Interactive feedback linking steps to concept definitions. ​
  - Expansion of teacher-annotated datasets. ​
  - Development of topic-specialized analysis models. ​
  - Randomized classroom trials to measure learning gains. ​
  - Integration with school LMS platforms. ​


📜 **License**
This project is licensed under the MIT License. See the LICENSE file for details.



# Citations
All the files I used to create my math app, MathMentor
AI. This includes the data files, the python scripts, and the original data.
Feel free to use anything useful you find here, but make sure to correctly cite the following dataset, which I used, as well as mine:
A Benchmark for Math Misconceptions: Bridging Gaps in Middle School Algebra with AI-Supported Instruction by Nancy Otero, Stefania Druga, and Andrew Lan.
