from dataaccess import get_message_dict, get_member_dict
import networkx as nx

if __name__ == '__main__':
        
    users = get_member_dict()
    messages = get_message_dict()

    net = nx.DiGraph()
    for k, m in messages.items():
        pmsg = m.parseMessage(['quote'])
        for q in pmsg['quote']:
            mid = q.get('message_id', None)
            if mid <> None and mid in messages:
                qMsg = messages[mid]
                if (m.member not in users) or (qMsg.member not in users):
                    continue

                uSender, uQuoted = users[m.member].realName, users[qMsg.member].realName
                if net.has_edge(uQuoted, uSender): # Direction from quoted to quoting user
                    net.edge[uQuoted][uSender]['weight'] += 1
                else:
                    net.add_edge(uQuoted, uSender, weight=1)

    print 'N:{}\tE:{}'.format(net.number_of_nodes(), net.number_of_edges())
    nx.write_gexf(net, 'data/processed_data/quote_net.gexf')