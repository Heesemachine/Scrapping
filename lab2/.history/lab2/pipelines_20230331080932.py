# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Lab2Pipeline:
    def process_item(self, item, spider):
        try:
            item["url"] = float(item.get(&quot;__name__&quot;).replace(&quot;\xa0&quot;, &quot;&quot;))
            return item
