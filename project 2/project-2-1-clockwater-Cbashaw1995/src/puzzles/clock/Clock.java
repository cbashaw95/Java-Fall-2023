package puzzles.clock;

import puzzles.common.solver.Configuration;

import java.util.Collection;

/**
 * Main class for the clock puzzle.
 *
 * @author Connor Bashaw
 */
public class Clock {
    /**
     * Run an instance of the clock puzzle.
     *
     * @param args [0]: the number of hours in the clock;
     *             [1]: the starting hour;
     *             [2]: the finish hour.
     */
    public static void main(String[] args) {
        // check for correct command line args
        if (args.length != 3) {
            System.out.println(("Usage: java Clock hours start finish"));
            System.exit(1);
        }
        //parse command line args into ints for each category
        int hours = Integer.parseInt(args[0]);
        int start = Integer.parseInt(args[1]);
        int end = Integer.parseInt(args[2]);

        // create a initial config and a solver for the clock puzzle
        ClockConfig initialConfig = new ClockConfig(hours, start, end);
        BFSSolver<ClockConfig> solver = new BFSSolver<>(initialConfig);

        //attempt to find a solution for the puzzle
        boolean solutionFound = solver.solve();

        // print inpur parameters
        System.out.println("Hours " + hours + ", Start: " + start + ",End: " + end);
        System.out.println("Total Configs: " + solver.getTotalConfigurations());
        System.out.println("Unique Configs: " + solver.getUniqueConfigurations());

        // if found print the steps to get from start to end
        if (solutionFound) {
            int step = 0;
            for (ClockConfig config : solver.getSolutionPath()) {
                System.out.println("Step " + step + ": " + config.getCurrentHour());
                step++;
            }
        } else {
            System.out.println("No solution found.");

        }

    }
}