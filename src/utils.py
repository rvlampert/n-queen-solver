import matplotlib.pyplot as plt
import os

def plot_values(min_values,max_values,average_values):
    plt.plot(range(1,len(min_values)+1), min_values, label = "Min conflicts")
    plt.plot(range(1,len(max_values)+1), max_values, label = "Max conflicts")
    plt.plot(range(1,len(average_values)+1), average_values, label = "Average conflicts")
    plt.xlabel('Generations')
    plt.ylabel('Conflicts')
    plt.title('Evolution')
    plt.legend()
    plt.show()

def print_solution(solution, time, N):

    print("\nTime to find the solution: ",time)
    print_board(solution)

def print_board(solution):
    
    N = len(solution)
    print("\nSolution: \n")
    print(solution)
    print("╔═══"+"╦═══"*(N-1)+"╗")
    for line in range(N):
        for col in range(N):
            print(f"║ ", end="")
            if line == solution[col]-1:
                print("# ", end="")
            else:
                print("  ", end="")
            
        print("║")
        if line < N-1:
            print("╠═══"+"╬═══"*(N-1)+"╣")
        else:
            print("╚═══"+"╩═══"*(N-1)+"╝")

