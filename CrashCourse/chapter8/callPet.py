def describe_Pet(animalType, animalName):
    """Display information about a pet."""
    print("\nI have a " + animalType +".")
    print("My " + animalType + "'s name is " + animalName.title() + ".")
    
#Keyword Argument
#describe_Pet(animalType='Cat', animalName='pupsik')