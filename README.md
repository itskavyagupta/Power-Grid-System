# power-grid-system

In this project, a power grid system where data of connected houses with different propagators are stored using python program with the help of graph data structures. The goal is to use graph data structure and perform certain operations such addition, removal of houses and propagators from the designed structure. Here we are using dictionary as an adjacency list to store the data in graph.

## Description

For this project implementation we have taken a scenario of a power grid system and electricity distribution to the houses attached with these power grids. Every power grid has power supply nodes/propagators that are providing power to different areas and localities more precisely to different houses.

Let's assume that there is a list of propagators from P1 to Pn. Each of these propagators are further connected with each other and different houses to provide the power. As we know that every power grid has its own capacity and providing power more than its capacity is not possible. Similarly each of the propagators comes with their own limitation and should not exhaust the assigned power limit. Each of the propagators may be connected with the H1 to Hk to provide the power supply. Let’s look at the block diagram of the proposed setup below. Each of these houses are connected with only one of the propagators in the power grid. Let’s look at some of the more insights-

- The propagator and house are connected using a directed edge with some weight. This weight represents the supply provided to the house based on the requirement.
- The propagators are connected with each other as well but the weight will be by default.
- Any new edge or house will be assigned to a propagator only if the demanded power request is available.
- All the propagators are locally stable and overall demand for a single propagator is always lesser than its capacity.
