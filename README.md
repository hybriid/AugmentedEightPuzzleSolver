# README

Using Machine Learning to Generate h-values**

## Description

We augmented the A* search algorithm with a heuristic built on machine learning to solve 8-Puzzle and 15-Puzzle instances.

## Dependencies
List of libraries we used:

    joblib==1.1.0
    
    matplotlib==3.4.3
    
    numpy==1.21.2
    
    pandas==1.3.4
    
    scikit_learn==1.0.1

 

## How to run
1. test.py: All the algorithms run on an 8-puzzle instance with 1000 random moves:
   
   ```python test.py```

2. test_fifteen.py: A* and MLS run on a 15-puzzle instance with 100 random moves:
  
   ```python test_fifteen.py```
   
3. testloop.py: Test an 'n' amount of 8-puzzle instances with various search algorithms. We then get relevant statistics such as average amount of expanded nodes.

   ```python testloop.py <n> (E.g python testloop.py 100)```
   
3. testloop_fifteen.py: Test an 'n' amount of 15-puzzle instances with various search algorithms. We then get relevant statistics such as average amount of expanded nodes.

   ```python testloop_fifteen.py <n> (E.g python testloop_fifteen.py 10)```
   
### Contributors

1. Nam Tang (namt@sfu.ca)

2. Matthew De Guzman (mgdeguzm@sfu.ca)  
