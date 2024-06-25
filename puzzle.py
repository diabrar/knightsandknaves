from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # has to be one of the two...
    Or(AKnight, AKnave),
    # but not both
    Not(And(AKnight, AKnave)),
    # if A is a knight they tell the truth
    Implication(AKnight, And(AKnight, AKnave)),
    # if A is a knave they lie
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is a knight or a knave, not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is also a knight or a knave, not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # if A is a knight, A and B are knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # if A is a knave, A and B are not both knaves.
    Implication(AKnave, Or(AKnight, BKnight))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is a knight or a knave, not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is also a knight or a knave, not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # if A is a knave, A is lying
    Implication(AKnave, Not(And(AKnave, BKnave))),
    # if A is a knight, A is telling the truth
    Implication(AKnight, And(AKnight, BKnight)),
    # if B is a knave, B is lying
    Implication(BKnave, And(AKnave, BKnave)),
    # if B is a knight, B is telling the truth
    Implication(BKnight, Not(AKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is a knight or a knave, not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B is also a knight or a knave, not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # C is also a knight or a knave, not both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If B is a knight, then A said i am a knave and C is a knave
    Implication(BKnight, And(
        And(
             # if A said i am a knave, A is lying
            Implication(AKnave, Not(AKnave)),
            Implication(AKnight, AKnave)),
            CKnave)),
    # If B is a knave, then A said i am a knight and C is a knight 
    Implication(BKnave, And(
        And(
            # if A said i am a knight...
            Implication(AKnight, AKnight),
            Implication(AKnave, Not(AKnight))), 
            CKnight)),
    # If C is a knight, then A is a knight and B is a knave
    Implication(CKnight, And(BKnave, AKnight)),
    # If C is a knave, then A is a knave and B is a knight
    Implication(CKnave, And(BKnight, AKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
