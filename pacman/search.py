# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    # from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):                                                      ############################## IMPLEMENTAR ESSA!!! ##################################
    """                                                                             

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    '''Tem que ser usado um tipo abstrato de dados do tipo PILHA,
    porque na busca em profundidade, os ultimos nohs que entram
    sao os primeiros a serem visitados e sairem da fronteira.'''

    
    visitados = {} "Eh um dicionario pois contem os nohs que foram retirados da PILHA e o caminho de como foram obtidos"

    solucao = [] "Uma lista de nohs representando o caminho que o agente ira seguir"

    pais = {} "Dicionario do qual 'solucao' vai ser preenchida com as direcoes"

    "Criamos o objeto 'fronteira' da classe Stack()"
    fronteira = util.Stack() "'fronteira' recebe a devolucao do método Stack() que cria um tipo abstrato de dados do tipo PILHA conforme implementada na classe util"
    "a fronteira sera uma tripla (noh na fronteira, direcao, custo)

    "A funcao getStartState() devolve uma dupla (x, y)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    nohInicial = problem.getStartState() "Inicializa o problema com seu ESTADO INICIAL, que sera uma dupla (x, y)"
    
    fronteira.push((nohInicial, 'Indefinida', 0)) "Coloca o estado inicial na pilha, ficando algo como [(x, y), 'Indefinida', 0]"
    

    if (problem.isGoalState(nohInicial) == True):
        return solucao "A lista 'solucao' esta vazia. Devolvema-la aqui porque se o noh inicial for a solucao,"
                        "isso significa que o agente simplesmente nao vai andar, isto e, seguira um conjunto de instrucoes vazio"

    objetivo = False
        
    while (fronteira.isEmpty == False and objetivo == False):
        noh = fronteira.pop() "Criamos 'noh', que é uma tripla (noh na fronteira, direcao, custo)"
        visitados[noh[0]] = noh[1] "'noh[0]' == 'noh na fronteira' (que é uma dupla (x, y)) e 'noh[1]' == 'direcao' (que é um nome da direção, ex.: 'South'), ou seja,"
                                    "o dicionario 'visitados' tem como chave as coordenadas do noh e como valores a direcao"
        
        "Verifica se o noh tirado da fronteira(visitado) eh o objetivo"
        if(problem.isGoalState(noh[0])):
            nohSolucao = noh[0] "'nohSolucao' é uma dupla (x, y) que é o objetivo do problema"
            objetivo = True "Para esse 'while' não ser mais executado"
            break "Para o laco 'for' abaixo não ser executado, pois ja chegamos no objetivo"

        for sucessor in problem.getSuccessors(noh[0]): "'sucessor' eh uma TRIPLA!!!"
           if(sucessor[0] not in visitados.keys()): "por isso pegamos 'sucessor[0]', pois estamos interessados apenas em suas coordenadas (x, y)"
              fronteira.push(sucessor) "bota cada 'sucessor' na pilha da 'fronteira'"
              pais[sucessor[0]] = noh[0]

    while (nohSolucao in pais.keys()):
        paiDoNohSolucao = pai[nohSolucao]
        solucao.insert(0, paiDoNohSolucao[1])
        nohSolucao = paiDoNohSolucao

    return solucao
              
    '''print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())'''
    
    util.raiseNotDefined()


def breadthFirstSearch(problem):                                                    ############################## IMPLEMENTAR ESSA!!! ##################################
    """
    Search the shallowest nodes in the search tree first.
    DICA: Utilizar util.PriorityQueue
    *** YOUR CODE HERE ***
    """

    visitados = {} "Eh um dicionario pois contem os nohs que foram retirados da PILHA e o caminho de como foram obtidos"

    solucao = [] "Uma lista de nohs representando o caminho que o agente ira seguir"

    pais = {} "Dicionario do qual 'solucao' vai ser preenchida com as direcoes"

    fronteira = util.Queue()

    "A funcao getStartState() devolve uma dupla (x, y)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    nohInicial = problem.getStartState() "Inicializa o problema com seu ESTADO INICIAL, que sera uma dupla (x, y)"
    
    fronteira.push((nohInicial, 'Indefinida', 0)) "Coloca o estado inicial na pilha, ficando algo como [(x, y), 'Indefinida', 0]"
    

    if (problem.isGoalState(nohInicial) == True):
        return solucao "A lista 'solucao' esta vazia. Devolvema-la aqui porque se o noh inicial for a solucao,"
                        "isso significa que o agente simplesmente nao vai andar, isto e, seguira um conjunto de instrucoes vazio"

    objetivo = False
        
    while (fronteira.isEmpty == False and objetivo == False):
        noh = fronteira.pop() "Criamos 'noh', que é uma tripla (noh na fronteira, direcao, custo)"
        visitados[noh[0]] = noh[1] "'noh[0]' == 'noh na fronteira' (que é uma dupla (x, y)) e 'noh[1]' == 'direcao' (que é um nome da direção, ex.: 'South'), ou seja,"
                                    "o dicionario 'visitados' tem como chave as coordenadas do noh e como valores a direcao"
        
        "Verifica se o noh tirado da fronteira(visitado) eh o objetivo"
        if(problem.isGoalState(noh[0])):
            nohSolucao = noh[0] "'nohSolucao' é uma dupla (x, y) que é o objetivo do problema"
            objetivo = True "Para esse 'while' não ser mais executado"
            break "Para o laco 'for' abaixo não ser executado, pois ja chegamos no objetivo"

        #############POR QUE VERIFICA SE NAO ESTA EM 'PAIS' TAMBEM????????????????????????????????????????????????????????
        for sucessor in problem.getSuccessors(noh[0]): "'sucessor' eh uma TRIPLA!!!"
           if(sucessor[0] not in visitados.keys() and sucessor[0] not in pais.keys()): "por isso pegamos 'sucessor[0]',"
                                                                                        "pois estamos interessados apenas em suas coordenadas (x, y)"
              fronteira.push(sucessor) "bota cada 'sucessor' na pilha da 'fronteira'"
              pais[sucessor[0]] = noh[0]

    while (nohSolucao in pais.keys()):
        paiDoNohSolucao = pai[nohSolucao]
        solucao.insert(0, paiDoNohSolucao[1])
        nohSolucao = paiDoNohSolucao

    return solucao
              
    util.raiseNotDefined()

    
def uniformCostSearch(problem):                                                     ############################## IMPLEMENTAR ESSA!!! ##################################
    """Search the node of least total cost first.
    *** YOUR CODE HERE ***
    """

    visitados = {} "Eh um dicionario pois contem os nohs que foram retirados da PILHA e o caminho de como foram obtidos"

    solucao = [] "Uma lista de nohs representando o caminho que o agente ira seguir"

    pais = {} "Dicionario do qual 'solucao' vai ser preenchida com as direcoes"

    fronteira = util.PriorityQueue()

    custo = {} "Dicionario que guarda os custos de um caminho. Vai servir para comparar custos de um mesmo caminho, para que o de custo menor seja escolhido"

    "A funcao getStartState() devolve uma dupla (x, y)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    nohInicial = problem.getStartState() "Inicializa o problema com seu ESTADO INICIAL, que sera uma dupla (x, y)"
    
    fronteira.push((nohInicial, 'Indefinida', 0), 0) "Coloca o estado inicial na pilha, ficando algo como [(x, y), 'Indefinida', 0]"
    

    if (problem.isGoalState(nohInicial) == True):
        return solucao "A lista 'solucao' esta vazia. Devolvema-la aqui porque se o noh inicial for a solucao,"
                        "isso significa que o agente simplesmente nao vai andar, isto e, seguira um conjunto de instrucoes vazio"

    objetivo = False
        
    while (fronteira.isEmpty == False and objetivo == False):
        noh = fronteira.pop() "Criamos 'noh', que é uma tripla (noh na fronteira, direcao, custo)"
        visitados[noh[0]] = noh[1] "'noh[0]' == 'noh na fronteira' (que é uma dupla (x, y)) e 'noh[1]' == 'direcao' (que é um nome da direção, ex.: 'South'), ou seja,"
                                    "o dicionario 'visitados' tem como chave as coordenadas do noh e como valores a direcao"
        
        "Verifica se o noh tirado da fronteira(visitado) eh o objetivo"
        if(problem.isGoalState(noh[0])):
            nohSolucao = noh[0] "'nohSolucao' é uma dupla (x, y) que é o objetivo do problema"
            objetivo = True "Para esse 'while' não ser mais executado"
            break "Para o laco 'for' abaixo não ser executado, pois ja chegamos no objetivo"

        for sucessor in problem.getSuccessors(noh[0]): "'sucessor' eh uma TRIPLA!!!"
           if(sucessor[0] not in visitados.keys()): "por isso pegamos 'sucessor[0]', pois estamos interessados apenas em suas coordenadas (x, y)"
              fronteira.push(sucessor) "bota cada 'sucessor' na pilha da 'fronteira'"
              pais[sucessor[0]] = noh[0]

    while (nohSolucao in pais.keys()):
        paiDoNohSolucao = pai[nohSolucao]
        solucao.insert(0, paiDoNohSolucao[1])
        nohSolucao = paiDoNohSolucao

    return solucao
              
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):                                  ############################## IMPLEMENTAR ESSA!!! ##################################
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    visitados = {} "Eh um dicionario pois contem os nohs que foram retirados da PILHA e o caminho de como foram obtidos"

    solucao = [] "Uma lista de nohs representando o caminho que o agente ira seguir"

    pais = {} "Dicionario do qual 'solucao' vai ser preenchida com as direcoes"

    #Criamos o objeto 'fronteira' da classe Stack()
    fronteira = util.Stack() "'fronteira' recebe a devolucao do método Stack() que cria um tipo abstrato de dados do tipo PILHA conforme implementada na classe util"
    "a fronteira sera uma tripla (noh na fronteira, direcao, custo)

    #A funcao getStartState() devolve uma dupla (x, y)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    nohInicial = problem.getStartState() "Inicializa o problema com seu ESTADO INICIAL, que sera uma dupla (x, y)"
    
    fronteira.push((nohInicial, 'Indefinida', 0)) "Coloca o estado inicial na pilha, ficando algo como [(x, y), 'Indefinida', 0]"
    

    if (problem.isGoalState(nohInicial) == True):
        return solucao "A lista 'solucao' esta vazia. Devolvema-la aqui porque se o noh inicial for a solucao,"
                        "isso significa que o agente simplesmente nao vai andar, isto e, seguira um conjunto de instrucoes vazio"

    objetivo = False
        
    while (fronteira.isEmpty == False and objetivo == False):
        noh = fronteira.pop() "Criamos 'noh', que é uma tripla (noh na fronteira, direcao, custo)"
        visitados[noh[0]] = noh[1] "'noh[0]' == 'noh na fronteira' (que é uma dupla (x, y)) e 'noh[1]' == 'direcao' (que é um nome da direção, ex.: 'South'), ou seja,"
                                    "o dicionario 'visitados' tem como chave as coordenadas do noh e como valores a direcao"
        
        #Verifica se o noh tirado da fronteira(visitado) eh o objetivo
        if(problem.isGoalState(noh[0])):
            nohSolucao = noh[0] "'nohSolucao' é uma dupla (x, y) que é o objetivo do problema"
            objetivo = True "Para esse 'while' não ser mais executado"
            break "Para o laco 'for' abaixo não ser executado, pois ja chegamos no objetivo"

        for sucessor in problem.getSuccessors(noh[0]): "'sucessor' eh uma TRIPLA!!!"
           if(sucessor[0] not in visitados.keys(): "por isso pegamos 'sucessor[0]', pois estamos interessados apenas em suas coordenadas (x, y)"
              fronteira.push(sucessor) "bota cada 'sucessor' na pilha da 'fronteira'"
              pais[sucessor[0]] = noh[0]

    while (nohSolucao in pais.keys()):
        paiDoNohSolucao = pai[nohSolucao]
        solucao.insert(0, paiDoNohSolucao[1])
        nohSolucao = paiDoNohSolucao

    return solucao
              
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
