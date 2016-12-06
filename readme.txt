There are two seperate projects for each task

For task1 the code is in java and hence can be run using eclipse.
Steps :

1. Open the IR4-task1 project using eclipse.
2. Run HW3.java
Note : For each query a corresponding file with top 100 results will be generated.
For ex : query-number -top-100-lucene-results.txt will be the file generated


For task2 :
1. open the project using pycharm or any python editor
2. Run task2.py
Note : For each query a corresponding file with top 100 results will be generated.
For ex : query-number -top-100-results.txt will be the file generated.


----------------------------------
Implementation of Program - task2
----------------------------------
Steps :

1. Calculate the Idf of all the terms in corpus.
2. Calculate weight of each term. Weight of each term is tf*idf
3. A matrix is created that consist of document_id (name_of_document) and its corresponding list of word and weights
3. The query is taken as input in a loop. For each query term the idf is assumed to be 1.
   Weight of each query term is then its term frequency.

4. Calculate Score of each document.
   4.1 For this iterate over the query terms.
   4.2 Multiply the weight of query term and the weight of the same term from matrix created above.
   4.3 Take the summation of all the above weights.
   4.4 Divide the summation with square root of (length of document and length of query)

5. Rank the documents in descending order and pick top 100 docs.
Note : The length of document and query is summation of weigths of all its query terms resp.


The above steps are to implement formula of cosine similarity :

  Cosine(Di,Q) = Σdij · qj for all terms t / square_root(Σt (dij ** 2) · Σt (qj ** 2)) for all terms t
  Explanation : The numerator of this measure is the sum of the products of the term weights
                for the matching query and document terms (known as the dot product or inner
                product). The denominator normalizes this score by dividing by the product
                of the lengths of the two vectors.
_______________________________________________________________________________________________________________________

Comparision of queries is in file comparision.txt