#!/usr/bin/python
import sys
import numpy

filename = sys.argv[1]
min_rating_num = int(sys.argv[2])
means = []
stds = []
product_num = 0
with open(filename) as infile:
    cur_product_id = ""
    cur_ratings = []
    for line in infile:
        cols = line.split(",")
        product_id = cols[1]
        rating = float(cols[2])
        if (cur_product_id == ""): cur_product_id = product_id
        if product_id != cur_product_id:
            product_num += 1
            if (len(cur_ratings) > min_rating_num):
                #means.append(numpy.mean(cur_ratings))
                stds.append(numpy.std(cur_ratings))
            cur_product_id = product_id
            cur_ratings = []
        cur_ratings.append(rating)
    product_num += 1
    if (len(cur_ratings) > min_rating_num):
        #means.append(numpy.mean(cur_ratings))
        stds.append(numpy.std(cur_ratings))

print "%s,%d,%f,%f" % (filename, len(stds), numpy.mean(stds), numpy.std(stds))
