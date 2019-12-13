from maps.basic_map import BasicMap
from scenario import Scenario
from person.stationary_lost_person import StationaryLostPerson
from person.stationary_searcher import StationarySearcher
from person.random_walk_lost_person import RandomWalkLostPerson
from person.shortest_path_lost_person import ShortestPathLostPerson
from person.random_walk_searcher import RandomWalkSearcher
import matplotlib.pyplot as plt



def create_latency_vs_timestep(max_latency, number_samples, max_timestep):
    iterations = []

    for i in range(max_latency):
        total = 0
        for j in range(number_samples):

            m = BasicMap(15, 15)

            middle = (7,7)

            # Add some lost persons to the map
            lp00 = RandomWalkLostPerson(m)
            lp00.init(middle)

            # Add some searchers to the map
            searcher00 = RandomWalkSearcher(m)
            searcher00.init(middle)

            s = Scenario(m, [lp00], [searcher00], i)
            count = s.simulate(max_timestep)  # Simulate for N time steps
            total += count
        avg = total / number_samples
        iterations.append(avg)


    plt.title("latency vs time step")
    plt.plot(list(range(max_latency)),iterations)
    plt.xlabel('latency')
    plt.ylabel('time step')
    plt.show()



# Work on this
def create_latency_vs_percent_found(max_latency, number_samples, max_timestep):
    iterations = []

    for i in range(max_latency):
        num_yes = 0
        for j in range(number_samples):

            m = BasicMap(15, 15)

            middle = (7,7)

            # Add some lost persons to the map
            lp00 = RandomWalkLostPerson(m)
            lp00.init(middle)

            # Add some searchers to the map
            searcher00 = RandomWalkSearcher(m)
            searcher00.init(middle)

            s = Scenario(m, [lp00], [searcher00], i)
            count = s.simulate(max_timestep)  # Simulate for N time steps
            if count != max_timestep:
                num_yes += 1
        perc_found = num_yes / number_samples
        iterations.append(perc_found * 100)


    plt.title("Latency vs Lost Percentage Found Rate")
    plt.plot(list(range(max_latency)),iterations)
    plt.xlabel('Latency')
    plt.ylabel('Percent Found')
    plt.show()



def create_searchers_vs_time(max_searchers, latency, number_samples, num_time_steps):
    iterations = []

    m = BasicMap(15, 15)
    middle = (7,7)

    
    for num_searchers in range(1, max_searchers):
        total = 0
        for i in range(number_samples):

            # Add some lost persons to the map
            lp00 = RandomWalkLostPerson(m)
            lp00.init(middle)

            searchers = []

            for j in range(num_searchers):
                # Add some searchers to the map
                searcher = RandomWalkSearcher(m)
                searcher.init(middle)
                searchers.append(searcher)


            s = Scenario(m, [lp00], searchers)
            count = s.simulate(100)  # Simulate for N time steps
            total += count
        avg = total / number_samples

        iterations.append(avg)


    plt.title("searchers vs time step")
    plt.plot(list(range(max_searchers - 1)),iterations)
    plt.xlabel('searchers')
    plt.ylabel('time step')
    plt.show()



if __name__ == '__main__':
    #create_latency_vs_percent_found(max_latency, number_samples, max_timestep):
    #create_searchers_vs_time(10, 10, 100, 100)
    #create_latency_vs_percent_found(100, 10000, 100)
    create_searchers_vs_time(100, 60, 10000, 100)
    # create_latency_vs_percent_found(50, 100, 50)
