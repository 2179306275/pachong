import weibo
import weibo_top
import weibo_comment

net = int(input("请输入操作（1.开始 2.停止）："))
while (net != 2):
    if (net == 1):
        choice1 = int(input("请选择爬取的方向：1.排行榜 2.关键词 3.评论："))
        if (choice1 == 1):
            # 调用爬取微博函数
            weibo_top.get_weibo_top()
        if (choice1 == 2):
            # 爬取关键字
            search_keyword = input("请输入搜索的关键词：")
            # 爬取页数
            max_search_page = int(input("请输入搜索的页数："))
            # 调用爬取微博函数
            weibo.get_weibo_list(v_keyword=search_keyword, v_max_page=max_search_page)
        if (choice1 == 3):
            # 目标微博ID，可循环爬取多个（这里只爬一个）
            weiboID_list = [str(x) for x in input("请输入微博ID(示例：4903111417922777),以逗号分隔：").split(',')]
            # 最大爬取页
            max_page = int(input("请输入搜索的页数："))
            # 调用爬取
            weibo_comment.get_bili_comment(weiboID_list=weiboID_list, max_page=max_page)


    net = int(input("是否重复爬取（1.是 2.否）："))