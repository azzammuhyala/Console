#kali.linux
#func:
import os
import time
import traceback

def clear_kali():
  os.system('cls' if os.name == 'nt' else 'clear'); print()

def func_main():
  try:
    name_kali = input("Your Name Kali. (Original: kali): ")[:25]
    device_kali = input("Your Device Kali. (Original: kali): ")[:40]
  except KeyboardInterrupt:
    print("\033[33mYou just terminated the program.\033[0m")
  except EOFError:
    print("\033[33mYou just terminated the program.\033[0m")
  except:
    print("\033[33mYou just terminated the program.\033[0m")
  if name_kali.isidentifier():
    touch_file = []
    dirs_name_to = []
    fuck_str = ''
    join_dirs = fuck_str + "/".join(dirs_name_to)
    add_slash = '/' if join_dirs else ''
    ori_colorBC = f"\033[36m┌──(\033[34m{name_kali}㉿{device_kali}\033[36m)-[\033[0m~{add_slash + join_dirs}\033[36m]\n└─$ \033[0m"
    ori_defaultW = f"┌──({name_kali}㉿{device_kali})-[~{add_slash + join_dirs}]\n└─$ "
    win_defaultKL = f"\033[94m┌──(\033[91m{name_kali}㉿{device_kali}\033[94m)-[\033[0m~{add_slash + join_dirs}\033[94m]\n└─\033[91m# \033[0m"
    inp_text_kali = ori_colorBC
    neoOS = "Kali GNU/Linux Rolling on Windows 10 x86_64"
    neoKernel = "4.4.0-17763-Microsoft"
    neoUptime = "10 mins"
    neoPackages = "209 (dpkg)"
    neoShell = "bash 4.4.23"
    neoTerminal = "/dev/tty1"
    neoCPU = "Intel i7-2600K (3) @ 3.411GHz"
    neoMemory = "2207MiB / 4095MiB"
    clear_kali()
    while True:
      try:
        print(join_dirs)
        kali_inp = input(inp_text_kali)
        if kali_inp:
          if kali_inp == "exit":
            break
          elif kali_inp == "clear":
            clear_kali()
          elif kali_inp == "console.py > fake-kali.linux > input > kali.Reset":
            clear_kali()
            inp_text_kali = ori_colorBC
          elif kali_inp == "console.py > fake-kali.linux > color input > kali.white":
            clear_kali()
            inp_text_kali = ori_defaultW
          elif kali_inp == "console.py > fake-kali.linux > input > kali.win":
            clear_kali()
            inp_text_kali = win_defaultKL
          elif kali_inp == "console.py > fake-kali.linux > neofetch.set":
            print("\033[33mpress 'Enter' if use original.\n\033[0m")
            inpNEOos = input("(Original: 'Kali GNU/Linux Rolling on Windows 10 x86_64') OS: ")
            if inpNEOos == "":
              neoOS
            else:
              neoOS = f"{inpNEOos}"
            inpNEOkernel = input("(Original: '4.4.0-17763-Microsoft') Kernel: ")
            if inpNEOkernel == "":
              neoKernel
            else:
              neoKernel = f"{inpNEOkernel}"
            inpNEOuptime = input("(Original: '10 mins') Uptime: ")
            if inpNEOuptime == "":
              neoUptime
            else:
              neoUptime = f"{inpNEOuptime}"
            inpNEOpackages = input("(Original: '209 (dpkg)') Packages: ")
            if inpNEOpackages == "":
              neoPackages
            else:
              neoPackages = f"{inpNEOpackages}"
            inpNEOshell = input("(Original: 'bash 4.4.23') Shell: ")
            if inpNEOshell == "":
              neoShell
            else:
              neoShell = f"{inpNEOshell}"
            inpNEOterminal = input("(Original: '/dev/tty1') Terminal: ")
            if inpNEOterminal == "":
              neoTerminal
            else:
              neoTerminal = f"{inpNEOterminal}"
            inpNEOcpu = input("(Original: 'Intel i7-2600K (3) @ 3.411GHz') CPU: ")
            if inpNEOcpu == "":
              neoCPU
            else:
              neoCPU = f"{inpNEOcpu}"
            inpNEOmemory = input("(Original: '2207MiB / 4095MiB') Memory: ")
            if inpNEOmemory == "":
              neoMemory
            else:
              neoMemory = f"{inpNEOmemory}"
            print("\033[32mSET 'neofetch' has fully change\n\033[0m")
          elif "neofetch" in kali_inp:
            time.sleep(2.4)
            line_name = len(name_kali) + 1 + len(device_kali)
            print(r"""..............                                      """ + "\033[34m" + f"\033[34m{name_kali}\033[0m@\033[34m{device_kali}" + r"""
            ..,;:ccc,.                              """ + "\033[0m-\033[34m" * line_name + r"""
          ......''';lxO.                            """ + f"\033[0mOS: {neoOS}\033[34m" + r"""
.....''''..........,:ld;                            """ + f"\033[0mKernel: {neoKernel}\033[34m" + r"""
           .';;;:::;,,.x,                           """ + f"\033[0mUptime: {neoUptime}\033[34m" + r"""
      ..'''.            0Xxoc:,.  ...               """ + f"\033[0mPackages: {neoPackages}\033[34m" + r"""
  ....                ,ONkc;,;cokOdc',.             """ + f"\033[0mShell: {neoShell}\033[34m" + r"""
 .                   OMo           ':""" + "\033[34m" + "\033[90mdd\033[34m" + r"""o.           """ + f"\033[0mTerminal: {neoTerminal}\033[34m" + r"""
                    dMc               :OO;          """ + f"\033[0mCPU: {neoCPU}\033[34m" + r"""
                    0M.                 .:o.        """ + f"\033[0mMemory: {neoMemory}\033[34m" + r"""
                    ;Wd
                     ;XO,                             """ + "\033[34m\033[31m\033[7m   " + "\033[0m\033[32m\033[7m   " + "\033[0m\033[33m\033[7m   " + "\033[0m\033[34m\033[7m   " + "\033[0m\033[35m\033[7m   " + "\033[0m\033[36m\033[7m   " + "\033[0m\033[37m\033[7m   \033[0m\033[34m" + r"""
                       ,d0Odlc;,..
                        ..',;:cdOOd::,.
                                 .:d;.':;.
                                    'd,  .'
                                      ;l   ..
                                       .o
                                         c
                                         .'
                                          .
""" + "\033[0m")
          elif "echo " in kali_inp:
            print(output_text[5:])
          elif 'echo "' in kali_inp:
            output_text = kali_inp[6:]
            print(output_text[:-1])
          elif "echo '" in kali_inp:
            output_text = kali_inp[6:]
            print(output_text[:-1])
          elif "whoami" in kali_inp:
            print(f"{name_kali}")
          elif "help" in kali_inp:
            print(r"""GNU bash, version 5.1.16(1)-release (x86_64-pc-linux-gnu)
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
Use `info bash' to find out more about the shell in general.
Use `man -k' or `info' to find out more about commands not in this list.

A star (*) next to a name means that the command is disabled.

 job_spec [&]                                                                                                            history [-c] [-d offset] [n] or history -anrw [filename] or history -ps arg [arg...]
 (( expression ))                                                                                                        if COMMANDS; then COMMANDS; [ elif COMMANDS; then COMMANDS; ]... [ else COMMANDS; ] fi
 . filename [arguments]                                                                                                  jobs [-lnprs] [jobspec ...] or jobs -x command [args]
 :                                                                                                                       kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]
 [ arg... ]                                                                                                              let arg [arg ...]
 [[ expression ]]                                                                                                        local [option] name[=value] ...
 alias [-p] [name[=value] ... ]                                                                                          logout [n]
 bg [job_spec ...]                                                                                                       mapfile [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [array]
 bind [-lpsvPSVX] [-m keymap] [-f filename] [-q name] [-u name] [-r keyseq] [-x keyseq:shell-command] [keyseq:readline>  popd [-n] [+N | -N]
 break [n]                                                                                                               printf [-v var] format [arguments]
 builtin [shell-builtin [arg ...]]                                                                                       pushd [-n] [+N | -N | dir]
 caller [expr]                                                                                                           pwd [-LP]
 case WORD in [PATTERN [| PATTERN]...) COMMANDS ;;]... esac                                                              read [-ers] [-a array] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t timeout] [-u fd] [name ...]
 cd [-L|[-P [-e]] [-@]] [dir]                                                                                            readarray [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [array]
 command [-pVv] command [arg ...]                                                                                        readonly [-aAf] [name[=value] ...] or readonly -p
 compgen [-abcdefgjksuv] [-o option] [-A action] [-G globpat] [-W wordlist] [-F function] [-C command] [-X filterpat] >  return [n]
 complete [-abcdefgjksuv] [-pr] [-DEI] [-o option] [-A action] [-G globpat] [-W wordlist] [-F function] [-C command] [>  select NAME [in WORDS ... ;] do COMMANDS; done
 compopt [-o|+o option] [-DEI] [name ...]                                                                                set [-abefhkmnptuvxBCHP] [-o option-name] [--] [arg ...]
 continue [n]                                                                                                            shift [n]
 coproc [NAME] command [redirections]                                                                                    shopt [-pqsu] [-o] [optname ...]
 declare [-aAfFgiIlnrtux] [-p] [name[=value] ...]                                                                        source filename [arguments]
 dirs [-clpv] [+N] [-N]                                                                                                  suspend [-f]
 disown [-h] [-ar] [jobspec ... | pid ...]                                                                               test [expr]
 echo [-neE] [arg ...]                                                                                                   time [-p] pipeline
 enable [-a] [-dnps] [-f filename] [name ...]                                                                            times
 eval [arg ...]                                                                                                          trap [-lp] [[arg] signal_spec ...]
 exec [-cl] [-a name] [command [argument ...]] [redirection ...]                                                         true
 exit [n]                                                                                                                type [-afptP] name [name ...]
 export [-fn] [name[=value] ...] or export -p                                                                            typeset [-aAfFgiIlnrtux] [-p] name[=value] ...
 false                                                                                                                   ulimit [-SHabcdefiklmnpqrstuvxPT] [limit]
 fc [-e ename] [-lnr] [first] [last] or fc -s [pat=rep] [command]                                                        umask [-p] [-S] [mode]
 fg [job_spec]                                                                                                           unalias [-a] name [name ...]
 for NAME [in WORDS ... ] ; do COMMANDS; done                                                                            unset [-f] [-v] [-n] [name ...]
 for (( exp1; exp2; exp3 )); do COMMANDS; done                                                                           until COMMANDS; do COMMANDS; done
 function name { COMMANDS ; } or name () { COMMANDS ; }                                                                  variables - Names and meanings of some shell variables
 getopts optstring name [arg ...]                                                                                        wait [-fn] [-p var] [id ...]
 hash [-lr] [-p pathname] [-dt] [name ...]                                                                               while COMMANDS; do COMMANDS; done
 help [-dms] [pattern ...]                                                                                               { COMMANDS ; }""")
          elif "touch" in kali_inp:
            try:
              file_name = kali_inp[6:]
              touch_file.append(file_name)
              print("")
            except:
              print(f"-bash: {kali_inp}: command not found\n")
          elif "rm -r " in kali_inp:
            name_file = kali_inp[6:]
            if name_file in touch_file:
              touch_file.remove(name_file)
              print("")
            else:
              print(f"rm: cannot remove '{name_file}': No such file or directory\n")
          elif kali_inp == "ls":
            try:
              time.sleep(0.3)
              print("  ".join(touch_file))
              if int(len(touch_file)) == 0:
                continue
              else:
                print("")
            except:
              print(f"-bash: {kali_inp}: command not found\n")
          elif kali_inp == "cd ..":
            try:
              dirs_name_to.pop(-1)
            except:
              print()
          elif "cd " in kali_inp:
            dirs_name_to.append(kali_inp[3:])
          else:
            print(f"-bash: {kali_inp}: command not found\n")
        else:
          print("")
      except KeyboardInterrupt:
        print("\033[33mYou just terminated the program.\033[0m")
        break
      except EOFError:
        print("\033[33mYou just terminated the program.\033[0m")
        break
      except Exception as e:
        print(f"\033[33mYou just terminated the program. {e}\033[0m")
        break
  else:
    print(f"\033[31mERROR! idError: 9\033[0m\nYour Name Kali. (Original: kali): \033[36m{name_kali}\033[31m\nerror: Invalid Character.\033[0m")

func_main()