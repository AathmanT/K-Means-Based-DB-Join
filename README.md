# K-Means-Based-DB-Join

## Problem Statement
Current implementation of join operation of H2 is also based on the Nested-loop method. It is costly in terms of disk access frequency. And this leads to a worst time complexity when it comes to handling join queries with big data. So, it is essential to experiment with different join strategies and propose a strategy that could handle join operation for H2 databases, especially when dealing with big data or dynamically changing tables.

### Proposed Solution
1. **Boosted with unsupervised learning, the feature from left table is checked whether there was a clustering already done based on the feature for that particular table.**

2. **If so, clustered memory of the table will be used if there is no updating from the table.** 

3. **Else if it is a join on new feature, clustering based on the feature is done. Same process happens to the right table.** 

4. **Then the similar clusters are only scanned for making the relevant cartesian product.** 

5. **Even when the tale is updated the saved model for a table (on specific feature) can add the new data to relevant cluster. By this it is intended to prevent scans for every join as well and to prevent the inefficiency caused through defining hash functions manually.** 

![Alt text](C:\Users\cvvin\Downloads/Algorithm.png?raw=true "Algorithm")


