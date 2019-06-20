# coding:utf-8


#------------------------------- preparation -------------------------------#

# make edge_list for BFS, DFS
def make_links_list(links_file, number_of_users):

    links_list = {}
    for i in range(number_of_users):
        links_list[i] = []
    
    f_links = open(links_file, "r")
    for line in f_links:
        start_node, target_node = line.split("\t")
        start_number, target_number = int(start_node), int(target_node)
        links_list[start_number].append(target_number)
        
    f_links.close()
    return links_list

# make list of users
def make_user_list(nicknames_file):
    f_nicknames = open(nicknames_file, "r")
    user_list = {}
    for line in f_nicknames:
        line = line.rstrip('\n')
        user_number, nickname = line.split('\t')
        user_number = int(user_number)
        user_list[user_number] = [nickname, "unreached"]
    f_nicknames.close()
    return user_list

#--------------------------------------------------------------------------#


#--------------------------------- search ---------------------------------#

def get_nickname_from_number(user_number, user_list):
    return user_list[user_number][0]

def get_number_from_nickname(nickname, user_list):
    return [k for k, value in user_list.items() if value[0] == nickname][0]

def reached_node(user_number, user_list):
    user_list[user_number][1] = "reached"

def BFS(start_number, target_number, links_list, user_list):
    path = []
    que = []
    que.append(start_number)
    reached_node(start_number, user_list)
    while que != []:
        current_number = que.pop(0)
        path.append(current_number)
        if current_number == target_number:
            return path
        unreached_count = 0
        for i in links_list[current_number]:
            if user_list[i][1] == "unreached":
                que.append(i)
                reached_node(i, user_list)
                unreached_count += 1
        if unreached_count == 0:
            path.pop()
    return 'Not Connected'

def DFS(start_number, target_number, links_list, user_list):
    reached_node(start_number, user_list)
    
    if start_number == target_number:
        return 'Connected'
    
    if links_list[start_number] == []:
        return 'Not Connected'
    for child_number in links_list[start_number]:
        if user_list[child_number][1] == "unreached":
            a = DFS(child_number, target_number, links_list, user_list)
            if a != 'Not Connected':
                return a
    return 'Not Connected'
    
def Search_Path(links_file, nicknames_file, number_of_users, start_name, target_name, BFS_or_DFS):
    links_list = make_links_list(links_file, number_of_users)
    user_list = make_user_list(nicknames_file)
    start_number = get_number_from_nickname(start_name, user_list)
    target_number = get_number_from_nickname(target_name, user_list)
    
    if BFS_or_DFS == 'BFS':
        answer_list = BFS(start_number, target_number, links_list, user_list)
    else:
        answer_list = DFS(start_number, target_number, links_list, user_list)

    if answer_list == 'Not Connected':
        print answer_list
    elif answer_list == 'Connected':
        print answer_list
    else:
        named_path = []
        for i in answer_list:
            name = get_nickname_from_number(i, user_list)
            named_path.append(name)
        print 'path = %s' % named_path
        step = len(answer_list)-1
        print 'step = %d' % step
        return named_path, step

#--------------------------------------------------------------------------#


#-------------------------------- question --------------------------------#

# BFS 最短経路とステップ数を返す
Search_Path('shima_links.txt', 'shima_names.txt', 7, 'Haraken', 'Shima', 'BFS')
Search_Path('links.txt', 'nicknames.txt', 49, 'clayton', 'jacob', 'BFS')
Search_Path('links.txt', 'nicknames.txt', 49, 'jacob', 'clayton', 'BFS')

# DFS 繋がっているかどうかのみを返す
Search_Path('shima_links.txt', 'shima_names.txt', 7, 'Haraken', 'Shima', 'DFS')
Search_Path('links.txt', 'nicknames.txt', 49, 'clayton', 'jacob', 'DFS')
Search_Path('links.txt', 'nicknames.txt', 49, 'jacob', 'clayton', 'DFS')

#--------------------------------------------------------------------------#
