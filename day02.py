import pandas as pd

scoremap = {'rock': 1, 'paper': 2, 'scissors': 3}
opponent = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
player = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
resmap = {'W': 6, 'L': 0, 'D': 3}
resmap2 = {'Z': 6, 'X': 0, 'Y': 3}

results = pd.DataFrame(
    {'A': ['D', 'W', 'L'],
     'B': ['L', 'D', 'W'],
     'C': ['W', 'L', 'D']},
     index=['X', 'Y', 'Z']
)

def score(input):
    a, b = input
    res = results.loc[b, a]
    myscore = scoremap[player[b]] + resmap[res]

    return myscore

print("Check results")
print(score(('A', 'Y')))
print(score(('B', 'X')))
print(score(('C', 'Z')))
df = pd.read_csv('input02.txt', delimiter=' ', header=None, names=['A', 'B'])

total = df.apply(score, axis=1).sum()
print(f"Total score is: {total}")

outcome = pd.DataFrame(
    {'A': ['scissors', 'rock', 'paper'],
     'B': ['rock', 'paper', 'scissors'],
     'C': ['paper', 'scissors', 'rock']},
     index=['X', 'Y', 'Z']
)


def newscore(input):
    a, res = input
    scoreshape = outcome.loc[res, a]
    myscore = scoremap[scoreshape] + resmap2[res]
    return myscore


print("Check new results")
print(newscore(('A', 'Y')))
print(newscore(('B', 'X')))
print(newscore(('C', 'Z')))
newtotal = df.apply(newscore, axis=1).sum()
print(f"Revised score is: {newtotal}")