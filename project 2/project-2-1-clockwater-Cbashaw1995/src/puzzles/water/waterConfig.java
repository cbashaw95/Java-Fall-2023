package puzzles.water;

import puzzles.common.solver.Configuration;

import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

/**
 * WaterConfig for the water buckets puzzle.
 *
 * @author Connor Bashaw
 */

public class waterConfig implements Configuration {

    private final int DesiredAmount;
    private final int[] BucketCapacities;
    private final int[] BucketAmounts;

    public waterConfig(int DesiredAmount,int[]BucketCapacities){
        this.DesiredAmount = DesiredAmount;
        this.BucketCapacities = Arrays.copyOf(BucketCapacities,BucketCapacities.length);
        this.BucketAmounts = new int[BucketCapacities.length];
    }
    public waterConfig(int DesiredAmount,int[]BucketCapacities, int[]bucketAmounts){
        this.DesiredAmount = DesiredAmount;
        this.BucketCapacities = Arrays.copyOf(BucketCapacities,BucketCapacities.length);
        this.BucketAmounts = Arrays.copyOf(bucketAmounts,bucketAmounts.length);
    }

    @Override
    public boolean isSolution() {
        for (int amount : BucketAmounts){
            if (amount == DesiredAmount){
                return true;
            }
        }
        return false;

    }

    @Override
    public Collection<Configuration> getNeighbors() {
        //initialize a list neighbors that is a list of configurations
        List<Configuration> neighbors = new ArrayList<>();

        for (int i = 0; i< BucketCapacities.length; i++){
            //fill bucket
            if (BucketAmounts[i] < BucketCapacities[i]){
                int[] newAmounts = BucketAmounts.clone();
                newAmounts[i] = BucketCapacities[i];
                neighbors.add(new waterConfig(DesiredAmount,BucketCapacities,newAmounts));
            }
            //transfer buckets
            for (int j = 0; j < BucketCapacities.length; j++){
                if (i != j && BucketAmounts[i] > 0 && BucketAmounts[j] < BucketCapacities[j]){
                    int [] newAmounts = BucketAmounts.clone();
                    int transferAmount = Math.min(BucketAmounts[i], BucketCapacities[j] - BucketAmounts[j]);
                    newAmounts[i] -= transferAmount;
                    newAmounts[j] += transferAmount;
                    neighbors.add(new waterConfig(DesiredAmount,BucketCapacities,newAmounts));

                }
            }
            if (BucketAmounts[i] > 0){
                int[] newAmounts = BucketAmounts.clone();
                newAmounts[i] = 0;
                neighbors.add(new waterConfig(DesiredAmount, BucketCapacities, newAmounts));
            }
        }
        return neighbors;
    }

    @Override
    public boolean equals(Object o){
        if (this == o){
            return true;
        }
        waterConfig that = (waterConfig) o;

        return Arrays.equals(BucketAmounts, that.BucketAmounts);
    }

    @Override
    public int hashCode(){
        return Arrays.hashCode(BucketAmounts);
    }

    @Override
    public String toString(){
        return Arrays.toString(BucketAmounts);
    }
}
