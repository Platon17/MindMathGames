import asyncio
from aiogram.fsm.storage.redis import Redis
import json
async def save(redis, key, value):
    await redis.set(key, value)


async def load(redis, key):
    return await redis.get(key)
async def main():
    test_dict ={'test1':
                   {'test11':'val11',
                    'test12':'val12'
                    },
               'test2':
                   {'test21': 'val21',
                    'test22': 'val22'
                    }
                }
    json_str = json.dumps(test_dict)
    await save(redis,'test_dict',json_str)
    s = await load(redis,'test_dict')
    d = json.loads(s)
    pass


if __name__ == "__main__":
    redis = Redis(host='localhost')
    asyncio.run(main())