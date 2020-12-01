
uri = [
    'data:image/webp;base64,UklGRiIAAABXRUJQVlA4IBYAAAAwAQCdASoBAAEADsD+JaQAA3AAAAAA',
    'data:image/webp;base64,UklGRhoAAABXRUJQVlA4TA0AAAAvAAAAEAcQERGIiP4HAA==',
    'data:image/webp;base64,UklGRkoAAABXRUJQVlA4WAoAAAAQAAAAAAAAAAAAQUxQSAwAAAARBxAR/Q9ERP8DAABWUDggGAAAABQBAJ0BKgEAAQAAAP4AAA3AAP7mtQAAAA==',
    'data:image/webp;base64,UklGRlIAAABXRUJQVlA4WAoAAAASAAAAAAAAAAAAQU5JTQYAAAD/////AABBTk1GJgAAAAAAAAAAAAAAAAAAAGQAAABWUDhMDQAAAC8AAAAQBxAREYiI/gcA',
    'data:image/webp;base64,UklGRiQAAABXRUJQVlA4IBgAAAAwAQCdASoBAAEAAwA0JaQAA3AA/vuUAAA'
 ]
   

   
#有scrapy的话，用parse_data_uri解码base64_url(含data字符)    
from w3lib.url import parse_data_uri
for i in range(5):
    base64_str = uri[i].split(',')[-1]
    if len(base64_str)%4 != 0:
        uri[i] += '='*(4-len(base64_str)%4)
    ret = parse_data_uri(uri[i]).data
    with open(f'{i}.webp','wb') as f:
        f.write(ret)
 
 
 
#用base64解码base64_url 
# import base64
# for i in range(5):
    # data = uri[i].split(',')[-1]
    # if len(data)%4 != 0:  #base64_url不足4的倍数，手动添加"="补足
        # data += '='*(4-len(data)%4)
    # ret = base64.b64decode(data) ##如果base64_url有特殊符号“+”，"/"就用base64.urlsafe_b64decode(data)
    # with open(f'{i}.webp','wb') as f:
        # f.write(ret)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        