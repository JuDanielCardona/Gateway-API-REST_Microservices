from flask import Flask, json

import asyncio
import nats

async def sendLog(log):
    try:
        log_dict = {
            "app_name": log.app_name,
            "log_type": log.log_type,
            "module": log.module,
            "log_date_time": log.log_date_time,
            "summary": log.summary,
            "description": log.description
        }

        log_json = json.dumps(log_dict)

        nc = await nats.connect("nats://localhost:4222")
        await nc.publish("ProfilesServer", log_json.encode())
        await nc.flush()
        await nc.close()
        print("Log sended.")
    except Exception as e:
        print("Error:", e)