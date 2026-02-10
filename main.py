import pandas as pd
# import sys
# sys.path.append('../my_modules')
from my_modules.module_1 import BCS

def main():
    df = pd.read_csv('input/vEdge-02-10-2026.csv')
    print('Choose one of them!:')
    print("""
1 = Total Router LA
2 = Total Router TLK
3 = Total Router PINS
4 = Done Upgrade
""")
    user_input = int(input('Choose 1 to 4: '))
    print(user_input)
    # BCS(df, user_input)
    if user_input == 1:
        BCS.getLintasartaRouter(df)
    elif user_input == 2:
        BCS.getTelkomRouter(df)
    elif user_input == 3:
        BCS.getPINSRouter(df)
    elif user_input == 4:
        BCS.getUpgradedRouter(df)
main()