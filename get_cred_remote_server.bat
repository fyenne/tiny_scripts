setlocal
%@Try%
call conda activate siming
echo ------------activated conda env----------------                       
call python "C:\Users\SRV-USAMYAN\Documents\My SugarSync\tiny_scirpts\get_cred_remote_server.py"
%@EndTry%
:@Catch
echo --failed--
:@EndCatch
timeout 4