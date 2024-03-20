import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"../src"))

import marscode_baas_sdk.redis as redis_module
# from a0_baas_sdk.redis import redis as redis_module

# result = redis_module.redis.hget("pythonsdk_hset002", "f04")
# result = redis_module.redis_clients["pysdk_resource_id_02"].hget("pythonsdk_hset002", "f02")

# result = redis_module.redis_clients["pysdk_resource_id_02"].hgetall("pythonsdk_hset002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].hincrby("pythonsdk_hset002", "some2", 211)

# result = redis_module.redis_clients["pysdk_resource_id_02"].hincrbyfloat("pythonsdk_hset002", "some2", 1.211)

# result = redis_module.redis_clients["pysdk_resource_id_02"].hkeys("pythonsdk_hset002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].hlen("pythonsdk_hset0021")

# result = redis_module.redis_clients["pysdk_resource_id_02"].hmget("pythonsdk_hset002", "some1", "some")

# result = redis_module.redis_clients["pysdk_resource_id_02"].hmset("pythonsdk_hset002", "some3", "v3", "some4", "v4")

# result = redis_module.redis_clients["pysdk_resource_id_02"].hvals("pythonsdk_hset002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].lindex("pythonsdk_list002", 123)

# result = redis_module.redis_clients["pysdk_resource_id_02"].llen("pythonsdk_list002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].lpop("pythonsdk_list002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].rpop("pythonsdk_list0021")

# result = redis_module.redis_clients["pysdk_resource_id_02"].rpoplpush("xxx:\{pythonsdk_list0022\}", "xxx:\{pythonsdk_list\}")

# result = redis_module.redis_clients["pysdk_resource_id_02"].lpushx("pythonsdk_list008", "qq")

# result = redis_module.redis_clients["pysdk_resource_id_02"].rpushx("pythonsdk_list008", "pp")

# result = redis_module.redis_clients["pysdk_resource_id_02"].lpush("pythonsdk_list002", "f","g")

# result = redis_module.redis_clients["pysdk_resource_id_02"].rpush("pythonsdk_list008", "f","g")

# result = redis_module.redis_clients["pysdk_resource_id_02"].llen("pythonsdk_list008")

# result = redis_module.redis_clients["pysdk_resource_id_02"].lrange("pythonsdk_list008", 0,-1)

# result = redis_module.redis_clients["pysdk_resource_id_02"].srandmember("pythonsdk_set008", 123)

# result = redis_module.redis_clients["pysdk_resource_id_02"].lset("pythonsdk_list002", 3, "aaa")
# result = redis_module.redis_clients["pysdk_resource_id_02"].hset("pythonsdk_hset002", "some5", "v5")
# result = redis_module.redis_clients["pysdk_resource_id_02"].hsetnx("pythonsdk_hset002", "some6", "v7")
# result = redis_module.redis_clients["pysdk_resource_id_02"].ltrim("pythonsdk_list002", 0, 3)


# result = redis_module.redis_clients["pysdk_resource_id_02"].get("pythonsdk_get001")
# result = redis_module.redis_clients["pysdk_resource_id_02"].set("pythonsdk_get009", "val0018", "xx")

# result = redis_module.redis_clients["pysdk_resource_id_02"].set("pythonsdk_get0099", "val0019", "nx")

# result = redis_module.redis_clients["pysdk_resource_id_02"].delete()

# result = redis_module.redis_clients["pysdk_resource_id_02"].exists("pythonsdk_get001")

# result = redis_module.redis_clients["pysdk_resource_id_02"].mget

# result = redis_module.redis_clients["pysdk_resource_id_02"].set("setkeyfor4param", "valuefor4param", "px", 10000,"xx")

# result = redis_module.redis_clients["pysdk_resource_id_02"].get("setkeyfor4param")

# result = redis_module.redis_clients["pysdk_resource_id_02"].mset("msetkey001", "msetvalue001", "msetkey001","msetkey002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].mset("user:{user1}", "value1", "user:{user2}", "value2", "user:{user3}","value3")

# result = redis_module.redis_clients["pysdk_resource_id_02"].get("msetkey001")

# result = redis_module.redis_clients["pysdk_resource_id_02"].setbit("msetkey001", 100, 1)

# result = redis_module.redis_clients["pysdk_resource_id_02"].getbit("msetkey0011", 110)

# result = redis_module.redis_clients["pysdk_resource_id_02"].strlen("msetkey001")


# result = redis_module.redis_clients["pysdk_resource_id_02"].hdel("pythonsdk_hset002", "qq","qqqs")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sadd("pythonsdk_set002", "one","two","one", "two")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sadd("pythonsdk_set003", "one","two","three")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sdiff("pythonsdk_set003", "pythonsdk_set002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sadd("prefix:\{pythonsdk_set002\}", "one","two","one", "two")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sadd("prefix:\{pythonsdk_set003\}", "one","two","three")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sdiff("prefix:\{pythonsdk_set002\}")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sismember("pythonsdk_set0031", "one1")

# result = redis_module.redis_clients["pysdk_resource_id_02"].smembers("pythonsdk_set003")

# result = redis_module.redis_clients["pysdk_resource_id_02"].smove("pythonsdk_set003", "pythonsdk_set002", "one")

# result = redis_module.redis_clients["pysdk_resource_id_02"].smembers("pythonsdk_set003")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sadd("\{pythonsdk_set002\}:qq", "one","two","zero","two")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sadd("\{pythonsdk_set002\}:pp", "one","two","three")

# result = redis_module.redis_clients["pysdk_resource_id_02"].sdiff("\{pythonsdk_set002\}:pp1", "\{pythonsdk_set002\}:qq1")


# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:001", 100, "val1")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:002", 100.11, "val2")
# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:002", 100.21, "val1")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zinterstore("\{pythonsdk_z002\}:003", 2, "\{pythonsdk_z002\}:001", "\{pythonsdk_z002\}:002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrange("\{pythonsdk_z002\}:003", 0, -1, 'withscores')

# result = redis_module.redis_clients["pysdk_resource_id_02"].zunionstore("\{pythonsdk_z002\}:004", 2, "\{pythonsdk_z002\}:001", "\{pythonsdk_z002\}:002")
# result = redis_module.redis_clients["pysdk_resource_id_02"].zrange("\{pythonsdk_z002\}:004", 0, -1, 'withscores')

# result = redis_module.redis_clients["pysdk_resource_id_02"].zcount("\{pythonsdk_z002\}:004", "0", "250")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zincrby("\{pythonsdk_z002\}:004", 2.5, "val1")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrangebyscore("\{pythonsdk_z002\}:004", "0", "150")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrank("\{pythonsdk_z002\}:004", "val1")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrank("\{pythonsdk_z002\}:004", "val1")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:004", 700.21, "val7")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:004", 800.21, "val8")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:004", 900.21, "val9")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:004", 1000.21, "val10")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zadd("\{pythonsdk_z002\}:004", 1100.21, "val11")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zremrangebyrank("\{pythonsdk_z002\}:004", 2, 3)

# result = redis_module.redis_clients["pysdk_resource_id_02"].zremrangebyscore("\{pythonsdk_z002\}:004", 1000, 1200)

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrevrange("\{pythonsdk_z002\}:004", 0, -1, "withscores")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrevrangebyscore("\{pythonsdk_z002\}:004", 1200, 0)

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrevrank("\{pythonsdk_z002\}:004", "val7")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrevrank("\{pythonsdk_z002\}:004", "val7")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zscore("\{pythonsdk_z002\}:004", "val8")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zunionstore("\{pythonsdk_z002\}:006", 2, "\{pythonsdk_z002\}:001", "\{pythonsdk_z002\}:002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrevrange("\{pythonsdk_z002\}:006", 0, -1, "withscores")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zinterstore("\{pythonsdk_z002\}:007", 2, "\{pythonsdk_z002\}:001", "\{pythonsdk_z002\}:002")

# result = redis_module.redis_clients["pysdk_resource_id_02"].zrevrange("\{pythonsdk_z002\}:007", 0, -1, "withscores")
# result = redis_module.redis_clients["49d0eebf34d540a788377135b11bfb7f"].zrevrange("\{pythonsdk_z002\}:007", 0, -1, "withscores")

# result = redis_module.redis_clients["49d0eebf34d540a788377135b11bfb7f"].zadd("\{pythonsdk_z002\}:004", 1100.21, "val11")

# result = redis_module.redis_clients["49d0eebf34d540a788377135b11bfb7f"].zadd("\{pythonsdk_z002\}:004", 1200.21, "val12")

# result = redis_module.redis_clients["49d0eebf34d540a788377135b11bfb7f"].zrangebyscore("\{pythonsdk_z002\}:004", 0, 1200)

# redis_module.redis.set_timeout((10, 20))
# result = redis_module.redis.zrangebyscore("\{pythonsdk_z002\}:004", 0, 1200)

# result = redis_module.redis.mset("\{same_slot\}:commonset002", "val002","\{same_slot\}:commonset003", "val003")

# result = redis_module.redis.mget("\{same_slot\}:commonset002", "\{same_slot\}:commonset002.5","\{same_slot\}:commonset003", "\{same_slot\}:commonset004")


# result = redis_module.delete("pythonsdk_hset002", "f04")
# result = redis_module.hget("pythonsdk_hset002", "f04")
# result = redis_module.hset("pythonsdk_hset002", "f04", "v04")

# redis_module.set_timeout((0.1,0.1))
# result = redis_module.type("pythonsdk_hset002")


# result = redis_module.redis.hget("pythonsdk_hset002", "f04")

# result = redis_module.set("setxxx", "f04")

# result = redis_module.sadd("pythonsdk_set00_0221", "one1","two1","one2", "two2")

# result = redis_module.smembers("pythonsdk_set00_0221")

# result = redis_module.srandmember("pythonsdk_set00_0221",2)

# result = redis_module.srem("pythonsdk_set00_0221","one")

# result = redis_module.spop("pythonsdk_set00_0221", 3)

# result = redis_module.smembers("pythonsdk_set00_0221")

# result = redis_module.setex("pythonsdk_somek00_0221", 10, "somev")

# result = redis_module.setnx("pythonsdk_somek02_0221", "qqq")

# .hmset("pythonsdk_hset002", "some3", "v3", "some4", "v4")

# result = redis_module.hmset("pythonsdk_hset002222", "some3", "v3", "some4", "v4")
# result = redis_module.hset("pythonsdk_hset002223", "some3", "v3")

# result = redis_module.setbit("pythonsdk_setbit002223", 3, 1)

# result = redis_module.hget("pythonsdk_hset002223", "some3")

# result = redis_module.hdel("pythonsdk_hset002223", "some3")

# result = redis_module.incr("pythonsdk_incr0227")

# result = redis_module.zunionstore("\\{pythonsdk_z002\\}:007", 2, "\\{pythonsdk_z002\\}:001", "\\{pythonsdk_z002\\}:002")

# result = redis_module.zunionstore("\{pythonsdk_z002\}:006", 2, "\{pythonsdk_z002\}:001", "\{pythonsdk_z002\}:002")

# pythonsdk_z002="qqq"
# result = redis_module.zunionstore("{pythonsdk_z002}:013", 2, "\{pythonsdk_z002\}:001", "\{pythonsdk_z002\}:002")

# result = redis_module.zadd("\{pythonsdk_z002\}:001", 400, "val4")

# result = redis_module.zadd("\{pythonsdk_z002\}:002", 300, "val3")

# result = redis_module.zunionstore("{pythonsdk_z003}:014", 2, "{pythonsdk_z003}:001", "{pythonsdk_z003}:002")

# result = redis_module.zadd("{pythonsdk_z003}:001", 400, "val4")

# result = redis_module.zadd("{pythonsdk_z003}:002", 300, "val3")

# result = redis_module.sdiff("prefix:{pythonsdk_set002}:key1", "prefix:{pythonsdk_set002}:key2")

# pythonsdk_set002="qqq"
# result = redis_module.sunion("prefix:{pythonsdk_set002}:key1", "prefix:{pythonsdk_set002}:key2")

# result = redis_module.sadd("prefix:{pythonsdk_set002}:key1", "one","two","one", "two")

# result = redis_module.sadd("prefix:{pythonsdk_set002}:key2", "one","two","three")

result = redis_module.zrange("\{pythonsdk_z002\}:001", 0, -1, 'withscores')

# result = redis_module.zrangebyscore("\{pythonsdk_z002\}:001", 0, 1000)

# result = redis_module.zrem("\{pythonsdk_z002\}:001", "val4", "val3")

# result = redis_module.zremrangebyrank("\{pythonsdk_z002\}:001", 0, 1)

# result = redis_module.zrevrange("\{pythonsdk_z002\}:001", 0, -1, 'withscores')

# result = redis_module.zrevrangebyscore("\{pythonsdk_z002\}:001", 880, 100)

print("result", result)
