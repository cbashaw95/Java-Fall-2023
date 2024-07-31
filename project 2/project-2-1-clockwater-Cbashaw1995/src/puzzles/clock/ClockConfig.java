package puzzles.clock;

import puzzles.common.solver.Configuration;

import java.util.Collection;
import java.util.HashSet;

public class ClockConfig implements Configuration {
    private int hours;
    private int currentHour;
    private int targetHour;

    //constructor for clock config
    public ClockConfig(int hours, int currentHour, int targetHour){
        this.hours= hours;
        this.currentHour = currentHour;
        this.targetHour = targetHour;
    }

    //check if current hour matches targeted hour
    @Override
    public boolean isSolution() {
        return currentHour == targetHour;
    }


    @Override
    public Collection<Configuration> getNeighbors() {
        Collection<Configuration> neighbors = new HashSet<>();

        //make a neighbor by moving the hour forward
        int nextHourForward = (currentHour % hours+1);
        neighbors.add(new ClockConfig(hours,nextHourForward, targetHour));

        //make a neigbor by moving the hour backward
        int nextHourBackwards;
        if (currentHour == 1 ){
            nextHourBackwards = hours;
        }else {
            nextHourBackwards = currentHour -1;
        }

        neighbors.add(new ClockConfig(hours, nextHourBackwards,targetHour));
        return neighbors;

    }

    @Override
    public boolean equals(Object o) {
        //check if two clock configs are equal
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        ClockConfig that = (ClockConfig) o;
        return hours == that.hours && currentHour == that.currentHour && targetHour == that.targetHour;
    }

    @Override
    public int hashCode() {

        //calculate a unique hashcode for the clock config
        return 31 * hours + currentHour;
    }

    @Override
    public String toString() {
        //stringify the clock config.
        return "ClockConfig{" +
                "hours=" + hours +
                ", start=" + currentHour +
                ", end=" + targetHour +
                '}';
    }

    public int getCurrentHour() {

        //get current hour
        return currentHour;
    }
}
