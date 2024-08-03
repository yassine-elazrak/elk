import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter

logger = logging.getLogger("logstash")
logger.setLevel(logging.DEBUG)   
 
handler = AsynchronousLogstashHandler(
    host="localhost", 
    port=50000,
    ssl_enabled=True, 
    ssl_verify=False,
    transport='logstash_async.transport.TcpTransport',
    database_path='')
 
formatter = LogstashFormatter()
handler.setFormatter(formatter)
 
logger.addHandler(handler)
 
# Send log records to Logstash 
logger.error('python-logstash-async: test error message.')
logger.info('python-logstash-async: test info message.')
logger.warning('python-logstash-async: test warning message.')
logger.debug('python-logstash-async: test debug message.')