import base64
import gzip
import json

def handler(event, context):
    output = []
    for record in event['records']:
        compressed_payload = base64.b64decode(record['data'])
        uncompressed_payload = gzip.decompress(compressed_payload)
        payload = json.loads(uncompressed_payload)
        output_record = {
            'recordId': record['recordId'],
            'data': binary(payload),
            'result': 'Ok'
        }
        output.append(output_record)
    return {'records': output}

def binary(dict):
    string = json.dumps(dict).encode('utf-8')
    return base64.b64encode(string).decode('utf-8')
