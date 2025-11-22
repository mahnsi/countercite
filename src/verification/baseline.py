from intertoold import combinations


def measure_difference(query, context):
    #returns a score
    pass


def ablation(context, query):
    modified_context = context.copy()
    for c in context:
        modified_context.remove(c)
        difference = measure_difference(query, modified_context)
        modified_context.append(c)
        # ...


def brute_force(context, query):
    n = len(context)
    indicies = list(range(n)) # list of 0...n-1
    minimal_sets = []

    for i in range(1, n+1): # for each subset size i
        for combo in combinations(indicies, i):
            subset = [context[j] for j in combo]

            difference = measure_difference(query, subset)

            # ...

    return minimal_sets

