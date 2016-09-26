import numpy as np

critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
    'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
    'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
    'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
    'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
    'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
    'The Night Listener': 4.5, 'Superman Returns': 4.0,
    'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
    'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
    'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
    'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane': 4.5,'You, Me and Dupree': 1.0,'Superman Returns': 4.0}}


def similarity(ratings, p1, p2):

    movies_in_common = []

    prefs1 = np.array([])
    prefs2 = np.array([])

    for movie in ratings[p1]:
        if movie in ratings[p2]:
            movies_in_common.append(movie)
            prefs1 = np.append(prefs1, ratings[p1][movie])
            prefs2 = np.append(prefs2, ratings[p2][movie])

    n = len(prefs1)
    if n == 0:
        return 0

    sum1 = np.sum(prefs1)
    sum2 = np.sum(prefs2)

    sum1sq = np.sum(np.square(prefs1))
    sum2sq = np.sum(np.square(prefs2))

    dot = np.dot(prefs1, prefs2)

    num = dot - (sum1 * sum2 / n)
    den = np.sqrt((sum1sq - np.square(sum1) / n) * (sum2sq - np.square(sum2) / n))

    if den == 0:
        return 0

    r = num / den
    return r

def getRecs(ratings, p1):

    sr_sum = {}
    s_sum = {}
    recs = []

    for person in ratings:
        if person == p1: continue

        sim_score = similarity(ratings, p1, person)
        # print 'sim_score ' + str(sim_score)
        if sim_score <= 0: continue
        for movie in ratings[person]:
            if movie not in ratings[p1]:
                sr_sum.setdefault(movie, 0)
                sr_sum[movie] += ratings[person][movie] * sim_score
                s_sum.setdefault(movie, 0)
                s_sum[movie] += sim_score

    # print sr_sum
    # print s_sum

    for movie, num in sr_sum.iteritems():
        recs.append((sr_sum[movie] / s_sum[movie], movie))

    recs.sort()
    recs.reverse()
    return recs
