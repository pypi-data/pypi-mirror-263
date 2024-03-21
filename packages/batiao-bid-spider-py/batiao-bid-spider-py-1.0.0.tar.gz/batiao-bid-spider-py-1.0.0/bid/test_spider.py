def test(_name):
    if _name != "__main__":
        return
    import os
    import sys
    import logging

    sys.path.append(os.getcwd())
    from utils.set_logging import init_log

    try:
        init_log()
    except:
        os.chdir(os.path.dirname(os.getcwd()))
        init_log()

    from spider import get_spider
    import api
    from utils import underlinecase_to_camelcase

    city_list = api.get_city_list()
    type_list = api.get_type_list()
    # 获取当前运行的爬虫名
    frame = sys._getframe(1)
    filename = frame.f_code.co_filename
    spider_name = filename.split("/")
    spider_name = spider_name[spider_name.__len__() - 1]
    spider_name = spider_name.split("\\")
    spider_name = spider_name[spider_name.__len__() - 1]
    spider_name = spider_name.replace(".py", "").replace("spider_", "")
    logging.info(
        f"DEBUG:spider_{spider_name}.{underlinecase_to_camelcase('spider_'+spider_name)}"
    )
    sp = get_spider(spider_name)
    if sp:
        setattr(sp, "city_list", city_list)
        setattr(sp, "type_list", type_list)
        sp.source = {
            "id": "0",
            "spider": spider_name,
            "status": "1",
        }
        sp = sp()
        sp.run()
    sys.exit(0)


def get_succ():
    return True
