'''
1. from each word pair, find the first different letters and form a order between two letters if possible
2. build a directed acyclic graph (DAG) from these relationship
3. reconstruct a dependency order from the DAG

We will use bfs to solve the problem
4. first find out all the nodes with zero in degrees and visit them.
5. find all the nodes these nodes conencted to
6. remove the coming nodes from the next level nodes
7. if any nodes has zero in degrees, put them into a queue
'''