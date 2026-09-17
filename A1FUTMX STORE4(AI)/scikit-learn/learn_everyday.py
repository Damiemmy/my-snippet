1- A model is not magic. A model is a mathematical representation of patterns learned from data.
2- A feature must be legitimately available at prediction time.
3- "Increasing attendance by one unit increases the model's predicted score by 0.5, holding study hours constant."
4- Think of a coefficient as the amount by which a feature contributes to the prediction per unit of that feature, holding the other features constant.
5- X = input variables/features, They provide the information from which the model learns to predict y. y variables can't be found in X because it leads to information leakage / target leakage During prediction.
6- in summary X = information available before prediction while y = thing we're trying to predict

7- If you put the answer itself into the input:

    X = study_hours
        attendance
        score

    you're essentially saying: "Predict the student's score while giving the model the student's score."😂

    That's not intelligence.That's cheating.

-8 interpolation intuition.: the wrong mental picture of human prediction not using machine learning

-9 let's imagine the model has effectively learned something like:

    score =
        coefficient_1 × study_hours
    + coefficient_2 × attendance
    + intercept

    This is where machine learning stops being mysterious.

    The algorithm isn't magically "understanding students."

    It's finding numerical parameters that produce a mathematical function fitting the training data according to the algorithm's objective.

- 10 A coefficient describes the change in the model's prediction associated with a one-unit change in that feature, holding the other included features constant.
- 11 the differencte between the actual score(y) and the predicted score(prediction(X)) is called the prediction error or residual, depending on the convention being used.