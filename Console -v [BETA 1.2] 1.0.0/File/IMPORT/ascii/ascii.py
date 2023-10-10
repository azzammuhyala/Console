#ascii
#func:

def ascii_logo(name):
  if name == "windows":
    print("\033[36m" + r"""                                ..,
                    ....,,:;+ccllll
      ...,,+:;  cllllllllllllllllll
,cclllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll

llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
llllllllllllll  lllllllllllllllllll
`'ccllllllllll  lllllllllllllllllll
       `' \*::  :ccllllllllllllllll
                        ````''*:cll
                                 ``
""" + "\033[0m")

  elif name == "apple":
    print(r"""                    ^7Y5.
                  ?B@@@B
                .G@@@@G:
                5@@&G!
      :~7??7!^. !?7!!7JJJ7~:
   :JB&@@@@@@@#GPG#&@@@@@@@&BJ:
  ?&@@@@@@@@@@@@@@@@@@@@@@@@@G~
 Y@@@@@@@@@@@@@@@@@@@@@@@@@B~
^@@@@@@@@@@@@@@@@@@@@@@@@@&:
7@@@@@@@@@@@@@@@@@@@@@@@@@G
7@@@@@@@@@@@@@@@@@@@@@@@@@#.
:&@@@@@@@@@@@@@@@@@@@@@@@@@P.
 Y@@@@@@@@@@@@@@@@@@@@@@@@@@#J^.
 .G@@@@@@@@@@@@@@@@@@@@@@@@@@@@J
  :B@@@@@@@@@@@@@@@@@@@@@@@@@@G.
   .5@@@@@@@@@@@@@@@@@@@@@@@@Y
     !B@@@@@@@@@@@@@@@@@@@@B~
       !5B#BGY?!~~!?5GB#B5!
""")
  
  elif name == "kali-linux":
    print("\033[34m" + r"""..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc',.
 .                   OMo           ':""" + "\033[90mdd\033[34m" + r"""o.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
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
  elif name == "python":
    print("\033[34m" + r"""              .:^^~~~~~^^:.
           :7JYY5555555555YJ!.
          .YP7..!55555555555PY.
          :5PJ~~JP555555555555:
          .?????????J555555555:
   :~7?????777777777J555555555:""" + "\033[33m" + r""".^^^^:.""" + "\033[34m" + r"""
 .?555555555555555555555555555:""" + "\033[33m" + r""":~~~~~~^.""" + "\033[34m"+ r"""
.JP555555555555555555555555555.""" + "\033[33m" + r""":~~~~~~~^""" + "\033[34m" + r"""
^555555555555555555555555555J^.""" + "\033[33m" + r"""^~~~~~~~~:""" + "\033[34m" + r"""
!5555555555Y?!!!!!!!!!!!!!~:.:""" + "\033[33m" + r"""^~~~~~~~~~:""" + "\033[34m" + r"""
~555555555!..:""" + "\033[33m" + r"""^^^^^^^^^^^^^^~~~~~~~~~~~~:""" + "\033[34m" + r"""
:55555555?""" + "\033[33m", r"""^~~~~~~~~~~~~~~~~~~~~~~~~~~~~.""" + "\033[34m" + r"""
 !555555P7""" + "\033[33m", r"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~:""" + "\033[34m" + r"""
  ^?Y55557.""" + "\033[33m" + r"""~~~~~~~~~~^^^^^^^^^^~~~~^^:.""" + "\033[34m" + r"""
    .::::..""" + "\033[33m" + r"""~~~~~~~~~^:::::::::.
          .~~~~~~~~~~~~~~^^~~~.
          .~~~~~~~~~~~~~:  :~~.
           .^~~~~~~~~~~~^^^^~:
             ..::^^^^^^^:::.
""" + "\033[0m")
  elif name == "ubuntu":
    print("\033[31m" + r"""            .-/+oossssoo+/-.
        `:+ssssssssssssssssss+:`
      -+ssssssssssssssssssyyssss+-
    .ossssssssssssssssss""" + "\033[0m" + r"dMMMNy" + "\033[31m" + r"""sssso.
   /sssssssssss""" + "\033[0m" + r"hdmmNNmmyNMMMMh" + "\033[31m" + r"""ssssss/
  +sssssssss""" + "\033[0m" + r"hm" + "\033[31m" + r"yd" + "\033[0m" + r"MMMMMMMNddddy" + "\033[31m" + r"""ssssssss+
 /ssssssss""" + "\033[0m" + r"hNMMM" + "\033[31m" + r"yh" + "\033[0m" + r"hyyyyhmNMMMNh" + "\033[31m" + r"""ssssssss/
.ssssssss""" + "\033[0m" + r"dMMMNh" + "\033[31m" + r"ssssssssss" + "\033[0m" + r"hNMMMd" + "\033[31m" + r"""ssssssss.
+ssss""" + "\033[0m" + r"hhhyNMMNy" + "\033[31m" + r"ssssssssssss" + "\033[0m" + r"yNMMMy" + "\033[31m" + r"""sssssss+
oss""" + "\033[0m" + r"yNMMMNyMMh" + "\033[31m" + r"ssssssssssssss" + "\033[0m" + r"hmmmh" + "\033[31m" + r"""ssssssso
oss""" + "\033[0m" + r"yNMMMNyMMh" + "\033[31m" + r"""sssssssssssssshmmmhssssssso
+ssss""" + "\033[0m" + r"hhhyNMMNy" + "\033[31m" + r"ssssssssssss" + "\033[0m" + r"yNMMMy" + "\033[31m" + r"""sssssss+
.ssssssss""" + "\033[0m" + r"dMMMNh" + "\033[31m" + r"ssssssssss" + "\033[0m" + r"hNMMMd" + "\033[31m" + r"""ssssssss.
 /ssssssss""" + "\033[0m" + r"hNMMM" + "\033[31m" + r"yh" + "\033[0m" + r"hyyyyhdNMMMNh" + "\033[31m" + r"""ssssssss/
  +sssssssss""" + "\033[0m" + r"dm" + "\033[31m" + r"yd" + "\033[0m" + r"MMMMMMMMddddy" + "\033[31m" + r"""ssssssss+
   /sssssssssss""" + "\033[0m" + r"hdmNNNNmyNMMMMh" + "\033[31m" + r"""ssssss/
    .ossssssssssssssssss""" + "\033[0m" + r"dMMMNy" + "\033[31m" + r"""sssso.
      -+sssssssssssssssss""" + "\033[0m" + r"yyy" + "\033[31m" + r"""ssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.
""" + "\033[0m")
  elif name == "android":
    print("\033[32m" + r"""         -o          o-
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMM""" + "\033[37mm:\033[32mNMMMMMMN\033[37m:m\033[32m" + r"""MMd`
      hMMMMMMMMMMMMMMMMMMh
  ..  yyyyyyyyyyyyyyyyyyyy  ..
.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMns
""" + "\033[0m")