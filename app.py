import redis
import rq
import func

q = rq.Queue(connection=redis.Redis())
job = q.enqueue(func.write_to_file, 'jernej.txt', 'http://www.jernejsila.com')
print job.key
