# Therapy Progress Tracker

This application helps track therapy progress by integrating **GAD-7** and **PHQ-9** scores with sentiment analysis of session notes. Using a pre-trained DistilBERT model and a simple Streamlit user interface, users can analyze emotional trends and visualize therapy outcomes.

---

## **Features**
1. Input GAD-7 and PHQ-9 scores for two therapy sessions.
2. Analyze session notes for sentiment trends using a pre-trained sentiment analysis model.
3. Combine clinical scores and sentiment analysis into a comprehensive progress report.
4. Visualize trends in GAD-7 and PHQ-9 scores alongside sentiment insights.

---

## **Prerequisites**
Ensure you have the following installed:

1. Python (>= 3.8)
2. Pip (Python package manager)

---

## **Installation Instructions**

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## **Running the Application**

1. **Start the Streamlit Application:**
   ```bash
   streamlit run POC_app.py
   ```

2. **Access the Application:**
   - Open the link provided in the terminal (usually `http://localhost:8501`) in your web browser.

---

## **Usage Instructions**

1. **Input Session Data:**
   - Use the sliders to input GAD-7 and PHQ-9 scores for two therapy sessions.
   - Enter session notes in the provided text areas.

2. **Analyze Progress:**
   - Click the **"Analyze Progress"** button to generate the progress report.

3. **View Results:**
   - Review the GAD-7 and PHQ-9 trends.
   - Check sentiment analysis results, including sentiment labels and confidence scores.

---

## **Directory Structure**
```
.
├── app.py                # Main Streamlit application file
├── requirements.txt      # List of dependencies
├── README.md             # Documentation file (this file)
└── ...                   # Additional scripts or data files
```

---

## **Requirements File**
Add the following to your `requirements.txt`:
```plaintext
transformers
streamlit
```

## **Detailed Workflow**

### 1. **Input Collection**
   - Users input GAD-7 and PHQ-9 scores for two therapy sessions.
   - Provide session notes via text areas.

### 2. **Sentiment Analysis**
   - The application uses the DistilBERT model fine-tuned on SST-2 for sentiment classification.
   - Outputs include a sentiment label (e.g., "POSITIVE" or "NEGATIVE") and a confidence score.

### 3. **Data Integration**
   - Combines GAD-7 and PHQ-9 scores with sentiment analysis results to generate a comprehensive progress report.

### 4. **Visualization**
   - Displays GAD-7 and PHQ-9 score trends alongside sentiment insights.

---

## **Example Run**

### Input:
- **GAD-7 Scores:** Session 1: 10, Session 2: 8
- **PHQ-9 Scores:** Session 1: 12, Session 2: 10
- **Session Notes:**
  - Session 1: "I feel overwhelmed but slightly hopeful."
  - Session 2: "Things are improving, but I still feel anxious."

### Output:
- **Session 1:**
  - GAD-7 Score: 10
  - PHQ-9 Score: 12
  - Sentiment: POSITIVE (Confidence: 0.85)
- **Session 2:**
  - GAD-7 Score: 8
  - PHQ-9 Score: 10
  - Sentiment: POSITIVE (Confidence: 0.92)

---

## **Contributing**
Feel free to contribute to this project by submitting issues or pull requests on GitHub.

---

