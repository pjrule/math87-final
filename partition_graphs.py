from maps.basic_map import BasicMap
from scenario import Scenario
from person.random_walk_lost_person import RandomWalkLostPerson
from person.random_walk_searcher import RandomWalkSearcher
import matplotlib.pyplot as plt
import statistics
from maps.quadrant_partitioner import QuadrantPartitioner
from person.vertical_sweep_searcher import VerticalSweepSearcher
import math


def getNoPartitionStats(num_searchers, number_samples, max_timestep, latency):
    num_yes = 0
    avg_found = []
    perc_found = 0
    num_timesteps_successful = []
    num_timesteps_overall = []
    for i in range(number_samples):

        m = BasicMap(101, 101)

        middle = (50,50)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init(middle)

        # Add some searchers to the map
        searchers = []
        for j in range(0, num_searchers):
            searcher = RandomWalkSearcher(m)
            searcher.init(middle)
            searchers.append(searcher)

        s = Scenario(m, [lp00], searchers, latency=latency)
        count = s.simulate(max_timestep)  # Simulate for N time steps
        if count < max_timestep:
            num_yes += 1
            num_timesteps_successful.append(count)
        num_timesteps_overall.append(count)
        perc_found = num_yes / (i+1)
        perc_found = perc_found * 100
        avg_found.append(perc_found)

    # Graph convergence
    plt.title("Convergence to expected probability of success, no partitioning")
    plt.plot(list(range(number_samples)), avg_found)
    plt.xlabel('Number of Samples')
    plt.ylabel('Probability of Success')
    plt.savefig('convergence_psucess.png')

    print("Result: Percent Lost Person Discovered = " + str(perc_found))
    print("Average Number of Time Steps (when successful): " + str(sum(num_timesteps_successful)/len(num_timesteps_successful)))
    print("Standard deviation: " + str(statistics.stdev(num_timesteps_successful)))
    print("Average Number of Time Steps (overall): " + str(sum(num_timesteps_overall)/len(num_timesteps_overall)))
    print("Standard deviation: " + str(statistics.stdev(num_timesteps_overall)))


def getQuadrantPartitionStats(num_searchers, number_samples, max_timestep, latency):
    num_yes = 0
    avg_found = []
    perc_found = 0
    num_timesteps_successful = []
    num_timesteps_overall = []

    for i in range(number_samples):

        m = BasicMap(101, 101)

        middle = (50,50)

        partitioner = QuadrantPartitioner()
        [rows_midpoint, cols_midpoint] = partitioner.partition(m)
        quad01_rows = (0, rows_midpoint)
        quad01_cols = (0, cols_midpoint)
        quad02_rows = (0, rows_midpoint)
        quad02_cols = (cols_midpoint, m.numColumns() - 1)
        quad03_rows = (rows_midpoint, m.numRows() - 1)
        quad03_cols = (0, cols_midpoint - 1)
        quad04_rows = (rows_midpoint, m.numRows() - 1)
        quad04_cols = (cols_midpoint, m.numColumns() - 1)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init(middle)

        # Add some searchers to the map
        searchers = []
        for j in range(0, num_searchers):
            if j % 4 == 0:
                # Assign to quadrant 1
                searcher = RandomWalkSearcher(m, quad01_rows, quad01_cols)
            elif j % 4 == 1:
                # Assign to quadrant 2
                searcher = RandomWalkSearcher(m, quad02_rows, quad02_cols)
            elif j % 4 == 2:
                # Assign to quadrant 3
                searcher = RandomWalkSearcher(m, quad03_rows, quad03_cols)
            else:
                # Assign to quadrant 4
                searcher = RandomWalkSearcher(m, quad04_rows, quad04_cols)
            searcher.init(middle)
            searchers.append(searcher)

        s = Scenario(m, [lp00], searchers, latency=latency)
        count = s.simulate(max_timestep)  # Simulate for N time steps
        if count < max_timestep:
            num_yes += 1
            num_timesteps_successful.append(count)
        num_timesteps_overall.append(count)
        perc_found = num_yes / (i+1)
        perc_found = perc_found * 100
        avg_found.append(perc_found)

    # Graph convergence
    plt.title("Convergence to expected probability of success, quadrant partitioning")
    plt.plot(list(range(number_samples)), avg_found)
    plt.xlabel('Number of Samples')
    plt.ylabel('Probability of Success')
    plt.savefig('convergence_psucess_quadrant.png')

    print("Result: Percent Lost Person Discovered = " + str(perc_found))
    print("Average Number of Time Steps (when successful): " + str(sum(num_timesteps_successful)/len(num_timesteps_successful)))
    print("Standard deviation: " + str(statistics.stdev(num_timesteps_successful)))
    print("Average Number of Time Steps (overall): " + str(sum(num_timesteps_overall)/len(num_timesteps_overall)))
    print("Standard deviation: " + str(statistics.stdev(num_timesteps_overall)))


def getLanePartitionStats(num_searchers, number_samples, max_timestep, latency, lane_size):
    num_yes = 0
    avg_found = []
    perc_found = 0
    num_timesteps_successful = []
    num_timesteps_overall = []
    # Final lane is just a bit wider than the others...
    # lanes = [(0, 9), (10, 19), (20, 29), (30, 39), (40, 49),
    #          (50, 59), (60, 69), (70, 79), (80, 89), (90, 100)]
    lanes = []
    lower = 0
    upper = lane_size - 1
    lanes.append((lower, upper))
    for i in range(0, num_searchers-1):
        # Each searcher gets a dedicated lane
        lower = upper + 1
        upper += lane_size
        lanes.append((lower, upper))
    print(lanes)

    for i in range(number_samples):
        m = BasicMap(101, 101)
        middle = (50,50)

        # Add some lost persons to the map
        lp00 = RandomWalkLostPerson(m)
        lp00.init(middle)

        # Add some searchers to the map
        searchers = []
        for j in range(0, len(lanes)):
            searcher = VerticalSweepSearcher(m, lanes[j])
            searcher.init((0, math.floor((lanes[j][0] + lanes[j][1])/2)))
            searchers.append(searcher)

        s = Scenario(m, [lp00], searchers, latency=latency)
        count = s.simulate(max_timestep)  # Simulate for N time steps
        if count < max_timestep:
            num_yes += 1
            num_timesteps_successful.append(count)
        num_timesteps_overall.append(count)
        perc_found = num_yes / (i+1)
        perc_found = perc_found * 100
        avg_found.append(perc_found)

    # Graph convergence
    plt.title("Convergence to expected probability of success, lanes partitioning")
    plt.plot(list(range(number_samples)), avg_found)
    plt.xlabel('Number of Samples')
    plt.ylabel('Probability of Success')
    plt.savefig('convergence_psucess_lanes.png')

    print("Result: Percent Lost Person Discovered = " + str(perc_found))
    print("Average Number of Time Steps (when successful): " + str(sum(num_timesteps_successful)/len(num_timesteps_successful)))
    print("Standard deviation: " + str(statistics.stdev(num_timesteps_successful)))
    print("Average Number of Time Steps (overall): " + str(sum(num_timesteps_overall)/len(num_timesteps_overall)))
    print("Standard deviation: " + str(statistics.stdev(num_timesteps_overall)))


def get_quadrantPartitionPerformance(num_searchers=15, max_timestep=100, latency=15, number_samples=1000):
    iterations = []

    for i in range(0, num_searchers+1):
        total = 0
        for j in range(number_samples):

            m = BasicMap(15, 15)

            partitioner = QuadrantPartitioner()
            [rows_midpoint, cols_midpoint] = partitioner.partition(m)
            quad01_rows = (0, rows_midpoint)
            quad01_cols = (0, cols_midpoint)
            quad02_rows = (0, rows_midpoint)
            quad02_cols = (cols_midpoint, m.numColumns() - 1)
            quad03_rows = (rows_midpoint, m.numRows() - 1)
            quad03_cols = (0, cols_midpoint - 1)
            quad04_rows = (rows_midpoint, m.numRows() - 1)
            quad04_cols = (cols_midpoint, m.numColumns() - 1)

            middle = (7,7)

            # Add some lost persons to the map
            lp00 = RandomWalkLostPerson(m)
            lp00.init(middle)

            # Add some searchers to the map
            searchers = []
            for j in range(0, i):
                if j % 4 == 0:
                    # Assign to quadrant 1
                    searcher = RandomWalkSearcher(m, quad01_rows, quad01_cols)
                elif j % 4 == 1:
                    # Assign to quadrant 2
                    searcher = RandomWalkSearcher(m, quad02_rows, quad02_cols)
                elif j % 4 == 2:
                    # Assign to quadrant 3
                    searcher = RandomWalkSearcher(m, quad03_rows, quad03_cols)
                else:
                    # Assign to quadrant 4
                    searcher = RandomWalkSearcher(m, quad04_rows, quad04_cols)
                searcher.init(middle)
                searchers.append(searcher)

            s = Scenario(m, [lp00], searchers, latency)
            count = s.simulate(max_timestep)  # Simulate for N time steps
            total += count
        avg = total / number_samples
        iterations.append(avg)

    plt.title("searchers vs time step")
    plt.plot(list(range(len(iterations))),iterations)
    plt.xlabel('searchers')
    plt.ylabel('time step')
    plt.show()
    print(iterations)
    return iterations


def get_lanePartitionPerformance(num_searchers=15, max_timestep=100, max_latency=15, number_samples=100):
    # TODO - Finish this.
    iterations = []

    num_rows = 15
    num_cols = 15

    for i in range(1, num_searchers+1):
        # Get our lanes!!!
        lanes = []
        lane_size = (num_cols - 1) / i
        for j in range(0, i):
            lower = j * lane_size
            upper = (j + 1) * lane_size
            lanes.append((math.floor(lower) + 1, math.floor(upper)))
        lanes[0] = (0, lanes[0][1])
        print(lanes)

        total = 0
        for j in range(number_samples):

            m = BasicMap(15, 15)

            middle = (7,7)

            # Add some lost persons to the map
            lp00 = RandomWalkLostPerson(m)
            lp00.init(middle)

            # Add some searchers to the map
            searchers = []
            for k in range(0, len(lanes)):
                searcher = VerticalSweepSearcher(m, lanes[k])
                searcher.init((0, math.floor((lanes[k][0] + lanes[k][1]) / 2)))
                searchers.append(searcher)

            s = Scenario(m, [lp00], searchers, max_latency)
            count = s.simulate(max_timestep)  # Simulate for N time steps
            total += count
        avg = total / number_samples
        iterations.append(avg)

    plt.title("latency vs time step")
    plt.plot(list(range(len(iterations))),iterations)
    plt.xlabel('latency')
    plt.ylabel('time step')
    plt.show()
    print(iterations)
    return iterations


if __name__ == '__main__':
    # 1000 simulations.
    # 101x101 grid with 1 lost person and 10 searchers.
    # Searchers have 100 timesteps to find lost person.
    # Lost person has 100 timesteps to move before searchers begin searching.
    # getNoPartitionStats(20, 1000, 200, 100)
    # getQuadrantPartitionStats(20, 1000, 200, 100)
    # getLanePartitionStats(20, 1000, 200, 100, 5)
    # iterations = get_quadrantPartitionPerformance()
    # with open('quadrants.csv', 'w') as f:
    #     for item in iterations:
    #         line = str(item) + ',' + '\n'
    #         f.write(line)
    iterations = get_lanePartitionPerformance()
    with open('lanes.csv', 'w') as f:
        for item in iterations:
            line = str(item) + ',' + '\n'
            f.write(line)