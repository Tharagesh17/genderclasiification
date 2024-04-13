import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Sample data (replace with your actual data source if needed)
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38],
     [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42],
     [181, 85, 43], [168, 75, 41], [168, 77, 41]]

Y = ['male', 'male', 'female', 'female', 'male', 'male',
     'female', 'female', 'female', 'male', 'male', 'female', 'female']

# Train the decision tree classifier
model = DecisionTreeClassifier()
model.fit(X, Y)

def predict_gender(height, weight, shoe_size):
    """Predicts gender based on input features."""
    prediction = model.predict([[height, weight, shoe_size]])
    return prediction[0]

st.title("Gender Prediction App")

st.subheader("Enter your physical attributes:")

height = st.number_input("Height (cm)", min_value=140, max_value=220)
weight = st.number_input("Weight (kg)", min_value=35, max_value=150)
shoe_size = st.number_input("Shoe Size", min_value=30, max_value=50)

if st.button("Predict Gender"):
    prediction = predict_gender(height, weight, shoe_size)
    st.write(f"Predicted Gender: {prediction}")

st.write("Note: This is a basic example. Real-world gender prediction can be complex and influenced by various factors beyond physical attributes.")

