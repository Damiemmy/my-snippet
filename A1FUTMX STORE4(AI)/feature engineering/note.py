1.)
🧠 One important observation

You created:
df["attendance_rate"] = df["attendance"] / 100
That's technically a rescaling/transformation.

Whereas:
df["study_efficiency"] = df["attendance"] / df["study_hours"]

is more interesting because you're creating a new relationship between two existing variables.

That's feature engineering.
And:
df["high_attendance"] = df["attendance"] >= 90

creates a Boolean feature.
So you've already touched three different forms of transformation.


2.)
Creating a column in a DataFrame doesn't automatically mean you've decided to give that column to the model.

Feature engineering and feature selection are separate decisions.

3.)⚔️ RULE-BASED AI VS MACHINE LEARNING

You told me from the beginning that you want to master both.

So let's establish the foundation.

Rule-based system:

Developer
   ↓
writes rules
   ↓
system follows rules

Example:

if score >= 70:
    return "Excellent"
else:
    return "Needs Improvement"

Machine Learning:

Developer
   ↓
provides data
   ↓
algorithm learns patterns
   ↓
model
   ↓
prediction

The developer doesn't explicitly write:

"if study_hours > 5 and attendance > 90, score = 82"

Instead, the algorithm estimates relationships from data.