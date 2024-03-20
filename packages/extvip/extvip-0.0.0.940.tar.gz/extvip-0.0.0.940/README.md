# Extvip.
<img src="https://img.shields.io/pypi/v/extvip?style=for-the-badge&logo=python">
<img alt="followers" src="https://img.shields.io/github/followers/antilagg?color=f429ff&style=for-the-badge&logo=github&label=Follow"/>

```less
                > Custom Console Going To Be Used For My Projects
                    And Available To Anyone Else Who Wants To Use <
```

---

### Installation
```
! package NOT FULLY available for non-personal use !
~ use at the knowledge of knowing it may be buggy ~

pip install extvip
```

### Usage
```py
# default shit if u want to only import for ease - auto switches #

from extvip import printf as print, inputf as input, init

init(debug=False)

print("[DEBUG] Should NOT Show")
print("(~) Should NOT Show")
print("[INFO] Should Show")
print("(*) Should Show")

# --------------------------------------------------------- #
# log format: [21:14:38] INF > test

from extvip import log

log.info(
    "info",
    sep=">" # separator OPTIONAL
)
log.error("error")
log.fatal("fatal")
log.success("success")
log.debug("debug")

log.log("Retrieved", code="6969")
log.vert("test", test=True, madeby="antilagvip")

# --------------------------------------------------------- #
# this is for custom cool stuff as seen here: 

import time
from extvip import BetaConsole

c = BetaConsole(speed=2)

while True:
    try:
        timestamp = c.getTimestamp()
        c.alphaPrint("[INF]", f"[{timestamp}] made by antilagvip :D", increment=False)
        time.sleep(0.001)
    except KeyboardInterrupt: exit(0)
```

---

## * [antilagvip@discord](https://discord.com/users/824027700851245138) | [antilagg@github](https://github.com/antilagg) | [antilag.dev](https://antilag.dev) *