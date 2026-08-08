import streamlit as st
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at top right,
                rgba(56, 189, 248, 0.12),
                transparent 35%
            ),
            radial-gradient(
                circle at top left,
                rgba(99, 102, 241, 0.10),
                transparent 30%
            ),
            #080d18;
    }

    /* Hide default Streamlit menu */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Hero section */
    .hero {
        padding: 35px 40px;
        border-radius: 24px;
        margin-bottom: 30px;

        background:
            linear-gradient(
                135deg,
                rgba(15, 23, 42, 0.95),
                rgba(30, 41, 59, 0.90)
            );

        border: 1px solid rgba(148, 163, 184, 0.20);

        box-shadow:
            0 20px 50px rgba(0, 0, 0, 0.30);
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 30px;

        background: rgba(56, 189, 248, 0.12);
        border: 1px solid rgba(56, 189, 248, 0.25);

        color: #7dd3fc;
        font-size: 13px;
        font-weight: 600;

        margin-bottom: 15px;
    }

    .hero h1 {
        font-size: 44px;
        font-weight: 750;
        margin: 0;

        color: #f8fafc;
    }

    .hero h1 span {
        color: #38bdf8;
    }

    .hero p {
        margin-top: 14px;

        color: #94a3b8;
        font-size: 17px;
        line-height: 1.7;
    }

    /* Section cards */
    .section-card {
        padding: 25px;
        border-radius: 20px;

        background: rgba(15, 23, 42, 0.72);

        border: 1px solid rgba(148, 163, 184, 0.15);

        margin-bottom: 20px;
    }

    /* Result */
    .result-card {
        padding: 35px;
        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(14, 116, 144, 0.16),
                rgba(30, 41, 59, 0.85)
            );

        border: 1px solid rgba(56, 189, 248, 0.30);

        text-align: center;

        margin-top: 25px;
        margin-bottom: 25px;
    }

    .result-title {
        color: #94a3b8;
        font-size: 16px;
        margin-bottom: 8px;
    }

    .result-score {
        color: #38bdf8;
        font-size: 60px;
        font-weight: 800;
        line-height: 1;
    }

    .result-label {
        color: #e2e8f0;
        font-size: 18px;
        margin-top: 12px;
    }

    /* Info cards */
    .info-card {
        padding: 20px;
        border-radius: 18px;

        background: rgba(15, 23, 42, 0.70);

        border: 1px solid rgba(148, 163, 184, 0.15);
    }

    .info-card h4 {
        margin: 0 0 8px 0;
        color: #f8fafc;
    }

    .info-card p {
        margin: 0;
        color: #94a3b8;
        line-height: 1.6;
    }

    /* Button */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;

        background: linear-gradient(
            135deg,
            #38bdf8,
            #6366f1
        );

        color: white;
        border: none;

        padding: 14px;

        font-size: 17px;
        font-weight: 700;
    }

    div.stButton > button:hover {
        border: none;
        color: white;

        background: linear-gradient(
            135deg,
            #0ea5e9,
            #4f46e5
        );
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        # 🎓 Student Predictor
        """
    )

    st.markdown("---")

    st.markdown("### About")

    st.write(
        """
        This application predicts a student's
        **Mathematics Score** using academic,
        demographic and preparation-related
        information.
        """
    )

    st.markdown("---")

    st.markdown("### 🤖 Model")

    st.write("Machine Learning Regression")

    st.markdown("---")

    st.markdown("### 📊 Prediction")

    st.write("Target: Mathematics Score")

    st.markdown("---")

    st.markdown("### 🔄 Pipeline")

    st.write("Student Data")
    st.write("↓")
    st.write("Preprocessing")
    st.write("↓")
    st.write("Feature Scaling")
    st.write("↓")
    st.write("ML Model")
    st.write("↓")
    st.write("Math Score")


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            🎓 MACHINE LEARNING • STUDENT ANALYTICS
        </div>

        <h1>
            Predict Student
            <span>Performance</span>
        </h1>

        <p>
            Estimate a student's Mathematics Score using
            demographic information, academic performance,
            parental education, lunch type and test preparation.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# QUICK INFO
# ============================================================

info1, info2, info3 = st.columns(3)

with info1:

    st.markdown(
        """
        <div class="info-card">

        <h4>🎯 Target</h4>

        <p>
        Mathematics Score
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with info2:

    st.markdown(
        """
        <div class="info-card">

        <h4>📚 Inputs</h4>

        <p>
        Academic + demographic factors
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with info3:

    st.markdown(
        """
        <div class="info-card">

        <h4>⚙️ Pipeline</h4>

        <p>
        Encoding + scaling + regression
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("")


# ============================================================
# CUSTOMER / STUDENT INPUT
# ============================================================

st.markdown("## 📝 Student Information")

st.write(
    "Enter the student's information below."
)


col1, col2 = st.columns(2)


# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    gender = st.selectbox(
        "Gender",
        [
            "male",
            "female"
        ],
        format_func=lambda x: x.title()
    )

    race_ethnicity = st.selectbox(
        "Race / Ethnicity",
        [
            "group A",
            "group B",
            "group C",
            "group D",
            "group E"
        ],
        format_func=lambda x: x.title()
    )

    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        [
            "bachelor's degree",
            "some college",
            "master's degree",
            "associate's degree",
            "high school",
            "some high school"
        ],
        format_func=lambda x: x.title()
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    lunch = st.selectbox(
        "Lunch",
        [
            "standard",
            "free/reduced"
        ],
        format_func=lambda x:
            "Free / Reduced" if x == "free/reduced"
            else "Standard"
    )

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        [
            "completed",
            "none"
        ],
        format_func=lambda x: x.title()
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0,
        max_value=100,
        value=70,
        step=1
    )


# ============================================================
# PREDICT BUTTON
# ============================================================

st.markdown("---")

predict = st.button(
    "🔮 Predict Mathematics Score",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict:

    try:

        # ----------------------------------------------------
        # Create CustomData object
        # ----------------------------------------------------

        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=
                parental_level_of_education,
            lunch=lunch,
            test_preparation_course=
                test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        # ----------------------------------------------------
        # Convert input to DataFrame
        # ----------------------------------------------------

        pred_df = data.get_data_as_dataframe()

        # ----------------------------------------------------
        # Run existing prediction pipeline
        # ----------------------------------------------------

        predict_pipeline = PredictPipeline()

        with st.spinner(
            "Analyzing student information..."
        ):

            results = predict_pipeline.predict(
                pred_df
            )

        prediction = float(results[0])

        # Keep score inside a sensible display range
        prediction = max(
            0,
            min(100, prediction)
        )

        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        st.markdown(
            f"""
            <div class="result-card">

                <div class="result-title">
                    Predicted Mathematics Score
                </div>

                <div class="result-score">
                    {prediction:.2f}
                </div>

                <div class="result-label">
                    out of 100
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # SCORE METRIC
        # ----------------------------------------------------

        score_col1, score_col2 = st.columns(2)

        with score_col1:

            st.metric(
                "Predicted Score",
                f"{prediction:.2f}"
            )

        with score_col2:

            if prediction >= 90:

                performance = "Excellent"

            elif prediction >= 75:

                performance = "Very Good"

            elif prediction >= 60:

                performance = "Good"

            elif prediction >= 40:

                performance = "Needs Improvement"

            else:

                performance = "At Risk"

            st.metric(
                "Performance Level",
                performance
            )

        # ----------------------------------------------------
        # SCORE BAR
        # ----------------------------------------------------

        st.markdown("### 📊 Score Visualization")

        st.progress(
            int(prediction)
        )

        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        if prediction >= 90:

            st.success(
                "🌟 Excellent predicted performance."
            )

        elif prediction >= 75:

            st.success(
                "👏 Very good predicted performance."
            )

        elif prediction >= 60:

            st.info(
                "👍 Good predicted performance."
            )

        elif prediction >= 40:

            st.warning(
                "📚 The predicted score suggests "
                "there may be room for improvement."
            )

        else:

            st.error(
                "⚠️ The predicted score is relatively low. "
                "Additional academic support may be useful."
            )

        # ----------------------------------------------------
        # INPUT SUMMARY
        # ----------------------------------------------------

        with st.expander(
            "🔎 View Prediction Inputs"
        ):

            input_display = pd.DataFrame(
                {
                    "Feature": [
                        "Gender",
                        "Race / Ethnicity",
                        "Parental Education",
                        "Lunch",
                        "Test Preparation",
                        "Reading Score",
                        "Writing Score"
                    ],
                    "Value": [
                        gender.title(),
                        race_ethnicity.title(),
                        parental_level_of_education.title(),
                        (
                            "Free / Reduced"
                            if lunch == "free/reduced"
                            else "Standard"
                        ),
                        test_preparation_course.title(),
                        reading_score,
                        writing_score
                    ]
                }
            )

            st.dataframe(
                input_display,
                use_container_width=True,
                hide_index=True
            )

    except Exception as e:

        st.error(
            "❌ Prediction failed."
        )

        st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🎓 Student Performance Predictor • "
    "Built with Python, Scikit-learn and Streamlit"
)
