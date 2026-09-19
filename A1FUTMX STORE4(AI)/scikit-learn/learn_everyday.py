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
-12 residuals retains direction while absolute error removes direction
-13 signed mean errors hide errors while absolute errors reveals errors e.g sign mean(-5,5)/2=0, absolute mean(5,5)/2=5.
-14 Don't say:MSE is better than MAE.That's not the right way to think about it.

    Instead:MAE and MSE emphasize different things.
    MAE:MAE is easier to interpret because it remains in the same units as the target, and it is less sensitive to large errors than MSE.

    - If large errors should receive substantially more weight, MSE reflects that.in addition,MSE It makes the difference much more significant
    - If you want an error measure that is easier to interpret and less dominated by large errors, MAE can be useful.

    '''
    🔥 Your biggest takeaway

        You should now be able to look at this:

        MAE
        ↓uses
        absolute errors
        ↓to get
        average distance from truth
        ↓in MAE
        large errors matter proportionally


        MSE
        ↓uses
        squared errors
        ↓to get
        average squared distance from truth
        ↓in MSE
        large errors matter disproportionately more

    '''


    #in conclusion: Choosing MAE vs MSE isn't about which formula is "better." It's about what kind of errors you want your evaluation or learning process to emphasize.
    And this is why we don't blindly say: “MSE is better than MAE.”They measure error differently and are useful for different purposes.
    
    MAE: treats errors proportionally,easier to interpret
    MSE:squares errors, heavily penalizes large errors, can be strongly influenced by outliers

    #FINAL WORD TO REMEMBER: 
    MAE penalizes errors proportionally, while MSE penalizes larger errors disproportionately because they are squared.