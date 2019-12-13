from maps.basic_map import BasicMap
from scenario import Scenario
from person.stationary_lost_person import StationaryLostPerson
from person.stationary_searcher import StationarySearcher
from person.random_walk_lost_person import RandomWalkLostPerson
from person.shortest_path_lost_person import ShortestPathLostPerson
from person.random_walk_searcher import RandomWalkSearcher
import matplotlib.pyplot as plt
from tqdm import trange


def create_latency_vs_timestep(max_latency, number_samples, max_timestep):
    iterations = []

    for i in trange(max_latency):
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

    plt.plot(iterations)
    plt.xlabel('Latency')
    plt.ylabel('Average number of search time steps')
    plt.savefig('latency_vs_time_steps.pdf', bbox_inches='tight')
    plt.close()
    # plt.show()



# Work on this
def create_latency_vs_percent_found(max_latency, number_samples, max_timestep):
    iterations = []

    for i in trange(max_latency):
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
            if s.num_rescued > 0:
                num_yes += 1
        perc_found = num_yes / number_samples
        iterations.append(perc_found * 100)

    plt.plot(iterations)
    plt.xlabel('Latency')
    plt.ylabel('% lost persons found')
    plt.savefig('latency_vs_percent_found.pdf', bbox_inches='tight')
    plt.close()
    # plt.show()



def create_searchers_vs_time(max_searchers, latency, number_samples, num_time_steps):
    iterations = []

    for num_searchers in trange(1, max_searchers + 1):
        total = 0
        for i in range(number_samples):
            m = BasicMap(15, 15)
            middle = (7,7)

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
            count = s.simulate(num_time_steps)  # Simulate for N time steps
            total += count
        avg = total / number_samples

        iterations.append(avg)


    plt.plot(list(range(1, max_searchers + 1)), iterations)
    plt.xlabel('Number of searchers')
    plt.ylabel('Average number of search time steps')
    plt.savefig('searchers_vs_time.pdf', bbox_inches='tight')
    plt.close()
    # plt.show()

if __name__ == '__main__':
    create_latency_vs_timestep(100, 10000, 100)
    create_latency_vs_percent_found(100, 10000, 100)
    create_searchers_vs_time(20, 15, 10000, 100)
