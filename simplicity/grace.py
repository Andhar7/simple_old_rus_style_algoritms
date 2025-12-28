
def algorithm_of_universe(life ,Sri):

    if Sri in life:
        print(f"Grace of Supreme is simple rule: {Sri}")
        return life.index(Sri), Sri
    else:
        print(f"Life is like You created")

        raise ValueError(f"Attention! This is optional point! Never play with it... DANGEROUS!")


if __name__ == "__main__":

    G = ["Gratitude"]

    R = ["Reliability"]

    A = ["Adroitness"]

    C = ["Concern"]

    E = ["Entusiasm"]

    Sri = [G, R, A, C, E]

    life = [0, 1, Sri]

    algorithm_of_universe(life, Sri)