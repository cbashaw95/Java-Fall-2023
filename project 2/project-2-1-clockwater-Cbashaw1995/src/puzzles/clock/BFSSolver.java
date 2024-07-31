package puzzles.clock;

import puzzles.common.solver.Configuration;

import java.util.*;

public class BFSSolver<T extends Configuration> {
    private final T initialConfig;
    private final Map<T, T> predecessorMap;
    private int totalConfigurations;
    private int uniqueConfigurations;
    private List<T> solutionPath;

    public BFSSolver(T initialConfig) {
        this.initialConfig = initialConfig;
        this.predecessorMap = new HashMap<>();
        this.totalConfigurations = 0;
        this.uniqueConfigurations = 0;
        this.solutionPath = new ArrayList<>();
    }

    public boolean solve() {
        Queue<T> queue = new LinkedList<>();
        Set<T> visited = new HashSet<>();

        queue.add(initialConfig);
        visited.add(initialConfig);

        while (!queue.isEmpty()) {
            T currentConfig = queue.poll();

            if (currentConfig.isSolution()) {
                reconstructSolutionPath(currentConfig);
                return true;
            }
            List<T> neighbors = (List<T>) new ArrayList<>(currentConfig.getNeighbors());
            totalConfigurations += neighbors.size();

            for (T neighbor : neighbors) {
                if (!visited.contains(neighbor)) {
                    predecessorMap.put(neighbor, currentConfig);
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
        return false;
    }

    public List<T> getSolutionPath() {
        return solutionPath;
    }

    public int getTotalConfigurations() {
        return totalConfigurations;
    }

    public int getUniqueConfigurations() {
        return predecessorMap.size();
    }

    private void reconstructSolutionPath(T finalConfig) {
        solutionPath.clear();
        T currentConfig = finalConfig;
        while (currentConfig != null) {
            solutionPath.add(0, currentConfig);
            currentConfig = predecessorMap.get(currentConfig);
        }
    }
}





