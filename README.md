파이썬 가상 환경 사용해 보기
[1] 가상 환경 디렉터리 생성하기
윈도우에서 명령 프롬프트를 실행하고 다음 명령어를 입력해 C:/venvs라는 디렉터리를 만들자.

루트 디렉터리를 반드시 C:/venvs로 해야 하는 것은 아니지만 실습 편의를 위해 이대로 지정하자.

[명령 프롬프트]

C:\Users\pahkey> cd \
C:\> mkdir venvs
C:\> cd venvs
[2] 가상 환경 만들기
파이썬 가상 환경을 만드는 다음 명령어를 입력해 실행하자.

[명령 프롬프트]

C:\venvs> python -m venv mysite
명령에서 python -m venv는 파이썬 모듈 중 venv라는 모듈을 사용한다는 의미다. 그 뒤의 mysite는 여러분이 생성할 가상 환경의 이름이다. 가상 환경의 이름을 반드시 mysite로 지을 필요는 없다. 만약 가상 환경의 이름을 awesomesite와 같이 지정했다면 책에 등장하는 mysite라는 가상 환경 이름을 awesomesite로 대체하여 읽으면 된다.

하지만 실습 진행의 편의를 위해 가상 환경 이름을 동일하게 하기를 권장한다.

명령을 잘 수행했다면 C:/venvs 디렉터리 아래에 mysite라는 디렉터리가 생성되었을 것이다. 이 디렉터리를 가상 환경이라 생각하면 된다. 그런데 가상 환경을 만들었다 해서 바로 가상 환경을 사용할 수는 없다. 가상 환경을 사용하려면 가상 환경에 진입해야 한다.

[3] 가상 환경에 진입하기
가상 환경에 진입하려면 우리가 생성한 mysite 가상 환경에 있는 Scripts 디렉터리의 activate 명령을 수행해야 한다. 다음 명령을 입력하여 mysite 가상 환경에 진입해 보자.

[명령 프롬프트]

C:\venvs>cd C:\venvs\mysite\Scripts
C:\venvs\mysite\Scripts> activate
(mysite) C:\venvs\mysite\Scripts>
그러면 C:/ 왼쪽에 (mysite)라는 프롬프트를 확인할 수 있다. 이름에서 볼 수 있듯 현재 여러분이 진입한 가상 환경을 의미한다.

[4] 가상 환경에서 벗어나기
현재 진입한 가상 환경에서 벗어나려면 deactivate라는 명령을 실행하면 된다. 이 명령은 어느 위치에서 실행해도 상관없다.

[명령 프롬프트]

(mysite) C:\venvs\mysite\Scripts> deactivate
가상 환경에서 벗어났다면 C:/ 왼쪽에 있던 (mysite)라는 프롬프트가 사라졌을 것이다. 지금까지 가상 환경의 개념과 실습을 진행해 보았다. 가상 환경이라는 개념이 조금은 생소하겠지만 익혀 두면 여러분의 웹 프로그래밍 경험에 도움이 될 것이다.

장고 설치하기
드디어 장고를 설치할 차례가 왔다. 앞에서 만든 mysite 가상 환경에 장고를 설치해 보자.

[1] 가상 환경인지 확인하기
명령 프롬프트 왼쪽에 (mysite) 프롬프트가 보이는지 확인하자. 만약 명령 프롬프트 왼쪽에 (mysite) 프롬프트가 보이지 않는다면 바로 이전의 실습을 참고하여 가상 환경에 진입한 상태에서 장고 설치를 진행하자.

[명령 프롬프트]

C:\venvs\mysite\Scripts> activate
(mysite) C:\venvs\mysite\Scripts>
[2] 가상 환경에서 장고 설치하기
mysite 가상 환경에 진입한 상태에서 pip install django==3.1.3 명령을 입력하자. pip은 파이썬 라이브러리를 설치하고 관리해 주는 파이썬 도구이다. pip install django==3.1.3는 pip으로 장고 3.1.3 버전을 설치하는 명령이라고 생각하면 된다. 다음 화면이 나오면 장고 설치가 잘 된 것이다.

- 가상 환경 진입은 바로 이전 실습에서 공부했다.
- pip은 '핍'이라 읽는다.

[명령 프롬프트]

(mysite) C:\venvs\mysite\Scripts> pip install django==3.1.3
Collecting django
  Using cached https://files.pythonhosted.org/packages/01/a5/fb3dad18422fcd4241d18460a1fe17542bfdeadcf74e3861d1a2dfc9e459/Django-3.1.3-py3-none-any.whl
Collecting asgiref~=3.2.10 (from django)
  Using cached https://files.pythonhosted.org/packages/d5/eb/64725b25f991010307fd18a9e0c1f0e6dff2f03622fc4bcbcdb2244f60d6/asgiref-3.2.10-py3-none-any.whl
Collecting sqlparse>=0.2.2 (from django)
  Using cached https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl
Collecting pytz (from django)
  Using cached https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl
Installing collected packages: asgiref, sqlparse, pytz, django
Successfully installed asgiref-3.2.10 django-3.1.3 pytz-2020.1 sqlparse-0.3.1

WARNING: You are using pip version 19.2.3, however version 20.2.3 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
그런데 마지막에 경고(WARNING) 문구가 보인다. pip이 최신 버전이 아니라는 내용이다.

개발자가 되고 싶다면 이런 경고 문구에 익숙해져야 한다.

[3] pip 최신 버전으로 설치하기
경고 메시지에 따라 python -m pip install --upgrade pip 명령을 입력해 pip을 최신 버전으로 설치하자.

[명령 프롬프트]

(mysite) C:\venvs\mysite\Scripts> python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl (1.4MB)
     |================================| 1.4MB 226kB/s
Installing collected packages: pip
  Found existing installation: pip 19.2.3
    Uninstalling pip-19.2.3:
      Successfully uninstalled pip-19.2.3
Successfully installed pip-20.0.2



mysite 가상 환경에 간단히 진입하기
mysite 가상 환경에 진입하려면 매번 명령 프롬프트를 실행하고 C:/venvs/mysite/Scripts 디렉터리로 이동하여 activate 명령을 수행해야 한다. 이런 일련의 과정을 한 번에 수행할 수 있는 배치 프로그램을 만들어 귀찮음을 덜어 보자.

[1] mysite.cmd 배치 파일 생성하기
mysite.cmd 파일을 venvs 디렉터리에 만들고 다음과 같이 작성하여 저장하자. 확장자 .cmd가 붙은 파일은 배치(batch) 파일이라 부르며, 명령어 입력과 실행을 한 번에 해주는 파일이라 생각하면 된다.

[파일 이름: C:/venvs/mysite.cmd]

@echo off
cd c:/projects/mysite
c:/venvs/mysite/scripts/activate
배치 파일의 내용은 C:/projects/mysite 디렉터리로 이동한 다음, C:/venvs/mysite/scripts/activate 명령을 수행하라는 뜻이다.

[2] 배치 파일 위치를 PATH 환경 변수에 추가하기
이 배치 파일이 명령 프롬프트 어느 곳에서나 수행될 수 있도록 C:/venvs 디렉터리를 시스템의 환경 변수 PATH에 추가해야 한다. 먼저 <윈도우키+R> 키를 입력하여 다음처럼 sysdm.cpl 명령을 입력한 다음 <확인>을 누르자.



그러면 다음과 같은 '시스템 속성' 창이 나타난다. 여기서 <고급> 탭을 선택하고 <환경 변수> 버튼을 누르자.



그러면 다음과 같은 '환경 변수' 창이 나타난다. 여기서 사용자 변수 중 <Path>를 선택하고 <편집> 버튼을 누르자.



그러면 다음과 같은 '환경 변수 편집' 창이 나타난다. 여기서 <새로 만들기> 버튼을 누르자.



그리고 다음 그림처럼 C:/venvs라는 디렉터리를 추가하고 <확인> 버튼을 누르자.



마지막으로 다음 '환경 변수' 창에서 <확인> 버튼을 누르자.

[3] PATH 환경 변수 확인하기
이렇게 하면 환경 변수 PATH에 C:/venvs 디렉터리가 추가되어 mysite.cmd 명령을 어디서든 실행할 수 있다. 명령 프롬프트를 다시 시작하자(그래야 변경된 환경 변수 PATH가 제대로 반영된다). 그리고 set path 명령을 실행하여 변경된 환경 변수 PATH의 내용을 확인해 보자. C:/venvs라는 디렉터리가 환경 변수 PATH에 포함되어 있으면 된다.

[명령 프롬프트]

C:\Users\pahkey>set path
Path=C:\Windows\system32; (... 생략 ...) ;C:\venvs
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
[4] 배치 파일 실행하여 가상 환경에 진입하기
이제 지금까지 만든 mysite 명령(배치 파일 이름)을 실행하여 가상 환경에 잘 진입하는지 확인해 보자. 참고로 윈도우에서 확장자가 .cmd인 파일은 확장자를 빼고 입력해도 된다.

[명령 프롬프트]

C:\Users\pahkey> mysite
(mysite) C:\projects\mysite>
맥 OS에서 가상 환경 진입하기

맥을 사용할 경우 mysite.cmd 대신 다음처럼 mysite.sh을 작성한다.

[파일 이름: /Users/pahkey/venvs/mysite.sh]

#!/bin/bash

cd /Users/pahkey/projects/mysite
source /Users/pahkey/venvs/mysite/bin/activate
그리고 맥 터미널에서 mysite.sh을 다음과 같이 수행하자.

$ /Users/pahkey/venvs/mysite.sh
