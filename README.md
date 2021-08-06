# welc0me 2 lazy microcontroller lib boii

you can use this lib both micropython or circuitpython<br/>
ez as fuk for lazy ppl like me not you matarfakar!

```python
from lib.io import p_digitalOut, p_digitalIn, p_analogIn, p_sleep

btn0 = p_digitalIn(3)
btn1 = p_digitalIn(4, 'up') #PULL_UP
btn2 = p_digitalIn(5, 'down') #PULL_DOWN
btn0.p_read()
btn1.p_read()
btn2.p_read()

led0 = p_digitalOut(2)
led0.p_read()
led0.p_high()
led0.p_low()

ana = p_analogIn(36)
ana.p_read()

p_sleep(1)
```
