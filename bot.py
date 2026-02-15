 $ python bot.py
Bot running...
Network Retry Loop (Bootstrap Initialize Application): Invalid token. Aborting retry loop.
Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 856, in initialize
    await self.get_me()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_extbot.py", line 2007, in get_me
    return await super().get_me(
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 989, in get_me
    result = await self._post(
             ^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 703, in _post
    return await self._do_post(
           ^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_extbot.py", line 369, in _do_post
    return await super()._do_post(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 732, in _do_post
    result = await request.post(
             ^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/request/_baserequest.py", line 198, in post
    result = await self._request_wrapper(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/request/_baserequest.py", line 375, in _request_wrapper
    raise exception
telegram.error.InvalidToken: Unauthorized

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_utils/networkloop.py", line 161, in network_retry_loop
    await do_action()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_utils/networkloop.py", line 136, in do_action
    await action_cb()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_application.py", line 489, in initialize
    await self.bot.initialize()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_extbot.py", line 315, in initialize
    await super().initialize()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 859, in initialize
    raise InvalidToken(f"The token `{self._token}` was rejected by the server.") from exc
telegram.error.InvalidToken: The token `8564896742:AAEvCnYgNWpJ49qsXWzmTbStzicbV5Bx6MQM` was rejected by the server.
Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 856, in initialize
    await self.get_me()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_extbot.py", line 2007, in get_me
    return await super().get_me(
           ^^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 989, in get_me
    result = await self._post(
             ^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 703, in _post
    return await self._do_post(
           ^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_extbot.py", line 369, in _do_post
    return await super()._do_post(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 732, in _do_post
    result = await request.post(
             ^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/request/_baserequest.py", line 198, in post
    result = await self._request_wrapper(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/request/_baserequest.py", line 375, in _request_wrapper
    raise exception
telegram.error.InvalidToken: Unauthorized

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/data/data/com.termux/files/home/bot.py", line 30, in <module>
    app.run_polling()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_application.py", line 839, in run_polling
    return self.__run(
           ^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_application.py", line 1054, in __run
    loop.run_until_complete(self._bootstrap_initialize(max_retries=bootstrap_retries))
  File "/data/data/com.termux/files/usr/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_application.py", line 1014, in _bootstrap_initialize
    await network_retry_loop(
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_utils/networkloop.py", line 161, in network_retry_loop
    await do_action()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_utils/networkloop.py", line 136, in do_action
    await action_cb()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_application.py", line 489, in initialize
    await self.bot.initialize()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/ext/_extbot.py", line 315, in initialize
    await super().initialize()
  File "/data/data/com.termux/files/usr/lib/python3.12/site-packages/telegram/_bot.py", line 859, in initialize
    raise InvalidToken(f"The token `{self._token}` was rejected by the server.") from exc
telegram.error.InvalidToken: The token `8564896742:AAEvCnYgNWpJ49qsXWzmTbStzicbV5Bx6MQM` was rejected by the server.
~ $ nano bot.py
~ $ python bot.py
Bot running...
