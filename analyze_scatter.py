#!/usr/bin/python
import sys
import numpy

filename = sys.argv[1]
min_rating_num = int(sys.argv[2])
means = []
stds = {}
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
                std = numpy.std(cur_ratings)
                std_key = "%.2f" % std
                if not std_key in stds: stds[std_key] = 0
                stds[std_key] += 1
            cur_product_id = product_id
            cur_ratings = []
        cur_ratings.append(rating)
    product_num += 1
    if (len(cur_ratings) > min_rating_num):
        #means.append(numpy.mean(cur_ratings))
        std = numpy.std(cur_ratings)
        std_key = "%.2f" % std
        if not std_key in stds: stds[std_key] = 0
        stds[std_key] += 1

print ",\n".join(["{ x:%s, y:%d, type:%s }" % (key, stds[key], sys.argv[3]) for key in stds.keys()])
#print ",".join(["%.2f" % std for std in stds])
