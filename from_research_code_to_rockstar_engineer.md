From Research Code to Software Rockstar


Motivation
Introduction

Exploration vs Exploitation

Toolsets 



Why am I writing this?
That is an excellent question ... partly this is a bit autobiographical as I started in research and have **slowly** transitioned more into software. I would like to share what I have learned and the larger picture that I have pieced together with the hopes that this will provide illumination for a number of different groups:

graduate students who want to understand how to become infinitely more employable or chart a path forward in terms of skills development
hiring professionals who want to understand the differences between these often conflated groups, especially when hiring data scientists

Second, I think that by ennumerating the differences in practices between these two groups will allow more intelligent decisions to be mad.



The difference between software engineering and the code that researchers write ... stems from the functional purpose of the code.

A large company is about exploiting a particular product that has already been found to be profitable

A startup is about finding that product ...

this is the exploitation versus exploration ... a fundamental tension between two different end goals

depth first vs breadth first.

Exploitation is about going deep ... it is optimizing something that already exists or the structures around this existing product needed to produce it

Exploration is about going broad ... it is search ... we don't know what works but we will search until we find something that works (or run out of resources, ie time and/or money)

When running analyses on data, we are exploring the data and what is possible.

This is a messy process and is often reflected in the code that is generated to accomplish this task.

We have multiple stages in the data science pipeline and when we are exploring, these stages will often change ... we will iterate rapidly ... something will change ...we will find something in the modeling phase that might require us to go back to the acquire phase ... and reaquire or acquire in a different fashion than we did before ... or clean in a new way.

Acquire
Clean
Model


Thus, the tools that are used for these tasks are optimized for a very different end goal than the tools of the software developer.


The software that gets written is often from scratch ... built with a patchwork of available tools cobbled together with duct tape. Is it scalable? No. Is it entirely reusable? No. Does it get the job done. most of the times, yes.

If the researcher was to start with a skeleton or framework from the production level code, this could work much better.
