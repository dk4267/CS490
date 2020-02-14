import pandas as pd

train_df = pd.read_csv("train_preprocessed.csv")
test_df = pd.read_csv('test_preprocessed.csv')

print(train_df['Survived'].value_counts(dropna='False'))

print(train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))

#The correlation between sex and survival is 0.74, which is a strong correlation.
#We should definitely keep this

