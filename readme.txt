Our project is done in Java and Python both. Majority of code is in Python as described below :

PYTHON

There are 4 seperate folders for 4 different task given :
 - task1
 - task2
 - task3 and
 - task_phase2

Folder task1 contains 3 files :
    1. task1_BM_25.py which is implementation of search engine with BM25 as retrieval model
    2. task1_cosine_sim.py which is implementation of search engine with Cosine Similarity as retrieval model
    3. task1_tf_idf.py which is implementation of search engine with TF-IDF as retrieval model

Folder task2 contains :
    1. task2_pseudo_relevance.py - contains implementation of query expansion with psuedo relevance feedback.

Folder task3 contains :
    1. task3A_tf_idf.py - which is implemetation of TF-IDF as retrieval model with stopping
    2. task3b_tf_idf    - which is implementation of TF-IDF as retrieval model but with stemmed corpus and query

Folder task_phase2 contains:
    1. task2_pseudo_releavance_with_stopping.py - which is implemetation of TF-IDF as retrieval model with stopping


To RUN the above files :

    A
     We need the following  :
     1. Path to corpus on which the index will be build
     2. Path where cleaned files will be stored.
     3. Path where query file is stored.
     Comments in code will help to plug above paths in correct place.

    B
     As these values are plugged in, Retreival model is initialized.
     All models needs three parameters,
      1. Index
      2. Path to document that contains entries of relevant documents for all given queries.
      3. Path to file where results of run will be stored.

    C
     For Evaluation of run the following will be needed :
      1. Path to file where Map results for following run will be stored.
      2. Path to file where MRR results for following run will be stored.
      3. Path to file where Rank_At_P results for following run will be stored.
      4. Path to file where Precision and Recall tables results for following run will be stored.

 - Once All the above values are plugged, just run code as normal python script.


OUTPUT :

   The ouput will be generated as follows :
     There will be 4 folders for given task, namely,
     1. run_task1
     2. run_task2
     3. run_task3
     4. run_phase2

     These folders contains files corresponding to 7 run.
     For examples, run_task1 contains
      a. task1_bm25_run.txt - run corresponding to bm25.
      b. task1_cosine_similarity - run corresponding to cosine similarity.
      c. task1_tf_idf_similarity - run correspinding to tf-idf.
     In addition to run results, it contains evaluation factor corresponding to each run which in turn contains 4 files :
        a. Map.txt - contains results for mean average precision.
        b. MRR.txt - contains mean reciprocal rank
        c. p_at_k.txt - contains rank a P where P is 5 and 20 for every query
        d. table_precision_recal.txt - contains table for precision and recal value at each retrieved document.


JAVA PART

    For task1 Lucene run - there is a seperate folder named 'Lucene' under main search-engine folder.
    It basically contains code for task1 lucene run, its corresponding output and evalutation results.

    For Snippet generation :


