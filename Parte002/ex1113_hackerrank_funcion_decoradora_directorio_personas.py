# Ejercicio 1113: HackerRank Función decoradora para formatear datos de personas.

# Let's use decorators to build a name directory! You are given some information about  people. Each person 
# has a first name, last name, age and sex. Print their names in a specific format sorted by their age in 
# ascending order i.e. the youngest person's name should be printed first. For two people of the same age, 
# print them in the order of their input.

# ...

def person_lister(f):
    def inner(people):
        people = sorted(people, key=lambda p: int(p[2]))
        
        result = []
        for p in people:
            result.append(f(p))
        
        return result
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
