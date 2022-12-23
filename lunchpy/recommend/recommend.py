import random

def recommend(matzips):
    # if store is None or len(store) == 0 then raise an exception
    if matzips is None or len(matzips) == 0:
        raise Exception("No stores found")

    # show all of them
    # for matzip in matzips:
    #     print(matzip.name)
    #     print(matzip.rating)
    #     print(matzip.address)
    #     print("")

    # sort stores by rating
    matzips = sorted(matzips, key=lambda matzip: matzip.rating, reverse=True)

    size = len(matzips)

    # only use the top 20% of stores
    # if size < 5: just use all of them
    if size > 5:
        matzips = matzips[:int(size * 0.2)]

    # randomly select 3 stores
    matzips = random.sample(matzips, 3)

    # sort stores by rating
    matzips = sorted(matzips, key=lambda matzip: matzip.rating, reverse=True)

   # return the top 3 stores
    return matzips
