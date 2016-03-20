__author__ = 'kangrong'
from suffix_tree.generate_tree import SuffixTree
from suffix_tree.ex_string import StringEx
from utils import *
# strs = "acrossthetauntonriverfromdightonindightonrockstatepark"
# strs = "abcabxabcdedeo"
# strs = "cacao"
# strs = ["banana","bano"]
strs = [
    "libertypike",
    "franklintn",
    "carothersjohnhenryhouse",
    "carothersezealhouse",
    "acrossthetauntonriverfromdightonindightonrockstatepark",
    "dightonma",
    "dightonrock",
    "6mineoflowgaponlowgapfork",
    "lowgapky",
    "lemasterjohnjandellenhouse",
    "lemasterhouse",
    "70wilburblvd",
    "poughkeepsieny",
    "freerhouse",
    "701laurelst",
    "conwaysc",
    "hollidayjwjrhouse",
    "mainandappletonsts",
    "menomoneefallswi",
    "mainstreethistoricdistrict",
    "addressrestricted",
    "brownsmillsnj",
    "hanoverfurnace",
    "hanoverbogironfurnace",
    "sofsavannahatfergusonaveandbethesdard",
    "savannahga",
    "bethesdahomeforboys",
    "bethesda"
]
# data = []
# for s in strs:
#     datus = []
#     for i in s:
#         datus.append(ord(i))
#     data.append(datus)
# print data
tree = SuffixTree()
# tree.put(StringEx([1,2,1,2,5]),1)
i = 0
for datum in strs:
    print "input:" + datum
    tree.put(StringEx(datum), i)
    ret = tree.search(StringEx("banan"))
    # if ret is not None:
    #     print "eeeeerror"

    for string in getSubstrings(datum):
        ex = StringEx(string)
        ret = tree.search(ex)
        if i not in ret:
            print "error:" + str(i) + "," + string

    # if ret.contain():
    #     print "error:"+str(i)+","+strs
    i += 1

# print tree
