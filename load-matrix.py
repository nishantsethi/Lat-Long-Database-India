# Load Matrix of distances between locations and Give the Six most near ones.
import pandas as pd

df = pd.read_csv("dist.csv")

state = input("Enter the State name in CamelCase ")
dis = df[state]


def PrintSmallest(arr, n):
    MAX = 1000000   # A large number for initial comparision
    firststate = MAX
    secstate = MAX
    thirdstate = MAX
    fourthstate = MAX
    fifthstate = MAX
    sixthstate = MAX

    for i in range(0, n):

        if arr[i] < firststate:
            sixthstate = fifthstate
            fifthstate = fourthstate
            fourthstate = thirdstate
            thirdstate = secstate
            secstate = firststate
            firststate = arr[i]

        elif arr[i] < secstate:
            sixthstate = fifthstate
            fifthstate = fourthstate
            fourthstate = thirdstate
            thirdstate = secstate
            secstate = arr[i]

        elif arr[i] < thirdstate:
            sixthstate = fifthstate
            fifthstate = fourthstate
            fourthstate = thirdstate
            thirdstate = arr[i]

        elif arr[i] < fourthstate:
            sixthstate = fifthstate
            fifthstate = fourthstate
            fourthstate = arr[i]

        elif arr[i] < fifthstate:
            sixthstate = fifthstate
            fifthstate = arr[i]

        elif arr[i] < sixthstate:
            sixthstate = arr[i]

    near_states = []
    near_states.append(df.loc[df[state] == firststate]["s"].iloc[0])
    near_states.append(df.loc[df[state] == secstate]["s"].iloc[0])
    near_states.append(df.loc[df[state] == thirdstate]["s"].iloc[0])
    near_states.append(df.loc[df[state] == fourthstate]["s"].iloc[0])
    near_states.append(df.loc[df[state] == fifthstate]["s"].iloc[0])
    near_states.append(df.loc[df[state] == sixthstate]["s"].iloc[0])

    print(near_states)


arr = dis
n = len(arr)
PrintSmallest(arr, n)
