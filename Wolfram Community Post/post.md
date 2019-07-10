# Code Embeddings for Wolfram Language

## Introduction

Will programs ever be able to write other programs? This question is a discussion point where the halting problem is a significant argument against it. But could we already use machine learning techniques to simplify the daily routine of programmers? We think, yes.

### Problem

The problem of applying the machine learning algorithms such as neural networks to the source code is that the source code is not a numerical thing. We need to map the programming code to real numbers. Such a transformation is called an embedding.

### Code Embeddings

How should this transformation look like? For example, we can split the code into pieces and apply one-hot encoding where each element of a vector is associated with exactly one element. But would it be effective? The source code of programs is not random data, it's a sequence of commands with some structure, and an embedding must utilise the structure of the code as much as possible.

### What is this project about

In our project, we tried to explore different forms of embeddings for Wolfram Language. And then, use this representation to find similar built-in functions. For this purpose, we gathered a lot of samples of code in Wolfram Language from different sources. Then we cleaned the samples and made them interpretable. We trained a couple of classical neural network architectures with various parameters to find vector representation for built-in functions in Wolfram Language. Also, we did experiments with a state-of-the-art method in source code embeddings. The details are explained in the following .

## Dataset

The success of machine learning tasks depends heavily on the quality of the data. There was no ready dataset for this task. We started collecting by ourselves.

### Sources of the data

To build a dataset we used all the Wolfram Mathematica documentation, the Mathematica's internal unencrypted files and 923 GitHub repositories as large as ~57Gb.

### Cleaning dataset

We found a bug  in `ToExpression`.

## Language modelling

### RNN

TBD

### Dropout

TBD

### TSNE

TBD

## code2vec

TBD

## Conclusions

## Future work

During the project, we built a pipeline to start exploring embedding for Wolfram Language. There are loads of open questions about optimal neural network architecture and parameters which can be studied in the future. Also, there are other several approaches based on machine learning successfully applied to different program languages [1], which could be implemented for the language. Finally,  it is interesting to find how to use the symbolic structure of Wolfram Language to represent programs expressively for machine learning.

1. Chen, Z. & Monperrus, M. A Literature Study of Embeddings on Source Code. ArXiv190403061 Cs Stat (2019). 
