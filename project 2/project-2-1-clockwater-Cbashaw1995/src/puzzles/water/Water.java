package puzzles.water;

import puzzles.clock.BFSSolver;
import puzzles.common.solver.Solver;

import java.util.Arrays;

/**
 * Main class for the water buckets puzzle.
 *
 * @author Connor Bashaw
 */
public class Water {

    /**
     * Run an instance of the water buckets puzzle.
     *
     * @param args [0]: desired amount of water to be collected;
     *             [1..N]: the capacities of the N available buckets.
     */
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Water amount bucket1 bucket2 ...");
            System.exit(1);
        } else {
            //set  desired amount to args 0
            int desiredAmount = Integer.parseInt(args[0]);

            //pare the bucket capacities from args 1
            int[] BucketCapacities = new int[args.length-1];
            for (int i = 1; i< args.length; i++){
                BucketCapacities[i-1] = Integer.parseInt(args[i]);
            }

            //create initial config for water with desired amount and capacities
            waterConfig initialConfig = new waterConfig(desiredAmount,BucketCapacities);

            //send inital config to solver
            BFSSolver<waterConfig> solver = new BFSSolver<>(initialConfig);

            //check solution and attempt to solve
            boolean solutionFound = solver.solve();

            //print print statements per the output files
            //start with desired amount and listing the capacities given in the input
            System.out.print("Amount: "+ desiredAmount);
            System.out.print(", Bucket Capacities: [" );

            for (int i = 0; i < BucketCapacities.length; i++){
                System.out.print(BucketCapacities[i]);
                if (i < BucketCapacities.length -1 ){
                    System.out.print(", ");
                }
            }

            // print total and unique confiugs
            System.out.println("]");
            System.out.println("Total configs: " +solver.getTotalConfigurations());
            System.out.println("Unique configs: " +solver.getUniqueConfigurations());

            //print solution steps if solution is found
            if (solutionFound){

                int steps = 0;

                for (waterConfig config : solver.getSolutionPath()) {
                    System.out.println("Step: " + steps + ": " + config);
                    steps++;
                }
                }else {
                System.out.println("No solution found");
            }

        }
    }
}
