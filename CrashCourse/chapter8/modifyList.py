#Start with some designs that need to be printed

    
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
        print("---- Original Unprinted Models ---")
        
        for model in unprinted_designs:
            print("Org1:" + model)

def show_completed_models(completed_models):
    """Show all models that were printed."""
    #Display all completed models
    print("\nThe following models have been completed: ")
    for model in completed_models:
        print(model)


unprinted_designs = ['iphone case','macbook case','apple watch case']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
