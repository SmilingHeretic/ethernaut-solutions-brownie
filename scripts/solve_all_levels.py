from brownie import (
    network,
    accounts,
    config,
    interface,
    Contract,
)
from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
)
from scripts.solve_level_0 import main as solve_level_0
from scripts.solve_level_1 import main as solve_level_1
from scripts.solve_level_2 import main as solve_level_2
from scripts.solve_level_3 import main as solve_level_3
from scripts.solve_level_4 import main as solve_level_4
from scripts.solve_level_5 import main as solve_level_5
from scripts.solve_level_6 import main as solve_level_6
from scripts.solve_level_7 import main as solve_level_7
from scripts.solve_level_8 import main as solve_level_8
from scripts.solve_level_9 import main as solve_level_9
from scripts.solve_level_10 import main as solve_level_10
from scripts.solve_level_11 import main as solve_level_11
from scripts.solve_level_12 import main as solve_level_12
from scripts.solve_level_13 import main as solve_level_13
from scripts.solve_level_14 import main as solve_level_14
from scripts.solve_level_15 import main as solve_level_15
from scripts.solve_level_16 import main as solve_level_16
from scripts.solve_level_17 import main as solve_level_17
from scripts.solve_level_18 import main as solve_level_18
from scripts.solve_level_19 import main as solve_level_19
from scripts.solve_level_20 import main as solve_level_20
from scripts.solve_level_21 import main as solve_level_21
from scripts.solve_level_22 import main as solve_level_22
from scripts.solve_level_23 import main as solve_level_23
from scripts.solve_level_24 import main as solve_level_24
from scripts.solve_level_25 import main as solve_level_25

def main():
    for level_id in range(0, 26):
        print(f"SOLVING LEVEL {level_id}")
        eval(f"solve_level_{level_id}()")
        print()