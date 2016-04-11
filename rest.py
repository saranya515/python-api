import web
import xml.etree.ElementTree as ET
import boto3
import datetime



urls = (
    '/clicks', 'get_clicks'
)

app = web.application(urls, globals())

class get_clicks:        
    def GET(self):
	dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('prod1.ad-processor.banner-clicks-aggregation.date-shift.DainikBhaskar')
        date = datetime.date.today().strftime("%Y-%m-%d")
        
        response = table.get_item(
            Key={
               'qualifier': 'testing://c1sdk/p1sdk',
               'targetDay': date
            }
        )

        item = response['Item']['clickCount']
        output = item +1
        table.put_item(
            Item={
              'clickCount': output,
              'qualifier': 'testing://c1sdk/p1sdk',
              'targetDay': date
            }
        )
        return output



if __name__ == "__main__":
    app.run()
