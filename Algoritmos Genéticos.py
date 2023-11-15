'''
Condiciones
~~~~~~~~~~~
1. Hay 5 casas.
2. El Matematico vive en la casa roja.
3. El hacker programa en Python.
4. El Brackets es utilizado en la casa verde.
5. El analista usa Atom.
6. La casa verde esta a la derecha de la casa blanca.
7. La persona que usa Redis programa en Java
8. Cassandra es utilizado en la casa amarilla
9. Notepad++ es usado en la casa del medio.
10. El Desarrollador vive en la primer casa.
11. La persona que usa HBase vive al lado de la que programa en JavaScript.
12. La persona que usa Cassandra es vecina de la que programa en C#.
13. La persona que usa Neo4J usa Sublime Text.
14. El Ingeniero usa MongoDB.
15. EL desarrollador vive en la casa azul.

Quien usa vim?

Resumen:
Colores = Rojo, Azul, Verde, Blanco, Amarillo
Profesiones = Matematico, Hacker, Ingeniero, Analista, Desarrollador
Lenguaje = Python, C#, JAVA, C++, JavaScript
BD = Cassandra, MongoDB, Neo4j, Redis, HBase
editor = Brackets, Sublime Text, Atom, Notepad++, Vim
'''

import random
import time
import matplotlib.pyplot as plt

genes =       ['001', '010', '011', '100', '101' ]
colors =      {'001' : 'red',          '010' : 'blue',          '011' : 'green',    '100' : 'white',    '101' : 'yellow'}
profession =  {'001' : 'Mathematician','010' : 'Hacker',        '011' : 'Engineer', '100' : 'Analyst',  '101' : 'Developer'}
lenguaje =    {'001' : 'Python',       '010' : 'C#',            '011' : 'Java',     '100' : 'C++',      '101' : 'JavaScript'}
database =    {'001' : 'Cassandra',    '010' : 'MongoDB',       '011' : 'HBase',    '100' : 'Neo4j',    '101' : 'Redis'}
editor =      {'001' : 'Brackets',     '010' : 'Sublime Text',  '011' : 'Vim',      '100' : 'Atom',     '101' : 'Notepad++'}

class Phenotype:

    # Se crea un individuo
    def __init__(self):      
        # Chromosoma que contiene un arreglo de genes
        self.chromosome = []
        
        # Puntaje que determina la eficiencia del fenotipo para resolver el problema
        self.score = 0



    # Inicializar el chromosoma con genes aleatorios sin repetirlos en las distintas categprías    
    def encode(self):
        # Se genera una pila de genes para cada categoría para que no se repitan los genes de la mismas categorías en las distintas casas
        col = genes.copy()
        prof = genes.copy()
        lang = genes.copy()
        db = genes.copy()
        ed = genes.copy()

        # Se mezclan al azar los genes de cada categoría
        random.shuffle(col)
        random.shuffle(prof)
        random.shuffle(lang)
        random.shuffle(db)
        random.shuffle(ed)
        
        # Se asignan los genes al chromosoma en el orden Color-Profesión-Lenguaje-Base de Datos-Editor
        for i in range(5):
            self.chromosome.append(col[i])
            self.chromosome.append(prof[i])
            self.chromosome.append(lang[i])
            self.chromosome.append(db[i])
            self.chromosome.append(ed[i])

        self.fitness()
        pass



    # Se traduce cada gen de 3 bits en los distintos nombres de cada categoría 
    # según el diccionario y se devuelve un arreglo con los datos de cada casa por separado        
    def decode(self):
        code = [[colors[self.chromosome[i*5 + 0]], 
                 profession[self.chromosome[i*5 + 1]], 
                 lenguaje[self.chromosome[i*5 + 2]], 
                 database[self.chromosome[i*5 + 3]], 
                 editor[self.chromosome[i*5 + 4]]] for i in range(5)]

        return code



    # Método para imprimir por pantalla de manera mas detallada el chromosoma del Fenotipo
    def printNice(self):
        code = self.decode()
        
        print("Casa 1: ", code[0])
        print("Casa 2: ", code[1])
        print("Casa 3: ", code[2])
        print("Casa 4: ", code[3])
        print("Casa 5: ", code[4])
        
        pass



    # Se introduce una mutación aleatoria de un unico gen del Fenotipo
    def mutate(self):
        self.chromosome[random.randrange(0,24)] = genes[random.randrange(0, 4)]
        pass

    
    
    # Se cruza dos chromosomas de Fenotipos diferentes para generar un solo chromosoma y asignarselo a este Fenotipo
    def crossover(self, parent_1, parent_2):
        self.chromosome.clear()
        indiceCorte = random.randrange(0, 23);        
        for gen in parent_1.chromosome[0:indiceCorte] : self.chromosome.append(gen)
        for gen in parent_2.chromosome[indiceCorte:25] : self.chromosome.append(gen)            
    pass
    
    

    # Se calcula la eficacia del chromosoma para resolver el problema dado basado en las restricciones del mismo
    def fitness(self):
        self.score = 0

        # Se asginan valores de premio y castigo para el puntaje
        ok_score = 1
        fail_score = -1
        
        # Se decodifica el chromosoma para poder tratarlo de manera mas sencilla 
        # (Este paso se podría evitar pero obligaría a trabajar al programador con genes de cadenas de bits)
        solution = self.decode()
        
        # Se castiga al Fenotipo en caso de que existan genes repetidos en las distintas categorías
        # (Combinaciones inválidas)
        for i in range(4):
            for j in range(i + 1, 5):
                if solution[i][0] == solution[j][0]: self.score += fail_score
                if solution[i][1] == solution[j][1]: self.score += fail_score
                if solution[i][2] == solution[j][2]: self.score += fail_score
                if solution[i][3] == solution[j][3]: self.score += fail_score
                if solution[i][4] == solution[j][4]: self.score += fail_score
        
        # Se premia al Fenotipo en caso de que se cumplan con las restricciones que se deben cumplir dentro de una misma casa
        for house in solution:
            if (house[1] == 'Mathematician' and house[0] == 'red') : self.score += ok_score 
            if (house[1] == 'Hacker' and house[2] == 'Python') : self.score += ok_score
            if (house[4] == 'Brackets' and house[0] == 'green') : self.score += ok_score
            if (house[1] == 'Analyst' and house[4] == 'Atom') : self.score += ok_score
            if (house[3] == 'Redis' and house[2] == 'Java') : self.score += ok_score
            if (house[3] == 'Cassandra' and house[0] == 'yellow') : self.score += ok_score
            if (house[3] == 'Neo4j' and house[4] == 'Sublime Text') : self.score += ok_score
            if (house[1] == 'Engineer' and house[3] == 'MongoDB') : self.score += ok_score
            if (house[1] == 'Developer' and house[0] == 'blue') : self.score += ok_score
        
        if (solution[2][4] == 'Notepad++') : self.score += ok_score
        if (solution[0][1] == 'Developer') : self.score += ok_score 

        # Se premia al Fenotipo en caso de que se cumplan con las restricciones que se deben cumplir en relación a otras casas
        for i in range(len(solution) - 1):
            if (solution[i][0] == 'white' and solution[i + 1][0] == 'green') : self.score += ok_score 
            
        for i in range(1, len(solution) - 1):
            if (solution[i][3] == 'HBase') : 
                if(solution[i - 1][2] == 'JavaScript' or solution[i + 1][2] == 'JavaScript'): self.score += ok_score 
            if (solution[i][3] == 'Cassandra') : 
                if(solution[i - 1][2] == 'C#' or solution[i + 1][2] == 'C#'): self.score += ok_score 
                
        # En total, se deben cumplir con 14 restricciones, por lo tanto, el puntaje mas alto posible es 14
        pass



class Riddle:

    # Se inicializal las variables para resolver el problema
    def __init__(self):
        
        
        # Arreglo que contiene a cada individuo (Fenotipo) de la población generada
        self.population = []
        
        # Maxima cantidad de generaciones por cada iteración
        self.maxGenerations = 100
        
        # Chance de que exista una mutación en cada individuo de la población entre generación y generación
        self.mutation_prop = 1
        
        # Proporción de cruce entre los individuos de la población entre generación y generación
        # Si el valor es menor a 0.5, la población va a decrecer de generación a generación
        # Si el valor es mayor a 0.5, la población va a crecer de generación a generación
        # Si el valor es 0.5, la población no crece ni decrece de generación a generación => se elige por default
        self.crossover_prop = 0.5
        
        # Cuenta de iteraciones, cada iteración corresponde a un ciclo completo de generaciones de una población determinada
        # Las poblaciones de cada iteración son independientes entre sí
        self.iterationCount = 0
        
        # Arreglo que guarda los mejores puntajes de cada generación para poder graficarlos
        self.history = []



    # Se inicia el proceso de resolución del problema
    # Se determina el tamaño de la población, la cantidad de generaciónes para cada población y la cantidad de iteraciones que se deben evaluar
    # Además, se asigna la proporción de mutaciones y la proporcion de cruce entre individuos
    def solve(self, n_population, generations = 3, iterations = 10, mutationRatio = 1, crossoverRatio = 0.5):
        
        self.iterationCount = 0
        self.maxGenerations = generations
        self.mutation_prop = mutationRatio
        self.crossover_prop = crossoverRatio
        
        # Variables para mostrar los datos (No aportan a la resolución, se utilizan solo de manera informativa)
        fitSum = 0
        bestFit = 0
        bestIndi = Phenotype()
        bestHistory = []
        
        break_condition = False
        
        print("")
        print(f"Población creada con {n_population} individuos")

        print("")
        print("Inicio del proceso iterativo")

        # Bucle de iteraciones. 
        # Se hace evolucionar a n cantidad de poblaciones hasta conseguir una que cumpla al 100% con las restricciones del problema 
        # o hasta que se cumpla la cantidad maxima de iteraciones
        while not(break_condition):
            self.iterationCount += 1
            # Se hace evolucionar a una nueva población
            fit, indi = self.evolve(n_population)
            fitSum += fit
            if (fit > bestFit) :
                bestFit = fit
                bestIndi.chromosome = indi.chromosome
                bestHistory = self.history.copy()
            # Se verifica que la población actual cumpla con las restricciones dadas
            if (fit >= 14) : break_condition = True
            # Se verifica que el número de iteraciones no supere al máximo
            if (self.iterationCount >= iterations) : break_condition = True
                
        self.history = bestHistory

        print("")
        print("Fin del proceso, mejor resultado")
        print("")
        
        if (bestFit == 14) :
            print("Exito! Se encontro una solución posible")
            print("")
        else :
            print("No se encontro una solución posible, intentelo de nuevo")
            print("")
        
        print("- Fitness:", round((bestFit / 14) * 100, 2), "%   (Avg:", round((fitSum/self.iterationCount)/14 * 100,2), "%)")
        print("")
        
        print("- Iterations:", self.iterationCount)
        print("")
        
        self.plot()
        print("")

        print("- Genoma:")
        print(bestIndi.chromosome)
        print("")
        
        print("- Individuo:")
        bestIndi.printNice()
        print("")


    # Se inicia un nuevo proceso de evolución de una población       
    def evolve(self, n_population):

        # Se genera una nueva población
        self.generate(n_population)
        self.history.clear()
        
        break_condition = False
        currentGeneration = 0
        
        # Se hace iterar a la población en las diferentes generaciones
        while not(break_condition):
                                 
            # Seleccion: Se seleccionan los individuos de la población que van a poblar a la nueva generación
            self.population = self.population[0:(int)(len(self.population) * self.crossover_prop)]
            
            # Crossover: Se cruzan de a pares los individuos con mejores resultados de la generación anterior y se generan dos nuevos hijos
            for index in range(0, len(self.population), 2): 
                if(index + 1 <= len(self.population)):
                    self.crossover(index, self.population[index], self.population[index + 1])
        
            # Mutate: Se introducen mutaciones aleatorias a los individuos de la nueva generación
            for ind in self.population: 
                self.mutate(ind, self.mutation_prop)

            # Condicion de corte: Se analiza si la evolución debe terminar
            
            # Se calcula el fitness de cada individuo y se lo reordena de mayor a menor (Siendo el primero el mejor)
            for ind in self.population: ind.fitness()
            self.population.sort(key = self.getScore, reverse = True)
            self.history.append(self.population[0].score)

            # Se consulta si el mejor individuo resuelve el problema
            if self.population[0].score >= 14 : break_condition = True

            # Se consulta si se supero la máxima cantidad de generaciones
            if currentGeneration >= self.maxGenerations : break_condition = True

            # Se analiza si la población crecio o decrecio mas de lo aceptado
            if len(self.population) <= 10 or len(self.population) > 50000: break_condition = True                    

            currentGeneration += 1
            
        
        self.status(currentGeneration - 1)
        return self.population[0].score, self.population[0]




    # Se genera una nueva población
    def generate(self, populationSize):
        self.population.clear()
        for x in range(0, populationSize):
            newbie = Phenotype()
            newbie.encode()
            self.population.append(newbie)



    # Se introduce una mutación al individuo basado en una probabilidad de mutación
    def mutate(self, ind, prob):
        if random.randrange(100) < prob * 100: ind.mutate()
        pass




    # Se introducen cruces entre indivuduos para conformar a la nueva generación
    # Se generan dos hijos nuevos por cada par de padres
    # El primero hijo contiene la primera parte del padre y la segunda de la madre
    # El segundo hijo contiene la primera parte de la madre y la segunda del padre
    def crossover(self, index, parent_1, parent_2):
        if(index == len(self.population)) : return
        
        child = Phenotype()
        child.crossover(parent_1, parent_2)
        self.population.append(child)

        child = Phenotype()
        child.crossover(parent_2, parent_1)
        self.population.append(child)
            
        pass



    # Función para ordenar la población basado en el puntaje de cada individuo
    def getScore(riddle, ind):
        return ind.score



    # Imprime por pantalla el estado de la evolución actual
    def status(self, currentGeneration):
        print("- Population:", len(self.population), "- Iteration:", self.iterationCount, "- Generations:", currentGeneration, "- Fitness:", round((self.population[0].score / 14) * 100, 2), "%")    
        pass



    # Imprime por pantalla un grafico con la evolución de la población actual
    def plot(self):
        plt.plot(self.history)
        plt.show()  
        pass
    
# Se inicializa el programa
start = time.time()

# Se genera un nuevo problema
rid = Riddle()
# Se resuelve el problema
rid.solve(n_population = 2000, generations = 100, iterations = 10, mutationRatio = 1, crossoverRatio = 0.5)

# Se muestran los resultados
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Tiempo transcurrido {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))