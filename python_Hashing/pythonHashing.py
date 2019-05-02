#!/usr/bin/env python3

"""
Author: Andrea Murphy
Date: May 1, 2019
DESC: Python Hashing
"""

from __future__ import division
import itertools
import re
import hashlib

# A shingle in this code is a string with K-words
K = 4

# Takes two sets and returns Jaccard coefficient
def jaccard_set(s1, s2):
    u = s1.union(s2)
    i = s1.intersection(s2)
    return len(i)/len(u)

# Makes a set of K-tokens
def make_a_set_of_tokens(doc):
    # replace non-alphanumeric char with a space, and then split
    tokens = re.sub("[^\w]", " ",  doc).split()

    sh = set()
    for i in range(len(tokens)-K):
        t = tokens[i]
        for x in tokens[i+1:i+K]:
            t += ' ' + x
        sh.add(t)
    return sh

if __name__ == '__main__':

    documents = ["The Transmission Control Protocol (TCP) is intended for use as a highly reliable host-to-host protocol between hosts in packet-switched computer communication networks, and in interconnected systems of such networks.",
                 "This document describes the functions to be performed by the Transmission Control Protocol, the program that implements it, and its interface to programs or users that require its services.",
                 "Computer communication systems are playing an increasingly important role in military, government, and civilian environments. This document focuses its attention primarily on military computer communication requirements, especially robustness in the presence of communication unreliability and availability in the presence of congestion, but many of these problems are found in the civilian and government sector as well",
                 "As strategic and tactical computer communication networks are developed and deployed, it is essential to provide means of interconnecting them and to provide standard interprocess communication protocols which can support a broad range of applications.  In anticipation of the need for such standards, the Deputy Undersecretary of Defense for Research and Engineering has declared the Transmission Control Protocol (TCP) described herein to be a basis for DoD-wide inter-process communication protocol standardization.",
                 "TCP is a connection-oriented, end-to-end reliable protocol designed to fit into a layered hierarchy of protocols which support multi-network applications. The TCP provides for reliable inter-process communication between pairs of processes in host computers attached to distinct but interconnected computer communication networks. Very few assumptions are made as to the reliability of the communication protocols below the TCP layer.  TCP assumes it can obtain a simple, potentially unreliable datagram service from the lower level protocols.  In principle, the TCP should be able to operate above a wide spectrum of communication systems ranging from hard-wired connections to packet-switched or circuit-switched networks."]
                 


"""
handle documents one by one
makes a list of sets which are compresized
of a list of K words string
"""
shingles = []
for doc in documents:
        # makes a set of tokens
        # sh = set([' ', ..., ' '])
    sh = make_a_set_of_tokens(doc)
    print(("sh = %s") %(sh))

    # hasing
    bucket = map(hash, sh)

    # print("bucket = %s") %(bucket)

    # shingles : list of sets (sh)
    shingles.append(set(bucket))

#print("shingles=%s") %(shingles)

combinations = list( itertools.combinations([x for x in range(len(shingles))], 2) )
print(("combinations=%s") %(combinations))

# compare each pair in combinations tuple of shingles
for c in combinations:
    i1 = c[0]
    i2 = c[1]
    jac = jaccard_set(shingles[i1], shingles[i2])
    print(("%s : jaccard=%s") %(c,jac))
