from dataaccess import get_forum_messages, get_member_dict
import networkx as nx

from utils import dict_cosine

def user_title_bipartite(messageIterator, users):
    umDict = dict()
    for m in messageIterator:
        tid = m.topic
        uid = m.member
        if uid not in users:
            continue
    
        if uid not in umDict:
            umDict[uid] = dict()
        if tid not in umDict[uid]:
            umDict[uid][tid] = 0
        umDict[uid][tid] += 1

    return umDict

if __name__ == '__main__':
    
    users = get_member_dict()
    messageIter = get_forum_messages()

    umDict = user_title_bipartite(messageIter, users)

    # Create user-topic bipartite network
    titles = set()
    for u in umDict:
        titles |= set(umDict[u].keys())
    print len(titles), 'unique title'

    bNet = nx.Graph()
    bNet.add_nodes_from(umDict.keys(), bipartite=0) # Add the node attribute "bipartite"
    bNet.add_nodes_from(titles, bipartite=1)

    for u in umDict:
        for t in umDict[u]:
            bNet.add_edge(u, t, weight=umDict[u][t])
    # TODO: Add also title and user names
    nx.write_gexf(bNet, 'data/processed_data/user_title_bipartite.gexf')

    # Compute user similarity based on title activity
    userSimNet = nx.Graph()
    for u1 in umDict:
        for u2 in umDict:
            sim = dict_cosine(umDict[u1], umDict[u2])
            if sim > 0:
                userSimNet.add_edge(users[u1].realName, users[u2].realName, weight=sim)
    nx.write_gexf(userSimNet, 'data/processed_data/users_similarity_by_title.gexf')

    # TODO: Instead of titles using topic provide better granularity.



