# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

from Witcher_mod import settings


class WitcherModPipeline:
    def __init__(self):
        self.connect = pymysql.connect(host=settings.MYSQL_HOST, user=settings.MYSQL_USER, passwd=settings.MYSQL_PASSWD,
                                       db=settings.MYSQL_DBNAME)
        self.cursor = self.connect.cursor()
        print("Mysql Success")

    def process_item(self, item, spider):
        insert_sql = """
        insert into data(name, url, size) VALUES (%s,%s,%s)
        """

        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['name'], item['url'], item['size']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
        print(item)
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()