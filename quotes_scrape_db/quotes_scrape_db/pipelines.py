# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import psycopg2
from supabase import create_client, Client
from dotenv import load_dotenv

class QuotesScrapeDbPipeline:
    def __init__(self):
        load_dotenv()
        
        # Connection Details
        USER = os.getenv("user")
        PASSWORD = os.getenv("password")
        HOST = os.getenv("host")
        PORT = os.getenv("port")
        DBNAME = os.getenv("dbname")

        # Create/Connect to database
        self.connection = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DBNAME)
        
        # Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        
    
    def process_item(self, item, spider):
        # Define insert statement
        self.cur.execute(""" insert into quotes (text, author) values (%s,%s)""", (
            item["text"],
            item["author"]
        ))

        # Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        # Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
