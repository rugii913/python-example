# 방법 1. import [패키지명].[모듈명]
import unit.character
unit.character.test()

# 방법 2. from [패키지명] import [모듈명] → 더 많이 사용하는 방법
from unit import item
item.test()

# 방법 3. from [패키지명] import * - 해당 패키지에 __init__.py 추가 및 import 대상 모듈 작성 필요
from unit import *
monster.test()

# 방법 4. import [패키지명] - 해당 패키지에 __init__.py 추가 및 import 대상 모듈 작성 필요
import unit
unit.monster.test()
