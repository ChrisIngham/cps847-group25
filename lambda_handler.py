import json

def lambda_handler(event, context):
    try:
        # iterate over each record
        for record in event['Record']:
            # handle event type
            if record['eventName'] == 'INSERT':
                insert(record)
            elif record['eventName'] == "MODIFY":
                modify(record)
            elif record['eventName'] == "REMOVE":
                remove(record)
     
    except Exception as e:
        print(e)
        return "error"


def insert(record):
    print('Handling Insert event')

    # get newImage content
    newImage = record['dynamodb']['NewImage']

    # parse the values
    newPlayerID = newImage['playerId']['S']



def modify(record):

    #parse oldImage and score
    oldImage= record['dynamobd']['OldImage']
    oldScore= oldImage['score']['N']

    # Parse oldImage and score

    newImage = record['dynamodb']['NewImage']
    newScore = newImage['score']['N']


    def remove(record):
        print('handling REMOVE events')

        # Parse oldImage
        oldImage = record['dynamodb']['OldImage']

        # Parse the values
        oldPlayerId = oldImage['playerId']['S']
