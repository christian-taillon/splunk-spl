
## DNS Record Lookup
`sourcetype=DnsRequestV4* DomainName= <dns>`

## CrowdStrike search for meainingful User logins
`index=main ComputerName=* sourcetype="UserLogonV8-v02"
    NOT UserName IN ("DWM*","UMFD*")
    NOT LogonType_decimal IN (0,5)
| eval logon_type = case(LogonType_decimal==2,"Interactive",
    LogonType_decimal==3,"Network",
    LogonType_decimal==4,"BATCH",
    LogonType_decimal==5,"service",
    LogonType_decimal==6,"Proxy",
    LogonType_decimal==7,"Unlock",
    LogonType_decimal==8,"Network_Clearatext",
    LogonType_decimal==9,"New_credentials",
    LogonType_decimal==10,"Remote Interfactive",
    LogonType_decimal==11,"cached_interactive",
    LogonType_decimal==12,"cached_remote_interactive",
    LogonType_decimal==13,"Cached_unlock",
    1==1,"error")
| eval IP4 = coalesce(RemoteAddressIP4, LocalAddressIP4)
| table _time UserName logon_type IP4 ComputerName
`

## Encoded PowerShell
`event_simpleName=ProcessRollup2 FileName=powershell.exe CommandLine IN (*-enc*,*encoded*)`

## Improper Local System Account Usage
`event_simpleName="ProcessRollup2" FileName IN (w3wp.exe,sqlservr.exe,httpd.exe,nginx.exe) UserName="LOCAL SYSTEM"`

## Renamed Executable Execution
`event_simpleName="NewExecutableRenamed"
| rename TargetFileName as ImageFileName
| join ImageFileName
    [ search event_simpleName="ProcessRollup2" ]
| table ComputerName SourceFileName ImageFileName CommandLine`


## LOL Binaries with Network
`event_simpleName="DnsRequest"
| rename ContextProcessId as TargetProcessId
| join TargetProcessId
    [ search event_simpleName="ProcessRollup2" FileName IN (Atbroker.exe , Bash.exe , Bitsadmin.exe , Certutil.exe , Cmd.exe , Cmstp.exe , Control.exe , Cscript.exe , Csc.exe , Dfsvc.exe , Diskshadow.exe , Dnscmd.exe , Esentutl.exe , Eventvwr.exe , Expand.exe , Extexport.exe , Extrac32.exe , Findstr.exe , Forfiles.exe , Ftp.exe , Gpscript.exe , Hh.exe , Ie4uinit.exe , Ieexec.exe , Infdefaultinstall.exe , Installutil.exe , Jsc.exe , Makecab.exe , Mavinject.exe , Mmc.exe , Msconfig.exe , Msdt.exe , Mshta.exe , Msiexec.exe , Odbcconf.exe , Pcalua.exe , Pcwrun.exe , Presentationhost.exe , Print.exe , Regasm.exe , Regedit.exe , Register-cimprovider.exe , Regsvcs.exe , Regsvr32.exe , Reg.exe , Replace.exe , Rpcping.exe , Rundll32.exe , Runonce.exe , Runscripthelper.exe , Schtasks.exe , Scriptrunner.exe , Sc.exe , SyncAppvPublishingServer.exe , Verclsid.exe , Wab.exe , Wmic.exe , Wscript.exe , Wsreset.exe , Xwizard.exe) ]`
