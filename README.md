# Eval

<img src="https://img.shields.io/github/license/MistaAsh/Eval"> <img src="https://img.shields.io/github/languages/top/MistaAsh/Eval"> <img src="https://img.shields.io/github/issues/MistaAsh/Eval"> <img src="https://img.shields.io/github/issues-pr/MistaAsh/Eval"> <img src="https://img.shields.io/github/last-commit/MistaAsh/Eval">

<p align="center">
    <img src="src/client/public/logo.png" />
</p>

This is Eval! A tool used to automate the  evaluation of test answers using Cohere powered APIs and scoring the answers based on suitable metrics.

<br>

## Motivation 
Evaluation of answer sheets conducted in the traditional way is a **tedious and critical task**. Lot of time and energy is invested by the teachers or examiners to thoroughly check answers for every question. There is a likelihood of showing bias by the examiners based on personal or situational circumstances. 

The overall process of evaluations causes **delays in declaration of results** and hence leads to slow progress in assessment based learning. Large volumes of answer sheets checking can also affect the **mental health** of teachers which could lead to **poor teaching performance**.

<br>    

## Scoring Metrics
1. Semantic Search - this is the primary scoring strategy of Eval. It is used to sematically understand the answer given and evaluate based on content rather than simply scoring based on textual similarities.
    - *Cohere Embed* was used to generate embeddings for 5 suggested answers for the question and the answer to be checked. Then we find the distance from the nearest neighbour out of the 5 suggestions and the answer. This distance is used to grade the answer.
2. Duplication Check - partially correct answers with duplication of text tended to get higher similarity scores compared to the ones without duplication.
    - To stop students from using this exploit to gain extra marks, a duplications checker was implemented based on *Jaccard-Similarity* between sentences within the answer.
3. Grammar Check - this strategy aims to check the grammar of the answer and assign a score based on the number of grammatical errors.
    - We used *Cohere Generate* endpoint to generate a grammatically correct version of the answer, then check for cosine similarity of the generated version with original version to check if the original version was grammatically correct.
4. Toxicity Check - this aims to detect for toxic content in the answer and penalize an answer if it is toxic.
    - We trained a custom classification model on Cohere using *Social Media Toxicity Dataset by SurgeAI* which gave a 98% precision on the test split.
5. Custom Checks - this allows for users to give different weights to each of the three different metrics based on how important they are for the evaluation of the answer. This allows for a more personalized evaluation of the answer.

<br>

## Built With
* Cohere API
* Scikit-learn
* Django Rest Framework
* NextJS
* Tailwind CSS
* Flask

<br>

## Installation
Refer to *INSTALLATION.md* for installation instructions.