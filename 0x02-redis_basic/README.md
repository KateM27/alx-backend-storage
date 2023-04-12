## 0x02. Redis basic

- Use redis for basic operations and as a simple cache

**Install Redis on Ubuntu**
```
sudo apt-get -y install redis server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

Start the redis server with `service redis-server start`

Connect to Redis with `redis-cli`

**Resources**
- [Redis commands](https://redis.io/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to use Redis with Python](https://realpython.com/python-redis/)
- [Redis crash course tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
