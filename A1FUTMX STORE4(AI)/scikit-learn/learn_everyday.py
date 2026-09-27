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

-15 random_state & test_size=0.2: random_state makes the random splitting process reproducible. while test_size ensure 80% is available for learning, while 20% is held back to evaluate the model on unseen examples.
-16 random_state: in some cases might make your data unrealistic e.g

'''
Let's use a concrete example.

Suppose:

2020
2021
2022
2023
2024
2025
2026

Your real goal:

Predict 2027 students

With a random split, you might accidentally create:

TRAIN
2020
2021
2023
2025
2026

TEST
2022
2024

Look carefully.

The model is learning from:

2026

while you're testing it on:

2022

But in the real world, you won't have this situation:

"Here's information from 2026. Now predict what happened in 2022."

You're trying to predict the future.

The realistic scenario is:

PAST                         FUTURE

2020 2021 2022 2023 2024 2025 2026
 |________________________________|
               TRAIN
                  ↓
                MODEL
                  ↓
                2027
                 TEST

That's a much more realistic simulation.
'''

17. 🔥 Here's the principle I want you to remember

    Your test set should answer:

    "How will my model perform on the kind of data it will encounter after deployment?"

    Not merely:

    "Can my model predict some randomly selected rows?"

    That's a much deeper way of thinking about ML.

18.) 🧠 Your understanding now

    I'd rate your current understanding like this:

    test_size       ✅
    random_state    ✅
    why splitting    ✅
    time-based issue 🟡 → needs this refinement

    The key correction:

    Randomly splitting time-dependent data can produce a test set that doesn't faithfully simulate the future deployment scenario. The problem isn't necessarily that performance becomes lower; the evaluation itself may become misleading.

    And you've now reached an important ML engineering principle:

    The way you evaluate a model should reflect the way the model will actually be used.

    That's the foundation for understanding data leakage, which is the "nastier problem" that comes next.

19.) Before saying Model A is better, I'd ask:

    1. Were both evaluated on the SAME dataset?
    2. Was the SAME evaluation procedure used?
    3. Was there any data leakage?
    4. Is the test set representative?
    5. Is the test set large enough?
    6. Is MAE appropriate for the problem?
    7. What does RMSE look like?
    8. Are there problematic outliers?
    9. How does each model perform across important subgroups?
    10. What is the baseline?
    11. Is the improvement statistically/practically meaningful?
    12. Are the features available at prediction time?

    That is ML engineering judgment.


#🔥 One principle I want permanently installed in your brain

    Never think:

    LOWER METRIC
        ↓
    BETTER MODEL
        ↓
    DEPLOY

    Think:

                        MODEL
                        │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
    Evaluation      Validity      Reality
            │             │             │
    MAE/RMSE       Leakage?       Production?
            │             │             │
    Test data      Bias?         Drift?
            │             │             │
            └─────────────┼─────────────┘
                        ↓
                ENGINEERING JUDGMENT

    That's the difference between knowing scikit-learn and becoming an ML engineer.

20.) Cross-validation does NOT mean:"We have more training data."

It means: We're repeatedly evaluating the model on different held-out portions of the training data.

And importantly:

    FINAL TEST SET:
    can still remain untouched until the end.

21.)

    ### Training vs Validation vs Test

    * **Training → Learn:** The model learns patterns from the training data.
    * **Validation → Decide:** I use validation results to choose and improve the model.
    * **Test → Evaluate:** I use the test set **once at the end** to measure final generalization.

    > **Never optimize for the test set.**
    > If test results influence my development decisions, the test set is no longer a clean final evaluation.

    **Remember:**
    **Train = Learn → Validate = Decide → Test = Evaluate**
22.)MSE and RMSE are sensitive to outlier in the data which is a better metrics for comparison and understand the errors in a data

23.)Baseline = a simple reference model. It tells us whether our ML model provides meaningful predictive value beyond a simple strategy.

    And one subtle point: the baseline doesn't define what is “accurate.” It tells us how much better or worse our model is relative to a simple alternative.

24.)A feature should be useful AND legitimately available at the exact moment the prediction is made.

25.)More features ≠ better model.

You could give a model 100 engineered features and actually make it worse because some are irrelevant, noisy, redundant, or leaking information.

So our pipeline becomes:

        Raw data
        ↓
        Understand the problem
        ↓
        Engineer candidate features
        ↓
        Check availability / leakage
        ↓
        Evaluate usefulness
        ↓
        Select features
        ↓
        Train model

26.)there's one more concept I want you to lock in before we move to model selection:

More features ≠ better model.

You could give a model 100 engineered features and actually make it worse because some are irrelevant, noisy, redundant, or leaking information.

So our pipeline becomes:

Raw data
   ↓
Understand the problem
   ↓
Engineer candidate features
   ↓
Check availability / leakage
   ↓
Evaluate usefulness
   ↓
Select features
   ↓
Train model

27.)

    Feature Engineering
    │
    ├── Transformation
    │   └── attendance → attendance_rate
    │
    ├── Ratios
    │   └── assignment_score / study_hours
    │
    ├── Interactions
    │   └── study_hours × attendance
    │
    ├── Aggregations
    │   └── average_assignment_score
    │
    ├── Categorical encoding
    │   └── department → numerical representation
    │
    ├── Scaling
    │   └── put numerical features on comparable scales
    │
    └── Domain features
        └── features designed from knowledge of the problem



28.) Before selecting the model,after checking this:
    1.)Data leakage — did the model get information it shouldn't have had?
    2.)Metric suitability — is MAE actually appropriate for this problem?
    3.)Test-set representativeness — does the test data resemble the data the model will encounter in reality?

But add these: investigate

                Candidate Models
                      │
              ┌───────┴────────┐
              ↓                ↓
        Performance        Engineering
              │                │
        ┌─────┼─────┐     ┌────┼─────┐
        ↓     ↓     ↓     ↓    ↓     ↓
      MAE   RMSE   CV   Complexity Cost Interpretability
        │
        ↓
   Leakage check
        ↓
 Test-set validity
        ↓
 Feature availability
        ↓
 Generalization
        ↓
 Final selection


29.) The test set should not become a playground for repeatedly choosing models.

If we keep doing:

try model A → look at test
try model B → look at test
try model C → look at test
change features → look at test
tune parameters → look at test

we gradually start adapting our development decisions to the test set.

That's exactly why we introduced validation and cross-validation.


30.) Hurray! Hurray!! Hurray!!!
        '''

        Now we connect everything

        You have now learned the pieces:

        Baseline
        ↓
        Feature Engineering
        ↓
        Candidate Models
        ↓
        Cross-Validation / Validation
        ↓
        Model Selection
        ↓
        Untouched Test Set
        ↓
        Final Evaluation

        This is the proper evaluation pipeline we were supposed to reach before starting the project.

        And now we're ready to build it.

        '''

        '''
31.)🔥 Foundation complete

We've now covered:

                ML DEVELOPMENT
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
   BASELINE     FEATURE ENG.   MODEL SELECTION
       │             │             │
       └─────────────┼─────────────┘
                     ↓
              EVALUATION
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
       Metrics    Cross-Val   Leakage
          │          │          │
          └──────────┼──────────┘
                     ↓
              FINAL TEST
                     ↓
             FINAL ASSESSMENT
        '''

#32.) To Get Categorical Columns in pandas:
categorical_columns = df.select_dtypes(include="object").columns
print(categorical_columns)

or 

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns
print(categorical_columns)

#33.) To Get the Duplicated percentage of data:

duplicate_percentage=df.duplicated().mean() * 100

#34.) During prediction you would have to drop target from X and include it in Y :
    target = "score"

    X = df.drop(columns=[target])
    y = df[target]
