windows use nt authority/system account to run powershell.
use cmd cd `D:\\Installs\\pstools `


```shell
psexec -i -s cmd.exe
# start in new window, system level cmd
whoami
# should be system now.
```